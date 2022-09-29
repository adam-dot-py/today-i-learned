# Using `map()`

map() function returns a map object (which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

## Syntax

`map(function, iterable)`

## Parameters

- function : It is a function to which map passes each element of given iterable.
- iterable : It is a iterable which is to be mapped.

## Like VLOOKUP

`map()` can be used to have similar functionality to a `vlookup` in Excel. By creating a dictionay of keys and values, a column in a `dataframe` can be used to lookup a key and return its value.

```python
import pandas as pd

staff_name = {100120 : 'Adam Lowe',
              100121 : 'Kerry Gough'}

d = [[100120, 'MI & Data Manager', 'UPE'],
     [100121, 'Head of Change & Data Management',' UPE']]

#--look up the employee number as a key in the dictionary and return its value (staff name)
df = pd.DataFrame(data=d, columns=['EmployeeNumber', 'JobTitle', 'Division'])

df['EmployeeName'] = df['EmployeeNumber'].map(staff_name)
```

|   EmployeeNumber | JobTitle                         | Division   | EmployeeName   |
|-----------------:|:---------------------------------|:-----------|:---------------|
|           100120 | MI & Data Manager                | UPE        | Adam Lowe      |
|           100121 | Head of Change & Data Management | UPE        | Kerry Gough    |

## To apply functions

```python
#-- double numbers with lambda
numbers = [1,2,3,4]
result = map(lambda x: x+x, numbers)
print(list(result))
```

[2, 4, 6, 8]

```python
#--use it with functions
def addition(n):
    return n + n

numbers = [1,2,3,4]
result = map(addition, numbers)
print(list(result))
```

[2, 4, 6, 8]

```python
#--add two lists together
numbers1 = [1,2,3,4]
numbers2 = [5,6,7,8]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))
```

[6, 8, 10, 12]

```python
#--extract letters from each word in a string, create nested list
words = ['cat', 'dog', 'fish']
result = list(map(list,l))
print(result)
```

[['c', 'a', 't'], ['d', 'o', 'g'], ['f', 'i', 's', 'h']]
