# Smoothed line charts

In this example, the `savgol_filter` function from `scipy.signal` is used to apply a `Savitzky-Golay` filter to the `y` data. The `window_length` parameter specifies the size of the smoothing window, and the `poly_order` parameter determines the order of the polynomial used to fit the samples within the window.

By plotting both the original data (`y`) and the smoothed data (`y_smoothed`), you can visualize the effect of the smoothing on the line plot. Adjusting the window_length and `poly_order` parameters can further refine the smoothing effect to suit your needs.

Note that the `scipy library` may need to be installed separately if it's not already available in your `Python` environment.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Generate some example data
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.2, size=100)

# Apply a smoothing function (Savitzky-Golay filter) to the data
window_length = 50  # The length of the smoothing window
poly_order = 3     # The order of the polynomial used to fit the samples within the window
y_smoothed = savgol_filter(y, window_length, poly_order)

# Plot the original data and the smoothed line
# plt.plot(x, y, label='Original')
plt.plot(x, y_smoothed, label='Smoothed')
plt.legend()

# Display the plot
plt.show()
```
