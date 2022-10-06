# Read a File From Databricks DBFS

The below code can be used to read a file from the Databricks `DBFS`, or `FileStore`.

```python
# File location and type
file_location = "/FileStore/tables/<filename.filetype>"
file_type = "csv"

# CSV options
infer_schema = "true" #--guess the dtypes
first_row_is_header = "true" #--sets the first row of the csv as header
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

#--remove spaces from column headers if required 
NewColumns = (column.replace(' ', '') for column in df.columns)
df = df.toDF(*NewColumns)

display(df)
```
