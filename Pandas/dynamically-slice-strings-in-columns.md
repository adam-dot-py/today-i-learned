# Dynamically Slice Strings in Columns

This is useful when you want to slice a string at a certain point but the length of the string can vary, like an email address.

```python
import pandas as pd

d = [['Adam', 'Lowe', 'adam.lowe@email.com']]
df = pd.DataFrame(data=d, columns=['FName','LName','Email'])

#--find the position of the character to strip before
df['pos'] = df['Email'].str.find('@')

#--apply this per row using lambda and string indexing, using the position to slice up to the character dynamically
df['id'] = df.apply(lambda x: x['Email'][0:x['pos']], axis=1)

#--one liner to avoid creating a new column
df['id'] = df.apply(lambda x: x['Email'][0:x['Email'].find('@')], axis=1)

print(df.to_markdown(index=False))
```

| FName   | LName   | Email               |   pos | id        |
|:--------|:--------|:--------------------|------:|:----------|
| Adam    | Lowe    | adam.lowe@email.com |     9 | adam.lowe |
