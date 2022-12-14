# Using datetime

## `datetime` basics

The `datetime` type contains information stored in `date` and `time`:

```python
from datetime import datetime, date, time

dt = datetime(2022, 8, 6, 14, 30, 0)

dt.day
# 6

dt.minute
# 5

dt.date()
# datetime.date(2022, 8, 6)
```

## Convert a Pandas column to datetime

Assuming a string date is in the column `pdf['date']`:

```python
import pandas as pd

pdf['date'] = pd.to_datetime(pdf['date'], format='%d-%m-%Y', errors='coerce')
```

## Using `strftime`

The `strftime` method formats a `datetime` as a string:

```python
dt.strftime ('%d/%m/%y')
# '06/08/2022'
```

## Using `strptime`

Strings can be converted (parsed) into `datetime` objects with the `strptime` function:

```python
datetime.strptime('20220608', '%y/%m/%d')
# datetime.datetime (2022, 06, 08, 0, 0) # returns zero for time information if missing from string
```

## Using `replace`

It can be useful to replace time fields of a series of `datetimes` - for example, replacing the minute and seconds fields with zero:

```python
dt.replace(minute=0, second=0)
# datetime.datetime(2022, 08, 06, 14, 0, 0)
```

## Reference table

| Type | Description                                                |
|-----:|-----------------------------------------------------------:|
| %Y   | Four-digit year                                            |
| %y   | Two-digit year                                             |
| %m   | Two-digit month [01, 12]                                   |
| %d   | Two-digit day [01, 31]                                     |
| %H   | Hour (24-hour clock) [00, 23]                              |
| %I   | Hour (12-hour clock) [01, 12]                              |
| %S   | Second [00, 61] (seconds 60, 61 account for leap seconds)  |
| %w   | Weekday as an integer [0 (Sunday), 6]                      |
| %U   | Week number of the year [00, 53]; Sunday is considered the first day of the week, and days before the first Monday of the year are week 0. |
| %W   | Week number of the year [00, 53]; Monday is considered the first day of the week, and days before the first Monday of the year are week 0. |
| %z   | UTC time zone offset as +HHMM or -HHMM; empty if time zone naive |
| %F   | Shortcut for %Y - %m - %d (e.g 2022-08-06) |
| %D   | Shortcut for %m/%d/%y (e.g 06/08/2022) |
| %B   | Shortcut for full month name           |
| %b   | Shortcut for shortened month name      |
