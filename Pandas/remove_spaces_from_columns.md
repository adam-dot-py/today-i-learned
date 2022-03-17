## Remove spaces from columns

The below can be used to remove spaces anywhere in column headers
```python
df.columns = [x.replace(' ','') for x in df.columns]
```

Additionally, the following can be used to remove whitespace at the beginning of end of a column header

```python
df.columns = [x.strip() for x in df.columns]
```