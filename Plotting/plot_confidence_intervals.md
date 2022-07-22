# Plot Confidence Intervals

Plotting confidence intervals on a graph can be done using the `ax.fill_between()` method.

```python
from matplotlib import pyplot as plt
import numpy as np

# some example data
x = np.linspace(0.1, 9.9, 20)
y = 5.0 * x

# set up confidence interval
ci = 1.96 * np.std(y)/np.sqrt(len(x)) # 95 percent confidence interval

# plot it
fig, ax = plt.subplots()
ax.plot(x, y)
ax.fill_between(x=x, y1=(y-ci), y2=(y+ci), color='b', alpha=.1)
```

![ci plotting example](/graph_examples/ci_plotting_example.svg)
