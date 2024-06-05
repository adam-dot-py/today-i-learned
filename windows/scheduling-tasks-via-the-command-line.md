# Scheduling tasks via the command line

Windows tasks can be scheduled directly from the **command line**. In the below example, we schedule a **Python** script to run every Monday at 6:05am.

`schtasks /create /tn "run_python_script" /tr "C:\Python39\python.exe C:\Scripts\my_script.py" /sc weekly /d MON /st 06:05 /ru "System"`

## Breakdown

- **/create**: Creates a new scheduled task.
- **/tn "run_python_script"**: Specifies the task name as "run_python_script".
- **/tr "C:\Python39\python.exe C:\Scripts\my_script.py"**: Specifies the task to run. In this case, it runs the Python executable (python.exe) followed by the path to your script (C:\Scripts\my_script.py).
- **/sc weekly**: Sets the schedule to weekly.
- **/d MON**: Specifies the day of the week to run the task (Monday).
- **/st 06:05**: Sets the start time to 6:05 AM.
- **/ru "System"**: Runs the task under the "System" account.