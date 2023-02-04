# Dynamically reference user root

This can be done using the `os` module, part of the Python standard library.

This is useful when a path needs to be referenced that is present on someones elses computer but needs to include the user root.

```python
import os
import pandas as pd
from os.path import expanduser

home = expanduser("~")
my_path = r"folder\path-to-file.txt"

print(os.path.join(home, my_path))
```

`C:\Users\Adam.Lowe\folder\path-to-file.txt`
