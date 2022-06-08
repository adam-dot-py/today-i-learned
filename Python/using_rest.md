# Using `rest`

Using `rest` is useful when we only want to retrieve certain elements from the beginning of a tuple. The use of `rest*` is used to capture an arbitrarily long list of positional arguments:

```python
values = 1, 2, 3, 4, 5

a, b, *rest = values

a
# 1

b
# 2

rest
# [3, 4, 5]
```

`a` and `b` are assigned the first two values, whilst the rest are assigned to `rest`. Whilst new to Python, using `rest` is the equivalent of assigning `_*` (underscore) as a variable name, which is commonly used for unwanted variables.
