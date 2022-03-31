# Add a column to Spark DataFrame

Adding columns to a Spark DataFrame can be done using the `withColumn()` method.

```spark
df = spark_df.withColumn(colName: "Col3", col : "apples")
```

Where `colName` is a `string` and `col` is an expression.