# Join multiple dataframes

This can be done using `function tools`. It is particularly useful for merging multiple dataframes of the same structure or those which have a common key.

```python
import functiontools as ft

list_dfs = [fdf, temp_df_1, temp_df_2]
# The following function is used to combine all of the datasets together: functools.reduce(function, iterable[, initializer])
final_df = ft.reduce(lambda left, right: pd.merge(left, right, on=['Business Unit', 'Country Name'], how='outer'), list_dfs)
```
