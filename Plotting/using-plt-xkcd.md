# Using plt.xkcd

`plt.xkcd()` can be used to turn normal `matplotlib` visuals into fun, hand drawn visuals.

## Boxplots

```python
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from seaborn import load_dataset
plt.xkcd()

tips = load_dataset('tips')

plt.figure(facecolor="w", figsize=(10,5))
sns.boxplot(x='day', y='total_bill', hue='time', data=tips)
plt.show()
```

![plt_xkcd](/graph_examples/plt_xkcd.png)

## Pie charts

```python
labels = ["Python", "C+", "Ruby", "Java"]
sizes = [215,130,245,210]
explode = [0.1,0,0,0]
plt.figure(facecolor="w", figsize=(10,5))
plt.pie(sizes, labels=labels, explode=explode, autopct='%0.1f%%')
plt.axis('equal')
plt.show()
```

![plt_xkcd_2](/graph_examples/plt_xkcd_2.png)
