# Round to nearest multiple

This function can be use to round to a nearest multiple, i.e 5:

```python
def round(x, base=5):
    return base * round(x/base)
```
