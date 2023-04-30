# Sorting zipped lists

This is useful when you have combining related data that is unordered, which then needs to be ordered.

```python
x = ["foo", "bar", "baz"]
y = [9, 10, 2]

zipped_list = list(zip(x, y))
sorted_list = sorted(zipped_list, key=lambda x: x[1]) # use the second item of each pair to sort by

print("Zipped list: \n", zipped_list)
print("\n")
print("Sorted list: \n", sorted_list)
```

`Zipped list: [('foo', 9), ('bar', 10), ('baz', 2)]`

`Sorted list: [('baz', 2), ('foo', 9), ('bar', 10)]`
