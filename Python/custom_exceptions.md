# Custom exceptions

Custom exceptions allow you to control error messages in Python, giving code more readability and an easier workflow for the user to debug.

```python
# setup custom exceptions as classes
class NoBambooFiles(Exception):
    """Exception raised when Bamboo_ is not in the file name."""
    pass

class TooManyFilesInSharepoint(Exception):
  """Exception raised when there are too many files in the source directory"""
  pass
```

```python
# iterate through files
try:
    files = folder.files
    if len(files) == 1:
        for file in files:
            if "Bamboo_" in file["Name"]:
                file_name = file["Name"].split(".")[0]
                suffix = file["Name"].split(".")[-1]
                sharepoint_file = folder.get_file(file["Name"])

                with NamedTemporaryFile(
                    delete=False, suffix="." + suffix
                ) as tmp:
                    tmp.write(sharepoint_file)

                    return tmp.name, file_name
            else:
                raise NoBambooFiles(
                    "Files in the directory are not in the nominal format. Please review."
                )
    else:
        raise TooManyFilesInSharepoint(
            "There is more than 1 file or none at all in the ingestion location. Please review."
        )
```