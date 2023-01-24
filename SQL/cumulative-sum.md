# Cumulative sum

The below example lets you create a cumulative sum based on the `ApplicationId` and `Timestamp` columns.

```sql
SELECT 
    ApplicationId,
    Timestamp,
    Col1,
    SUM(Col1) OVER(ORDER BY ApplicationId, Timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS Col2
FROM MyTable
ORDER BY RowId
```
