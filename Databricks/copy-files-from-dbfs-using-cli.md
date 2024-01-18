# Copy files from DBFS using the CLI

>[!NOTE]
>
>This requires your Databricks account to be configured.

When you have the `databrick cli` installed, you can use it to access the `filestore`.

## Copying Entire Folder

`databricks fs cp -r dbfs:/path/to/folder my/local/path --profile dev`

You need to ensure to include the `recursive` flag using `-r`.

The `--profile dev` part should only be used if you need to switch to a different instance.

## Copying a single file

`databricks fs cp dbfs:/path/to/folder/my_file.txt my/local/path`

When copying a single file, provide the file path to the full file and leave out the `recursive -r` flag.

