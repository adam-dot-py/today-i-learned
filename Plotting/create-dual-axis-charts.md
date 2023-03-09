# Create dual axis charts

Dual axis charts are great for plotting two variables against each other on a singular graph. Care should be taken to ensure readibility but when used properly they help create good visualisations to show a singular story.

```python
import pandas as pd
import os
import matplotlib.pyplot as plt

x_label = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
average_temp = [5.2, 5.3,7.6,9.9,13.3,16.5,18.7, 18.5, 15.7, 12.0, 8.0, 5.5]
average_percipitation_mm = [55.2, 40.9, 41.6, 43.7, 49.4, 45.1, 44.5, 49.5, 49.1, 68.5, 59.0, 55.2]

london_climate = pd.DataFrame(
  {
    'average_temp': average_temp,
    'average_percipitation_mm': average_percipitation_mm
  }, 
  index=x_label
)

# Create the figure and axes object
fig, ax = plt.subplots()
# Plot the first x and y axes:
london_climate.plot(
    use_index=True, 
    kind='bar',
    y='average_percipitation_mm', 
    ax=ax, 
    color='orange'
)
# Plot the second x and y axes. 
# By secondary_y = True a second y-axis is requested
london_climate.plot(
    use_index=True, 
    y='average_temp', 
    ax=ax, 
    secondary_y=True,
    color='blue'
)

plt.show()
```

![Dual axis example](/graph_examples/dual-axis-example-1.png)

It can also be done using `Seaborn`, for a greater degree of control:

> Note: We use mpatches.Patch() to fix the legend being displayed incorrectly with the bar chart color.

```python
# plot line graph on axis #1
ax1 = sns.lineplot(
    x=london_climate.index, 
    y='average_temp', 
    data=london_climate, 
    sort=False, 
    color='blue'
)
ax1.set_ylabel('average temp')
ax1.set_ylim(0, 25)
ax1_patch = mpatches.Patch(color='blue', label='average temp')
ax1.legend(handles=[ax1_patch], loc="upper left")

# set up the 2nd axis
ax2 = ax1.twinx()

# plot bar chart on axis #2
sns.barplot(
    x=london_climate.index, 
    y='average_percipitation_mm', 
    data=london_climate, 
    color='orange', 
    alpha=0.5, 
    ax = ax2       # Pre-existing axes for the plot
)
ax2.grid(False) # turn off grid #2
ax2.set_ylabel('average percipitation mm')
ax2.set_ylim(0, 90)
ax2_patch = mpatches.Patch(color='orange', label='average percipitation mm')
ax2.legend(handles=[ax2_patch], loc="upper right")
plt.show()
```

![Dual axis example 2](/graph_examples/dual-axis-example-2.png)
