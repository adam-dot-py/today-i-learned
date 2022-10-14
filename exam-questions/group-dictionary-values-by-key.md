# Group Dictionary Values By Key

Grouping a dictionary by `values` and their associated `keys` can be done via `dict.setdefault()`.

```python
#--if order is required we can call the sorted() method first
#--The setdefault() method returns the value of the item with the specified key
#--If the key does not exist, insert the key, with the specified value
d = {1: 6, 2: 1, 3: 1, 4: 9, 5: 9, 6: 1}
v = {}

for key, value in sorted(d.items()):
    v.setdefault(value, []).append(key)
```

`{6: [1], 1: [2, 3, 6], 9: [4, 5]}`

```python
#--if no order is required we can use sets()
d = {1: 6, 2: 1, 3: 1, 4: 9, 5: 9, 6: 1}
v = {}
for key, value in d.items():
    v.setdefault(value, set()).add(key)
```

`{6: [1], 1: [2, 3, 6], 9: [4, 5]}`

_That the output of the set values is sorted is a coincidence, a side-effect of how hash values for integers are implemented; sets are unordered structures._
