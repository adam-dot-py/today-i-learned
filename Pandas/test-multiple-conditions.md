# Test multiple conditions

This is useful for when you want to return a value if the conditions equate to true or false.

## Example

In this example, we want to evaluate if the `Visa Outcome` is equal to `Pending` and whether the `CAS Status` is equal to `Assigned`, `Used` or `Current`. Default behaviour will return `TRUE` or `FALSE`. When using `astype(int)`, the column will return `1` else `0`.

```python
pdf['PendingOutcome'] = (pdf['VISA Outcome'].isin(['Pending'])) & (pdf['CAS Status'].isin(['Assigned', 'Used', 'Current'])).astype(int)
```
