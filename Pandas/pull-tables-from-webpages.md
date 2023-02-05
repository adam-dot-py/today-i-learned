# Pulling tables from websites into Dataframes

Pandas can pull tables from websites in combination with the requests module.

```python
import requests
import pandas as pd

url = 'http://www.ffiec.gov/census/report.aspx?year=2011&state=01&report=demographic&msa=11500' # Your URL
html = requests.get(url).content
df = pd.read_html(html)[0] # get the first table
```

## Advanced usage

In this example, we can use `Selenium` to load a dynamic `javascript` table on a webpage. There are two tables and code extracts both before merging them together.

```python
import re
import pycountry
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options

urls = ['https://www.timeshighereducation.com/world-university-rankings/2023/world-ranking#!/page/0/length/-1/sort_by/rank/sort_order/asc/cols/stats',
        'https://www.timeshighereducation.com/world-university-rankings/2023/world-ranking#!/page/0/length/-1/sort_by/rank/sort_order/asc/cols/scores']

options = Options()
options.add_argument('-headless')

for i, url in enumerate(urls):
    driver = webdriver.Firefox(options=options)
    
    # get the first table
    if i == 0:
        driver.get(url)
        print(f'Firefox -> opened {url}')
        for i in range(1,4):
            time.sleep(i)
            print(f"Waiting {i} second(s)...")
        soup = BeautifulSoup(driver.page_source, 'lxml')
        table = soup.find_all('table')
        df1 = pd.read_html(str(table))[0]
        driver.close()
    else:
        # then merge the second table
        driver.get(url)
        print(f'Firefox -> opened {url}')
        for i in range(1,4):
            time.sleep(i)
            print(f"Waiting {i} second(s)...")
        soup = BeautifulSoup(driver.page_source, 'lxml')
        table = soup.find_all('table')
        df2 = pd.read_html(str(table))[0]
        driver.close()
        
        # merge df1 and df2 together - merges on the index, and only columns that are not matching.
        merge_cols = df2.columns.difference(df1.columns)       
        fdf = pd.merge(df1, df2[merge_cols], left_index=True, right_index=True, how='outer')

# create a pattern that will match any country in pycountry.countries
names = '|'.join([country.name+"$" for country in pycountry.countries])
pattern = re.compile(names, re.UNICODE | re.IGNORECASE)

'''
We apply some regex to clean up the university column.
  - First, take out any country name found at the end of the string
  - Then, take out any instance of the word Explore at the end of a string
  - Finally, Hong Kong is an edge case. Take out the second instance of it appearing in a string.
'''
fdf['Name Country/Region'] = fdf['Name Country/Region'].apply(lambda x: pattern.sub("", x).strip())
fdf['Name Country/Region'] = fdf['Name Country/Region'].apply(lambda x: re.sub(pattern=r"explore$", string=x, repl="", flags=re.IGNORECASE))
fdf['Name Country/Region'] = fdf['Name Country/Region'].apply(lambda x: re.sub(pattern=r"Hong Kong$", string=x, repl="", count=1))

'''
Some more data cleanup
'''
fdf = fdf.astype({'Female:Male Ratio' : str, 'Rank' : str})
```
