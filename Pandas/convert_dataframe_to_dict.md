# Convert a dataframe to a dictionary

This is useful for creating dictionaries for later mapping or further use.

|    |   id |   value |
|---:|-----:|--------:|
|  0 |    0 |    10.2 |
|  1 |    1 |     5.7 |
|  2 |    2 |     7.4 |

where `df` is the `dataframe`:

```python
df_dict = dict(zip(df.id, df.value))
```
