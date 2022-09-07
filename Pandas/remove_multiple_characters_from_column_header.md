# Remove multiple strings from column header

```python
for char in list(' -?:,;{}()\n\t='):
    pdf.columns = [x.replace(char,'') for x in pdf.columns]
```