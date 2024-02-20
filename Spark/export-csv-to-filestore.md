# Export CSV to FileStore

You can export a `Spark` `dataframe` to `FileStore` and export the resulting `csv` using the below process.

This uses `coalesce` to force the resulting file to just 1 file, which goes against typical `Spark` processing, which would partion an output for better performance.

```spark
# write to dbfs filestore, consolidating down to just one file
sql_query.coalesce(1).write.format('csv').option('header', 'true').mode('overwrite').save('/FileStore/monthly_returns.csv')
```
