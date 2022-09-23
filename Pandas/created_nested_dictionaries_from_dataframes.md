# Created a nested dictionary from a dataframe

This is a useful process when you need to have a singular key, with multiple sub keys and values, such as regions and countries within those regions and their population numbers.

```python
data = [['Afghanistan', 'CollegeA', 50],
        ['Afghanistan', 'CollegeB', 100],
        ['Italy', 'CollegeA', 90],
        ['Italy', 'CollegeB', 50]]

df = pd.DataFrame(data=data, columns=['Country', 'College', 'Enrolled'])
```

| Country     | College   |   Enrolled |
|:------------|:----------|-----------:|
| Afghanistan | CollegeA  |         50 |
| Afghanistan | CollegeB  |        100 |
| Italy       | CollegeA  |         90 |
| Italy       | CollegeB  |         50 |

```python
my_dict = defaultdict(dict)

for i, row in df.iterrows():
    my_dict[row.Country][row.College] = row['Enrolled']
```

```python
defaultdict(dict,
            {'Afghanistan': {'CollegeA': 50, 'CollegeB': 100},
             'Italy': {'CollegeA': 90, 'CollegeB': 50}})
```

We can then change this back to a normal dictionary using:

```python
my_dict = dict(my_dict)
```

```python
{'Afghanistan': {'CollegeA': 50, 'CollegeB': 100},
 'Italy': {'CollegeA': 90, 'CollegeB': 50}}
 ```
