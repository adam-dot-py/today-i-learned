# Create boxplots

Box plots show the five-number summary of a set of data: including the minimum score, first (lower) quartile, median, third (upper) quartile, and maximum score.

## Create a single boxplot

```python
import seaborn as sns
from matplotlib import pyplot as plt

exercise = sns.load_dataset('exercise')
sns.boxplot(x='time', y'pulse', hue='kind', data=exercise)
plt.show()
```

![Boxplot Exercise](/graph_examples/sns_boxplot_single.png)

## Create two or more plots together

```python
import seaborn as sns
from matplotlib import pyplot as plt

exercise = sns.load_dataset('exercise')
penguin = sns.load_dataset('penguins')

# Stack 2 plots per column
fig, ax = plt.subplots(2, 1, figsize=(8, 8)) # create 2 plots on top of each other
g1 = sns.boxplot(x='time', y='pulse', hue='kind', data=exercise, ax=ax[0])
g2 = sns.boxplot(x='species', y='body_mass_g', hue='sex', data=penguin, ax=ax[1])
plt.show()
```

![Boxplot Exercise](/graph_examples/sns_boxplots_multiple.png)
