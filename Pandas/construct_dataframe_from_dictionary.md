# Constructing a Dataframe From a Dictionary

You can create a dataframe in Python using Pandas from a dictionary. You construct it in the same way standard dictionaries are constructured.

```python
d = {'col1': [1, 2], 'col2': [3, 4]}

df = pd.DataFrame(data=d)
```