# Add a cumulative sum column to a Dataframe

`pd.cumsum()` is useful for lots of things but a specific use case for a running total in a DataFrame.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame([[2.0, 1.0],
                   [3.0, np.nan],
                   [1.0, 0.0]],
                   columns=list('AB'))

df['C'] = df['A'].cumsum()
```

output:

|    |   A |   B |   C |
|---:|----:|----:|----:|
|  0 |   2 |   1 |   2 |
|  1 |   3 | nan |   5 |
|  2 |   1 |   0 |   6 |