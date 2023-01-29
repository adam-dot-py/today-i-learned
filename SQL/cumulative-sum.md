# Cumulative sum

The below example lets you create a cumulative sum based on the `ApplicationId` and `Timestamp` columns.

## Example 1

```sql
SELECT 
    ApplicationId,
    Timestamp,
    Col1,
    SUM(Col1) OVER(ORDER BY ApplicationId, Timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS Col2
FROM MyTable
ORDER BY RowId
```

## Example 2

Another way to do it is to use a window function:

```SQL
SELECT
  sales.id,
  sales.amount,
  SUM(sales.amount) OVER (ORDER BY sales.id) AS cumulative_sum
FROM
  sales
```
