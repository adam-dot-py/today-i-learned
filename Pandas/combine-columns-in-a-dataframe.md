# Combine columns in a Dataframe

When looking to merge columns, we can do so by only merging columns where values in the first column argument are blank. The `combine_first` method within the Pandas library allows you to combine two series, where it fills the NaN values in the first series with values from the second series.

```python
# Merge the two columns
df['SourceMedium'] = df['SourceMedium_1'].combine_first(df['SourceMedium_2'])

print(df)
```

After that, you can drop the column that is no longer required:

```python
df = df.drop(['SourceMedium_1'], axis=1)

print(df)
```
