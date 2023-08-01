# Custom sort a list

The below is an example of sorting a list of months that are not in order but can be used for any use case.

```python
month_order = {
    'Jan': 1,
    'Feb': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'Aug': 8,
    'Sept': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}

months = ['June', 'Jan', 'Feb']
months.sort(key=lambda month: month_order[month])
```

Will then return `Jan, Feb, June`.
