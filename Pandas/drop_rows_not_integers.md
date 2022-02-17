## Dropping rows that are not integers (numbers)

In Pandas, you can easily drop rows that are not integers by using the `isdigit` function. The example below pulls data from The Guardian's University Rankings Table, but the initial `dataframe` has rows with column headers parsed together. 

```python

import pandas as pd
import requests

url = 'https://www.theguardian.com/education/ng-interactive/2021/sep/11/the-best-uk-universities-2022-rankings'
html = requests.get(url).content
df_list = pd.read_html(html)

# Inspect the dataframes
df = df_list[-1]

# This converts the values in the column to strings and then checks if it's a digit - true values are returned, resulting in the expected dataframe.
df = df[df['2022'].apply(lambda x: str(x).isdigit())]
df.head()
```