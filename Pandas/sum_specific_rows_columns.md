# Sum specific rows or columns

This is useful when you do not want to sum the entire row but only certain columns.

```python
sum_cols = ['A', 'B', 'C', 'D']

df['sum'] = df[sum_cols].sum(axis=1) # Returns the sum of the row. axis = 0 would sum the column.
```
