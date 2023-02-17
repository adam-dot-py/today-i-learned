# Copy directories

```python
import shutil
import os

# Define the source and destination folders
source_folder = '/path/to/source/folder'
destination_folder = '/path/to/destination/folder'

# Use shutil.copytree to copy the source folder to the destination folder
shutil.copytree(source_folder, destination_folder)
```