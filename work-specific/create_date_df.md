# Create a date DataFrame

The below function can be used to create a `DataFrame` containing dates and their corresponding metadata. Useful for PowerBI!

```python
import pandas as pd

def create_date_table(start='2000-01-01', end='2030-12-31'):

  df = pd.DataFrame({"Date": pd.date_range(start, end, freq='D').to_series()})
  df["Day"] = df.Date.dt.day
  df["Month"] = df.Date.dt.month
  df["FirstOfMonth"] = df.Date.dt.to_period('M').dt.to_timestamp()
  df["MonthName"] = df.Date.dt.month_name()
  df["Week"] = df.Date.dt.week
  df["ISOweek"] = df.Date.dt.weekofyear
  df["DayOfWeek"] = df.Date.dt.dayofweek
  df["Quarter"] = df.Date.dt.quarter
  df["Year"] = df.Date.dt.year
  df["FirstOfYear"] = df.Date.dt.to_period('Y').dt.to_timestamp()
  df["Style112"] = df.Date.dt.strftime('%Y%m%d')
  df["Style101"] = df.Date.dt.strftime('%d/%m/%Y')
  df.Date = df.Date.dt.strftime('%Y-%m-%d')
  df.FirstOfMonth = df.FirstOfMonth.dt.strftime('%Y-%m-%d')
  df.FirstOfYear = df.FirstOfYear.dt.strftime('%Y-%m-%d')
  return df

df = create_date_table()
```
