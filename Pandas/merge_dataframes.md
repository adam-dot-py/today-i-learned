# Merging dataframes

Merging dataframes is done via `pd.concat`. 

```python
df = pd.DataFrame(np.random.randint(0, 50, size = (4, 5)), columns = list('ABCDE'))
df2 = pd.DataFrame(np.random.randint(0, 50, size = (4, 5)), columns = list('ABCDE'))

frames = [df, df2]
df = pd.concat(frames, ignore_index=True)
```

## Output

|    |   A |   B |   C |   D |   E |
|---:|----:|----:|----:|----:|----:|
|  0 |  34 |  37 |   6 |  39 |  20 |
|  1 |  47 |  27 |  42 |   7 |  18 |
|  2 |  27 |   6 |  41 |  45 |  16 |
|  3 |  10 |  14 |  18 |  41 |  28 |
|  4 |  28 |  15 |  43 |  47 |   3 |
|  5 |  19 |   4 |  38 |  44 |   5 |
|  6 |  32 |  16 |  34 |   6 |  11 |
|  7 |  28 |  45 |  19 |  44 |  24 |

Further syntax including handling dataframes of different shapes can be found [here](https://pandas.pydata.org/docs/user_guide/merging.html).
