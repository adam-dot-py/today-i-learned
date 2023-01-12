# Lookup value in a dictionary

This allows you to lookup a value inside a nested dictionary, but can be adapted to lookup a value in any standard Python `dict`.

This particular example has a country as a key with a nested dictionary containing colleges and their values.

```python
d = {'UK' : {'College1' : 10, 'College2' : 15},
     'Scotland' : {'College1' : 20, 'College2' : 50}
}

def fy_lookup_value(dictionary, country, college):

    """lookup_forecast_value(dictionary, country, college) --> returns forecast value in a nested dictionary for FY23.

    Parameters:
    dictionary: the dictionary to look in.
    country: the country to look for.
    college: the college to look for, which will return the forecast value.
    """

    for k in dictionary.keys():
        if k == country:
            for c, v in dictionary[k].items():
               if c == college:
                     return v

fy_lookup_forecast_value(dictionary=d, country='UK',college='College1')
```

`10`
