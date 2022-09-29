# Rename Branches

To rename the current branch:

`git branch -m <newname>`

To rename a branch while pointed to any branch:

`git branch -m <oldname> <newname>`

> You need to use `git branch -M <newname> if only changing capitalisation, otherwise Git will say it exists`

To push the local branch and reset the upstream branch:

`git push origin -u <newname>`

To delete the more branch;

`git push origin --delete <oldname>`
