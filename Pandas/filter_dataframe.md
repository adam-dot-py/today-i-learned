# Filtering Pandas Dataframes

You can filter dataframes in Pandas in multiple ways:

## Example 1

Uses slicing with filter statements

```python
data = {'origin': ["JFK", "MAN"], 'carrier': ["B6", "B7"]}

df = pd.DataFrame(data=data)

new_df = df[(df.origin == 'JFK') & (df.carrier == 'B6')]
```

## Example 2

This method uses language similar to SQL, it is more elegant and easier to read. You also do not need to constantly reference dataframe when calling columns.

```python
new_df = df.query('origin == "JFK" & carrier == "B6"')
```

## Example 3

`loc` is the equivalent of Location, which can also be used to filter data. This is similar to example 1 but shows a different way to do it.

```python
new_df = df.loc[(df.origin == "JFK") & (df.carrier == "B6")]
```

## Filter dataframe by string criteria

You can filter a dataframe by subset criteria, such as a column containing a string value:

```python
df[df['A'].str.contains("hello")]
```

When combined with `~`, you can remove results from a dataframe. Using without `~` will show results just for the criteria.

This can also be combined with other filtering techniques such as `isin`:

```python
~df[df['A'].str.contains("hello")] & ~df['A'].isin(['hello'])]
```
