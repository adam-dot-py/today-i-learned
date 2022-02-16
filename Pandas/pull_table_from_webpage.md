# Pulling tables from websites into Dataframes

Pandas can pull tables from websites in combination with the requests module. 


```python
import requests
import pandas as pd

url = 'http://www.ffiec.gov/census/report.aspx?year=2011&state=01&report=demographic&msa=11500' # Your URL
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1] # Adjust if multiple tables
print(df)
df.to_csv('my data.csv')
```
