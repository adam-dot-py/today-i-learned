# Using Fuzzy Matching

Python can utilise fuzzy matching to look up words to identify best matches. In the below example, I use it to look up agents from one dataset with another.

```python
import pandas as pd
from fuzzywuzzy import process

# Sample DataFrames
bcu_agents = pd.read_excel('bcu-agents.xlsx', sheet_name='bcu-agents')
bcuic_agents = pd.read_csv('bcuic-agents.csv').dropna(subset=['AgencyCode'])

# Define a function to perform fuzzy lookup
def fuzzy_lookup(row):
    query = row['Company'] # row can be interpreted as df, with the column being selected
    match = process.extractOne(query, bcuic_agents['AgencyName']) # returns a tuple
    best_match = match[0]
    similarity_score = match[1]
    
    if similarity_score >= 90:  # Adjust the similarity threshold as needed
        return 'joint', best_match
    else:
        return 'non-joint', None

# Apply the fuzzy_lookup function to each row in bcu_agents
bcu_agents[['MatchStatus', 'BestMatch']] = bcu_agents.apply(fuzzy_lookup, axis=1, result_type='expand')
```
