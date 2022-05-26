# Sum columns

Summing columns can be done via the `df.sum()` method with the `df.loc[]` method. When summing columns, be aware that this does add `column_total` to the `index`.

```python
import pandas

df = pandas.DataFrame({'col1' : [1, 2], 'col2' : [3, 4], 'col3' : ['a', 'b']})

df.loc['column_total', :] = df.sum(numeric_only=True, axis=0) # add to row index, sum all the columns
df.loc[:, 'row_total'] = df.sum(numeric_only=True, axis=1) # add to column index, sum sll the rows
```

|              |   col1 |   col2 | col3   |   row_total |
|:-------------|-------:|-------:|:-------|------------:|
| 0            |      1 |      3 | a      |           4 |
| 1            |      2 |      4 | b      |           6 |
| column_total |      3 |      7 | nan    |          10 |

We use `:` within `df.loc[]` to slice the DataFrame.

The syntax for `df.loc[]` is `df.loc[row-label, column-label]`. Inside of the `loc[]` method, you need to specify the labels of the rows or columns that you want to retrieve. Leaving just a `:` returns all, either all columns or all rows. `df.loc[]` uses the index or column labels. You can use `df.iloc[]` for numeric positional arguments.
