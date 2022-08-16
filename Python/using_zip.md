# Using Zip

## Typical usage

```python
# given a zipped sequence, zip can be applied in a clever way to unzip the sequence.
# another way to think about this is converting a list of rows into a list of columns.

players = [('Mohamaded', 'Salah'), ('Luis', 'Diaz'), ('Darwin', 'Nunez')]

first_names, last_names = zip(*players) # asterisk takes all the tuple values

print(first_names)
print(last_names)
```

('Mohamaded', 'Luis', 'Darwin')
('Salah', 'Diaz', 'Nunez')

You can also use it to create dictionaries:

```python

keys = [1,2,3]
values = ['foo','baz','bar']
d = dict(zip(keys, values))
print(d)
```

{1: 'foo', 2: 'bar', 3: 'baz'}
