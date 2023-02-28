# Recover a deleted file

Use the `git checkout` command to restore the deleted file from the previous commit or branch. For example, if the deleted file was last present in a commit with hash "abc123", you can use the following command to retrieve the file:

```bash
git checkout abc123 -- path/to/deleted/file
```

If the file was last present in a branch called "my-branch", you can use the following command to retrieve the file:

```bash
git checkout my-branch -- path/to/deleted/file
```

If you accidentally delete a file from your local working directory and want to retrieve it, you can use the `git checkout` command with the name of the file instead of a commit or branch. For example, if you accidentally deleted a file called `myfile.txt`, you can use the following command to restore it:

```bash
git checkout -- myfile.txt
```
