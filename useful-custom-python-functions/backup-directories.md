# Backup directories

A custom script to backup a given folder to another location, such as a network drive.

```python
def main():
    
    # packages 
    import shutil

    def backup_folder():
        """Copy a folder to another destination.
        
        Parameters
        ----------------------------------------
        src_folder : input
          The folder to be copied
        dst_folder : input
          The destination to copy to
        """
        src_folder = str(input("Folder to backup: "))
        dst_folder = str(input("Location for backup: "))
        print(f"Copying {src_folder} -> {dst_folder}")
        try:
            shutil.copytree(src=src_folder,
                            dst=dst_folder,
                            ignore=None,
                            dirs_exist_ok=True)
        except Exception as e:
            print(f"Failed with the error -> {e}")
        print("Complete")
        
    backup_folder()

if __name__ == "__main__":
    main()
```
