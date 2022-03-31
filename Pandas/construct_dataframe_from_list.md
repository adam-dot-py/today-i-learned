# Construct a Dataframe from a list

DataFrames can be constructed using `lists`. The below are 3 usage examples.

## Example 1

This will create a generic column list, with a column name of 0 (index position) and standard indexing.

```python
# import pandas as pd
import pandas as pd

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

df = pd.DataFrame(lst)
df
```

## Example 2

This lets you define the index and column name.

```python
import pandas as pd

lst = [1, 2, 3, 4, 5, 6]

df = pd.DataFrame(lst, index =['a', 'b', 'c', 'd', 'e', 'f'], columns =['Values'])
```

## Example 3

This allows you to combine 2 lists or more and define the column names.

```python
import pandas as pd

lst = ['A', 'B', 'C', 'D', 'E', 'F']

lst_2 = [1, 2, 3, 4, 5, 6]

df = pd.DataFrame(list(zip(lst, lst_2)), columns =['Name', 'val'])
df
```
