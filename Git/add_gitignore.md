# Adding a .gitignore file and resyncing

To untrack a single file that has already been added/initialized to your repository, i.e., stop tracking the file but not delete it from your system use: 

`git rm --cached filename`

To untrack every file that is now in .gitignore:

First commit any outstanding code changes, and then, run this command:

`git rm -r --cached .`

This removes any changed files from the index(staging area), then just run:

`git add .`

Commit it:

`git commit -m ".gitignore is now working"`
