# Removing text after a certain character

There are two good ways to do this, both achieve the same result. 

## Using `split`

```python
text = "This is a string. This should be removed. This should stay."
sep = '.'

stripped = text.split(sep=sep, maxsplit=1)[0]

print(stripped)
```

Output: `This is a string`

`strip` will split the string into a list of elements after the split. You can assign maxsplit to another value to perform further splits where detected.

```python
text = "This is a string. This should be removed. This should stay."
sep = '.'

stripped = text.split(sep=sep, maxsplit=2)

print(stripped)
```

Output: `['This is a string', ' This should be removed', ' This should stay.']`

You can then use index slicing to access whichever element of the list you require.

## Using `partition`

```python
text = 'some string... this part will be removed.'
head, sep, tail = text.partition('...')

print(head, sep, tail)
```

Output: `some string ...  this part will be removed.`

By assigning `head`, `sep` and `tail` to `text.partition` we can achieve the same result as above with index slicing. `partition` assigns anything before the argument to head, it assigns the seperator to `sep` and anything after the seperator to `tail`.
