# Download and Save Files

Python can be used to download files from the internet.

## Smaller files

Where the file is small, it is safe to load the file all into memory:

```python
url = "https://stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2021-financial-year-provisional/Download-data/annual-enterprise-survey-2021-financial-year-provisional-csv.csv"

r = requests.get(url)

with open('download.csv', 'wb') as handle:
    handle.write(r.content)
```

## For larger files

However, for larger files it is not efficient to load the file into memory. Instead, we should iterate over the file and `stream` it.

```python
from tqdm import tqdm
import requests

r = requests.get(url, stream=True)

with open('download.csv', 'wb') as handle: # file extension should be whatever the target download file is
    for data in tqdm(r.iter_content()):
        handle.write(data)
```

`tqdm` is used to provide a progress bar.

## Downloading ZipFiles

```python
import requests, zipfile, io

url = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-large-zip-file.zip"

r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall() # can also include any path to save elsewhere
```

Recent versions of Microsoft Windows Explorer use Deflate64 compression when creating ZIP files larger than 2GB. With the ubiquity of Windows and the ease of using "Sent to compressed folder", a majority of newly-created large ZIP files use Deflate64 compression.

However, support for Deflate64 in the open-source ecosystem is very poor! Most ZIP libraries have declined to implement Deflate64, citing its proprietary nature.

### Download the ZipFile (including a Deflate64 type)

```python
import requests

url = "https://www.hesa.ac.uk/data-and-analysis/students/table-28.csv"

r = requests.get(url, stream=True)
with open('table_28.zip', 'wb') as handle:
    print(f"File found -> {r.ok}")
    for data in tqdm(r.iter_content(chunk_size=10000)): # 10 mbs per second 
        handle.write(data)
```
