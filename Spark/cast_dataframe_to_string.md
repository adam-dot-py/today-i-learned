# Cast a dataframe to string format

This is useful when you want to neutralise a `dataframe` of multiple `dtypes` to just `strings`. For example, if you have numerical `dtypes` with `NaN` values, this may trigger an error. Casting to `string` will avoid this type of error.

`df.select([col(c).cast("string") for c in df.columns])`
