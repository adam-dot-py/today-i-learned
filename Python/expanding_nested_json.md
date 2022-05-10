# Expanding nested JSON

Where nested JSON is within a Pandas DataFrame, for example like so:

responses = 

|    |          id | custom_variables                                                                           |
|---:|------------:|:-------------------------------------------------------------------------------------------|
|  0 | 13463999357 | {'College': 'LULC', 'Module': 'LZIFB001M', 'Semester': '202202', 'Programme': 'Temporary'} |

It is sometimes not possible to access these through standardised methods, such as `pd.json_normalize`. Instead, we can use the following to `pop` the values and create a new DataFrame, joining it back to our original DataFrame.

```python
custom_variables = pd.DataFrame([{} if x == None else x for x in responses.pop('custom_variables')])

response_data = pd.concat([responses, custom_variables], axis=1)
```

The resulting dataframe is joined back to the original, with the nested JSON now being expanded. Where nothing exists in the column (i.e no nested JSON), an empty dictionary is returned.

|    |          id | custom_variables.College   | custom_variables.Module   |   custom_variables.Semester | custom_variables.Programme   |   custom_variables.Intake |
|---:|------------:|:---------------------------|:--------------------------|----------------------------:|:-----------------------------|--------------------------:|
|  0 | 13463999357 | LULC                       | LZIFB001M                 |                      202202 | Temporary                    |                       nan |
