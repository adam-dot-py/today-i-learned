# Joining strings

For this particular challenge, write a `function` that takes a `list` value and return a `string` with all the items seperated by a comma and a space with and inserted before the last item.

```python
spam = ["eggs", "bacon", "cheese"]

def items_except_list(items):
    if len(items) == 0:
        return print("Blank list!")
    elif len(items) == 1:
        return print(items[0])
    else:
        items_exception_last = ', '.join(map(str, items[:-1])) # create a string out of all items except the last one
        return print(f"{items_exception_last} and {items[-1]}") # concat them all together

items_except_list(spam)
```
