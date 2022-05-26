# Flatten list of nested lists

If I need to flatten a list which has nested lists (lists in lists) I can use these approaches:

## List Comprehension

```python
t = [[1,2,3], [4,5,6], [7,8,9]]

flat_list = [item for sublist in t for item in sublist]
```

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[1, 2, 3, 4, 5, 6, 7, 8, 9]

## Alternative loop

The above is the same as:

```python
flat_list = []

for sublist in t:
    for item in sublist:
        flat_list.append(item)
```

[1, 2, 3, 4, 5, 6, 7, 8, 9]
