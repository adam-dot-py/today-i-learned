# Rename directories

Using the `os` module and `Path` function, we can iterate over a directory and rename folders and subfolders. In the below example, we iterate over the directory and rename any folder that is named July.

```python
for root, dirs, files in os.walk(os.getcwd()):
    for dir_name in dirs:
        if dir_name == "July":
            dir_path = Path(root, dir_name)
            new_dir_path = Path(root, "June")
            os.rename(dir_path, new_dir_path)
```
