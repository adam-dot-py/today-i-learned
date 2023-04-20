# Uninstall all Python packages

Useful when needing to neutralise a Python distribution.

First, export all installed packages:

`pip freeze > requirements.txt`

Next, uninstall each one by one:

`pip uninstall -r requirements.txt`

To remove all of them at once:

`pip uninstall -r requirements.txt -y`

To do all the above as a single command:

`pip uninstall -y -r <(pip freeze)`
