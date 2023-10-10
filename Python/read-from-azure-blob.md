# Read from Azure Blob Storage

The below can be used to read data out of a Azure data lake.

```python
from azure.storage.blob import BlobClient
import pandas as pd
from io import BytesIO

# Replace 'your_connection_string' and 'your_blob_name.csv' with your actual values
connection_string = "<your-connection-string>"
blob_name = "example-folder/example-file.csv"  # Specify the CSV file name
container_name = "example-container-name"

# Create a BlobClient using the connection string
blob_client = BlobClient.from_connection_string(conn_str=connection_string, 
                                                container_name=container_name, 
                                                blob_name=blob_name)
try:
    # Download the CSV blob content
    blob_data = blob_client.download_blob()
    content = blob_data.readall()

    # Convert the binary content to a DataFrame using pandas
    df = pd.read_csv(BytesIO(content))
    
    # Now you have a pandas DataFrame containing the CSV data
    print(df.head(1))
except Exception as e:
    print(f"An error occurred: {str(e)}") 
```
