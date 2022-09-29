# Calculate days between two dates

This is useful for calculating how many days are between two given dates. Can be adjusted for other calculations.

```python
from datetime import datetime

def days_between(date_1, date_2):
    date_1 = datetime.strptime(date_1, "%d/%m/%Y")
    date_2 = datetime.strptime(date_2, "%d/%m/%Y")
    return abs((date_2 - date_1).days)

days_between('13/08/2022', '18/08/2022')
```
