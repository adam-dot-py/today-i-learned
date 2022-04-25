# Using the OVER clause

This table is called `DIM_EQUIPMENT`:

|VIN     |MAKE    |MODEL    |YEAR    |COLOR  |
|-------:|-------:|--------:|-------:|------:|
|1234ASDF|Ford    |Taurus   |2008    |White  |
|1234JKLM|Chevy   |Truck    |2005    |Green  |
|5678ASDF|Ford    |Mustang  |2008    |Yellow |

```sql
SELECT 
  VIN,
  MAKE,
  MODEL,
  YEAR,
  COLOR,
  COUNT(*) OVER (PARTITION BY YEAR) AS COUNT2
FROM DIM_EQUIPMENT
```

The return would be:

|VIN     |MAKE    |MODEL    |YEAR    |COLOR  |COUNT2|
|-------:|-------:|--------:|-------:|------:|-----:|
|1234JKLM|Chevy   |Truck    |2005    |Green  |1     |
|1234ASDF|Ford    |Taurus   |2008    |White  |2     |
|5678ASDF|Ford    |Mustang  |2008    |Yellow |2     |

Where rows are not being grouoed but still being aggregated by `YEAR` and matched on `ROW`. We are able to count without `GROUP BY` on `YEAR` and match with row.
