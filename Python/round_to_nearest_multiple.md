# Round to the nearest multiple

This function can be used to round a number to the closest given multiple:

```python
def round_to_nearest_multiple(x, multiple):
    """round_to_nearest_multiple(x, multiple) --> rounds a number to the closest multiple given
    
    Parameters:
    x = the number to round
    multiple = the closest multiple to round to
    """

    return multiple * round(x/multiple)

round_to_nearest_multiple(4, multiple=5)
```

The above output would be 5, since 4's closest multiple of 5 is 5.
