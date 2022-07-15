# Moving the legend outside a graph

This can be done using the `bbox_to_anchor` method:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)

fig = plt.figure()
ax = plt.subplot(111)

for i in range(5):
    ax.plot(x, i * x, label='$y = %ix$' % i)

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1, fancybox=True, title="This is my title")

plt.show()
```
