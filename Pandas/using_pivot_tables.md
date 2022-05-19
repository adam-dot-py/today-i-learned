# Using pivot tables

Pivot tables are really useful for shaping and aggregating data in different ways.

## Example Usage

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})

table = pd.pivot_table(df,
                       index=['A', 'B'],
                       values='D',
                       columns=['C'],
                       aggfunc=np.sum)
```

## Context Usage - using `pivot_table` with `groupby`

We can use this to present survey data in different ways, like so:

```python
grouped = np.round(df.groupby(['Area', 'QuestionNumber', 'EntityProviderCode'])['Weighting'].agg(np.mean),2).reset_index()

final = grouped.pivot_table(index=['Area', 'QuestionNumber'],
                            columns=['EntityProviderCode'],
                            values='Weighting')
```

`index` can be used group the data in numerous ways, alongside multiple `columns` as well.

Wrapping `grouped` in `np.round()` restricts the values to a given decimal place, in this instance 2.
