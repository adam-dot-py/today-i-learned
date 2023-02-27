# Add text to plots

In the below example we can use `ax.text` to create a customised legend effect, showing the countries that make up other and their values.

```python
year = 'AY 202223'
top_10_pv = pd.pivot_table(data=df.loc[(df['AcademicYear'] == year) & (df['Group'] == 'Top 10')],
                           index='Recruitment Country',
                           values='Enrolled at Census',
                           aggfunc=sum)

top_10_pv.sort_values(by='Enrolled at Census', ascending=False, inplace=True)

other_pv = pd.pivot_table(data=df.loc[(df['AcademicYear'] == year) & (df['Group'] == 'Others')],
                           index='Recruitment Country',
                           values='Enrolled at Census',
                           aggfunc=sum,
                           margins=True,
                           margins_name='Others')

other_pv.sort_values(by='Enrolled at Census', ascending=False, inplace=True)

fpv = pd.concat([top_10_pv, other_pv.head(1)])

legend_labels = [f"{c} : {v}" for c, v in zip(other_pv.index, other_pv['Enrolled at Census'])][1:]

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(data=fpv, x=fpv.index, y='Enrolled at Census', color='#007F7B', edgecolor='black', ax=ax)
plt.xticks(rotation=90)
plt.xlabel(None)
plt.ylabel(None)
for container in ax.containers:
    ax.bar_label(container, label_type='center', fontweight='bold', color='white')
ax.text(10.8, 2.7, '\n'.join(legend_labels), fontsize=8, bbox=dict(facecolor='white', alpha=0.5, boxstyle='round')) # add text to plot
plt.title(f"Twente Pathway College: Enrolled at Census {year}", fontsize=12, loc='left', pad=10, fontweight='bold')
# plt.tight_layout()
plt.savefig(f"{year}_tpc.png", dpi=200, bbox_inches='tight')
plt.show()
```

![Text on plot](/graph_examples/text-on-plot.png)
