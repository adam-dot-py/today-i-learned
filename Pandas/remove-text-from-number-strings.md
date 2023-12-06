# Remove text from number strings

In some instances when cleaning data, you may have text in columns like `age`, where the data may be something like `25 years`. In this case, we want to just have `25`.

We can solve this by iterating over the string (`x`) and joining it if it meets the parameters.

```python
df['Age'] = df['Age'].apply(lambda x: ''.join(filter(str.isdigit, str(x).split('.')[0])) if pd.notnull(x) else np.nan)
```
