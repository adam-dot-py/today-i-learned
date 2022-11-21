# Create QR Codes

This is useful for creating QR codes from survey link builders. Used as part of a project in Navitas.

```python
import qrcode
import pandas as pd
import zipfile as zp
import os

path = r'C:\Users\Adam.Lowe\path_to_file'

all_links = []
exclude = ['Instructions', 'validations', 'survey_link']

for root, dir, files in os.walk(path):
    for file in files:
        if file.endswith('.xlsx'):
            benchmark_dict = pd.read_excel(os.path.join(root, file), sheet_name=None, skiprows=9, engine='openpyxl')
            for name, frame in benchmark_dict.items():
                if name not in exclude:
                    frame['source'] = name
                    all_links.append(frame)
                
link_df = pd.concat(all_links)

# Method 1

colleges = link_df['source'].unique()
link_df = link_df.loc[(~link_df['Programme'].str.contains('Example', na=False))]

urls = [(row[0], row[1], row[2], row[3]) for row in zip(link_df['source'], link_df['Programme'], link_df['Module Code'], link_df['URL'])]

for i, (college, programme, module, url) in enumerate(urls):
    os.makedirs(college, exist_ok=True)
    img = qrcode.make(url)
    img.save(f"{college}/{programme}_{module}.png")
    
    with zp.ZipFile(f"{college}_qr_codes.zip", "w") as zipF:
        for root, dirs, files in os.walk(f"{college}"):
            for file in files:
                zipF.write(os.path.join(root, file), compress_type=zp.ZIP_DEFLATED)
```
