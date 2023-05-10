# Fill `NaN` values in dataframes

The below can be used to dynamically go through a dataframe, filling numerical values with a `0` and other values, like strings, with a text value, in this case `.`.

```python
df.apply(lambda x: x.fillna(0) if x.dtype.kind in 'biufc' else x.fillna('.'))
```

`biufc` is used to identify boolean, integer, unicode, float & complex data types.
