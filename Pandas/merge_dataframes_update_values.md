# Merge Dataframes and update values

```python
## This had a very specific use case of using DataFrames, but dictionary updates can be used also
starting_df = {'ARUC' : 0, 'BPC' : 0, 'HIC': 0, 'UA92' : 0, 'UNIC' : 0}
update_df = {'BPC' : 20, 'HIC' : 30}

starting_df = pd.DataFrame(colleges.items(), columns = ['College', 'Responses'])
update_df = pd.DataFrame(update_df.items(), columns = ['College', 'Responses'])

"""
Create the final DataFrame
--------------------------
This will merge the two together, creating two identical columns with the append _x and _y. 
_y will be from the table on the right, and in this example is the update_df value. 
_x will be from the left, and in this example is the starting_df value. 
_y will have NaN values where no update is found, therefore to keep the 'true' values create a new column and update _y with the values from _x. 
This is done via fillna(), passing _x as the argument to fill with. 
Then drop the _x and _y columns.
"""

final_df = starting_df.merge(update_df, on='College', how='left', sort='College')
final_df['Responses'] = final_df['Responses_y'].fillna(final_df['Responses_x']).astype(int)
final_df.drop(columns={'Responses_x', 'Responses_y'}, inplace=True)
```
