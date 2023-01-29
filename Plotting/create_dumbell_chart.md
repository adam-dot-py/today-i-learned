# Create a dumbbell chart

Dumbbell charts are great for showing the difference between two variables.

## Example 1

import matplotlib.pyplot as plt

```python
# Data for the two ends of the dumbbell
x1 = [1, 2, 3]
x2 = [1.5, 2.5, 3.5]
colleges = ['A', 'B', 'C']

# Create the scatter plot for the two ends of the dumbbell
plt.scatter(x1, colleges, c='b', marker='o')
plt.scatter(x2, colleges, c='r', marker='o')

# Draw the connecting lines between the two ends of the dumbbell
for i in range(len(x1)):
    plt.plot([x1[i], x2[i]], [y1[i], y2[i]], 'k-')
    
# Add labels and show the plot
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```

![Example dumbbell chart](/graph_examples/plt_dumbell_chart_example.png)

## Example 2

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
