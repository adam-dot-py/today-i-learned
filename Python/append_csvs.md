# Appending (or combining) CSVs in Python

Using `Python`, you can easily append multiple CSV files into one `Dataframe`, which can then be exported. 

In the below example, it uses `glob` to grab all files in a directory with a given `extension`, in this case a `CSV`. 

It's important that the column headers match, otherwise new columns will be created with alias names. 

```Python
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

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