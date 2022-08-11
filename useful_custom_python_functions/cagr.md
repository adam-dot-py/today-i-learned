# Compounded Annual Growth Rate

Useful for calculating CAGR in a dataframe for each country.

```python
def cagr(end_value, start_value, years):
    result = ((end_value / starting_value)**(1 / years)-1)*100
    return result
```

```python
pdf['CAGR'] = cagr(end_value=pdf['2020/21'],
                   start_value=pdf['2017/18'], 
                   years=3).fillna(0)
```
