# Creating lineplots

The below code is used to create lineplots where multiple categorical variables (like University names) are present in the data. It loops through each element in the `Name of Provider` column (once grouped) and produces a visual, which is then overlayed onto the same `ax`.

```python
fig, ax = plt.subplots(figsize=(8,6))
for label, df in rank_melt.groupby('Name of Provider'):
    ax = df.plot(kind='line', x='Year', y='Rank', ax=ax, label=label, marker='o')

ax.legend(loc='center left', bbox_to_anchor=(1,0.5), ncol=1, fancybox=True)
ax.set_ylabel('Rank')
ax.set_ylim(ax.get_ylim()[::-1]) # invert the y axis
ax.set_xlabel('Year')

plt.show()
```

![line_plot_example](/graph_examples/lineplot_example.png)