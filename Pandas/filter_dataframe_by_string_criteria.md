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