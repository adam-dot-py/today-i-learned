# Limiting a DataFrame

We can limit a dataframe using the standard `df.head()` command, like this:

```python
import pandas as pd

csv_file = 'example.csv'
df = pd.read_csv(csv_file)

df.head(10) # return the first 10 rows
```

We can also return the final N rows:

```python
df.tail(10) # return the final 10 rows
```

## Using iloc

We can achieve the same result using `df.iloc[]`:

```python
import pandas as pd

csv_file = 'example.csv'
df = pd.read_csv(csv_file)

df.iloc[:5] # return all columns and the the first 5 rows
```

Using `df.iloc[]` we can also limit and return just a certain column:

```python
import pandas as pd
import numpy as np 

df = pd.DataFrame(np.random.randint(1, 50, size=(10, 4)), columns='ABCD')

df['A'].iloc[:5]
```

|   A |
|----:|
|  10 |
|  12 |
|  10 |
|   3 |
|  29 |
