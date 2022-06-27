# Using `rank()`

`rank()` is useful for categorising data in an orderly way. We can use it to rank countries by most enrolments or by a college that had the best score, amongst limitless other things. 

## Example

```python
import pandas as pd

df['Rank'] = df['2020/21'].rank(ascending=False, method='first', na_option='top')
```

|     | Country of domicile                                |   2014/15 |   2015/16 |   2016/17 |   2017/18 |   2018/19 |   2019/20 |   2020/21 |   18/21 CAGR |   Rank |
|----:|:---------------------------------------------------|----------:|----------:|----------:|----------:|----------:|----------:|----------:|-------------:|-------:|
|  48 | China                                              |     89735 |     90735 |     95595 |    107215 |    121080 |    141870 |    143820 |     8.98668  |      1 |
| 104 | India                                              |     18440 |     16890 |     16900 |     20335 |     27495 |     55465 |     84555 |    75.3649   |      2 |
| 165 | Nigeria                                            |     18080 |     16210 |     12820 |     10685 |     10810 |     13020 |     21305 |    40.3873   |      3 |
| 240 | United States                                      |     17190 |     17500 |     18065 |     19485 |     20620 |     20730 |     19220 |    -3.45443  |      4 |
| 101 | Hong Kong (Special Administrative Region of China) |     16275 |     16855 |     16870 |     16620 |     16375 |     16370 |     16655 |     0.851338 |      5 |

This creates a new column in the dataframe called `Rank`, where the college is ranking from 1 based on total enrolments in 2020/21.
`method='first'` will assign ranks to matching enrolments based on when they appeared in the dataset. `na_option='top'` will assign rank in ascending order where there is no value for '2020/21'.

Further documentatio can be found [here.](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rank.html)