# Create a top N and others pivot table

These are a useful analysis technique for showing the largest top N items in a dataset, along with a combined sum of the very of the dataset.

```python
df['Group'] = ["Top 10" if x in df.nlargest(10, 'PopTotal')['Location'].values else "Others" for x in df['Location']]

df_top_10 = pd.pivot_table(data=df.loc[df['Group'] == 'Top 10'],
                           index='Location',
                           values='PopTotal',
                           aggfunc=sum)

df_others = pd.pivot_table(data=df.loc[df['Group'] == 'Others'],
                           index='Group',
                           values='PopTotal',
                           aggfunc=sum)

fdf = pd.concat([df_top_10, df_others])
```