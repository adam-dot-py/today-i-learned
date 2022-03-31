# Constructing a DataFrame From a Dictionary

You can create a dataframe in Python using Pandas from a dictionary. You construct it in the same way standard dictionaries are constructured.

```python
d = {'col1': [1, 2], 'col2': [3, 4]}

df = pd.DataFrame(data=d)
```

Where there is no list values for the keys, it makes more sense to construct a dataframe using the `pd.Series` method:

```python
questions = dict(zip(question_id, question_text))

df = pd.Series(questions, name="QuestionText")
df.index.name = "QuestionID"
df = df.reset_index()
```

This will produce a dataframe.

You can also do it using the items method:

```python
df = pd.Dataframe(questions.items(), columns=['QuestionID','QuestionText'])
```
