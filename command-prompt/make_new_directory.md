# Make a new folder using command prompt

## Create a folder

To create a directory in MS-DOS or the Windows command line (cmd), use the `md` or `mkdir` MS-DOS command. For example, below, we are creating a new directory called `test` in the current directory.

`mkdir test`

## Create a folder with spaces

If you want to create a directory with spaces, you need to surround the directory name with quotes. In the example below, we create a `my test directory` in the current directory.

`mkdir "my test directory"`

## Create a folder in the Parent directory

To create a directory in the parent directory without first moving to that directory, you can use the command below. This example moves back one directory to create the "example" directory.

`mkdir ..\example`
