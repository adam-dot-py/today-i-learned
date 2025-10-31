# Read CSVs using SQL

The below can be used to read `csv` files using `SQL` in Databricks.

This particular example reads all files in the folder.

```sql
SELECT * FROM read_files(
  '/mnt/other-source/sharepoint/Aivree-Admissions/*.csv',
  format => 'csv',
  header => true,
  multiLine => true,
  quote => '"',
  escape => '"',
  mode => 'PERMISSIVE',
  inferSchema => true,
  schemaEvolutionMode => 'rescue'
)
```