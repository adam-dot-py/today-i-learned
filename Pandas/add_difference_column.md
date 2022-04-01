# Add a difference column to a DataFrame

Using `pd.diff()` we can add a column that shows the difference between each row of data. This is useful for showing changes in values.

```python

df = pd.DataFrame([[1.0, 2.0],
                   [3.0, np.nan],
                   [1.0, 3.0]],
                   columns = list('AB'))

df['C'] = df['A'].diff()
```

Output: 

|    |   A |   B |   C |
|---:|----:|----:|----:|
|  0 |   1 |   2 | nan |
|  1 |   3 | nan |   2 |
|  2 |   1 |   3 |  -2 |