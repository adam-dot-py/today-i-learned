# Read html into a dataframe

Sometimes we may want to scrape a table from a website, in which we would use something like `BeautifulSoup` combined with `Pandas`. In the below example, we use `BeautifulSoup` with `requests` to scrape a table showing populations of countries.

```python
import pandas as pd
import requests
from io import StringIO
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/world-population/population-by-country/"
html = requests.get(url).content

soup = BeautifulSoup(html, "html")
table = soup.find_all('table')
html_content = '\n'.join(str(item) for item in table)
html_io = StringIO(html_content)

df = pd.read_html(html_io, index_col='#')[0]
```

|   # | Country (or dependency)   |   Population  (2023) | Yearly  Change   |   Net  Change |   Density  (P/Km²) |   Land Area  (Km²) |   Migrants  (net) |   Fert.  Rate |   Med.  Age | Urban  Pop %   | World  Share   |
|----:|:--------------------------|---------------------:|:-----------------|--------------:|-------------------:|-------------------:|------------------:|--------------:|------------:|:---------------|:---------------|
|   1 | India                     |           1428627663 | 0.81 %           |      11454490 |                481 |            2973190 |           -486136 |           2   |          28 | 36 %           | 17.76 %        |
|   2 | China                     |           1425671352 | -0.02 %          |       -215985 |                152 |            9388211 |           -310220 |           1.2 |          39 | 65 %           | 17.72 %        |
|   3 | United States             |            339996563 | 0.50 %           |       1706706 |                 37 |            9147420 |            999700 |           1.7 |          38 | 83 %           | 4.23 %         |
|   4 | Indonesia                 |            277534122 | 0.74 %           |       2032783 |                153 |            1811570 |            -49997 |           2.1 |          30 | 59 %           | 3.45 %         |
|   5 | Pakistan                  |            240485658 | 1.98 %           |       4660796 |                312 |             770880 |           -165988 |           3.3 |          21 | 35 %           | 2.99 %         |