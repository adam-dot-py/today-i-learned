# Create a mean row or column

We can use `.loc` and apply `df.mean()` to create either a row or column calculation:

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 100, size=(5,4)), columns=list('ABCD')) # random DataFrame

df.loc[:, 'mean'] = df.mean(axis=1) # compute on rows
df.loc['mean', :] = df.mean(axis=0) # compute on columns
```

|    A |   B |   C |    D |   mean |
|-----:|----:|----:|-----:|-------:|
| 74   |  33 |  96 | 66   |  67.25 |
| 69   |  17 |  95 | 38   |  54.75 |
| 45   |   8 |  22 |  3   |  19.5  |
| 96   |  95 |  86 | 22   |  74.75 |
| 63   |  82 |  21 | 40   |  51.5  |
| 69.4 |  47 |  64 | 33.8 |  53.55 |
