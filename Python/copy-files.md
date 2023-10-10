# Copy Files

In the below example, I used a script to copy files from a directory to another directory.

```python
import shutil
import os

# get the user path and destination path so it can be executed by anyone... if they have synced the folder to their machine.
user_path = os.path.expanduser("~")
teams_path_name = "Navitas Pty Ltd\DATA+ Data Accuracy, Transparency, and Advancements - Exception Reports\Reports"
teams_path = os.path.join(user_path, teams_path_name) # create the destination path 

# source destination of the files to copy
source_path = 'exported-pdfs'

# Create a list of the files to copy
files_to_copy = os.listdir(source_path)

# Copy the files to the new destination
try:
    for file in files_to_copy:
        source_file_path = os.path.join(source_path, file)
        destination_file_path = os.path.join(teams_path, file)
        shutil.copy(source_file_path, destination_file_path)
    print(f"Complete. Copied {len(files_to_copy)} files.")
except Exception as e:
    print(f"Failed with exception: {e}")
```
