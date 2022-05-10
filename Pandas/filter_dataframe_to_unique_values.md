# Filter a DataFrame to unique values in a column

It is sometimes useful to filter a DataFrame to unique items, for example when wanting to identify what questions are being asked in survey, where the dataset is full of duplicate questions as students respond.

This can be achieved by applying the `drop_duplicates` method to a DataFrame.

```python
questions_output = questions[[ 
    'QuestionNumber',
    'QuestionText
]].drop_duplicates(subset=['QuestionNumber'])
```

`subset` can accept a list of columns, in which any duplicate entries will be dropped. Here, we are returning only unique `QuestionNumbers`.

|    |   QuestionNumber | QuestionText                                                                               |
|---:|-----------------:|:-------------------------------------------------------------------------------------------|
|  4 |                1 | Teaching staff are good at explaining things                                               |
|  5 |                2 | Teaching staff have made the subject interesting                                           |
|  6 |                3 | The course is intellectually stimulating                                                   |
|  7 |                4 | My course and teaching staff are challenging me to achieve my best work                    |
|  8 |                6 | My course provides me with opportunities to explore ideas or concepts in depth and breadth |
