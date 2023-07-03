# Add a row to a pivot table

In the below example, we have a `pandas dataframe` which is looking at response rate data, counting the number of responses each day. What we want is the count to start from zero but when using the `count` aggregate function we will always start from 1 or more. To get around this, we insert a blank row after we have compiled our pivot table which starts from zero. I also want it to start from a particular date, so in this example we start from `2023-04-17`.

```python
# store the timestamps for each unique respondent in a dict
timestamp_dict = {}
for i, row in df.iterrows():
    timestamp_dict[row['ID']] = row['Timestamp']

tdf = pd.DataFrame(timestamp_dict.items(), columns=['ID', 'date_created'])
response_pivot = tdf.pivot_table(index='date_created', aggfunc='count') \
    .apply(lambda x: x.cumsum())

# start the count from zero by inserting this line
start_date = pd.to_datetime('2023-04-17').date()
start_count = 0    
new_row = pd.DataFrame({response_pivot.columns[0] : [start_count]}, index=[start_date])
response_pivot = pd.concat([new_row, response_pivot])
```
