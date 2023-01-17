# Create a zipped folder

To turn a directory into a zipped folder, we can use `shututil`. `shututil` is part of the Python Standard Library.

## Syntax

`shutuil.make_archive(base_name, format, base_dir)`

## Example

`shututil.make_archive(base_name='tables_zipped', format='zip', base_dir='my_dir')`

We can also use `zipfile`, allowing greater control over which files are to be zipped:

```python
import os
import zipfile
    
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))

with zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir('tmp/', zipf)
```
