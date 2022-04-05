# Convert value counts to a seperate DataFrame

This is useful when you have rows of non-unique values and you want to have a seperate DataFrame with counts for each.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'Fruits' : ['Apple', 'Apple', 'Banana', 'Orange', 'Lemon', 'Orange']})

fruit_value_counts = df.Fruits.value_counts()

df = pd.DataFrame(fruit_value_counts).reset_index()
df.columns = ['Fruit', 'Count']
```

## Output

|    | Fruit   |   Count |
|---:|:--------|--------:|
|  0 | Apple   |       2 |
|  1 | Orange  |       2 |
|  2 | Banana  |       1 |
|  3 | Lemon   |       1 |