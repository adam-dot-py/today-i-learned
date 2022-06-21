# Using docstrings

Docstrings allow you to document your code directly in Python, which can be called by other developers to understand what a class or function is doing, as well as it's required and optional arguments.

> PEP 257: [available here](https://peps.python.org/pep-0257/)

## Example

```python
def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> Doesn't do anything, just prints.

    Parameters:
    arg1: the first argument. Whatever you feel like passing.
    arg2: second argument. Defaults to None.
    """
    print(arg1, arg2)
```

To call the docstring, use `print(myFunction.__doc__)`.

## Best practice

- Enclose docstrings in triple quotes
- First line should be summary sentence of the functionality
- Modules: List important classes, functions, exceptions
- Classes: List important methods

## Functions

- List parameters and explain each, one per line
- If there's a return value, then list it; otherwise omit
- If the function raises exceptions, mention those
