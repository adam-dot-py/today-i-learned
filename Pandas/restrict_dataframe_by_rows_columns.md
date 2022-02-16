# Restricting Dataframes By Rows and Columns 

You can use the `pd.set_option` function to limit a dataframe by either maximum rows or columns. 

`pd.set_option('max_rows', 2)` would return the dataframe limited to just 2 rows, the rest would be seperated by an elipsis.

`pd.set_option('max_columns', 2)` would return the dataframe limited to just 2 columns, the rest would be seperated by an elipsis.