# Using `os`

`os` is a module that allows us to explore the file system of a computer. We can use it to locate files, create directories, create new files and much more. Below are examples of using `os` and its use cases.

## Iterate over CSVs to create a dataframe

Using `os` to walk through files in a directory which meet specific conditions, like a certain extension and a string in its file name:

```python
all_files = []
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if (file.endswith(".csv")) & ("Table-28" in file):
            print(f"{file} --> to dataframe")
            all_files.append(os.path.join(root, file))

combined = pd.concat([pd.read_csv(f, skiprows=14, delimiter=',', header='infer') for f in all_files])
```

## Reference the root user path on any os

```python
import os

home = os.path.expanduser('~')
print(home)

path_to_file = os.path.join(home, 'my_folder')
print(path_to_file)
```

```
/home/adam
/home/adam/my_folder
```