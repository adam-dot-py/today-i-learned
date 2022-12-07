# Get the latest records

You can use the below to show only the latest records, based on a `date` column being present in the table.

In this example, `t.rn = 1` refers to the latest data, other matching records will increment up indicating later records.

```sql
SELECT * FROM (
    SELECT
      username,
      date,
      value,
      row_number() OVER(PARTITION BY username ORDER BY date DESC) as rn
    FROM
      yourtable
) t
WHERE t.rn = 1
```
