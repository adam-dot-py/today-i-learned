# Merging dataframes

There are several ways to merge dataframes.

## Using pandas.merge

Using this method requires a primary key to be present on both tables, in order to join records. In the below example, we match rows on the left table. Any rows without a match in the right table are dropped.

```python
import pandas as pd

df1_data = {'Fruit' : ['Apple','Bannana','Pear'], 'Colour' : ['Red','Yellow','Green']}
df2_data = {'Fruit' : ['Apple','Bannana','Pear','Strawberry'], 'Quantity' : [4,8,2,6]}
df1 = pd.DataFrame(data=df1_data)
df2 = pd.DataFrame(data=df2_data)

merged_df = pd.merge(left=df1, right=df2, on='Fruit', how='left')
````

| Fruit   | Colour   |   Quantity |
|:--------|:---------|-----------:|
| Apple   | Red      |          4 |
| Bannana | Yellow   |          8 |
| Pear    | Green    |          2 |

You can also preserve rows on the join. Here, non-matching rows on the right table are still joined but replaced with `nan` values in columns from the left.

```python
import pandas as pd
import numpy as np

df1_data = {'Fruit' : ['Apple','Bannana','Pear'], 'Colour' : ['Red','Yellow','Green']}
df2_data = {'Fruit' : ['Apple','Bannana','Pear','Strawberry'], 'Quantity' : [4,8,2,6]}
df1 = pd.DataFrame(data=df1_data)
df2 = pd.DataFrame(data=df2_data)

merged_df = pd.merge(left=df1, right=df2, on='Fruit', how='right').fillna(np.nan)
```

| Fruit      | Colour   |   Quantity |
|:-----------|:---------|-----------:|
| Apple      | Red      |          4 |
| Bannana    | Yellow   |          8 |
| Pear       | Green    |          2 |
| Strawberry | nan      |          6 |

## Using Concat
Merging dataframes is done via `pd.concat`.

```python
df = pd.DataFrame(np.random.randint(0, 50, size = (4, 5)), columns = list('ABCDE'))
df2 = pd.DataFrame(np.random.randint(0, 50, size = (4, 5)), columns = list('ABCDE'))

frames = [df, df2]
df = pd.concat(frames, ignore_index=True)
```

## Output

|    |   A |   B |   C |   D |   E |
|---:|----:|----:|----:|----:|----:|
|  0 |  34 |  37 |   6 |  39 |  20 |
|  1 |  47 |  27 |  42 |   7 |  18 |
|  2 |  27 |   6 |  41 |  45 |  16 |
|  3 |  10 |  14 |  18 |  41 |  28 |
|  4 |  28 |  15 |  43 |  47 |   3 |
|  5 |  19 |   4 |  38 |  44 |   5 |
|  6 |  32 |  16 |  34 |   6 |  11 |
|  7 |  28 |  45 |  19 |  44 |  24 |

Further syntax including handling dataframes of different shapes can be found [here](https://pandas.pydata.org/docs/user_guide/merging.html).
