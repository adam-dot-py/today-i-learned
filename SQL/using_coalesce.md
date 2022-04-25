# Using coalesce

`COALESCE` returns the first non-null value in a list.

```sql
SELECT 
COALESCE (
    NULL, NULL, 'Orange', NULL, 'Banana'
    )
;
```
