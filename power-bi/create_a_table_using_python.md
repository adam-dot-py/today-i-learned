# Create a table in Power BI using Python

This can be used to create a date table in PowerBI but the functionality can be used to create data tables of any kind using the power of Python.

This example creates a data table comprised of `dates` and the many different customisations for `datetime` and the `dt` accessor, as well as `strftime` transformations.

- [pd.date_range documentation](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html)
- [strftime documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

```python
import pandas as pd

start = '1/1/2020' # start date
end = '12/31/2021' # end date

df = pd.DataFrame(pd.date_range(start, end, freq='H', tz='GMT'), columns = ['Datetime']) # tz is timezome, freq relates to time frequency (H is every hour).
df['LocaleTime'] = df["Datetime"].dt.strftime('%c')
df['Day'] =df["Datetime"].dt.day
df['Month'] = df["Datetime"].dt.month
df['Year'] = df["Datetime"].dt.year
df['time'] =df["Datetime"].dt.time
df['timezone'] =df["Datetime"].dt.tz
df['Hour'] =df["Datetime"].dt.hour
df['Quarter'] =df["Datetime"].dt.quarter
df['MonthName'] = df["Datetime"].dt.strftime('%b')
df['Week Name'] = df["Datetime"].dt.strftime('%A')
df['WeekNumber'] = df["Datetime"].dt.strftime('%W')
df['Weekday'] = df["Datetime"].dt.weekday
df['TimeofDay'] = df["Datetime"].dt.strftime('%p')
df['UTC_offset'] = df["Datetime"].dt.strftime('%z')
df['DayofYEar'] = df["Datetime"].dt.dayofyear
df['Century'] = df["Datetime"].dt.strftime('%Y')
```
