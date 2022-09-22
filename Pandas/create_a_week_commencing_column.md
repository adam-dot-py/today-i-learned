# Create a week commencing column

Week commencing is really useful when used in conjunction with `groupby`, as we can condense daily data down to a single instance, with all values aggregated.

Firstly, we need to convert our date column in a dataframe to a `datetime` object using `pandas.to_datetime`:

```python
import pandas as pd

frame['Date'] = pd.to_datetime(frame['Date']) # create a datetime object
```

After that, we can create a week commencing column using `to_period()` and `lambda`:

```python
frame['week_commencing'] = frame['Date'].dt.to_period('W').apply(lambda r: r.start_time)
```

Without `lambda`, the start and end time will be returned. We apply `lambda` to only return the `start_time`.
