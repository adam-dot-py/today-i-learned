# Create a barplot

## Simple bar plot

```python
import pandas
import matplotlib.pyplot as plt

df = pandas.DataFrame({"College" : ['College A', 'College B'],
                       "Overall" : [2.83, 3.67]})

df.plot(x='College', y='Overall', kind='bar') ] # can pass a list x or y for multiple plots
plt.tight_layout()
plt.show()
```

![Barplot example 2](/graph_examples/barplots_2.png)

## Overlaying bars

You can also overlay bar charts to create interesting visuals, like showing target vs actual:

```python
import numpy as np
import pandas as pd


d = {"University" : ['College1', 'College2', 'College3'],
     "Actual" : [1000, 2000,3000],
     "Target" : [500, 1000, 2000]}

test = pd.DataFrame(data=d)

fig, ax = plt.subplots(figsize=(10,6))
test.plot(kind='bar', x='University', y='Actual', ax=ax, width=0.3, color='#007F7B', edgecolor='black', linewidth=1)
test.plot(kind='bar', x='University', y='Target', ax=ax, width=0.4, alpha=0.8, color='grey', linewidth=1, edgecolor='black')

plt.tight_layout()
```

![overlaying bar chart](/graph_examples/overlay_bar_chart.png)

## Advanced bar plot

Creating singular barplots can be done via `plt.bar`, but you can also combine two or more charts together to layout bars next to each other, like so:

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(15,6))

labels = ['College 1', 'College 2', 'College 3', 'College 4',' College 5']
means = [80, 70, 64, 78, 81]
py_means = [90, 56, 81, 80, 90]

x = np.arange(len(labels))  # the label locations
width = 0.35

rects1 = plt.bar(x - width / 2,
        means,
        width=width,
        edgecolor='black',
        color='#FF8A4A',
        label='2022')

rects2 = plt.bar(x + width / 2,
        py_means,
        width=width,
        edgecolor='black',
        color='#FFC000',
        label='2021')

# Add bar labels
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Apply the function
autolabel(rects1)
autolabel(rects2)

# Additional formatting with titles, labels etc
ax.set_ylabel('Overall Satisfaction')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=90)
ax.set_yticks(np.arange(0, 101, 10))
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1, fancybox=True)
plt.tight_layout()
plt.show()
```

![Barplot example](/graph_examples/barplots.png)
