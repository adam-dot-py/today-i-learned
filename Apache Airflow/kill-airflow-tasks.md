# Kill airflow tasks

First find the  process ids for **webserver** and **scheduler** in the `.pid` files that are generated when running these processes. The best practice is to first kill the process id and then overwirte the process id file with an empty string, like so:

Kill the process:

```
cat $AIRFLOW_HOME/airflow-webserver.pid | xargs kill
```

Write an empty string to the .pid file:

```
echo "" > $AIRFLOW_HOME/airflow-webserver
```

When running **Airflow** commands, run them with the `-D`, or **daemon** argument to ensure they run as with a `pid`, like so:

```
airflow scheduler -D
```