# Databricks: Data Engineering Best Practices

A reference guide covering best practices and recommended approaches for data engineering on the Databricks platform.

---

## Table of Contents

1. [Medallion Architecture](#medallion-architecture)
2. [Unity Catalog and Governance](#unity-catalog-and-governance)
3. [Delta Live Tables (DLT)](#delta-live-tables-dlt)
4. [Databricks Workflows](#databricks-workflows)
5. [Notebook Organisation](#notebook-organisation)
6. [DBFS and External Storage](#dbfs-and-external-storage)
7. [Cluster Management](#cluster-management)
8. [Monitoring and Observability](#monitoring-and-observability)
9. [Security and Access Control](#security-and-access-control)
10. [Cost Optimisation](#cost-optimisation)

---

## Medallion Architecture

Structure data into three layers: **Bronze**, **Silver**, and **Gold**.

| Layer | Purpose | Format | Example |
|---|---|---|---|
| **Bronze** | Raw ingestion, no transformations | Delta (append-only) | `bronze.raw_events` |
| **Silver** | Cleaned, conformed, joined | Delta | `silver.customers` |
| **Gold** | Aggregated, business-ready | Delta | `gold.monthly_revenue` |

### Bronze: land raw data with minimal transformation

```python
# Preserve original data — add metadata columns only
df_bronze = (
    df_raw
    .withColumn("_ingested_at", F.current_timestamp())
    .withColumn("_source_file", F.input_file_name())
)

df_bronze.write.format("delta").mode("append").saveAsTable("bronze.raw_events")
```

### Silver: clean, validate and conform

```python
df_silver = (
    df_bronze
    .filter(F.col("customer_id").isNotNull())
    .withColumn("event_date", F.to_date(F.col("event_timestamp")))
    .withColumnRenamed("custmr_nm", "customer_name")
    .dropDuplicates(["event_id"])
)

df_silver.write.format("delta").mode("overwrite").saveAsTable("silver.events")
```

### Gold: aggregate for reporting and consumption

```python
df_gold = (
    df_silver
    .groupBy("customer_id", "event_date")
    .agg(F.count("event_id").alias("event_count"), F.sum("revenue").alias("total_revenue"))
)

df_gold.write.format("delta").mode("overwrite").saveAsTable("gold.daily_customer_revenue")
```

---

## Unity Catalog and Governance

### Use Unity Catalog for centralised data governance

Unity Catalog provides a three-level namespace: `catalog.schema.table`.

```sql
-- Create a catalog
CREATE CATALOG IF NOT EXISTS my_org;

-- Create schemas per domain
CREATE SCHEMA IF NOT EXISTS my_org.finance;
CREATE SCHEMA IF NOT EXISTS my_org.marketing;

-- Reference tables consistently
SELECT * FROM my_org.finance.transactions;
```

### Apply fine-grained access control at table and column level

```sql
-- Grant read access to analysts
GRANT SELECT ON TABLE my_org.gold.monthly_revenue TO `analysts`;

-- Grant write access to a service principal
GRANT MODIFY ON TABLE my_org.silver.customers TO `etl-service-principal`;

-- Restrict a sensitive column
ALTER TABLE my_org.silver.customers ALTER COLUMN email SET MASK mask_email;
```

### Tag tables and columns for discoverability

```sql
ALTER TABLE my_org.silver.customers SET TAGS ('domain' = 'crm', 'pii' = 'true');
ALTER TABLE my_org.silver.customers ALTER COLUMN email SET TAGS ('pii' = 'true');
```

### Use service principals, not personal accounts, for automated pipelines

Register a service principal and assign it the minimum required permissions for each pipeline.

---

## Delta Live Tables (DLT)

### Use DLT for declarative pipeline development

DLT manages dependencies, retries, and data quality checks automatically.

```python
import dlt
from pyspark.sql import functions as F

@dlt.table(
    name="bronze_raw_events",
    comment="Raw events landed from source system",
    table_properties={"quality": "bronze"}
)
def bronze_raw_events():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load("/mnt/landing/events/")
        .withColumn("_ingested_at", F.current_timestamp())
    )

@dlt.table(
    name="silver_events",
    comment="Cleaned and validated events",
    table_properties={"quality": "silver"}
)
@dlt.expect_or_drop("valid_customer_id", "customer_id IS NOT NULL")
@dlt.expect_or_drop("valid_event_date", "event_date IS NOT NULL")
def silver_events():
    return (
        dlt.read_stream("bronze_raw_events")
        .withColumn("event_date", F.to_date(F.col("event_timestamp")))
        .dropDuplicates(["event_id"])
    )
```

### Use `@dlt.expect` decorators to enforce data quality inline

| Decorator | Behaviour on violation |
|---|---|
| `@dlt.expect` | Record the violation, keep the row |
| `@dlt.expect_or_drop` | Drop the violating row |
| `@dlt.expect_or_fail` | Fail the pipeline |

```python
@dlt.expect("non_negative_revenue", "revenue >= 0")
@dlt.expect_or_drop("valid_customer", "customer_id IS NOT NULL")
@dlt.expect_or_fail("unique_event", "event_id IS NOT NULL")
def silver_events():
    return dlt.read_stream("bronze_raw_events")
```

### Prefer Streaming Tables over Materialised Views for incremental loads

Streaming Tables process only new data on each run; Materialised Views recompute fully.

---

## Databricks Workflows

### Use Workflows (Jobs) for all production orchestration — not manual notebook runs

```json
{
  "name": "daily_etl_pipeline",
  "tasks": [
    {
      "task_key": "ingest_raw",
      "notebook_task": { "notebook_path": "/pipelines/01_ingest" }
    },
    {
      "task_key": "transform_silver",
      "depends_on": [{ "task_key": "ingest_raw" }],
      "notebook_task": { "notebook_path": "/pipelines/02_transform" }
    }
  ]
}
```

### Pass parameters to notebooks using task values or widgets

```python
# In notebook 01_ingest — set a task value for downstream tasks
dbutils.jobs.taskValues.set(key="rows_ingested", value=df.count())

# In notebook 02_transform — retrieve the task value
rows = dbutils.jobs.taskValues.get(taskKey="ingest_raw", key="rows_ingested", default=0)
print(f"[INFO] Rows available for transformation: {rows}")
```

### Use `dbutils.notebook.exit()` to return status from each notebook task

```python
import json

dbutils.notebook.exit(json.dumps({"status": "success", "rows_written": 12500}))
```

### Set alerting and retry policies on jobs

Configure email or webhook alerts on failure, and set sensible retry counts (e.g. 2 retries with a 5-minute delay) for transient errors.

---

## Notebook Organisation

### One notebook, one responsibility

| Notebook | Responsibility |
|---|---|
| `01_ingest.py` | Read from source, write to Bronze |
| `02_transform.py` | Clean and conform data, write to Silver |
| `03_aggregate.py` | Build Gold layer aggregations |
| `04_validate.py` | Run data quality checks |

### Use `%run` to share utility functions across notebooks

```python
# In a shared utilities notebook: /utils/spark_helpers
def read_delta(table_name: str):
    return spark.read.table(table_name)

def write_delta(df, table_name: str, mode: str = "overwrite"):
    df.write.format("delta").mode(mode).saveAsTable(table_name)
```

```python
# In your pipeline notebook
%run /utils/spark_helpers

df = read_delta("silver.customers")
```

### Use `%md` cells to document intent, not just implementation

```markdown
## Step 2: Clean customer data

Filter out records with null customer IDs and standardise name casing.
Any records dropped here are logged in the audit table.
```

---

## DBFS and External Storage

### Prefer external locations (ADLS, S3) over DBFS for production data

DBFS is local to the workspace and not suitable for shared or governed data.

```python
# Mount external storage (legacy approach)
dbutils.fs.mount(
    source="abfss://container@storageaccount.dfs.core.windows.net/",
    mount_point="/mnt/silver",
    extra_configs={"fs.azure.account.key.storageaccount.dfs.core.windows.net": dbutils.secrets.get("scope", "key")}
)

# Preferred: Use Unity Catalog External Locations instead of mounts
```

### Use Unity Catalog External Locations over legacy DBFS mounts

External Locations are governed, auditable, and compatible with Unity Catalog access controls.

```sql
CREATE EXTERNAL LOCATION my_silver_storage
URL 'abfss://silver@mystorageaccount.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL my_credential);
```

### Never store sensitive data or credentials in DBFS

Use Databricks Secret Scopes for all credentials.

---

## Cluster Management

### Use cluster policies to enforce cost controls and configuration standards

Cluster policies restrict configuration options available to users, preventing oversized clusters and enforcing naming conventions.

### Enable auto-scaling for interactive clusters, fixed size for batch jobs

```python
# For batch jobs, fixed size avoids auto-scale overhead
# Set in the job cluster config:
# num_workers: 4
```

### Use photon-enabled clusters for SQL-heavy workloads

Photon is a vectorised query engine that significantly accelerates Delta Lake reads and SQL queries.

### Set `auto_termination_minutes` on all interactive clusters

Prevents idle clusters from running indefinitely and incurring unnecessary costs.

---

## Monitoring and Observability

### Write pipeline audit records to a Delta table

```python
from datetime import datetime

audit_record = spark.createDataFrame([{
    "pipeline_name": "daily_etl",
    "run_date": datetime.utcnow().date().isoformat(),
    "rows_read": rows_read,
    "rows_written": rows_written,
    "status": "success",
    "timestamp": datetime.utcnow().isoformat()
}])

audit_record.write.format("delta").mode("append").saveAsTable("audit.pipeline_runs")
```

### Use Databricks Lakehouse Monitoring for automated data quality tracking

Lakehouse Monitoring profiles your Delta tables and tracks schema drift, null rates, and distribution shifts over time.

```python
# Enable monitoring via the UI or API
# databricks.sdk or REST API:
# POST /api/2.0/lakehouse-monitoring/tables/{table_name}
```

### Review the Spark UI for performance bottlenecks

Key things to check:
- **Stages with long task durations** → data skew or large shuffles
- **Spill to disk** → increase executor memory or reduce partition size
- **High GC time** → reduce data in memory, consider persisting to disk

---

## Security and Access Control

### Use row-level security for multi-tenant data

```sql
-- Create a row filter function
CREATE FUNCTION my_org.row_filter(customer_region STRING)
RETURN customer_region = current_user_region();

-- Apply it to a table
ALTER TABLE my_org.silver.customers SET ROW FILTER my_org.row_filter ON (region);
```

### Rotate secrets regularly and use short-lived tokens where possible

Never embed tokens or storage keys directly in notebook code or workflow configs.

### Audit data access using Unity Catalog system tables

```sql
-- View recent table access events
SELECT *
FROM system.access.audit
WHERE action_name = 'SELECT'
  AND request_params.table_full_name = 'my_org.silver.customers'
ORDER BY event_time DESC
LIMIT 100;
```

---

## Cost Optimisation

### Use spot/preemptible instances for non-critical batch workloads

Configure spot instances on worker nodes in your cluster settings to reduce compute costs by up to 70%.

### Enable `optimizeWrite` and `autoCompact` to reduce small file overhead

```sql
ALTER TABLE silver.events SET TBLPROPERTIES (
  'delta.autoOptimize.optimizeWrite' = 'true',
  'delta.autoOptimize.autoCompact' = 'true'
);
```

### Run `OPTIMIZE` and `VACUUM` on a schedule

```sql
-- Schedule weekly in a Databricks Workflow
OPTIMIZE my_org.silver.events ZORDER BY (customer_id);
VACUUM my_org.silver.events RETAIN 168 HOURS;
```

### Use serverless compute for light workloads and SQL queries

Serverless warehouses and serverless compute eliminate the cluster startup overhead for short-lived tasks.

### Right-size clusters using the Cluster Utilisation dashboards

Review CPU, memory, and I/O utilisation in the Databricks workspace to identify over-provisioned clusters.
