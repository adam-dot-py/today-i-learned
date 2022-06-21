# Pad the axis

By default, graphs can sometimes have values bunched up to the spines, which can sometimes be unsightly, especially with scatter graphs of varying circle sizes. To get around this, you can arrange your x and y ticks as normal and then limit both axises:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(2004,2017,500)
y =np.clip(np.random.normal(13,7,500),0,24)

plt.scatter(x,y)
plt.xticks(range(2004,2017,3),[str(i) for i in range(2004,2017,3)],rotation=45)
plt.yticks(range(0,24,3),[str(i)+':00' for i in range(0,24,3)])

plt.xlim(2002,2019)
plt.ylim(-3,28)
plt.show()
```

![axis padding example](/graph_examples/axis_padding_example.png)
