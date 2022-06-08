# Using range

The `range()` function returns an iterator that yields a sequence of evenly seperated integers:

```python
range(10)
# range (0, 10)

list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

You can also include a start, end and step (increment):

```python
list(range(0, 10, 2)) # start at zero, go up to but not including 10 in increments of 2
# [0, 2, 4, 6, 8]
```

It can also go backwards:

```python
list(range(10, 0, -2)) # start at 10, progress down to but not including zero in increments of 2
# [10, 8, 6, 4, 2]
```

`range()` produces integers up to but not including the given endpoint.
