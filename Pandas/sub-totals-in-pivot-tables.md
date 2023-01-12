# Subtotals in pivot tables

The below example shows how to add sub totals to pivot tables. By default this functionality is not available. It involves creating margins on the initial index, and then looping over each other index. Finally, everything is combined back together.

```python
'''
Uses the first index to generate a total margin, the second index does not have a margin. Tables are then concated together.
'''
def pivot_sub_totals(df, indexes, columns, values, aggfunc, margins_name, fill_value=0):
    listOfTable=[]
    for n, x in enumerate(indexes, start=1):
        if n == 1: 
            pivot = pd.pivot_table(data=pdf,
                                   index=indexes[:n], # select all indexes
                                   columns=columns,
                                   values=values,
                                   aggfunc=aggfunc,
                                   margins=True,
                                   margins_name=margins_name,
                                   fill_value=fill_value)
        else:
            pivot = pd.pivot_table(data=pdf,
                                   index=indexes[:n],
                                   columns=columns,
                                   values=values,
                                   aggfunc=aggfunc,
                                   margins=True)
            
        pivot = pivot.reset_index()
        for column in indexes[n:]:
            pivot[column] = ''
        listOfTable.append(pivot)
    concatTable = pd.concat(listOfTable).sort_index()
    concatTable = concatTable.set_index(keys=indexes)
    return concatTable.sort_index(axis=0, ascending=True)

pivot_sub_totals(df=pdf.loc[pdf['UT_year'] == 2020],
                 indexes=['UT_year','Faculty','Study programme code'],
                 columns='BSA advice',
                 values='Student number',
                 aggfunc=lambda x: len(x.unique()),
                #  aggfunc='count',
                 margins_name='Total Enrolments'
                 )
```
