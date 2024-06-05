# Using crontab

**Crontab** is used for scheduling tasks in Linux. To access **crontab**, use the `crontab -e` command.

## Setting up a cron tasks

The below example creates a job that runs every 5 minutes every day:

`*/5 * * * * ~/duckdns/duck.sh >/dev/null 2>&1`

- `*/5`: This means "every 5 minutes". The `*/` syntax is used to specify a step value.
- `*`: This means *every hour*.
- `*`: This means *every day of the month*.
- `*`: This means *every month*.
- `*`: This means *every day of the week*.

## Viewing the cron log

To view the **crontab** log, use `grep CRON /var/log/syslog`. This is the standard file path for logging cron activity and the command would need to change if that path was to change. 

`grep`, short for *global regular expression print*, is a command used for searching and matching text patterns in files contained in the regular expressions. So, in the above command, we are searching for files in the given directory that contain *CRON*.