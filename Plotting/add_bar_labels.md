# Add labels to barplots

## Single group barplots

For single group bar plots, pass the single bar container:

```python
import seaborn as sns
from matplotlib import pyplot as plt

tips = sns.load_dataset('tips')

ax = sns.barplot(x='day', y='tip', data=tips)
ax.bar_label(ax.containers[0])
plt.show()
```

## Multi group plots

For multi-group bar plots (with `hue`), iterate the multiple bar containers:

```python
import seaborn as sns
from matplotlib import pyplot as plt

tips = sns.load_dataset('tips')
ax = sns.barplot(x='day', y='tip', hue='sex', data=tips)

for container in ax.containers:
    ax.bar_label(container)

plt.show()
```
