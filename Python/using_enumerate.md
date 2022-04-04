# Using enumerate

When using a `for` loop, it is useful to access both the position - or count - of a value, as well as the value. There numerous ways to approach this problem, including: 

## Using an index counter

```python
drivers = ['HAM','LEC','VER']
```

In this example the index is stored as a variable, which is updated by 1 per loop, until all of the items in the list have been accessed,

```python
index = 0 

for i in drivers: 
    print(index, i)
    index += 1
```

## Using the `range` function

In this example the range size is based on the length of the list, with positioning from 0. We access the values iteratively using the `index`, then print them within the loop.

```python
for index in range(len(drivers)):
    value = drivers[index]
    print(index, value)
```

## Using the `enumerate` function

In this example the Python `enumerate` function is used. When you use `enumerate()`, the function gives you back two loop variables:

- The count of the current iteration
- The value of the item at the current iteration

```python
for index, driver in enumerate(drivers):
    print(index, driver)
```
