# Using requests

The `requests` module in Python is extremely useful for communicating with APIs as well as downloading information and files from the Internet.

## Simple Usage

```python
import requests

payload = {'key1' : 'value1', 'key2' : 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

print(r.url)
```

The `payload` object can be used to pass additional arguments to the URL string, such as API parameters.

## Working Example

This is a typical usage in a working context, for use with SurveyMonkey.

```python
host = "https://api.surveymonkey.net/v3/"
client = requests.session()
client.headers = {"Authorization" : f"Bearer {access_token}",
                               "Content-Type" : "application/json"}

response_url = host + f"surveys/{survey_id}/responses/bulk/"
payload = {'per_page' : '100', 'simple' : 'true'}
response = client.get(response_url, params=payload)

print(f"{response.status_code} -> {response.reason}")
```

200 -> OK

You can also use it with `pandas` to extract data from a website into a DataFrame:

```python
import requests
import pandas

url = 'http://www.ffiec.gov/census/report.aspx?year=2011&state=01&report=demographic&msa=11500' # Your URL
html = requests.get(url).content
df_list = pandas.read_html(html)
df = df_list[-1] # Adjust if multiple tables
print(df)
df.to_csv('my data.csv')
```

`requests` has significantly more uses and capability than the above examples but these serve as typical usage. More information can be found in the [documentation.](https://docs.python-requests.org/en/latest/user/quickstart/)
