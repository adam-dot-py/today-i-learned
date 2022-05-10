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
