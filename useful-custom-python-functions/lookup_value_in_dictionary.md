# Lookup a value in a dictionary

```python
def ay_lookup_forecast_value(dictionary, country, college):

    """lookup_forecast_value(dictionary, country, college) --> returns forecast value in a nested dictionary for FY23.

    Parameters:
    dictionary: the dictionary to look in.
    country: the country to look for.
    college: the college to look for, which will return the forecast value.
    """

    for k in dictionary.keys():
        if k == country:
            for c, v in dictionary[k].items():
               if c == college:
                     return v
```

This can then be applied to a row in a `pandas` dataframe, when used in conjunction with `apply()` and `lambda`.

```python
# The point of this is to lookup the country in the dictionary and return their value for 2022/23

nvt_final_df['AY2022/23'] = nvt_final_df.apply(lambda row: ay_lookup_forecast_value(dictionary=ay_forecast_countries_dict, 
                                                                                    country=row['RecruitmentCountry'], 
                                                                                    college=row['College']), axis=1) \
                                                                                    .replace(np.inf,0).fillna(0).astype(int) # perform the calculation on the row
```
