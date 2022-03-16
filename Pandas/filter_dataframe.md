## Filtering Pandas Dataframes

You can filter dataframes in Pandas in multiple ways: 

**Example 1**

Uses slicing with filter statements

```python
data = {'origin': ["JFK", "MAN"], 'carrier': ["B6", "B7"]}

df = pd.DataFrame(data=data)

new_df = df[(df.origin == 'JFK') & (df.carrier == 'B6')]
```

**Example 2**

This method uses language similar to SQL, it is more elegant and easier to read. You also do not need to constantly reference dataframe when calling columns. 
```python
new_df = df.query('origin == "JFK" & carrier == "B6"')
```

**Example 3**

`loc` is the equivalent of Location, which can also be used to filter data. This is similar to example 1 but shows a different way to do it. 

```python
new_df = df.loc[(df.origin == "JFK") & (df.carrier == "B6")]
```