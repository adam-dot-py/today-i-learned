# Write, append and read files

You can write files in Python using the below examples

## Writing a text file

```python
# This would overwrite a file with the new string
with open('file.txt', 'w') as fp: 
    fp.write("This is a string.")
```

You can also write multiple lines like this:

```python
line1 = "First line"
line2 = "Second line"
line3 = "Third line"
with open('my_file.txt','w') as fp:
    fp.writelines([line1, line2, line3])
```

or like this:

```python
line1 = "First line"
line2 = "Second line"
line3 = "Third line"
with open('my_file.txt','w') as fp:
    fp.write(f'{line1}\n{line2}\n{line3}\n')
```

## Appending a text file

```python
# This would append a file with the new string
with open('file.txt', 'a') as fp: 
    fp.write("This is a string.")
```

## Reading a text file

```python
# This would read a file
with open('file.txt', 'r') as fp: 
    print(fp.read())
```

## Writing JSON

```python
# This would overwrite a file
with open('data.json', 'w') as fp: 
    json.dump(data, fp, indent=4, sort_keys=True)
```
