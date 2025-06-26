# Enable Change Data Feed (CDF)

For all new tables in a Databricks workspace:

```spark
set spark.databricks.delta.properties.defaults.enableChangeDataFeed = true;
```

For an existing table:

```spark
ALTER TABLE <table_name> SET TBLPROPERTIES (delta.enableChangeDataFeed = true)
```