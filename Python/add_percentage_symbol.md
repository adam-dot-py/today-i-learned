# Add the percentage symbol to a column

In some cases, users may want the percentage symbol in a dataframe, for example when sending an automated email on response rates. This is, in most cases, not recommended as the value is a string. It is much better to have the decimal value in all cases.

```python
respondents = 100
population = 200

response_rate = respondents / population * 100
response_rate = response_rate.astype(str) + '%'
```

`result` is `50%`. This can also be applied to dataframes.
