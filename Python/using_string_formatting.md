# Using String Formatting

String formatting can be used to format elements of a string, such as reducing decimal places and setting data types. This substitutes formatted arguments into the string, producing a new string.

```python
template = '{0:.2f} {1:s} are worth US${2:d}'

template.format(4.5560, 'Argentine Pesos', 1)
```

'4.56 Argentine Pesos are worth US$1'

- `{0:.2f}` means to format the first argument as a floating-point number with 2 decimal places.

- `{1:s}` means to format the second argument (remember, this uses index positioning) as a string.

- `{2:d}` means to format the third argument as an exact integer.
