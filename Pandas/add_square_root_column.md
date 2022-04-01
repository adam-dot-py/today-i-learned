# Adding the square root of a value to a column

Finding the square root can be done by:

## Method 1

```python

import pandas as pd
import numpy as np

df1 = {
    'State':['Arizona AZ','Georgia GG','Newyork NY','Indiana IN','Florida FL'],
   'Score':[4,47,55,74,31]}
 
df1 = pd.DataFrame(df1,columns=['State','Score'])

df1['Score_squareroot'] = df1['Score'] ** (1/2)
```

## Method 2

```python
df1['Score_suareroot'] = np.sqrt((df1.Score))
```
