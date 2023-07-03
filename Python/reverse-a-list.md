# Reverse or slice a list

Python has powerful slice notation for lists, using the `[start:stop:step]` syntax. The basic slicing technique is to define the starting point, the stopping point, and the step size – also known as stride.

Below is a basic usage:

```python
x = [1,2,3,4,5,6,7,8,9,10]

print(f"Full list {x[:]}")
print(f"Every 2 values: {x[::2]}")
print(f"Reversed list {x[::-1]}")
```

Full list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] \
Every 2 values: [1, 3, 5, 7, 9] \
Reversed list [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
