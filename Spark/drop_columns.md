# Drop columns from DataFrames

You can drop single columns or multiple columns, depending on the use case.

## Drop multiple columns

```python
drop_columns = ['TagData', 'Text']
raw_response_df = spark.createDataFrame(data=responses,
                                        schema=response_schema).drop(*drop_columns) # Pass all the arguments of drop_columns
```

## Drop single column

```python
raw_response_df = spark.createDataFrame(data=responses,
                                        schema=response_schema).drop(col('Text'))
```
