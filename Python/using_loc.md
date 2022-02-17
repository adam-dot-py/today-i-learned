# Using loc and iloc

You can subset a dataframe using either `loc` or `.iloc`. Note that `index` starts from position 0.

**Example**

`df.loc[3:5]` will return rows 3, 4 and 5. 

`df.loc[3, 'sepal_length']` will return the value in row 3 in column 'sepal_length'. 

`df.iloc[3,0]` will return rows the same value as above, as the column is index 0.