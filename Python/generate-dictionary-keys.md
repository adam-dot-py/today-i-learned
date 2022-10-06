# Generate Dictionary Keys

Useful for when you have an list and you want to assign incremental value.

## Using Range

```python
my_dict = {f"Key {n}" : "Value {n}" for n in range(5)}
```

{'Key 0': ' Value 0', 'Key 1': ' Value 1', 'Key 2': ' Value 2', 'Key 3': ' Value 3', 'Key 4': ' Value 4'}

## Using Enumerate

```python
fruits = ['Banana', 'Apple', 'Pear']
fruit_dict = dict(list(enumerate(fruits)))
```

{0: 'Banana', 1: 'Apple', 2: 'Pear'}

## Using For Loop

```python
fruits = ['Banana', 'Apple', 'Pear']
fruit_dict = {}

for i in range(len(fruits)):
    fruit_dict[fruits[i]] = i
```

{'Banana': 0, 'Apple': 1, 'Pear': 2}

## Using Zip

```python
fruits = ['Banana', 'Apple', 'Pear']
key_values = [5,10,20]
fruit_dict = dict(zip(fruits,key_values))
```

{'Banana': 5, 'Apple': 10, 'Pear': 20}
