# List files in a directory

To list files, we can use the `os` module in Python. In the below example, we simply `print` the names of files ending in `.xlsx` in the script directory but this can be used to do more advanced things like combining files or creating dataframes.

```python
import os

directory = './'
for file os.listdir(directory):
    if file.endswith('.xlsx'):
        print(file)
```
