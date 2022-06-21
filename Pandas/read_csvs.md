# Read .csv Files

This page is dedicated to the `read_csv` function and will grow with more TILs.

We can read csv files in `pandas` using the `read_csv` function. This allows us to take a csv file and create a data frame, simply using:

```python
import pandas as pd

df = pd.read_csv('path/to/csv/file.csv')
```

## Omit a specific column

We can use list comprehension to omit certain columns, if we wanted to:

```python
import pandas as pd

# list the column names

cols = list(pd.read_csv('/path/to/csv/file.csv', nrows=1))

# bring in the data, but omit a column

df = pd.read_csv('/path/to/csv/file.csv', usecols=[i for i in cols if i != 'column name'])
```

## Use only certain columns

We can pass a list to `usecols` to bring in only certain columns

```python
import pandas as pd

cols = ['column1', 'column2', 'column3']
df = pd.read_csv('/path/to/csv/file.csv', usecols=cols)
```
