# Merge dataframes with only unique columns

This is particularly useful to avoid the having to drop `suffixes`. It checks what columns are different and only those are joined.

## Using `merge` and getting column difference

```python
x = [
    [10,20],
    [30,40],
    [50,60]
]

y = [
    [10,20,"foo"],
    [30,40,"bar"],
    [50,60,"baz"]
]

df1 = pd.DataFrame(data=x, columns=["val1", "val2"])
df2 = pd.DataFrame(data=y, columns=["val1","val2","type"])

merge_cols = df2.columns.difference(df1.columns) # check what columns are different in df2 to df1

fdf = pd.merge(df1, df2[merge_cols], left_index=True, right_index=True, how='outer')
```

|   val1 |   val2 | type   |
|-------:|-------:|:-------|
|     10 |     20 | foo    |
|     30 |     40 | bar    |
|     50 |     60 | baz    |

## Using a `regex` in a `filter`

```python
df1 = pd.DataFrame(data=x, columns=["val1", "val2"])
df2 = pd.DataFrame(data=y, columns=["val1","val2","type"])

fdf = df1.merge(df2, left_index=True, right_index=True,
                 how='outer', suffixes=('', '_y'))

fdf.drop(fdf.filter(regex='_y$').columns, axis=1, inplace=True)
```

|   val1 |   val2 | type   |
|-------:|-------:|:-------|
|     10 |     20 | foo    |
|     30 |     40 | bar    |
|     50 |     60 | baz    |
