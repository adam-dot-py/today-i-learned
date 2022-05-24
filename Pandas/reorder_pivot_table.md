# Reorder a pivot table

Reordering pivot tables can be done using `reindex`. 

```python
response_pivot = response_df.pivot_table(index=['id', 'date_created'],
                                columns='pages.answers.heading',
                                values='simple_text',
                                aggfunc=sum)

response_pivot = response_pivot.reindex([
    'Your Name:',
    'Your Position:',
    'Your Department:',
    'Information/Data Analysis Requested:',
    'How will the data analysis/information being requested be used?',
    'What is your ideal turnaround time?',
    'What type of data does your request need?'], axis=1)
```

`reindex` should be passed columns that are present in the dataset but not the index columns themselves, in this case `id` and `date_created`.

Additional arguments and functionality can be found [here.](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html)

