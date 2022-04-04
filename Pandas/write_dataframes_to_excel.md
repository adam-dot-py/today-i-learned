# Write DataFrames to Excel

You can use the `pd.to_excel` method to write to a singular Excel file and tab. However, when you want to write multiple DataFrames to a singular Excel file with multiple sheet names, you should use `writer`.

```python
import pandas as pd
import numpy as np
path = 'path\to\file'

df1 = pd.DataFrame(np.random.randint(1,100, size=(5,4)), columns = list('ABCD'))
df2 = pd.DataFrame(np.random.randint(1,50, size=(10,5)), columns = list('ABCDE'))

writer = pd.ExcelWriter(path = path, engine='xlsxwriter')

df1.to_excel(writer, sheet_name='df1', ignore_index=True)
df2.to_excel(writer, sheet_name='df2', ignore_index=True)

writer.save()
writer.close()
```
