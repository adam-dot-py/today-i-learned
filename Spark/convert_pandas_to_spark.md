## Convert a Pandas dataframe to a Spark dataframe

The below will convert a Pandas dataframe into a Spark dataframe. 

```python 

df = pd.Dataframe({'col1' : [1,2], 'col2' : [3,4]})

# Define a Spark session
spark = SparkSession.builder.appName("app_name").getOrCreate()

# Create the DataFrame
spark_df = spark.createDataFrame(df)
```
