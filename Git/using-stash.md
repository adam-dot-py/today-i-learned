# Using stash

Use `git stash` when you want to record the current state of the working directory and the index, but want to go back to a clean working directory. This is particularly useful when want to rebase the working directory with master but ensure you are on a clean directory, before bringing back the changes.

## Stash changes

`git stash`

## Bring back stashes

`git stash pop n` where `n` is the index number of the stash.
