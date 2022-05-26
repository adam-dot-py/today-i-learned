# Using Group By

`pd.groupby` allows us to split the object, apply a function, and combine the results. This can be used to group large amounts of data and compute operations on these groups.

> Note: You can use `.apply(display)` to a `groupby` object to display it without using `agg`: `df.groupby('Animal).apply(display)`

```python
import pandas as pd

d = {'Animal' : ['Falcon', 'Falcon', 'Parrot', 'Parrot'], 
     'Max_Speed' : [380., 370., 24., 26.]}

df = pd.DataFrame(data=d)

df.groupby(['Animal']).agg({'Max_Speed' : 'mean'}) # Other agg functions can be passed like nunique
```

| Animal   |   Max_Speed |
|:---------|------------:|
| Falcon   |         375 |
| Parrot   |          25 |

## Hierarchical Indexes

We can groupby different levels of a hierarchical index using the level parameter:

```python
arrays = [['Falcon', 'Falcon', 'Parrot', 'Parrot'],
          ['Captive', 'Wild', 'Captive', 'Wild']]

index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))

df = pd.DataFrame({'Max Speed': [390., 350., 30., 20.]}, index=index)

df.groupby(level=0).mean()
df.groupby(level="Type").mean()
```

| Animal   |   Max Speed |
|:---------|------------:|
| Falcon   |         370 |
| Parrot   |          25 |

| Type    |   Max Speed |
|:--------|------------:|
| Captive |         210 |
| Wild    |         185 |

## Rename `agg` column returns

You can rename the return column from `groupby` by passing the column name as a variable in `agg`, with the column to perform the operation on and the required operation as a `tuple`:

```python
group = df.groupby(by=['legislation', 'age_range']).agg(count_legislation=('legislation', 'count'))
```

| legislation                                       | age_range   |   count_legislation |
|:--------------------------------------------------|:------------|--------------------:|
| Misuse of Drugs Act 1971 (section 23)             | 10-17       |                  10 |
| Misuse of Drugs Act 1971 (section 23)             | 18-24       |                  23 |
| Misuse of Drugs Act 1971 (section 23)             | 25-34       |                  27 |
| Misuse of Drugs Act 1971 (section 23)             | over 34     |                  25 |
| Police and Criminal Evidence Act 1984 (section 1) | 10-17       |                   3 |
| Police and Criminal Evidence Act 1984 (section 1) | 25-34       |                   2 |
| Police and Criminal Evidence Act 1984 (section 1) | over 34     |                   6 |
