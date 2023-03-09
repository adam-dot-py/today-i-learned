# Plot a Python dictionary

This is useful for quickly plotting a dictionary - particulary if it involves a singular `key`, `value` schema.

```python
import numpy as np
import matplotlib.pyplot as plt

flips = 1000
outcomes = np.random.randint(0,2, size=flips)
adjusted_outcome = np.where(outcomes > 0, "Heads", "Tails")
unique, count = np.unique(adjusted_outcome, return_counts=True)

d = dict(zip(unique, count))
plt.bar(*zip(*d.items()))
plt.show()
```

![Example Python Dictionary](/graph_examples/plot-python-dictionary.png)
