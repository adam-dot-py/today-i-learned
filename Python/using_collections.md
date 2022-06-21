# Using collections

## namedtuple

Named tuples allow you to generate more readable code than the traditional usage of tuples, where you reference values by positional arguments.

```python
import collections
Point = collections.namedtuple("Point", "x y") # Define the name and field names
p1 = Point(10, 30)
p2 = Point(20, 40)

print(p1, p2)
```

Point(x=10, y=30) Point(x=20, y=40)

You can then also call the field names as positions.

```python
print(p1.x, p1.y)
```

10, 30

## defaultdict

`defaultdict` is useful where any key that you want to add to a dictionary requires a default value. defaultdict can make code easier to read and test. It is only useful in certain situations, for example you would not use this where you need to check if a key is present in a dictionary as an indicator, as every key will be assigned the default value.

```python
# How to count without the use of defaultdict

from collections import defaultdict

fruits = ['apple', 'banana', 'apple', 'banana', 'orange']
fruitCounter = {}

# Count the items in the list
for fruit in fruits:
    if fruit in fruitCounter.keys():
        fruitCounter[fruit] += 1
    else:
        fruitCounter[fruit] = 1

# print the result
for (k, v) in fruitCounter.items():
    print(k + ": " + str(v))
```

```python
# How to count with the use of default dict

from collections import defaultdict

fruits = ['apple', 'banana', 'apple', 'banana', 'orange']
fruitCounter = defaultdict(int) # requires a factory function
# fruitCounter = defaultdict(lambda: 100) # can also be a lambda function

# Count the items in the list
for fruit in fruits:
    fruitCounter[fruit] += 1

# print the result
for (k, v) in fruitCounter.items(): # variable unpacking sets the key to k and value to v, since items returns key and value
    print(k + ": " + str(v))
```

## ordereddict

An `ordereddict` is a dictionary object that remembers the order in which values are inserted. In this code example, we create a `ordereddict` of sports team and their win loss record.

```python
from collections import OrderedDict

sportTeams = [("Liverpool", (30, 5)), ("ManCity", (31, 4)),
              ("Chelsea", (25, 10)), ("Tottenham", (24, 11)), 
              ("Man United", (24, 11)), ("Everton", (23, 12))]

sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True) # get the first item of the tuple, which is wins. Sort by wins.

teams = OrderedDict(sortedTeams)

# use popitem to remove the top item and get the top team
tm, wl = teams.popitem(False)
print("Top team: ", tm, wl)

# get the next 4 top teams
for i, team in enumerate(teams, start=1):
    print(i, team)
    if i == 4:
        break
```

```python
Top team:  ManCity (31, 4)
1 Liverpool
2 Chelsea
3 Tottenham
4 Man United
```

## deque

Double ended queue, pronounced "deck". 

Deques are hybrid objects that are similar to stacks. They are memory efficient and allow for easy manipulation of a list of items, by adding or removing items from the left or right. Deques support iteration.

```python
from collections import deque
import string

d = collections.deque(string.ascii_lowercase) # create a deque list

# iterate over the deque
print("Item count: ", str(len(d)))
for elem in d: 
    print(elem.upper(), end=",")

```

Item count:  26
A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,

```python
# manipulate items
d.pop() # pop from the right
d.popleft() # pop from the left
d.append(2) # append to the right
d.appendleft(1) # append to the left

print(d)
```

deque([1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 2])