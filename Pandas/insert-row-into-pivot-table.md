# Insert a row into a pivot table

To insert a row into a `pivot table`, the below can be used. In this example, the `pivot table` consists of an `index` and a `column` called `count` (which is created as a result of only a `value` argument being passed but no `column`.).

The purpose of the `pivot table` is to count the daily number of responses to a survey. Each index represents a day. Therefore, to start from zero, we insert a date before the start of the survey and set its value to `0`. We set the date and value to variables, then use `pd.DataFrame` to construct the new row, before using `pd.concat` to append the two new pivot tables (or dataframes) together.

```python
# pivot the data and convert values to a cumulative sum
pvt = df.pivot_table(index='date_created', values='count', aggfunc=np.sum) \
        .apply(lambda x: x.cumsum())

# start the count from zero by inserting this line
start_date = pd.to_datetime('2023-03-23')
start_count = 0    
new_row = pd.DataFrame({pvt.columns[0] : [start_count]}, index=[start_date])
pvt = pd.concat([new_row, pvt])
```

You can also pass new row into standard `dataframes` like so:

```python
import pandas as pd

x = ['foo', 'bar', 'baz']
y = [10, 20, 30]

df = pd.DataFrame({'Names' : x, 'Values' : y})
new_row = pd.DataFrame({'Names' : 'bazbar', 'Values' : 40}, index=[len(df.index)])

pdf = pd.concat([df, new_row])
```

|    | Names   |   Values |
|---:|:--------|---------:|
|  0 | foo     |       10 |
|  1 | bar     |       20 |
|  2 | baz     |       30 |
|  3 | bazbar  |       40 |

It is important to always pass an `index` argument if values are not scalar i.e passed in `[]`. If values _are_ scalar, then there is no need to pass an `index` argument.
