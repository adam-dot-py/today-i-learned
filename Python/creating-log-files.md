# Creating log files

By using `logging`, you can create log files that log the actions of a script, making it easy to debug
or find issues within your code.

To use `logging`, first import the package

```python
import logging
```

Next, you need to configure a basic `logging` config:

```python
todays_date = datetime.today().date()
log_file_name = f"error_log_{todays_date}"
logging.basicConfig(filename=log_file_name,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO,
                    force=True)
```

The use of `force=True` ensures that any previous loggers using
the root handle are removed.

To log events, you simple call `logging` with the required action

```python
logging.error("This is an error")
logging.info("This is information")
logging.warning("This is a warning")
```

