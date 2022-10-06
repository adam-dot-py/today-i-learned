# Remove Characters From Column Headers

This is useful for when you need to remove or replace any characters in the headers of a `spark` dataframe, such as removing white spaces.

```spark
NewColumns = (column.replace(' ', '') for column in df.columns)
df = df.toDF(*NewColumns)
```
