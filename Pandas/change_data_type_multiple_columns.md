## Change the datatype of multiple columns at once

This can be done by passing a dictionary as an argument in `astype`. 

```python
df = df.astype({'choice_metadata.weight' : 'int64',
               'choice_id' : 'int64',
               'row_id' : 'int64',
               'id' : 'int64',
               'questions.answers.id' : 'int64',
               'ResponseDate' : 'datetime64'})
```