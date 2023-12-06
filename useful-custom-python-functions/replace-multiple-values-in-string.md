# Replace multiple items in a string

This small function allows you to replace multiple values in a string at once.

```python
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

my_dict = {'%' : '', '/' : ''}

df.columns = [replace_all(x, my_dict) for x in df.columns]
```
