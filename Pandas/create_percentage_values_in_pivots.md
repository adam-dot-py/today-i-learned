# Create percentage columns in pivot pivots

```python
import pandas as pd
import numpy as np

pdf = pd.DataFrame({'A':['x','y','z','x','y','z'],
                 'B':['one','one','one','two','two','two'],
                 'C':[2,18,2,8,2,18]})

pivot = pdf.pivot_table(index=['A','B'],
                    aggfunc=np.sum)

pivot['% of grand total'] = (pivot.C / pivot.C.sum() * 100) # create a percentage of grand total
pivot['pct of B'] = (pivot.C / pivot.groupby(level=0).C.transform(sum) * 100) # create a percentage of category
```

| A   | B   |   C |   % of grand total |   pct of B |
|:----|:----|----:|-------------------:|-----------:|
| x   | one |   2 |                  4 |         20 |
| x   | two |   8 |                 16 |         80 |
| y   | one |  18 |                 36 |         90 |
| y   | two |   2 |                  4 |         10 |
| z   | one |   2 |                  4 |         10 |
| z   | two |  18 |                 36 |         90 |
