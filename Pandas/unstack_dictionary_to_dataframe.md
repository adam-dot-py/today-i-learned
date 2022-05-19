# Unstack a dictionary to a DataFrame

Unstacking dictionaries can be useful where you want to join to another DataFrame, for example to match against a population. Typically you could use `map` to match against a dictionary `key`, but this can be problematic with nested dictionaries.

```python
import pandas

active_enrolments = {
    'Col1' : {'Value1' : 482, 'Value2' : 101, 'Value3' : 43},
    'Col2' : {'Value1' : 178, 'Value2' : 106, 'Value3' : 50}
}

s = pandas.DataFrame(active_enrolments).unstack().rename_axis(('Key', 'Sub key')).rename('Values').reset_index()
```

`rename_axis` should contain the `keys` and `keys` of the nested dictionary. `rename` should then be the name of the `values` for the associated `sub key`. Finally, `reset_index` resets the index to start from 0.

| Key   | Sub key   |   Values |
|:------|:----------|---------:|
| Col1  | Value1    |      482 |
| Col1  | Value2    |      101 |
| Col1  | Value3    |       43 |
| Col2  | Value1    |      178 |
| Col2  | Value2    |      106 |
| Col2  | Value3    |       50 |
