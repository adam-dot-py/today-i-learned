# Sort dataframes by multiple columns

Sometimes we may need to sort our dataframes by multiple columns and in different orders. For example, we may want to sort by an id ascending and college name ascending.

We can do this like so:

```python
df.sort_values(by=['id', 'College'], ascending=[True, True])
```

Passing lists to `by` and `ascending` allows us to control which columns to sort by and in which order, as well as how to sort them.
