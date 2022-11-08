# Round Multiple Columns

This is useful for rounding multiple float columns at once, with two options:

## Option 1 - using a dictionary

```python
df = df.round({'Col1' : 2,
               'Col2' : 2})
```

## Option 2 - using columns

```python
round_columns = ['Col1','Col2']
df[round_columns] = df['round_columns'].round(2) # two decimal places
```
