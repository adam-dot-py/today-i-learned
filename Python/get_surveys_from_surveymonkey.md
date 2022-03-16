## Get Survey IDs from SurveyMonkey API

The below function can be used to generate a list of surveys owned in your SurveyMonkey account, provided you have a developer account with API access. The result is a Pandas dataframe with a survey list. 

```python

import pandas as pd 
import http.client
import json
import os

access_token = os.environ.get('access_token_surveymonkey')

def get_survey_ids(access_token):

    conn = http.client.HTTPSConnection("api.surveymonkey.com")
    headers = {
        'Accept' : "application/json",
        'Authorization' : f"Bearer {access_token}"
    }

    conn.request("GET", f"/v3/surveys/", headers=headers)
    res = conn.getresponse()
    surveys_data = res.read()
    surveys = json.loads(surveys_data)

    if res.status >= 400:
        raise RuntimeError(f'Request failed: {res.status}')

    survey_list = pd.json_normalize(surveys['data'])

    return survey_list

surveys = get_survey_ids(access_token=access_token)

surveys
```