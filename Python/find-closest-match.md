# Find the closest matching value

This custom function allows you to pass a value and return its closest matching higher value. I used this in the `Global Flows Project` to find values.

```python
## custom function to find the closest gdp when using 90% GER
gdp_values = [70000, 75000, 80000, 85000, 90000]
def find_closest_gdp(lst, target):
    higher_values = sorted([x for x in lst if x > target])
    if not higher_values:
        return 70000
    return min(higher_values, key=lambda x: abs(x - target))
```
