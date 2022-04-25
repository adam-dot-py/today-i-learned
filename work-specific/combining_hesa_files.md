# Combining HESA files

The below was used to combine HESA files. I renamed the files to their respective academic year and then combined them all. To get a more readable academic year, I replaced the values with a formatted string using a dictionary and `map`.

This is useful where you need to extract different tables from HESA filtered to different variables, and then combine all together into one large dataset.

```python
import pandas as pd
import glob
import os

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
# df = pd.concat([pd.read_csv(f, skiprows=17) for f in all_filenames ])

data = []

for f in all_filenames:
    frame = pd.read_csv(f, skiprows=17)
    frame['AcademicYear'] = os.path.basename(f).replace('_entrants.csv','') # remove the appended string in the filename
    frame.columns = [x.replace(' ','') for x in frame.columns] # remove spaces from column headers
    data.append(frame)

df = pd.concat(data) # combined data

academic_years=  {
    '201415' : '2014/15',
    '201516' : '2015/16',
    '201617' : '2016/17',
    '201718' : '2017/18',
    '201819' : '2018/19',
    '201920' : '2019/20',
    '202021' : '2020/21',
}
df['AcademicYear'] = df['AcademicYear'].map(academic_years)

df = df.query('HEprovider != "Total"')
df.to_csv('extract.csv', index=False)
```