# SurveyMonkey API

This is my custom code for getting respones from SurveyMonkey. Can be tweaked for usage in other scenarios.

```python
class SurveyMonkeyAPI():
  """
  A class to initiate the SurveyMonkey API. This class has no methods but is passed to the SurveyResults class to be inherited.
  
  Attributes
  --------------
  self.host : str
    The URL for the API.
    
  self.client
    Initialises a session using the requests module.
    
  client.headers : dict
    The headers for the API GET request, contains the Authorization and Content-Type.
  
  Methods
  --------------
  access_token : str
    The API access_token. WARNING: very sensitive!!  
  """
  
  def __init__(self, access_token: str):
    self.access_token = access_token
    self.host = "https://api.surveymonkey.net/v3/"
    self.client = requests.session()
    self.client.headers = {"Authorization" : f"Bearer {self.access_token}",
                          "Content-Type" : "application/json"}
    
class SurveyResults(SurveyMonkeyAPI):
  """
  A class to perform GET requests on the SurveyMonkey API. Used to fetch and wrangle survey data for ingestion into the lake or other sources.
  Attributes are inherited through the SurveyMonkey API class.
  
  Attributes
  --------------
  self.host : str
    Inherited from class SurveyMonkeyAPI, the URL for the API.
    
  self.client
    Inherited from the class SurveyMonkeyAPI, initialises a session using the requests module.
    
  self.access token : str
    Inherited from the class SurveyMonkeyAPI, the API access_token. WARNING: very sensitive!!
  
  Methods
  --------------
  get_questions(survey_ids)
    Iterates through the survey IDs and generates a dictionary of questions, returning the name, order and type.
  
  get_collectors(survey_ids)
    Iterates through the survey IDs and fetches collectors, returning a dictionary containing collector IDs as key, with name, URL and as nested key:values.
  
  get_responses(survey_ids)
    Iterates through the survey IDs and fetches JSON data, to be passed to get_responses. Cycles through each page where the 'next' key provides a URL. Produces a Pandas df of response data.
  
  organise_responses(response)
    Wrangles JSON data into a Pandas df. 
  """
  
  def __init__(self, access_token: str):
    """
    Parameters
    --------------
    access token : str
      Inherited from the class SurveyMonkeyAPI, the API access_token. WARNING: very sensitive!!
    """
    super().__init__(access_token)
    
  def get_questions(self, survey_id: int):
    """Gets the questions of the given survey ID and produces a dictionary object.
    Keys are question ID. Values are a nested dictionary containing question text, order and type
    
    Parameters
    --------------
    survey_id : int
    """
    questions_dict = defaultdict(dict)
    url = self.host + f"surveys/{survey_id}/details"
    details = self.client.get(url)
    details_data = details.json()
    df = pd.json_normalize(data=details_data,
                           record_path=['pages', 'questions', 'headings'],
                           meta=[['pages', 'questions','id'], ['pages', 'questions', 'position'],['pages','questions','subtype']])
    df['heading'] = df['heading'].str.replace('<br>','') # get rid of the <br> in one of the questions

    for i, row in df.iterrows():
        questions_dict[row['pages.questions.id']] = {'heading' : row['heading'], 
                                                     'position' : row['pages.questions.position'],
                                                     'type' : row['pages.questions.subtype']}
    return questions_dict

  def get_collectors(self, survey_id: int):
    """Gets the collectors for the given surveys. Collectors can be used to identify the surveying period, or any specicial use cases for a survey.
    
    Parameters
    --------------
    survey_id : int
    """
    collector_dict = defaultdict(dict) 
    url = self.host + f"surveys/{survey_id}/collectors"
    collectors = self.client.get(url)
    collector_data = collectors.json()

    df = pd.json_normalize(data=collector_data,
                           record_path=['data'])
      
    for i, row in df.iterrows():
      collector_dict[row['id']] = {'name' : row['name'],
                                   'type' : row['type'],
                                   'href' : row['href']}
    return collector_dict
  
  def get_responses(self, survey_ids: int, start_created_at):
    """Fetches and wrangles all of the responses to the given survey ids from the given start date.
    Uses get_questions() and get_collectors() to build dictionary objects for the survey IDs, to be used in organise_responses() for mapping columns.
    
    Parameters
    --------------
    survey_id : int
    
    start_created_at : 
      if the fetch date is overrriden, then starts at the given date. If not, it will fetch data from today.
    """
    
    # For each response
      # Iterate through the survey_ids which are passed as arguments
      # the API supports only 100 responses per page, so loop through the 'next' url found in the json response
      # not all surveys have more than 100 responses, so wrap the loop in a try/except so it will continue through the survey ids if it fails
      # pass the response to organise_responses
      
    all_responses = []   
    for i in survey_ids:      
      try:        
        response_url = self.host + f"surveys/{i}/responses/bulk"
        payload = {'per_page' : '100',
                   'simple' : 'true',
                   'status' : 'completed',
                   'start_created_at' : str(start_created_at)}

        response = self.client.get(response_url, params=payload)
        response_data = response.json()
        
        questions = self.get_questions(survey_id=i)
        collectors = self.get_collectors(survey_id=i)
        all_responses.append(self.organise_responses(response=response_data, question_dict=questions, collector_dict=collectors))
        
        while 'next' in response_data['links']:
          response = self.client.get(response_data['links']['next'], params=payload)
          response_data = response.json()
          all_responses.append(self.organise_responses(response_data, question_dict=questions, collector_dict=collectors))      
      except:  
        pass

    all_responses = pd.concat(all_responses)
    all_responses.sort_values(by=['date_created','College','Qnumber'],inplace=True)

    return all_responses
  
  def organise_responses(self, response, question_dict, collector_dict):
    """Wrangles fetched responses using pandas.json_normalize. Produces a dataframe to be returned.
    Contextual data is extracted from the menu subtype questions, which provides College, Programme, Subject and Intake data for each unique respondent.
    New columns are created containing College, ProgrammeLevel, Intake, SubjectArea, Question Number, Collector Source and the date of response.
    The returned object response is appended to a list for concatenating in get_responses().
    
    Parameters
    --------------
    response
      The JSON GET return
    
    question_dict
      A nested dictionary containing question ID, with nested values containing contextual data like question name, order and type
      
    collector_dict
      A nested dictionary containing collector ID, with nested values containing contextual data like collector name, type and href    
    """
    
    # For each response
      # Create a Pandas dataframe, extracting key fields. Wrangle the data.
      # Remove unwanted text from the questions, such as <br>.
      # As this survey does not have custom variables built in, build a new dataframe and extract 'menu' type questions. These are student contextual data, like College and Programme.
      # Create a new Pandas dataframe containing just menu questions.
      # Create a dictionary containing this contextual information for each unique respondent. Key is the unique ID, with a nested dictionary containing key:values.
      # Question dictionary and collector dictionary are passed as arguments to organise_responses, containing details about the surveys such as question orders and collector names.
      # Create new columns in the dataframe, mapping keys to the dictionary.
      
    responses = pd.json_normalize(data=response['data'],
                                 record_path=['pages','questions','answers'],
                                 meta=['id', ['pages','questions','id'],['pages','questions','heading'],['pages','id'],['pages','questions','subtype'],['date_created'],['total_time'],['collector_id']],
                                 errors='ignore')
    
    def remove_text(text: str, exclude: str):
      for string in exclude:
        if string in text:
          text = text.replace(string,'')
      return text
    
    responses['pages.questions.heading'] = responses['pages.questions.heading'].apply(lambda x: remove_text(text=x, exclude=["<br>"]))
    
    context_questions = 'menu'
    query = responses['pages.questions.subtype'].isin([context_questions])
    student_variables = responses.loc[query]  
    student_variables_dict = defaultdict(dict)
    
    for i, row in student_variables.iterrows():
      student_variables_dict[row['id']][row['pages.questions.heading']] = row['simple_text']
    
    responses['College'] = responses['id'].map(student_variables_dict).apply(lambda x: x['Your college'])
    responses['ProgrammeLevel'] = responses['id'].map(student_variables_dict).apply(lambda x: x['Your programme level'])
    responses['Intake'] = responses['id'].map(student_variables_dict).apply(lambda x: x['Your intake'])
    responses['SubjectArea'] = responses['id'].map(student_variables_dict).apply(lambda x: x['Your subject area'])
    responses['Qnumber'] = responses['pages.questions.id'].map(question_dict).apply(lambda x: x['position'])
    responses['Collector'] = responses['collector_id'].map(collector_dict).apply(lambda x: x['name'])
    responses['date_created'] = pd.to_datetime(responses['date_created']).dt.tz_localize(None)

    return responses
    ```
