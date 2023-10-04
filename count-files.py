import os

total = 0
exclude = set(['work-specific', 'graph_examples', 
               'til', 'supporting-images', 
               '.vscode', 'README.md', 
               '.gitignore', 'example-datasets',               
               'notebook.ipynb', '.git'])

for root, dirs, files in os.walk(os.getcwd()):
    dirs[:] = [d for d in dirs if d not in exclude]
    total += len(files)
    
print(f"There are {total} files so far.")