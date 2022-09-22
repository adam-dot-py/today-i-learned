# Perform calculations on multi-level pivot tables

Performing calculations on multi level indexes is particularly useful when we want to calculate the percentage or proportion of a variable. In the below example, we can look at each countries share of the total `Enrolled` and then also the share of the `Region`.  

```python
import pandas as pd

lst = [['EMEAA', 'Afghanistan', 20], ['EMEAA', 'Iran', 80],
       ['EUROPE', 'Italy', 50], ['EUROPE', 'Spain', 50]]

df = pd.DataFrame(data=lst, columns=['Region', 'Country', 'Enrolled'])
```

| Region   | Country     |   Enrolled |
|:---------|:------------|-----------:|
| EMEAA    | Afghanistan |         20 |
| EMEAA    | Iran        |         80 |
| EUROPE   | Italy       |         50 |
| EUROPE   | Spain       |         50 |

```python
grouped = pd.pivot_table(data=df,
                          index=['Region', 'Country'],
                          values='Enrolled',
                          aggfunc=sum)

grouped['overallShare'] = grouped['Enrolled'] / grouped['Enrolled'].sum(axis=0) # calculates on the total sum of enrolled
grouped['regionShare'] = grouped['Enrolled'] / grouped.groupby(level=0)['Enrolled'].transform(sum) # calculates on the region multi-level index
```

|  Region   |     Country   |   Enrolled |   overallShare |   regionShare |
|:---------:|--------------:|-----------:|---------------:|--------------:|
| EMEAA     | Afghanistan   |         20 |           0.1  |           0.2 |
| EMEAA     | Iran          |         80 |           0.4  |           0.8 |
| EUROPE    |  Italy        |         50 |           0.25 |           0.5 |
| EUROPE    |  Spain        |         50 |           0.25 |           0.5 |
