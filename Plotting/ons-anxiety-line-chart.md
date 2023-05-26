# Office for National Statistics: Anxiety Levels

This is a chart I created plotting anxiety data published by the Office for National Statistics.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

VALUE_FONT_NAME = {'fontname': 'Consolas'}

# get the data
df = pd.read_excel('source/qualityoflifeintheukmay2023.xlsx', sheet_name='1.4_Anxiety', skiprows=16)[0:47]
df.columns = [col.split('\n')[0].strip() for col in df.columns]
df = df.rename(columns={'Estimate': 'Estimate%'})

df['quarterly'] = df['People rating their anxiety yesterday as very low'].str[-10:]
df['quarterly'] = df['quarterly'].str.replace("[()]", "").str[:5]
df['year'] = df['People rating their anxiety yesterday as very low'].str[-4:]
df['quarterly'] = df['year'] + '' + df['quarterly']

df = df.tail(45)

x = df['quarterly'].values
y = df['Estimate%'].values

fig, ax = plt.subplots(figsize=(12, 7))
linepoints = ax.plot(x, y, color='#5f6062', lw=3, alpha=.7, zorder=2)
first_linepoint = ax.plot(x[0], y[0], marker='o', markersize=12, markeredgecolor='white', color='#f7bb43', zorder=3)
last_linepoint = ax.plot(x[-1], y[-1], marker='o', markersize=12, markeredgecolor='white', color='#007F7B', zorder=3)
ax.hlines(y=y.mean(), xmin=0, xmax=len(x), linestyles='--', lw=2, color='#70bc4e', alpha=.7, zorder=3)

# styling
# title
ax.text(x=0.13, y=1.005, s="% of people rating their anxiety yesterday as very low", ha='left', fontsize=16, weight='bold', alpha=.9, fontfamily="Bahnschrift", transform=fig.transFigure)

# subtitle
ax.text(x=0.13,
        y=0.952,
        s='Adults aged 16 years and over were asked to rate how anxious did they feel yesterday on a scale from 0 to 10,\nwhere 0 was "not at all" and 10 was "completely". The very low rating of anxiety is defined as answering 0 or 1 out of 10.',
        ha='left',
        fontsize=11,
        weight='bold',
        alpha=.5,
        fontfamily="Bahnschrift",
        transform=fig.transFigure)

# source
ax.text(x=0.13, y=-0.05, s="Office for National Statistics (ONS), released 12 May 2023, ONS website, statistical bulletin, Quality of life in the UK: May 2023", ha='left', fontsize=11, weight='bold', alpha=.5, fontfamily="Bahnschrift", transform=fig.transFigure)  # source

# custom legend
custom_legend = [
    mlines.Line2D([], [], color='#70bc4e', linestyle='dashed', label='Average % with very low anxiety')
]

# Add the legend to the plot
legend_font = {'family': "Bahnschrift", 'size': 11, 'weight': 'bold'}
fig.legend(handles=custom_legend, loc=(0, 0.5), bbox_to_anchor=(0.13, 0.895), ncol=4, fontsize=10, prop=legend_font)

# add fancy lines and rectangle
ax.plot([0.13, 0.91],
        [1.07, 1.07],
        transform=fig.transFigure,
        clip_on=False,
        color='#007F7B',
        linewidth=.6)

ax.add_patch(mpatches.Rectangle((0.13, 1.07),
                                0.06,
                                -0.025,
                                facecolor='#007F7B',
                                transform=fig.transFigure,
                                clip_on=False,
                                linewidth=.6))

# adjust grid
ax.grid(which='major', axis='y', lw=1.2, alpha=.7, zorder=1)

# adjust x axis
ax.set_xticks(np.arange(0, len(x), 4)) # have labels every 4 positions
ax.set_xticklabels(x[::4], rotation=90, fontfamily="Bahnschrift") # amend list to take every 4 values using x[::4]
ax.xaxis.set_tick_params(length=5, pad=5, labelsize=10)

# adjust y axis
ax.yaxis.set_ticks(np.arange(20, 51, 10))
ax.yaxis.set_ticklabels(np.arange(20, 51, 10), ha='right', va='bottom', **VALUE_FONT_NAME)
ax.yaxis.set_tick_params(length=0, labelleft=False, labelright=True, labelsize=11, pad=15)

# adjust spines
for spine in ["top", "left", "right"]:
    ax.spines[spine].set_visible(False)

ax.spines["bottom"].set_lw(1.2)
ax.spines["bottom"].set_capstyle("butt")

plt.savefig('images/ons-anxiety-levels-latest.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()
```


