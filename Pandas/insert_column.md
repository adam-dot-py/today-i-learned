# Insert a column into a dataframe

You can insert a column into a `DataFrame` using `pd.insert`. This can be a singular value or a combination (such as summing values together).

```python
import pandas as pd

d = {'col1' : [1, 2], 'col2' : [3, 4]}

df = pd.DataFrame(data=d)
df.insert(loc=2, column='col3', value=[5, 6])
```

|    |   col1 |   col2 |   col3 |
|---:|-------:|-------:|-------:|
|  0 |      1 |      3 |      5 |
|  1 |      2 |      4 |      6 |
