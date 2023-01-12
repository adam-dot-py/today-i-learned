# Replace values in a column

Replacing values in columns can be done in different ways. Below are two examples.

## Example 1

In this example you can pass a nested dictionary with the column names and then the values to change.

```python

pdf.replace({'Column1' : {'oldvalue' : 'newvalue'}, inplace=True)

# or

pdf = pdf.replace({'Column1' : {'oldvalue' : 'newvalue'})
```

## Example 2

In this example you can change a value specifically in a column.

```python
pdf['Column1] = pdf['Column1].replace('oldvalue', 'newvalue')

# or

pdf['Col]
```

## Example 3

This method allows you to replace different types of values and also across multiple columns.

```python
replace_values = {'J' : 1, 'N' : 0}
pdf[['Dropout', 'Switch']] = pdf[['Dropout', 'Switch']].replace(replace_values)
```
