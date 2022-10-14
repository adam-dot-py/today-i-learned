# Perform Calculations on Dictionaries

`keys` and `values` can be accessed in dictionaries via `.keys()` and `.values()`, allowing calculations to be done.

```python
my_dict = {'Adam' : 90, 'Billy' : 90, 'Gary' : 70, 'Luke' : 65}
student_names = list(my_dict.keys())

total = 0
for x in my_dict.values():
    total += x

average_grade = total / len(student_names)

print('Students', student_names, 'Average Score:', average_grade)
```

Students ['Adam', 'Billy', 'Gary', 'Luke'] Average Score: 78.75
