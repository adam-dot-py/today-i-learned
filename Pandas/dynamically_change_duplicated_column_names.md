# Dynamically change duplicated column names

We can dynamically rename duplicated columns in a `pandas` `DataFrame` using a `dictionary` with a nested `list` of valid alternative names.

```python
d = {'x' : ['x1','x2','x3']}
df.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)
```

This utilises `lambda` to assign a value from the nested `list` if the column name matches the `key`, using `pop`. `pop` will return a value whilst also removing it from the `list`.
