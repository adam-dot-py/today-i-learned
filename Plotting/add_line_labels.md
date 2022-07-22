# Add line plot labels

Adding line plot labels allows for more readability in charts, with Python allowing full control over how they are formatted and presented. Below is an example using `seaborn`.

```python

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset('flights')

# group to years

year_flights = flights.groupby('year').sum().reset_index()

# plot a graph
sns.set_style('darkgrid')
fig, ax = plt.subplots(figsize=(10,8))
sns.lineplot(x='year', 
             y='passengers', 
             data=year_flights, 
             marker='o', 
             color='#007F7B', 
             ax=ax, 
             linewidth=2, 
             markersize=10,
             markeredgecolor='black')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Passengers', fontsize=14)
ax.set_title('Total Yearly Passengers', fontsize=14)

for x, y in zip(year_flights['year'], year_flights['passengers']):
    plt.text(x=x, 
             y=y-150, 
             s="{:.0f}".format(y), 
             color='black')
plt.tight_layout()
plt.show()
```

![line plot with labels example](/graph_examples/line_plot_labels.svg)
