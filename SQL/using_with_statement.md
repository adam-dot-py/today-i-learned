# Using the WITH clause

The `WITH` clause can be used to generate sub queries, which improves efficiency and readability.

## Basic use

```sql
WITH cte_quantity
AS
(SELECT
    SUM(Quantity) AS Total
FROM OrderDetails
GROUP BY ProductID)
 
SELECT
    AVG(Total) AS average_product_quantity
FROM cte_quantity
```
