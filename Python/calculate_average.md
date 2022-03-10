## Calculate average in Python

You find the average by summing all of the values and then dividing by the total number of values. In Python, you can create a function to accept a list of values and then return the average.
```python
numbers = [4.0,3.0,4.0,4.5,2.5,4.7]

def calculate_average(numbers): 
    sum_num = 0
    for t in num:
        sum_num += t

    avg = sum_num / len(num)
    return avg

calculate_average(numbers=numbers)
```

The variable ```sum_num``` takes each value in the ```numbers``` list and sums it. The average is then `sum_num / len(num)`. 