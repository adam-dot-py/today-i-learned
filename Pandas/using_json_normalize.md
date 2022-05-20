# Using JSON normalize

`pandas.json_normalize` allows you to take a JSON object or string and create a flat table.

```python
    raw_responses = pd.json_normalize(data=response['data'],
                                      record_path=['pages', 'questions', 'answers'],
                                      meta=['id', ['pages', 'questions', 'id'], ['pages', 'questions', 'heading'], ['pages', 'id'], ['custom_variables'], ['date_created'], ['total_time']],
                                      errors='ignore')
```

The positional keyword `data` is the JSON object to normalize. This is the root directory, but you can start from a different path, like the above example, where we start from `data`.

`record_path` is the path in each object to list of records. If not passed, data will be assumed to be an array of records. Items within this path are returned.

`meta` is additional fields to be included alongside the `record_path`. You can take elements from `sub-paths` by nesting a list. For example `['id', ['pages', 'questions', 'id']]` will return the `id` as well as the `question id`.
