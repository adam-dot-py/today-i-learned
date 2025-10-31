# Unpivot Dataframes (AKA Melt)

Melting, or unpivot as Polars calls it, can be done like so:

```python
melted = df.unpivot(
    index=["BusinessUnit", "BudgetCountry", "MarketingSemester"],        # columns to keep as identifiers
    on=["Domestic", "International-Offshore", "International-Onshore"],  # columns to unpivot
    variable_name="StudentType",                                         # new column name for old column headers
    value_name="ForecastValue"                                           # new column name for their values
)
```