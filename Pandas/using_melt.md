# Using `pd.melt`

`pandas.melt` is useful for transposing a wide format table to a long table`.

## Melt entire DataFrame based on id

```python
df = pandas.DataFrame({"College" : ['College 1', 'College 2', 'College 3', 'College 4', 'College 5', 'College 6'],
                       "Student recruitment into college" : [3.0, 4.0, 3.0, 3.0, 3.0, 3.0], 
                       "Student progression to university" : [2.0, 3.0, 4.0, 3.0, 3.0, np.nan],
                       "Student performance post progression" : [3.0, 4.0, 3.0, 3.0, 2.5, np.nan],
                       "Sales and marketing integration" : [2.0, 4.0, 4.0, 3.0, np.nan, 3.0],
                       "Student experience" : [3.0, 4.0, 4.0, 3.0, 2.5, 4.0],
                       "Uni and college strategy" : [4.0, 3.0, 4.0, 3.0, 2.5, 4.0],
                       "Overall" : [2.83, 3.67, 3.66, 3.00, 2.25, 3.00]})

melt = pandas.melt(df, 
                   id_vars=['College'], 
                   var_name='Question', 
                   value_name='Score')
```

| College   | Question                         |   Score |
|:----------|:---------------------------------|--------:|
| College 1 | Student recruitment into college |       3 |
| College 2 | Student recruitment into college |       4 |
| College 3 | Student recruitment into college |       3 |
| College 4 | Student recruitment into college |       3 |
| College 5 | Student recruitment into college |       3 |

## Melt by ID and certain columns

You can also melt by certain columns:

```python
melt = pandas.melt(df,
                   id_vars=['College'],
                   value_vars=['Student recruitment into college', 'Student progression to university'], 
                   var_name='Question', 
                   value_name='Score')
```

| College   | Question                          |   Score |
|:----------|:----------------------------------|--------:|
| College 1 | Student recruitment into college  |       3 |
| College 2 | Student recruitment into college  |       4 |
| College 3 | Student recruitment into college  |       3 |
| College 4 | Student recruitment into college  |       3 |
| College 5 | Student recruitment into college  |       3 |
| College 6 | Student recruitment into college  |       3 |
| College 1 | Student progression to university |       2 |
| College 2 | Student progression to university |       3 |
| College 3 | Student progression to university |       4 |
| College 4 | Student progression to university |       3 |
| College 5 | Student progression to university |       3 |
| College 6 | Student progression to university |     nan |
