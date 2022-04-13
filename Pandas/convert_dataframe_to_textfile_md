# Converting a DataFrame to a text file

DataFrames can be written to text files using the `pd.to_string` method, in combination with `open`.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 50, size = (4, 5)), columns = list('ABCDE'))

with open ('df_to_txt', 'w') as fp:
    fp.write(df.to_string())
```
