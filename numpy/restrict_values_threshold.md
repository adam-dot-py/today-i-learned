# Restrict values to a certain threshold

Given an interval, values outside the interval are clipped to the interval edges. For example, if an interval of [0, 1] is specified, values smaller than 0 become 0, and values larger than 1 become 1.

You can also specify the edges to be `None` if one of the sides should not be restricted. For example, when calculating confidence intervals to not go above 100%.

```python
import numpy as np

a = np.arrange(0, 10)
```

`array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])`

```python
b = np.clip(a, 1, 8)
```

`array([1, 1, 2, 3, 4, 5, 6, 7, 8, 8])`

You can also wrap it around a function: 

```python
conf_df['ci_upper'] = np.clip((conf_df.pctAgree + ci).round(), a_min=0, a_max=100)
```
