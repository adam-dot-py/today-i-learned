# Using case

Until version `3.10`, Python never had a feature that implemented what the `switch` statement does in other programming languages. Instead, you had use `if` and `elif` statements, like so:

```python
def html_status(status):
    if status == 400: return "OK"
    elif status == 500: return "Problem"
    else: return "Something went wrong"
    
html_status(500)
```

`Problem`

With the new `case` functionality, you can achieve the same result like so:

```python
def html_status(status):
    match status:
        case 400:
            return "OK"
        case 500:
            return "Problem"
        case _:
            return "Something went wrong"

html_status(500)
```

`Problem`