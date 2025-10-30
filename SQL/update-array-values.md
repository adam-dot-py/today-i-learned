# Update Array Values

When working with array values you can utilise the `transform` function in SQL iterate over the values and update them with new values.

The below is an example of how to achieve that:

```sql
UPDATE raw.sales_employees
SET destination_coverage = transform(destination_coverage, x -> CASE WHEN x = 'WLIC SCO' THEN 'WLIC' ELSE x END)
WHERE array_contains(destination_coverage, 'WLIC SCO');
```