# Rename a column in Pandas

You can use `df.rename` with the `columns` parameter to rename multiple columns at once.

```python
df = df.rename(columns={"A": "a", 
                        "B": "c"})
```

Alternatively, pass the argument `inplace` to not declare it:

```python
df.rename(columns={"A": "a", 
                   "B": "c"}, inplace=True)
```

You can also assign new column names in a list with `df.columns`:

```python
df.columns = ['col1', 'col2', 'col3', 'col4', 'col5']
```

The amount of columns needs to be the same as the `shape` of the `DataFrame`.
