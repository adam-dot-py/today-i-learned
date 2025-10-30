# Extract JSON from string

To extract JSON fields from a string column in SQL on Databricks, use the built-in functions like `get_json_object` or `from_json`.

`get_json_object(json_string, '$.field')` extracts a specific field from a JSON string.

`from_json(json_string, schema)` parses the JSON string into a struct, which you can then select fields from.

```sql
%sql
SELECT
  get_json_object(UserFeedback, '$.fieldName') AS extracted_field
FROM edp.latest.aivree_assessment_feedback
```

```sql
%sql
SELECT
  from_json(UserFeedback, 'fieldName STRING, anotherField INT') AS parsed_json
FROM edp.latest.aivree_assessment_feedback
```