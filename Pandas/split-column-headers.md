# Split column headers

This is useful if you have a column headers that you wish to split at a certain character. Use `str.split()` and pass the given split argument and then use indexing to select the returning required value. In the below I want the first value to the left of the split, so pass `0` index position.

```python
df.columns = [col.split('\n')[0] for col in df.columns]
```
