# Check if a certain type

When needing to check if a variable is of a certain type, for example to check if a row item from a `Pandas` dataframe is a specific type, you can check it using the `isinstance()` method.

```python
text = 1
def check_type(text):
    if isinstance(text, str):
        print('Is text!')
    else:
        print('Not text!')

check_type(text)
```

I used this as a real world example here:

```python
def remove_text(text: str, exclude: str, replace_with: str):
    # check if the text is a string, if not return the original value - likely NaN
    if not isinstance(text, str):
        return text
    for string in exclude:
        if string in text:
            text = text.replace(string, replace_with)
    return text
```
