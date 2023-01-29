# Subtract previous row

## Example 1

In SQL, you can use a self-join to join a table to itself, and then use the "LAG()" function to access the value of a previous row, and subtract it from the current row.
Here is an example of how you can subtract the previous row's value from the current row's value for a column called "value" in a table called "data":

```SQL
SELECT
  current.id,
  current.value - LAG(current.value) OVER (ORDER BY current.id) AS difference
FROM
  data current
```

## Example 2

```SQL
SELECT
  sales1.product,
  sales1.date,
  sales1.amount - LAG(sales2.amount) OVER (PARTITION BY sales1.product ORDER BY sales1.date) AS difference
FROM
  sales sales1
JOIN
  sales sales2
ON
  sales1.product = sales2.product AND
  sales1.date = sales2.date + INTERVAL 1 DAY
```

This query uses a self join to join the "sales" table to itself, and then uses the "LAG()" function to access the value of the previous row of "amount" for the same "product", and subtract it from the current row's value of "amount". The "PARTITION BY" clause is used to ensure that the "LAG()" function only looks at the previous row within the same partition of rows with the same product.
