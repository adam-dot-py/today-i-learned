# Unpack Nested Lists to a Dictionary

We can unpack a list to a dictionary, where the first item is the key and the second item is a value. This creates a dictionary with keys and values as lists.

```python
d = [['ARUC', 'Germany'],['ARUC', 'UK'], ['BPC','UK']]

v = {}
for groups in d:
    v.setdefault(groups[0], []).append(groups[1])

print(v)
```
