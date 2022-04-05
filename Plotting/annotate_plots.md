# Annotate plots

`plt.annotate()` is a method used to add commentary to a plot. There are lots of different customisation options, [see here](https://matplotlib.org/stable/tutorials/text/annotations.html#sphx-glr-tutorials-text-annotations-py) for more information.

## Example

```python
fig, ax = plt.subplots(figsize=(12,8))

colors = ['#c8102E', '#6CABDD']

liverpool = sns.lineplot(x='RoundNumber', y = 'liverpool_cumulative_points', label='Liverpool FC', color = '#c8102E', linewidth = 3, marker='o', markersize=8, markeredgecolor = 'black', data=final_df)
man_city = sns.lineplot(x='RoundNumber', y = 'man-city_cumulative_points', label = 'Manchester City FC', color = '#6CABDD', linewidth = 3, marker='o', markersize=8, markeredgecolor = 'black', data=final_df)

ax.set_xticks(final_df['RoundNumber'])
ax.set_ylabel('Points', size='large', fontweight='bold')
ax.set_xlabel('Match Number', size='large', fontweight='bold')

liverpool.annotate(text="Liverpool lose form",
                   xy=(20, 40), 
                   xytext = (80, -40), 
                   textcoords = 'offset points', 
                   arrowprops=dict(color = '#c8102E'),
                   bbox = dict(boxstyle='round', fc = '1', ec = 'black'),
                   va = 'center',
                   ha = 'center',
                   size = 'large')
```
