# Keep only NaN value in a dataframe

Use `pandas.Series.isnull` on the column to find the missing values and index with the result. This is useful for when you only want to see records with null values.

```python
import pandas as pd

data = pd.DataFrame({'ticker': ['aapl', 'msft', 'goog'],
                     'opinion': ['GC', nan, 'GC'],
                     'x1': [100, 50, 40]})

data = data[data['opinion'].isnull()]
```
