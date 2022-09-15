# Using bins or buckets

Using bins or buckets is really useful when we want to categorise continious numerical data.

In this example, we will create a mock `dataframe` containing random scores between `0` and `100` for `1000` students. The aim is to categorise these scores into grades.

```python
def create_df():

    df = pd.DataFrame({'score' : np.random.randint(0,100,1000)})
    return df

df = create_df()
```

## Using `loc[]` and `between()`

This method identifies the value that is between the areas of interest and then returns the corresponding value we choose. It uses keywords like 'right' and 'both' to define boundaries and for which side is `inclusive`, for example for scores between 0 and 50 we pass `both` as both boundaries are `inclusive`.

```python
df.loc[df['score'].between(0,50,'both'), 'grade'] = 'C'
df.loc[df['score'].between(50,80,'right'), 'grade'] = 'B'
df.loc[df['score'].between(80,100,'right'), 'grade'] = 'A'
```

This is useful only when there are a small number of bins required, otherwise several lines of code will need to be written.

## Using `pd.cut()`

This allows us to define bins and labels and bucket values into discrete intervals.

This is useful when there are multiple bins. The number of bin ranges must match the label length:

- 0 to 50 = C
- 50 to 80 = B
- 80 to 100 = A

```python
bins = [0,50,80,100]
labels = ['C','B','A']
df['grade'] = pd.cut(x=df['score'], 
                     bins=bins, 
                     labels=labels, 
                     include_lowest=True)
```

## Using `pd.qcut()`

Similar to cut, however this will attempt to assign values into evenly distributed buckets, based upon the number of quintiles we pass to `q`.

```python
df['grade'], cut_bin = pd.qcut(x=df['score'],
                               q=3,
                               labels=['C','B','A'],
                               retbins=True
```

If we pass `retbins=True` then `(bins, values)` is returned, hence why multiple assignment of variables.

## Using `value_counts()`

Where assining back to the `df` is not required, you can achieve similar results by passing `bins` as an argument in `value_counts()`.

```python
df['score'].value_counts(bins=[0,50,80,100])
```
