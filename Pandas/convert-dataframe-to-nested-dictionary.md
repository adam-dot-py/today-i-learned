# Convert a dataframe to a nested dictionary

This is particularly useful for when you want to group to a category and have keys, values for elements.

|    |    id | User   | Question      | Answer    |
|---:|------:|:-------|:--------------|:----------|
|  0 | 11111 | Adam   | Your age      | 29        |
|  1 | 11111 | Adam   | Your gender   | Male      |
|  2 | 11111 | Adam   | Your industry | DevOps    |
|  3 | 11122 | Vicky  | Your age      | 30        |
|  4 | 11122 | Vicky  | Your gender   | Female    |
|  5 | 11122 | Vicky  | Your industry | Education |

```python
from collections import defaultdict
d = defaultdict(dict)
for i, row in df.iterrows():
    mydict[row['id']][row['Question']] = row['Answer']
```

```defaultdict(dict,
            {11111: {'Your age': 29,
              'Your gender': 'Male',
              'Your industry': 'DevOps'},
             11122: {'Your age': 30,
              'Your gender': 'Female',
              'Your industry': 'Education'}})
```

You can then use this in a similar way to `VLOOKUP()` or `INDEX(), MATCH()`

```python
'''
use the id as the lookup value and then lambda to select a nested key to return a value
'''
df['Industry'] = df['id'].map(d).apply(lambda x: x['Your industry'])
```

|    |    id | User   | Question      | Answer    | Industry   |
|---:|------:|:-------|:--------------|:----------|:-----------|
|  0 | 11111 | Adam   | Your age      | 29        | DevOps     |
|  1 | 11111 | Adam   | Your gender   | Male      | DevOps     |
|  2 | 11111 | Adam   | Your industry | DevOps    | DevOps     |
|  3 | 11122 | Vicky  | Your age      | 30        | Education  |
|  4 | 11122 | Vicky  | Your gender   | Female    | Education  |
|  5 | 11122 | Vicky  | Your industry | Education | Education  |