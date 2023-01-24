# Using tmux

The `tmux` package allows you to create a separate shell which you can detach from and let it run in the background. If you had a one-off program that you know is going to take a long time (a make build command for instance), you can create a `tmux` session, run your long running command, detach from that session, and logout of the pi without worry.

## Create a session

`tmux new -s your_session_name`

Then run your Python script within this window.

## Detach from the session

```python
"Hit Ctrl + B"
"Then D"
```

## Reattach to session

```python
# list all the sessions running
tmux list-sessions

# attach to your session
tmux a -t your_session_name
```
