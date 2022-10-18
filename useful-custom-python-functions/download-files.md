# Download files

```python
import requests
import re
import os
import sys
from tqdm import tqdm

class DownloadFile:
    '''
    DownloadFile(self, url) --> downloads the file at the targeted url)

    Parameters:
    url = the target url for the file download

    Methods:
    get_download = download the file
    get_content_type = print the content type of the file
    '''
    def __init__(self, url):
        self.url = url
        self.fname = self.url.split("/")[-1]
        
    def __str__(self):
        return f"{self.fname}"

    def get_download(self):
        r = requests.get(self.url, stream=True)
        with open(f"{self.fname}", 'wb') as handle:
            for data in tqdm(r.iter_content(chunk_size=10000)):
                handle.write(data)
        print(f"Downloaded {self.fname}")
            
    def get_content_type(self):
        r = requests.head(self.url)
        headers = r.headers
        content_type = headers.get('content-type')
        return content_type

x = DownloadFile(url='https://ofslivefs.blob.core.windows.net/files/NSS%20data%202022/September/NSS_taught_all22_CAH.xlsx')
x.get_download()
```
