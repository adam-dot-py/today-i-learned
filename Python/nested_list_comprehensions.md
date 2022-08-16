# Nested List Comprehensions

```python

# The For part of the list comprehension is arranged according to the order of nesting
# any filter condition is put at the end as before

all_data = [['John', 'Michael','Emily','Mary', 'Steven'],
            ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]

# method 1

names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e') >= 2] # find names with more than or equal to 2 e's
    names_of_interest.extend(enough_es)

names_of_interest

# method 2

result = [name for names in all_data for name in names if name.count('e') >=2]

# method 3 
some_tuples = [(1,2,3), (4,5,6), (7,8,9)]
flattened = [x for tup in some_tuples for x in tup]

## which is the same as

flattened = []
for tup in some_tuples:
    for x in tup:
        flattened.append(x)

flattened
```
