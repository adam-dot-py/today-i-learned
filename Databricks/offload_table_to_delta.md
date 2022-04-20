# Offload a table to delta and recall in Databricks

Functions have been created within our Databricks environment to offload datasets to delta for use in reports, such as PBI.

To access these functions, you need to have the below code as a cell in your notebook

`%run /Functions/_delta_operations`

This will produce two functions that will be available to use:

- offload_dataset_to_delta(dataset_dataframe, database_name: str, table_name: str, mode_type: str, merge_schema: bool)
- get_schema_from_metadata(metadata_table, source_name, dataset_name, data_type_mapping=_DEFAULT_DATA_TYPE_MAPPING)

## Example of offloading data to delta and calling

The below code example looks at offloading `df_extract` to a domain delta table:

```python
offload_dataset_to_delta(dataset_dataframe=raw_response_df, 
                         database_name='raw', 
                         table_name='surveymonkey_upe_annual_survey_response', 
                         mode_type='overwrite', 
                         merge_schema=False)
```

This can then be called elsewhere, including other notebooks, with the below:

```python
df = spark.sql("SELECT * FROM raw.surveymonkey_upe_annual_survey_response").toPandas() # get the survey response data
```

Here we are recalling it using SQL and transforming back to a pandas `DataFrame`.
