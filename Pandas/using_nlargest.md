# Using `nlargest()`

`nlargest()` is useful for quickly return a given number of rows in a dataframe based on a value.

```python
import pandas as pd
df.nlargest(n=3, columns='2020/21')
```

| Country of domicile   |   2014/15 |   2015/16 |   2016/17 |   2017/18 |   2018/19 |   2019/20 |   2020/21 |   18/21 CAGR |   Rank |
|:----------------------|----------:|----------:|----------:|----------:|----------:|----------:|----------:|-------------:|-------:|
| China                 |     89735 |     90735 |     95595 |    107215 |    121080 |    141870 |    143820 |      8.98668 |      1 |
| India                 |     18440 |     16890 |     16900 |     20335 |     27495 |     55465 |     84555 |     75.3649  |      2 |
| Nigeria               |     18080 |     16210 |     12820 |     10685 |     10810 |     13020 |     21305 |     40.3873  |      3 |

This will return a dataframe showing the top 3 records based on the value in column 2020/21. A list of columns can be passed to `columns`, ordering by the first value and then the second.
