# Add a title to a plot

This can be done using the `plt.title()` function.

```python
import seaborn as sns
from matplotlib import pyplot as plt

tips = sns.load_dataset('tips')
ax = sns.barplot(x='day', y='tip', hue='sex', data=tips)
for container in ax.containers:
    ax.bar_label(container)
plt.title('Tips by Day and Gender', weight='bold').set_fontsize(14) # Add title
plt.show()
```
