# Create dynamic bat scripts

This can be used to create a `.bat` script that can run independent of the machine it runs on -- like when using OneDrive. We first get the absolute path to the directory, then get the full directory to the script and finally execute it.The `%~dp0` references the current working directory of the `.bat` file.

```powershell
@echo off
rem Get the absolute path to the directory containing this batch script
set "SCRIPT_DIR=%~dp0"

rem Print the absolute path to the directory containing this batch script
set "PYTHON_SCRIPT=%SCRIPT_DIR%update-script.py"

rem Run your Python script
python "%PYTHON_SCRIPT%"
pause
```

When a dynamic structure is not needed, we can use the following to execute a `.bat` script:

```powershell
python %~dp0python_script.py
```

If running a `.bat` file from another location is required, we can use:

```powershell
python path\to\script.py
```
