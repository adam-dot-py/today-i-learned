# Dataframes to tuples

Converting a dataframe to a tuple is useful for when needing to create a collection of items, particularly for storing unique rows of data for future iteration and value cherry-picking.

Lets say we have a dataframe like so:

```python
country_df = (
    df[["CountryCode", "Recruitment Country", "Recruitment Region"]]
    .sort_values(by="CountryCode", ascending=True)
    .drop_duplicates()
)
```

This dataframe is producing a unique dataset of CountryCodes, Recruitment Country and Regions. To turn this into a tuple, we can do this:

```python
tuple_list = country_df.itertuples(index=False, name=None)
```

Now, we can call something like this:

```python
for alpha, country, region in tuple_list:
    print(f"Alpha Code: {alpha}, Country: {country}, Region: {region}")
```