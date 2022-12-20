# Select distinct on one column

This can be done by creating a calculated partion column via a subquery and filtering the output.

```sql
SELECT  *
FROM    (SELECT ID, SKU, Product,
                ROW_NUMBER() OVER (PARTITION BY PRODUCT ORDER BY ID) AS rn
         FROM   MyTable) AS a
WHERE   a.rn = 1
```
