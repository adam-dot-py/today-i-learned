# Create Pie Charts

The below is an example of creating an advanced pie chart.

```python
pdf = pd.read_csv('source/nationality_data.csv')
pdf.rename(columns={'Active Enrolments today' : 'value'}, inplace=True)
labels = dict(zip(pdf['CountryName'][:10], pdf['CountryName'][:10])) # get the top 10 countries

"""
since we got the top 10 countries above in a dictionary, we can map each country to it to assign it a label. 
where a country is not in the top 10, we label it Others
"""
pdf['label'] = pdf['CountryName'].map(labels).fillna('Others')

# groupby by labels and value
country = pdf.groupby('label')['value'].sum().reset_index()
country['Pct'] = np.round(country['value'] / country['value'].sum() * 100,0).astype(int) # calculate percentage of the total
country.sort_values(by='Pct',ascending=True, inplace=True) # sort lowest to highest

legend_labels = [f'{n} {v}%' for n, v in zip(country['label'], country['Pct'])] # add a custom legend label, which includes the value
myexplode = [0,0,0,0,0,0,0,0,0,0,0.1] # blow Others out of the pie
colors = sns.color_palette('tab20')

 # create the pie
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10,8))
plt.pie(country['Pct'], 
        colors=colors, 
        startangle=0, 
        explode=myexplode)
plt.legend(title='Countries:',
           labels=legend_labels, 
           bbox_to_anchor=(1,0.5), 
           loc='center left', 
           fancybox=True)
plt.show()
```

![Pie chart example](/graph_examples/pie_chart_example.png)
