# Appending (or combining) CSVs in Python

Using `Python`, you can easily append multiple CSV files into one `Dataframe`, which can then be exported.

In the below example, it uses `glob` to grab all files in a directory with a given `extension`, in this case a `CSV`.

It is important that the column headers match, otherwise new columns will be created with alias names.

```Python
extension = 'csv'
all_filenames = [i for i in glob.glob(f'*.{extension}')]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, error_bad_lines=True) for f in all_filenames ])
combined_csv.sort_values(by=['studyPeriodCode'], ascending=True)
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
```

You can also do it this way:

```python
data = []

for x in all_files:
    frame = pd.read_csv(x)
    data.append(frame)

df = pd.concat(data)
```

or this way using `os`:

```python
import os
import pandas as pd

all_files = []
for root, dirs, files in os.walk(os.getcwd): # or enter an absolute path to your dir
    for file in files: 
        if file.endswith(".csv"): # can have multiple conditions
            all_files.append(os.path.join(root, file))

pdf = pd.concat([pd.read_csv(f) for f in all_files])
```

with multiple conditions:

```python
import os
import pandas as pd

all_files = []
for root, dirs, files in os.walk(os.getcwd): # or enter an absolute path to your dir
    for file in files: # can have multiple conditions
        if (file.endswith(".csv")) & ("some-string" in file):
            all_files.append(os.path.join(root, file))

pdf = pd.concat([pd.read_csv(f) for f in all_files])
```
