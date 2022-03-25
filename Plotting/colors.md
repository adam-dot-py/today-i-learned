# Changing bar colours

In Seaborn, you can provide a `list` into the `palette` variable. The order of the list is important, as the bars will be coloured in order.

```python
colors = ['red', 'green', 'blue']

ax = sns.countplot(x="class", hue="who", palette=colors, data=titanic)
```
