# Count Files in a Directory

```python
#--count how many files are generated
total = 0
for root, dir, files in os.walk(os.path.join(os.getcwd(), 'exports')):
    total += len(files)
print(f"{total} exports created.")
```
