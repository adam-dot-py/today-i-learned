# Classes

A Class is like an object constructor, or a "blueprint" for creating objects.

All classes have a function called `__init__()`, which is always executed when the class is being initiated.

Use the `__init__()` function to assign values to object properties, or other operations that are necessary to do when the object is being created.

The `self` parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named `self` , you can call it whatever you like, but it has to be the first parameter of any function in the class.

 If you are working on something that exists individually and has its own logic that is separate from others, you should create a class for it.

```python

import pandas as pd
import requests

class SurveyMonkeyAPI(object):

    '''
    Overview:

    Uses the request module to start the initial string of the SurveyMonkey API get string,
    to be built on by other functions. 
    =======================================================================================
    Return:

    self.host : initial GET string
    self.client : contains persistent parameters across the functions

    =======================================================================================
    '''
    
    def __init__(self, access_token):
        self.host = "https://api.surveymonkey.net/v3/"
        self.client = requests.session()
        self.client.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

class SurveyResults(SurveyMonkeyAPI):
    def __init__(self, access_token):
        super().__init__(access_token)

    def get_responses(self, survey_id, end_created_at=today):

        '''
        Overview: 

        Return all the responses in a survey as a Pandas DataFrame
        =======================================================================================
        Return:

        all_responses : a Pandas Dataframe of the responses

        =======================================================================================
        '''

        url = self.host + f"surveys/{survey_id}/responses/bulk/?simple=true&status=completed&per_page=100&end_created_at={end_created_at}"
        response = self.client.get(url)
        response_data = response.json()

        if response.status_code >= 400: 
            raise Exception(f"Request failed: {response.status_code}")

        all_responses = [self.organise_responses(response_data)]

        while 'next' in response_data['links']:
            response = self.client.get(response_data['links']['next'])
            response_data = response.json()
            all_responses.append(self.organise_responses(response_data))


        all_responses = pd.concat(all_responses)

        return all_responses


survey = SurveyResults(access_token=access_token) # Instantiate the class and create an object
df = survey.get_responses(survey_id=survey_id) ] # access the methods of that object
```
