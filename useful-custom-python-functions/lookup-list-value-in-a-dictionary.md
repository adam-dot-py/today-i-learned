# Lookup a list value in a dictionary

This is good for when you have dictionary keys where the values are lists and you want to iterate over them or lookup a value.

To return a specific index position relating to the key:

```python
def lookup_value(dictionary, key, item):
    '''lookup_value(dictionary, key, item) --> looks up a key and returns a value based on index position in a nested dictionary
    where values are lists.

    Parameters:
    dictionary: the dictionary to search for keys and values
    subject: the subject to search for (or, the key)
    item: the index position to specify with item to return
    '''
    for k, v in my_dict.items():
        if k == key:
            if(isinstance(v, list)):
                return v[item]
```

To print all of the values relating to the key:

```python
def lookup_value(dictionary, key, item):
    '''lookup_value(dictionary, key, item) --> looks up a key and returns a value based on index position in a nested dictionary
    where values are lists.

    Parameters:
    dictionary: the dictionary to search for keys and values
    subject: the subject to search for (or, the key)
    item: the index position to specify with item to return
    '''
    for k, v in my_dict.items():
        if k == key:
            if(isinstance(v, list)):
                for values in v:
                    print(values)
```
