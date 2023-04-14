# Add columns to temporary dataframe views

When working with views on dataframes that are not in place (or temporary) it is possible to add columns that become part of the temporary view. This is useful to avoid getting a `CopyWarning` which can result when trying to add a column to a copied dataframe.

```python
pdf.loc[pdf['College'] == college, 'loadDate'] = load_date
pdf.loc[pdf['College'] == college, 'ReportingMonth'] = month_name
new_df = pdf.loc[pdf['College'] == college]
```
