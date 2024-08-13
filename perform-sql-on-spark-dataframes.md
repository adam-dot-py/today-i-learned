# Perform SQL on Spark Dataframes

To perform SQL queries on Spark dataframes you first need to create a temporary view. Assuming we have a dataframe called `df`, then we would do it as so:

```python
df.createOrReplaceTemporaryView("my-view")
sql_query = spark.sql("select * from my-view")
display(sql_query)
"""
