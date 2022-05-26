# Create a lineplot with markers

## Single marker for last value

This is useful for showing the last value at the end of a lineplot, to show progression:

```python
# Some filtering
df = pandas.read_csv('../Example_datasets/country_data.csv')
df = df[df['Location'].isin(['United Kingdom']) & df['Variant'].isin(['Medium'])]
df = df[df['Time'] <= 2020]

max_year = df[df['Location'] == 'United Kingdom']['Time'].max() # get max year
pop_total = df[(df['Location'] == 'United Kingdom')][df['Time'] == 2020]['PopTotal'] # get the value for the year

ax = df[df['Location'] == 'United Kingdom'].plot(x='Time', y='PopTotal', legend=False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.scatter(x=[max_year], y=[pop_total], s=70, clip_on=False, linewidth=0) # add the end marker
plt.annotate(str(int(pop_total / 1000)) + "k", xy=[max_year, pop_total], xytext=[7, -2], textcoords='offset points')
```

![Lineplot with single marker](/graph_examples/plt_subplots_6.png)

## Multiple markers

This is useful for plotting the value points:

```python
# Some filtering
df = pandas.read_csv('../Example_datasets/country_data.csv')
df = df[df['Location'].isin(['United Kingdom']) & df['Variant'].isin(['Medium']) & df['Time'].isin([2000, 2010, 2020])]
# df = df[df['Time'] <= 2020]

ax = df[df['Location'] == 'United Kingdom'].plot(x='Time', y='PopTotal', legend=False, marker='o')
ax.set_xticks([2000, 2010, 2020])
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.savefig('../graph_examples/plt_subplots_7.png')
plt.show()
```

![Using multiple markers](/graph_examples/plt_subplots_7.png)

## Using `markevery` to highlight certain points

This is the same as above, but good for highlighting key areas of interest:

```python
import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(-np.pi, np.pi, 30)
ys = np.sin(xs)
markers_on = [12, 17, 18, 19]
plt.plot(xs, ys, '-gD', markevery=markers_on, label='line with select markers')
plt.legend()
```

![Using mark every](/graph_examples/plt_subplots_8.png)
