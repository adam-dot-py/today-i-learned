# Using the UNION clause

The `UNION` operator is used to combine the result-set of two or more SELECT statements.

- Every `SELECT` statement within `UNION` must have the same number of columns
- The columns must also have similar data types
- The columns in every `SELECT` statement must also be in the same order

## `UNION` syntax

```sql
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM  table2
;
```

## `UNION ALL` syntax

`UNION ALL` is used to return all values, including duplicates, where as `UNION` will only return distinct values.

```sql
SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2
;
```
