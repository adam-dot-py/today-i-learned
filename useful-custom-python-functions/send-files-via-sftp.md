# Send files via SFTP

This function can be used to send files via a SFTP server.

```python
def send_xml_data(self, hostname, username, password, port, remote_dir) -> None:
    """
    Establishes an SFTP connection and uploads each file to the
    specified SFTP server.

    hostname, username and password should be extracted from Azure keyvault for safety.
    """
    self.hostname = hostname
    self.username = username
    self.password = password
    self.port = port
    self.remote_dir = remote_dir
    
    # connect to the server
    with pysftp.Connection(hostname, username, password, port) as sftp:
    # change to the remote dir
    sftp.cwd(remote_dir)
    
    # local path to file
    # upload the file
    sftp.put(self.file_path)
```
