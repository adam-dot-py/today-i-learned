# Sum rows

Summing rows is done via `pd.sum()` whilst passing the `axis` argument of 1. You can also pass `axis=0` to sum columns.

These two methods show how to sum all rows and selected rows.

## Sum all rows

```python
# Create a DataFrame of random numbers between 0 and 100, with 5 rows and 4 columns.
df = pd.DataFrame(np.random.randint(0,100, size=(5,4)), columns=list('ABCD'))

# Create a new column comprised of the summed rows
df['E'] = df.sum(axis=1)
```

Output:

|    |   A |   B |   C |   D |   E |
|---:|----:|----:|----:|----:|----:|
|  0 |  48 |  79 |  98 |  50 | 275 |
|  1 |  58 |  35 |  22 |  38 | 153 |
|  2 |  51 |  70 |   8 |  11 | 140 |
|  3 |   2 |  60 |  68 |  63 | 193 |
|  4 |  59 |  35 |   5 |  38 | 137 |

## Sum selected rows

```python
# Create a DataFrame of random numbers between 0 and 100, with 5 rows and 4 columns.
df = pd.DataFrame(np.random.randint(0,100, size=(5,4)), columns=list('ABCD'))

# Create a new column comprised of summed rows of your choosing

# Make a list of all the columns then drop 'D'
col_list = list(df)
col_list.remove('D')

df['E'] = df[col_list].sum(axis=1)
```

Output:

|    |   A |   B |   C |   D |   E |
|---:|----:|----:|----:|----:|----:|
|  0 |   4 |  54 |   3 |  95 |  61 |
|  1 |  91 |  37 |  81 |  53 | 209 |
|  2 |  78 |   9 |  89 |  49 | 176 |
|  3 |  79 |  44 |  19 |  23 | 142 |
|  4 |  40 |  75 |  58 |  46 | 173 |