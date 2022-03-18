## Introspection

Using `?` against an object, method or function will describe what it is (i.e type) or what it does (i.e a function). This also allows you to view the doc string for a function. 

**Example**

```python
def add_numbers(a,b): 
    """
    Sums two numbers together
    
    Returns
    -------

    the_sum : type of arguments
    """

    return a + b
```

By typing `add_numbers?`, information about the function will be revealed, including the doc string. 

Additionally, typing `add_numbers??` will reveal the code used in the function.