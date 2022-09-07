# Show duplicated columns

To return columns in a `dataframe` that are duplicates, we can use the `duplicated()` method.

`df.columns[df.columns.duplicated()]`

This will return an index containing duplicated column names.
