# Drop columns from delta tables

Databricks Runtime 10.2+ supports dropping columns if you enable [Column Mapping mode](https://docs.databricks.com/en/delta/delta-column-mapping.html).

```sql
ALTER TABLE <table_name> SET TBLPROPERTIES (
  'delta.minReaderVersion' = '2',
  'delta.minWriterVersion' = '5',
  'delta.columnMapping.mode' = 'name'
)
```

After that, you can drop a column using standard `SQL` syntax

```sql
ALTER TABLE table_name DROP COLUMN col_name
ALTER TABLE table_name DROP COLUMNS (col_name_1, col_name_2, ...)
```
