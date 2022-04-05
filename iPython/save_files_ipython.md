## Saving, loading and running files in the iPython environment

You can write a session to file using the magic function `%%writefile`. 

`%%writefile myfile.py`

    write/save cell contents into myfile.py (use -a to append). Another alias: %%file myfile.py

To run

`%run myfile.py`

    run myfile.py and output results in the current cell

To load/import

`%load myfile.py`

    load "import" myfile.py into the current cell

For more magic and help

`%lsmagic`

    list all the other cool cell magic commands.

%COMMAND-NAME?

    for help on how to use a certain command. i.e. %run?
