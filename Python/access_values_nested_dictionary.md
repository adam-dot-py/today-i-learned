# Access values in nested dictionary

Accessing values in a nested dictionary can be done via the `map` method, whilst also using `apply` and `lambda` functions.

When mapping, the return will be a nested dictionary containing the items for the matched value in `map`. `lambda` then allows for the dictionary to be sliced to the desired value in the nested dictionary.

```python
question_dict = {
    '60733065' : {'QuestionText' : 'Teaching staff are good at explaining things', 'Area' : 'The teaching on my course', 'Scale' : 'Scale01'},
    '60733066' : {'QuestionText' : 'Teaching staff have made the subject interesting', 'Area' : 'The teaching on my course', 'Scale' : 'Scale01'}
}

d = {'questionID' : ['60733065', '60733066']}
test_df = pd.DataFrame(data=d)

test_df['QuestionText'] = test_df.questionID.map(question_dict).apply(lambda x: x['QuestionText'])
test_df['Area'] = test_df.questionID.map(question_dict).apply(lambda x: x['Area'])
test_df['Scale'] = test_df.questionID.map(question_dict).apply(lambda x: x['Scale'])
```
