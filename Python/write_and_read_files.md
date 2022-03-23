## Write to file

You can write files in Python using the below examples

### Writing a text file and reading

```python
with open('file.txt', 'w') as fp: 
    fp.write("This is a string.")
```

```python
with open('file.txt', 'r') as fp: 
    print(fp.read())
```

### Writing JSON

```python
with open('data.json', 'w') as fp: 
    json.dump(data, fp, indent=4, sort_keys=True)
```
