# Convert String Column to Datetime

In Pandas you can convert a string column into a datetime, by calling `pd.to_datetime`. 

**Example**

`planets['year_dt'] = pd.to_datetime(planets['year], format='%Y')` would convert a date value of 2006 to 2006-01-01, the first day of the year. Additional customisation can be achieved by changing the format parameter. 