# Download a file

This is similar to `wget` in Linux.

```python
import requests
import os
import re
import sys
from tqdm import tqdm

def main():

    path = r'c:\Users\User\Downloads'

    class DownloadFile:
        '''
        downloadFile(self, fname, extension, url) --> downloads the file at the targeted url)

        Parameters:
        self.url = sys.arg for the target url to download
        self.fname = name of the file, taken from the last section of the url

        Methods:
        download = download the file
        content_type = print the content type of the file
        '''
        def __init__(self):
            self.url = sys.argv[1]
            self.fname = self.url.split("/")[-1]

        def __str__(self):
            return f"{self.fname}"

        def get_download(self):
            r = requests.get(self.url, stream=True)
            with open(f"{os.path.join(path, self.fname)}", 'wb') as handle:
                for data in tqdm(r.iter_content(chunk_size=10000)):
                    handle.write(data)
            print(f"Downloaded {self.fname}")
              
        def get_content_type(self):
            r = requests.head(self.url)
            headers = r.headers
            content_type = headers.get('content-type')
            return content_type

    x = DownloadFile()
    x.get_download()

if __name__ == '__main__':
    main()
```
