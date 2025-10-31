# Add columns

To add a column to a Polars `dataframe`, use the following:

```python
df = df.with_columns(
    pl.lit("AGREED").alias("ForecastType"),
    pl.lit(136).alias("Period_SK"),
    pl.lit(loaddate).alias("Date"),
)
```

`with_columns` method can accept any number of new columns