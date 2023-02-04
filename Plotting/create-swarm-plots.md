# Create swarm plots

Swarm plots are great for looking at the distribution of a variable in a category. The below is an example of a swarm plot created in `seaborn`.

```python
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('iris')

fig, ax = plt.subplots(figsize=(10,5))
sns.swarmplot(x='species', y='petal_length', data=data, ax=ax)
plt.tight_layout()
plt.show()
```

![swarm plot example](/graph_examples/swarm-plot-example.png)