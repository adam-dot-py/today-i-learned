# Using `spark.table`

The `spark.table` command can be used to load the contents of an entire table. This is quicker than using `spark.sql` if you want to use all elements of a table.

```python
df = spark.table("domain.navigate__base")
```

The above code would load the entire table contents to a spark dataframe.
