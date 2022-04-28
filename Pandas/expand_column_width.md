# Expand the column width in a DataFrame

Sometimes data is truncated in a DataFrame when you want to see it all. To expand the width of columns, use:

```python
import pandas as pd 

pd.set_option('display.max_colwidth', None)
```

Using `None` expands the column out to the full width of the data. You can pass an integer value to control this more.
