# Convert Seconds to Various Timeseries

This class contains functions which parses seconds into other `floats`.

```python
class convert():
    """
    A class to convert seconds to various formats.
    --------------
    seconds : float
      The number of seconds elapsed between the current timestamp and the previous timestamp.

    Methods
    --------------  
    to_minutes()
      Convert seconds to minutes
    to_hours()
      Convert seconds to hours
    to_days()
      Convert seconds to days
    """

    def __init__(self, seconds: float):
        self.seconds = seconds
    
    def to_minutes(self):
        minutes = self.seconds // 60
        return minutes
      
    def to_hours(self):
        hour = self.seconds // 3600
        return hour
      
    def to_days(self):
        days = self.seconds // 86400
        return days
    
    def to_hours(self):
        hour = self.seconds // 3600
        return hour
```
