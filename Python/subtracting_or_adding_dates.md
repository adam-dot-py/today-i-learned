# Subtracting or adding dates together

The below example can be used to find the previous day date, and can be configured to subtracting further days using the `days` variable in timedelta.

```python
from datetime import date, timedelta
yesterday = date.today() - timedelta(days=1)
yesterday.strftime('%m-%d-%y')
```
