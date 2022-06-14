# Using asterisks and what they do

Using astersisks are not just for performing exponential functions like multiplication, but can be used for other things like:

- Using `*` and `**` to pass arguments to a function
- Using `*` and `**` to capture arguments passed into a function
- Using `*` to accept keyword-only arguments
- Using `*` to capture items during tuple unpacking
- Using `*` to unpack iterables into a list/tuple
- Using `**` to unpack dictionaries into other dictionaries

## Example - passing all arguments to print

```python
fruits = ['tomato', 'pear', 'lemon', 'apple']
print(fruits)
```

The output would be `['tomato', 'pear', 'lemon', 'apple']`, which is a `<class 'list'>` data type.

Say we wanted to access all of the elements of the as a string, we could do this:

```python
print(fruits[0], fruits[1], fruits[2], fruits[3])
```

The output would be `tomato pear lemon apple`, which works but is clumsy to code.

We can use `*` to pass all of the list items to the print function to achieve the same result:

```python
print(*fruits)
```

The output would be `tomato pear lemon apple` as a string. The '*' operator is passing all items in the `fruits` list into the `print` function as seperate arguments, without us needing to know how many arguments are in the list.

## Example - passing keyword arguments

The `**` operator can be used to pass keyword arguments. You can take the key-value pairs from a dictionary and unpack them into keyword arguments, as part of a function call:

```python
date_info = {'year' : '2022', 'month' : '04', 'day' : '28'}
filename = "{year}-{month}-{day}.txt".format(**date_info)
```

The output would be `2022-04-28.txt`.

## Using `*` and `**` multiple times

The operators can be used multiple times in function calls:

```python
fruits = ['tomato', 'pear', 'lemon', 'apple']
numbers = [1, 2, 3, 4, 5]

print(*numbers, *fruits)
```

The output would be `1 2 3 4 5 tomato pear lemon apple`, outputing all items of both lists together without defining all of the items.

The same can be done for the `**` operator: 

```python
date_info = {'year' : '2022', 'month' : '04', 'day' : '28'}
track_info = {'artist' : 'John Mayer', 'title' : 'Gravity'}
filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(
    **date_info,
    **track_info)
```

The output would be `2022-04-28-John Mayer-Gravity.txt`. Care needs to be taken when using `**` multiple times though, as you cannot pass the same keyword argument multiple times. The keys must be distinct or an exception will be raised.

## Example - Positional arguments with keyword only arguments

Keyword-only arguments are function arguments which can only be specified using the keyword syntax, meaning they cannot be specified positionally.

```python
brand_colours = {'bmw' : 'blue', 'mercedez' : 'silver', 'ferrari' : 'red'}
def get_multiple(*keys, dictionary, default=None): 
    return [
        dictionary.get(key, default)
        for key in keys
    ]

get_multiple('bmw', 'ferrari', 'ford', dictionary=brand_colours, default='Unknown')
```

This would return `['blue', 'red', 'unknown']`. The arguments `dictionary` and `default` come after `*keys` which means they can only be specified as keyword arguments. If they get specified positionally an error will occur, like so: 

```python
get_multiple('ferrari', 'bmw', dictionary=brand_colours, 'mercedez')
```

## Example Function

```python
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result
```

`print(addition(10, 20, 10))`
Return: 40

Can also pass a list of items:

```python
myNums = [10, 20, 10]
print(addition(*myNums))
```

Return: 40
