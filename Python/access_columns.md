# Accessing columns 

You can access columns in Python by either referencing the column label or by using `iloc`.

**Using column label**
`df['col1']`

The same result can also be obtained using the iloc function. iloc arguments require integer-value indices instead of string-value names. To reproduce the above column example we can use the following code snippet:

**Using iloc**
`df.iloc[:,0]`

Both of these methods return all of the values in the first column. 