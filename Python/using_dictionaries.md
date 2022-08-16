# Using dictionaries

## Add items to a dictionary

```python
my_dict = {
    "brand" : "Peugeot",
    "model" : "3008",
    "year" : "2018"
}

# Add a value to a dictionary
my_dict["color"] = "grey"

print("My car is a {brand} {model} from {year} in {color}".format(**my_dict))
```

The output would be `My car is a Peugeot 3008 from 2018 in grey`

## Get items from a dictionary

```python
x = my_dict.get("model")

print(x)
```

The output would be `3008`.

## Get multiple values of a key in a dictionary

```python
word_freq = {'is' : [1, 4, 6, 7, 8, 9],
             'at' : [3, 5, 6, 3, 10, 3],
             'test' : [2, 6, 8, 5, 1 , 4]}

value_list = word_freq['at']
print(value_list)
```

The output would be `[3, 5, 6, 3, 10, 3]`

## Append multiple values to a key in a dictionary

This can be done via the `extend` function.

```python

word_freq['at'].extend([2, 4, 6])
```

The values `2, 4, 6` would be added to the values for the key `at`.

You can also use this function to append values to an existing key, or create a new one if it does not exist:

```python
def add_values_to_dict(dictionary, key, values):
    if key not in dictionary:
        dictionary[key] = list()
    dictionary[key].extend(values)
    return dictionary

add_values_to_dict(word_freq, 'add', [21, 10, 13])
print(word_freq)
```

In the above function, the values given as argument will be appended if the `key` is found. If not `key` is found then a new dictionary entry is created with the values.

## Search for a value in a dictionary

```python
word_freq = {'is'   : [1, 3, 4, 8, 10],
             'at'   : [3, 10, 15, 7, 9],
             'test' : [5, 3, 7, 8, 1],
             'this' : [2, 3, 5, 6, 11],
             'why'  : [10, 3, 9, 8, 12] }

# Check if a value exist in dictionary with multiple value
value = 10

# Get list of keys that contains the given value
list_of_keys = [key for key, list_of_values in word_freq.items() if value in list_of_values]

if list_of_keys:
    print(list_of_keys)
else:
    print('Value does not exist in the dictionary')
```

This uses list comprehension to search for a given `value` and return the keys that contain that `value`. If no `key` contains the `value`, then the `else` statement is used. The list comprehension statement is saying for each pair, check if the given `value` exists associated with the `key` or not. If yes, put that key in `list_of_keys`.

## Other uses

```python
d1 = {'a' : 10, 'b' : 20, 'c' : 'an integer'}

'b' in d1 # return true or false if present
d1['a'] # return value for the given key
d1.update({'d' : 40, 'e' : [1,2,3,4], 'a' : 15}) # add new items, or update existing items in place
del d1['c'] # delete a key-value pair
ret = d1.pop('b') # return the value whilst deleting the key-value in the dictionary

## Constructing dicts

# Method 1
key_list = range(3)
value_list = ['foo', 'bar', 'baz']
mapping = {}

for key, value in zip(key_list, value_list):
    mapping[key] = value

# Method 2
other_dict = dict(zip(range(5), reversed(range(5))))

# Method 3
words = ['apple','bat','bar','atom','book']
by_letter = {}

for word in words:
    letter = word[0] # get the first letter of each word
    if letter not in by_letter:
        by_letter[letter] = [word] # if the letter does not exists as a key, create it and assign the word to it as a list
    else:
        by_letter[letter].append(word) # if it does exist, append the word to the value list

by_letter

# Method 4

from collections import defaultdict

by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)

by_letter

# Method 5

for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)

by_letter

# Method 6 - dict comprehension

strings = ['foo', 'bar', 'baz']
my_dict = {val : index for index, val in enumerate(strings)}
my_dict
```
