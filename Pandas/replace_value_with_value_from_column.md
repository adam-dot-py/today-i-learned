## Replace a column value with a value from another column

You can replace a value in a column with the value from another, based on a condition, using the below:

```python
df['col1'] = np.where(df['col1'] == 0, df['col2'], df['col1'])
```
The above statement says where the value is equal to zero in `col1`, replace it with the value of `col2`, if not then leave it as `col1`.