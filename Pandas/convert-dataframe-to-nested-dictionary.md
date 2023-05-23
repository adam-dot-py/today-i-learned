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

Furthermore, you can use it this way to return another value if a match is not found:

`df['Industry'] = df['id'].map(lambda x: d.get(x, "Not found").get('Your industry'))`

## Iterating using tuples

Sometimes using `iterrows` can be resource intensive and it may be a better alternative to use tuples. The outcome is the same but achieved differently:

```python
d = defaultdict(dict)
userquestions = [(row[0],row[1],row[2],row[3]) for row in zip(df['id'],df['User'],df['Question'],df['Answer'])]

for i, (userid, username, question, answer) in enumerate(userquestions):
  d[userid][question] = answer

df['Industry'] = df['id'].map(d).apply(lambda x: x['Your industry'])
```
