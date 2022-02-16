# Combining Columns

In Pandas, you can create a new column from a combination of columns, resulting in the data being joined. If you add a seperator, like an underscore, you can easily read the return value.

```
scores = {"player" : ['Mane', 'Salah', 'Jota'],
          "team" : ['Liverpool','Liverpool', 'Liverpool'],
          "score" : [10, 5, 9]
          }

df = pd.DataFrame(scores)

df['player_team'] = df['player'] + '_' + df['team']

```