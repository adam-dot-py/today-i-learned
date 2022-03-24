# Count the number of files in a directory

Counting files in Python can be done via the `os` module and the `os.walk()` method.

## Count all files in directory (including subdirectory)

```python
total = 0

for root, dirs, files in os.walk(your_dir):
    total += len(files)

print(f'The total number of files is {total')
```

## Count all files in only certain directories

```python
total = 0
exclude = set(['.git'])

for root, dirs, files in os.walk(your_dir):
    dirs[:] = [d for d in dirs if d not in exclude]
    total += len(files)

print(f'The total number of files is {total}')
```
