# Best practice: Heat map

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors
import matplotlib.ticker as mticker

d = [
     ["College A", 'Academic Support', 0.85],
     ["College A", 'Teaching', 0.76],
     ["College A", 'Opportunities', 0.92],
     ["College B", 'Academic Support', 0.78],
     ["College B", 'Teaching', 0.84],
     ["College B", 'Opportunities', 0.67]
    ]

df = pd.DataFrame(data=d, columns=['College', 'Area', 'Value'])

heatmap_data = df.pivot_table(index='Area', columns='College', values='Value').values

FONT_FAMILY = "Bahnschrift"
VALUE_FONT_FAMILY = "Consolas"
BLUE = "#08306c"
GRID_COLOR = "#A8BAC4"

# get the college names and area names
colleges = df['College'].unique()
areas = df['Area'].unique()

# #custom color map
# cmap_red_green = mcolors.LinearSegmentedColormap.from_list(
#     'custom_colormap', [(0,'#B3D6D2'),
#                         (0.50, '#B3D6D2'), 
#                         (0.60, '#B3D6D2'), 
#                         (0.70, '#8DC1BD'),
#                         (0.80, '#007F7B'),
#                         (0.90, '#007F7B'),
#                         (1, '#007F7B')])

# Set the color limits
vmin = 0.6
vmax = 1

# plot the graph
fig, ax = plt.subplots(figsize=(10,6))
heatmap = ax.imshow(heatmap_data, cmap='Blues', vmin=vmin, vmax=vmax, aspect='auto', zorder=1)

# Set the tick labels and position
ax.set_xticks(np.arange(len(colleges)))
ax.set_xticklabels(colleges, ha='center', fontfamily=FONT_FAMILY, rotation=45)
ax.xaxis.set_tick_params(labeltop=True,
                         labelbottom=False,
                         bottom=False,
                         labelsize=11,
                         pad=1)

ax.set_yticks(np.arange(len(areas)))
ax.set_yticklabels(areas, fontfamily=FONT_FAMILY, fontsize=11)

# adjust spines
for spine in ["top", "left", "right", "bottom"]:
        ax.spines[spine].set_lw(1.2)
        ax.spines[spine].set_capstyle("butt")

# Add colorbar
cbar = plt.colorbar(heatmap)

# Add lines around each heatmap box
for i in range(len(areas)):
    for j in range(len(colleges)):
        rect = patches.Rectangle((j-0.5, i-0.5), 1, 1, linewidth=.5, edgecolor=GRID_COLOR, facecolor='none', alpha=0.4, zorder=2)
        ax.add_patch(rect)

# add annotations       
for i in range(len(areas)):
    for j in range(len(colleges)):
        value = heatmap_data[i,j]
        text = ax.text(x=j, y=i, s=f'{value:.0%}', ha='center', va='center', fontfamily=FONT_FAMILY)

# Set the colorbar label
cbar.set_label('Overall Satisfaction (%)', fontfamily=FONT_FAMILY, fontsize=12)

# Format colorbar values as percentages
cbar.ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1, decimals=0))

# Add titles
ax.text(x=-0.10, y=1.02, s="Area Satisfaction", transform=fig.transFigure, ha='left', fontsize=14, fontname=FONT_FAMILY, weight='bold')
ax.text(x=-0.10, y=.99, s="Darker sectors are better.", fontname=FONT_FAMILY, transform=fig.transFigure, ha='left', fontsize=11, alpha=.7)

# Set source text
ax.text(x=-0.10, y=0.05, s="Source: Annual Student Survey", transform=fig.transFigure, ha='left', fontsize=9, fontname=FONT_FAMILY, alpha=.7)

ax.plot([-0.10, .90],                # Set width of line
        [1.08, 1.08],                # Set height of line
        transform=fig.transFigure,   # Set location relative to plot
        clip_on=False, 
        color=BLUE, 
        linewidth=.6)

ax.add_patch(plt.Rectangle((-0.10, 1.08),               # Set location of rectangle by lower left corder
                           0.05,                        # Width of rectangle
                           -0.025,                      # Height of rectangle. Negative so it goes down.
                           facecolor=BLUE, 
                           transform=fig.transFigure, 
                           clip_on=False, 
                           linewidth = 0))

plt.savefig("graph_examples/heatmap-best-practice.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.show()

```

![Best practice: heat maps](/graph_examples/heatmap-best-practice.png)