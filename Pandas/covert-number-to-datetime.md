# Convert a number to datetime

To convert a column with a value of `44830` to a date format like `DD/MM/YYYY`, you can use the `to_datetime()` function in `Pandas`. The number `44830` represents the number of days since `January 1, 1900`, which is the `Excel` date system.

```python
df['Start Date'] = pd.to_datetime(df['Start Date'], origin='1899-12-30', unit='D').dt.strftime('%d/%m/%Y')
```

- The `to_datetime()` function is used to convert the column to a datetime format.
- The origin parameter is set to `1899-12-30` to align with the `Excel` date system, which considers `January 1, 1900`, as day 1.
- The unit parameter is set to `D` to indicate that the values in the column represent the number of days.
- Finally, `dt.strftime('%d/%m/%Y')` is used to format the resulting datetime values as `DD/MM/YYYY`.
