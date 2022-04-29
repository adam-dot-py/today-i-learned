# Create a dumbbell chart

Dumbbell charts are great for showing the difference between two variables.

```python
%matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

d = {'College' : ['ARUC', 'BPC', 'ICRGU', 'TCSU'],
     'NPS' : [70, 80, 60, 40],
     'NPS + 1 Model' : [80, 90, 70, 80]}

df = pd.DataFrame(data=d)
df.sort_values(by='College', ascending=False, inplace=True) # invert the y axis

my_range = range(1, len(df.index)+1) # so the range does not include column header
plt.hlines(y=my_range, 
           xmin=df['NPS'],
           xmax=df['NPS + 1 Model'],
           color='grey',
           alpha=0.4)

plt.scatter(x=df['NPS'], 
            y=my_range, 
            color='red', 
            label='NPS',
            marker='o',
            s=80)


plt.scatter(x=df['NPS + 1 Model'], 
            y=my_range, 
            color='blue', 
            label='NPS + 1 Model',
            marker='o',
            s=80)

plt.yticks(my_range, df['College'])
plt.xticks(np.arange(-100, 101, 10), rotation=90)
plt.xlabel('NPS Score')
plt.ylabel('College')
plt.legend()
plt.tight_layout()
```

![matplotlib scatter chart](/graph_examples/matplotlib_scatter.png)