# Create a countplot

## Single categorical graph

Plot a single variable

```python
import seaborn as sns
sns.set_theme(style="darkgrid")
titanic = sns.load_dataset("titanic")
ax = sns.countplot(x="class", data=titanic)
```

![Countplot Example](/graph_examples/sns_countplot_single_category.png)

## Two categories

Plot two categorical variables

```python
import seaborn as sns
sns.set_theme(style="darkgrid")
titanic = sns.load_dataset("titanic")
ax = sns.countplot(x="class", hue="who", data=titanic)
```

![Countplot Example](/graph_examples/sns_countplot_two_categories.png)

## Horizontal

Plot the bars horizontally

```python
ax = sns.countplot(y="class", hue="who", data=titanic)
```

![Countplot Example](/graph_examples/sns_countplot_horizontal_bars.png)
