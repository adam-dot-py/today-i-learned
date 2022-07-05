# Check If Year Is A Leap Year

```python
# Return True if leap year and false if not

def is_leap(year):

    leap = False

    if (year % 4 == 0) and (year % 100 != 0): # if the year can be divided by 4 and is not divisable by 100, True
        leap = True
    elif (year % 100 == 0) and (year % 400 != 0): # if the year is divisible by 100 and not divisable by 400, False
        leap = False
    elif (year % 400 == 0): # if the year is divisable by 400, True
        leap = True
    
    return leap
```
