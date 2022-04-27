# Flatten JSON function

This function can be used to flatten JSON in a Pandas dataframe row.

However, the type of the row needs to be changed first from type `str`. This is done via `literal_eval`: 

```python
from ast import literal_eval

df['coursePackage'] = df['coursePackage'].apply(literal_eval)
```

You can then flatten JSON using this function:

```python
def flatten_json(nested_json, exclude=['']):
  
    out = {}

    def flatten(x, name='', exclude=exclude):
        if type(x) is dict:
            for a in x:
                if a not in exclude: flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out
```
