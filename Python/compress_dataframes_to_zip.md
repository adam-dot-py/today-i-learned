# Compress multiple dataframes to zip

When dealing with a file of large size - like `xlsx` or `csv` - it is often best to write to a compressed folder.

```python
compression_method = dict(method='zip', archive_name='responses.csv')

df.to_csv('responses.zip', index=False, compression=compression_method)
```

`compression_method` is a dictionary where by we tell the `compression` variable we want to create a zipped folder with the name `responses.csv`. This creates a `zip` folder containing the file.

You can also write multiple files to a zip file using the inbuilt module `zipFile`.

```python
import pandas as pd
import numpy as np
import zipfile

# Create dataframes

df1 = pd.DataFrame(np.random.randint(1, 100, size = (4,5)), columns = list("ABCDE"))
df2 = pd.DataFrame(np.random.randint(1, 100, size = (4,5)), columns = list("ABCDE"))
df3 = pd.DataFrame(np.random.randint(1, 100, size = (4,5)), columns = list("ABCDE"))

# Extract the dataframes to CSVs
frames = {'df1' : df1,
          'df2' : df2,
          'df3' : df3}

with zp.ZipFile('zip.zip', 'w') as zipF:
    csvs = []
    # Create CSVs then write them to a zip
    for i in range(1, len(frames) + 1): # we plus 1 to get [0,1,2,3,4] instead of [0,1,2] as values from 1 are used to match to the dictionary
        frame = frames['df' + str(i)] # df0 would not match, but df1 does.
        frame.to_csv("df" + str(i) + ".csv")
        csvs.append("df" + str(i) + ".csv")
        for csv in csvs:
            zipF.write(csv, compress_type=zp.ZIP_DEFLATED)
```
