# Round to the nearest multiple

This function can be used to round a number to the closest given multiple:

```python
def round_to_nearest_multiple(*argv, base=5):
    
    """round_to_nearest_multiple(argv*, base) --> rounds a number to the closest base given
    
    Parameters:
    argv* = the number or list of values to round
    base = the closest multiple to round to. Defaults to 5.
    """

    for arg in argv:
        return base * round(arg/base)

round_to_nearest_multiple(4, base=5)
```

The above output would be 5, since 4's closest multiple of 5 is 5.
