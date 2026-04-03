# Spark in Databricks: Best Practices for Data Engineering

A reference guide covering best practices and recommended approaches when using Apache Spark in Databricks for data engineering workloads.

---

## Table of Contents

1. [Cluster Configuration](#cluster-configuration)
2. [Reading and Writing Data](#reading-and-writing-data)
3. [DataFrame Operations](#dataframe-operations)
4. [Partitioning and Optimisation](#partitioning-and-optimisation)
5. [Delta Lake](#delta-lake)
6. [Schema Management](#schema-management)
7. [Caching and Persistence](#caching-and-persistence)
8. [Error Handling and Logging](#error-handling-and-logging)
9. [Secrets and Configuration](#secrets-and-configuration)
10. [Testing and Data Quality](#testing-and-data-quality)

---

## Cluster Configuration

### Use the right cluster type for the job

| Workload Type | Recommended Cluster |
|---|---|
| Interactive development | Single-node or small multi-node |
| Batch ETL | Job clusters (auto-terminate) |
| Streaming | Long-running job clusters |
| Ad-hoc analysis | Shared interactive cluster |

### Always use job clusters for production pipelines

Job clusters start fresh, terminate on completion, and avoid resource contention with interactive workloads.

```python
# In Databricks Workflows, configure a new job cluster per task
# rather than using an existing all-purpose cluster
```

### Set `spark.conf` settings at cluster or job level, not in code where possible

```python
# Avoid scattering configs throughout your notebooks
# Prefer setting these in cluster spark config or workflow task config:
# spark.sql.shuffle.partitions = 200
# spark.databricks.delta.optimizeWrite.enabled = true
```

---

## Reading and Writing Data

### Always define a schema when reading CSV or JSON

Avoid schema inference in production — it is slow and can change unexpectedly.

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType

schema = StructType([
    StructField("id", IntegerType(), nullable=False),
    StructField("name", StringType(), nullable=True),
    StructField("created_at", TimestampType(), nullable=True),
])

df = spark.read.schema(schema).csv("/mnt/raw/data/", header=True)
```

### Use `mergeSchema` cautiously and `enforceSchema` where data quality matters

```python
# Allow new columns to be added over time (use with care)
df = spark.read.option("mergeSchema", "true").parquet("/mnt/data/")
```

### Prefer Parquet or Delta over CSV for internal data storage

```python
# Write as Delta for full ACID support and time travel
df.write.format("delta").mode("overwrite").save("/mnt/silver/my_table")

# Register as a table for SQL access
spark.sql("CREATE TABLE IF NOT EXISTS my_table USING DELTA LOCATION '/mnt/silver/my_table'")
```

### Use `overwriteSchema` only when intentionally changing a table schema

```python
df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable("my_table")
```

---

## DataFrame Operations

### Prefer `select` over `drop` for explicit column control

```python
# Prefer this — explicit about what you want
df_clean = df.select("id", "name", "created_at", "status")

# Avoid this — fragile when upstream schema changes
df_clean = df.drop("unwanted_col")
```

### Use `withColumnRenamed` when renaming a single column

```python
df = df.withColumnRenamed("custmr_id", "customer_id")
```

### Chain transformations to keep code readable

```python
from pyspark.sql import functions as F

df_transformed = (
    df
    .filter(F.col("status") == "active")
    .withColumn("full_name", F.concat_ws(" ", F.col("first_name"), F.col("last_name")))
    .withColumn("created_date", F.to_date(F.col("created_at")))
    .select("id", "full_name", "created_date", "status")
)
```

### Use `F.col()` from `pyspark.sql.functions` instead of `df["col"]`

```python
from pyspark.sql import functions as F

# Preferred
df.filter(F.col("age") > 30)

# Avoid — breaks in chained transformations involving multiple DataFrames
df.filter(df["age"] > 30)
```

### Avoid `collect()` on large DataFrames

`collect()` pulls all data to the driver — use only for small, aggregated results.

```python
# Fine for small aggregations
total = df.agg(F.count("*")).collect()[0][0]

# Dangerous on large datasets — avoid
all_rows = df.collect()
```

### Use `display()` for development, not `show()`

```python
# In Databricks notebooks — richer, paginated output
display(df)

# show() is fine for quick checks in scripts
df.show(5, truncate=False)
```

---

## Partitioning and Optimisation

### Set `spark.sql.shuffle.partitions` appropriate to your data size

The default is 200, which is too high for small datasets and too low for very large ones.

```python
# Rule of thumb: aim for ~128MB per partition after a shuffle
spark.conf.set("spark.sql.shuffle.partitions", "50")
```

### Partition Delta tables on columns used frequently in filters

```python
df.write.format("delta").partitionBy("year", "month").save("/mnt/silver/events")
```

### Use `OPTIMIZE` and `ZORDER` to improve query performance on Delta tables

```sql
-- Compact small files
OPTIMIZE silver.events

-- Co-locate data for common filter columns
OPTIMIZE silver.events ZORDER BY (customer_id, event_date)
```

### Enable Auto Optimize for write-heavy tables

```python
# Set at table level
spark.sql("ALTER TABLE silver.events SET TBLPROPERTIES ('delta.autoOptimize.optimizeWrite' = 'true', 'delta.autoOptimize.autoCompact' = 'true')")
```

### Avoid shuffles where possible — broadcast small lookup tables

```python
from pyspark.sql.functions import broadcast

df_result = large_df.join(broadcast(small_lookup_df), on="lookup_key", how="left")
```

### Repartition before writing large datasets

```python
# Repartition to control output file count
df.repartition(10).write.format("delta").mode("overwrite").save("/mnt/silver/my_table")
```

---

## Delta Lake

### Use Delta format for all production tables

Delta provides ACID transactions, time travel, schema enforcement, and automatic file management.

```python
df.write.format("delta").mode("append").saveAsTable("bronze.raw_events")
```

### Use `MERGE` (upsert) for incremental loads

```python
from delta.tables import DeltaTable

target = DeltaTable.forName(spark, "silver.customers")

(
    target.alias("target")
    .merge(
        source=df_updates.alias("source"),
        condition="source.customer_id = target.customer_id"
    )
    .whenMatchedUpdateAll()
    .whenNotMatchedInsertAll()
    .execute()
)
```

### Use time travel for auditing and recovery

```python
# Query a previous version
df_v1 = spark.read.format("delta").option("versionAsOf", 1).load("/mnt/silver/customers")

# Query by timestamp
df_yesterday = spark.read.format("delta").option("timestampAsOf", "2024-01-01").load("/mnt/silver/customers")
```

### Run `VACUUM` to manage storage costs

```sql
-- Remove files older than 7 days (default retention)
VACUUM silver.customers

-- Reduce retention period (use with caution — disables older time travel)
VACUUM silver.customers RETAIN 168 HOURS
```

### Enable Change Data Feed for downstream consumers

```sql
ALTER TABLE silver.customers SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true')
```

```python
# Read only the changes since a given version
df_changes = (
    spark.read.format("delta")
    .option("readChangeFeed", "true")
    .option("startingVersion", 5)
    .table("silver.customers")
)
```

---

## Schema Management

### Enforce schema on Delta tables — do not silently accept schema drift

```python
# This will raise an error if the incoming schema does not match
df.write.format("delta").mode("append").save("/mnt/silver/customers")
```

### Use `StructType` to define schemas programmatically

```python
from pyspark.sql.types import StructType, StructField, StringType, LongType, TimestampType

customer_schema = StructType([
    StructField("customer_id", LongType(), nullable=False),
    StructField("name", StringType(), nullable=True),
    StructField("email", StringType(), nullable=True),
    StructField("created_at", TimestampType(), nullable=True),
])
```

### Centralise schemas in a shared module or widget-driven config

Keep schema definitions in one place to avoid duplication across notebooks.

---

## Caching and Persistence

### Only cache DataFrames that are reused multiple times

```python
df_customers = spark.read.table("silver.customers").cache()

# Use df_customers in multiple operations...
df_customers.unpersist()  # Always unpersist when done
```

### Use `persist()` with a storage level for more control

```python
from pyspark import StorageLevel

df.persist(StorageLevel.MEMORY_AND_DISK)
```

### Avoid caching large DataFrames unnecessarily — it puts pressure on executor memory

---

## Error Handling and Logging

### Use `dbutils.notebook.exit()` to return structured status from notebooks

```python
import json

try:
    # main logic
    result = {"status": "success", "rows_written": df.count()}
except Exception as e:
    result = {"status": "failed", "error": str(e)}
    raise
finally:
    dbutils.notebook.exit(json.dumps(result))
```

### Log key metrics using `print` or a structured logger

```python
print(f"[INFO] Records read: {df.count()}")
print(f"[INFO] Records written to silver.customers: {df_clean.count()}")
```

### Validate data quality before writing to downstream layers

```python
row_count = df.count()
null_ids = df.filter(F.col("customer_id").isNull()).count()

assert null_ids == 0, f"Found {null_ids} null customer_id values — aborting write."
assert row_count > 0, "DataFrame is empty — aborting write."
```

---

## Secrets and Configuration

### Never hard-code credentials — always use Databricks Secrets

```python
# Store secrets in Databricks Secret Scopes and access via dbutils
storage_account_key = dbutils.secrets.get(scope="my-scope", key="storage-account-key")

spark.conf.set(
    "fs.azure.account.key.mystorageaccount.dfs.core.windows.net",
    storage_account_key
)
```

### Use widgets to parameterise notebooks

```python
dbutils.widgets.text("environment", "dev", "Environment")
dbutils.widgets.text("run_date", "", "Run Date (YYYY-MM-DD)")

env = dbutils.widgets.get("environment")
run_date = dbutils.widgets.get("run_date")
```

---

## Testing and Data Quality

### Use `Great Expectations` or `deequ` for automated data quality checks

For lighter-weight inline checks:

```python
def assert_no_nulls(df, column: str):
    null_count = df.filter(F.col(column).isNull()).count()
    assert null_count == 0, f"Column '{column}' contains {null_count} nulls."

def assert_unique(df, column: str):
    total = df.count()
    distinct = df.select(column).distinct().count()
    assert total == distinct, f"Column '{column}' is not unique: {total} rows, {distinct} distinct."

assert_no_nulls(df_clean, "customer_id")
assert_unique(df_clean, "customer_id")
```

### Write unit tests for transformation logic using pytest and small DataFrames

```python
# test_transformations.py
import pytest
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local").appName("tests").getOrCreate()

def test_full_name_concat(spark):
    data = [("John", "Doe"), ("Jane", "Smith")]
    df = spark.createDataFrame(data, ["first_name", "last_name"])
    df = df.withColumn("full_name", F.concat_ws(" ", F.col("first_name"), F.col("last_name")))
    results = [row["full_name"] for row in df.collect()]
    assert results == ["John Doe", "Jane Smith"]
```

### Use `dbutils.notebook.run()` to orchestrate multi-notebook pipelines and capture exit values

```python
result = dbutils.notebook.run(
    path="/pipelines/transform_customers",
    timeout_seconds=600,
    arguments={"environment": "prod", "run_date": "2024-06-01"}
)

import json
status = json.loads(result)
assert status["status"] == "success", f"Notebook failed: {status}"
```
