# Recover tables via version history and CDF (Change Data Feed)

When CDF is enabled on a table in Databricks, we can use the version history to restore back to a specific version. This is useful for recovering data.

First, identify which version to roll back to by inspecting the history of the table:

```sql
describe history <table_name>;
```

Then, use the following query to restore back to a selected version:

```sql
restore table <table_name> to version as of <version_number>;
```
