# Create a dataframe of dummy dates

Useful for creating a dataframe consisting of a range of dates and a good example of list comprehension.

```python
import pandas as pd
from datetime import datetime

years_to_fill = list(range(2000,2041))

df = pd.DataFrame({"the_date" : [datetime(year, 12, 31) for year in years_to_fill]})
df['source_iso_country_code'] = "UNK"
```
