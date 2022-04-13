# Using Group By

`pd.groupby` allows us to split the object, apply a function, and combine the results. This can be used to group large amounts of data and compute operations on these groups.

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
