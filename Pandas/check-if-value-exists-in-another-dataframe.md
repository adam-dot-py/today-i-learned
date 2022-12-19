# Check if value exists in another dataframe

This can be done using `pandas.assign`. It allows you to check an exist column value exists in another, in the same dataframe or from another dataframe.

```python

d = {'List1' : [12345, 'abc', 'def', 6789], 'List2' : ['abc','def',23456,12345]}

pdf = pd.DataFrame(data=d)
pdf = pdf.assign(inList1=pdf['List2'].isin(pdf['List1']).astype(int))
```

| List1   | List2   |   inList1 |
|:--------|:--------|----------:|
| 12345   | abc     |         1 |
| abc     | def     |         1 |
| def     | 23456   |         0 |
| 6789    | 12345   |         1 |

## Check if value exists from another dataframe

In this example, we are checking if the value of `ndf['List2']` exists in `pdf['List1']`.

```python
d1 = {'List1' : [12345, 'abc', 'def', 6789]}
d2 = {'List2' : ['abc','def',23456,12345]}

pdf = pd.DataFrame(data=d1)
ndf = pd.DataFrame(data=d2)

pdf = pdf.assign(inList2=pdf['List1'].isin(ndf['List2']).astype(int))
```

| List1   |   inList2 |
|:--------|----------:|
| 12345   |         1 |
| abc     |         1 |
| def     |         1 |
| 6789    |         0 |
