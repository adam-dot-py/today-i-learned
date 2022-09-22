# Perform calculations using rows

This is useful when we want to divide certain rows by each other or subtract. A specific use case for this would be to calculate conversion.

This functionality uses `loc` and `iloc`.

```python
import pandas as pd

data = [['Applications', 100, 200],
        ['Offers', 100, 200],
        ['Acceptances', 80, 160],
        ['Enrolled', 50, 120]]

df = pd.DataFrame(data=data, columns=['Pipeline', 'FY21', 'FY22'])
df = df.set_index('Pipeline')
df.loc['Conversion', :] = df.iloc[3] / df.iloc[1] # Enrolled / Offers
```

| Pipeline     |   FY21 |   FY22 |
|:-------------|-------:|-------:|
| Applications |  100   |  200   |
| Offers       |  100   |  200   |
| Acceptances  |   80   |  160   |
| Enrolled     |   50   |  120   |
| Conversion   |    0.5 |    0.6 |

## Using a pivot table

```python
import pandas as pd

data = [['Applications', 100, 200],
        ['Offers', 100, 200],
        ['Acceptances', 80, 160],
        ['Enrolled', 50, 120]]

df = pd.DataFrame(data=data, columns=['Pipeline', 'FY21', 'FY22'])

pivot = pd.pivot_table(data=df,
                      index='Pipeline',
                      values=['FY21', 'FY22'],
                      aggfunc=sum)

pivot.loc['conversion', :] = pivot.iloc[2] / pivot.iloc[3] # Enrolled / Offers
```

| Pipeline     |   FY21 |   FY22 |
|:-------------|-------:|-------:|
| Acceptances  |   80   |  160   |
| Applications |  100   |  200   |
| Enrolled     |   50   |  120   |
| Offers       |  100   |  200   |
| conversion   |    0.5 |    0.6 |
