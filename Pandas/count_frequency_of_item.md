# Count the frequency of an item

Using `pandas`, we can count the frequency of an item appearing in a column or a dataset. This uses `groupby` with `transform` so that the column can be added back to the dataframe with an aligned index.

| FruitType   |
|:------------|
| Apple       |
|Apple        |
|Banana       |
|Orange       |
|Banana       |

```python
df['Frequency'] = df.groupby('FruitType')['FruitType'].transform('count')
```

| FruitType   |   Frequency |
|:------------|------------:|
| Apple       |           2 |
|Apple        |           2 |
|Banana       |           2 |
|Orange       |           1 |
|Banana       |           2 |

If returning back to the dataframe is **not required**, then this can also be achieved by:

```python
df.groupby('FruitType').count()
```

| FruitType   |   Frequency |
|:------------|------------:|
| Apple       |           2 |
|Banana       |           2 |
|Orange       |           1 |
