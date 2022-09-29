# Pruning and deleting branches from GitHub

To update the repo and remove branches that have been deleted from GitHub, use:

`git fetch --prune`

To delete branches manually:

```git
// delete branch locally
git branch -d localBranchName

// delete branch remotely
git push origin --delete remoteBranchName
```

Git will not let you delete the branch you are currently on so you must make sure to checkout a branch that you are NOT deleting. For example: `git checkout main`

Delete a branch with `git branch -d <branch>`.

For example: `git branch -d fix/authentication`

The `-d` option will delete the branch only if it has already been pushed and merged with the remote branch. Use `-D` instead if you want to force the branch to be deleted, even if it hasn't been pushed or merged yet.

The branch is now deleted locally.
