# Using `np.where`

`np.where()` can be used to evaluate a condition, sort of like `if` and `else`. We can use it to return elements chosen from x or y depending on condition, these elements can be hard input values or alternatively another value from a column in a dataframe.

## Example 1

In this example we compare a benchmark figure to an actual figure. Where the actual is greater than the benchmark, we return `1` else `0`. These can be string values or reference other columns. Where we reference another column, it will return the value from that column in the same index.

```python
pdf['2021_taught_isAboveBenchmark'] = np.where(pdf['2021_taught_Agree_%'] > pdf['2021_taught_benchmark_%'],1,0)
```
