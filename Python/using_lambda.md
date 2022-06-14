# Using lambda Functions

`lambda` functions allow you to produce small, anonymous functions. They can be passed arguments like any other function. They are typically used in place and just when they are needed.

## Example

These functions convert temperatures, using the `map` function and defining new functions.

```python
def CelsiusToFahrenheit(temp):
    return (temp * 9/5) + 32

def FahrenheitToCelsius(temp):
    return (temp-32) * 5/9

ctemps = [0, 12, 34, 100]
ftemps = [32, 65, 100, 212]

print(list(map(CelsiusToFahrenheit, ctemps)))
print(list(map(FahrenheitToCelsius, ftemps)))
```

- [32.0, 53.6, 93.2, 212.0]
- [0.0, 18.333333333333332, 37.77777777777778, 100.0]

We can make this easier to read and less complex, using `lambda` to replace the need to define entire functions:

```python
ctemps = [0, 12, 34, 100]
ftemps = [32, 65, 100, 212]
print(list(map(lambda t: (t * 9/5) + 32, ctemps)))
print(list(map(lambda t: (t-32) * 5/9, ftemps)))
```

We get the same result, with less complex code.

- [32.0, 53.6, 93.2, 212.0]
- [0.0, 18.333333333333332, 37.77777777777778, 100.0]
