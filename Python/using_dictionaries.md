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
