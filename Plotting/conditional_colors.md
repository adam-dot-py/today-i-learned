# Conditional colours

You can set colour based on conditions, for example for a bar chart to be red if the value is negative and green if the value is positive. This is useful for charts on a negative to positive axis, for example when plotting NPS. 

```python

colors = ['g' if x > 0 else 'r' for x in nps['Score']]
```

`g` and `r` can be switched to use any of the `matplotlib` color arguments.

You then just pass the `colors` variable as a keyword argument, for example in `matplotlib` or `seaborn`.
