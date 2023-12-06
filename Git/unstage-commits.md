# Unstage commits

If you have commited changes but want to uncommit the latest change, you can use the following:

`git restore --staged file.txt`

You can also do this:

```git reset --soft HEAD~1`

After this, you'll have the first changes in the index (visible with `git diff --cached`), and your newest changes not staged.
