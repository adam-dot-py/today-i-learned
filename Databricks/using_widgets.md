# Using widgets

Widgets allow you to add interactivity to Jupyter notebooks, including those inside Databricks. They can be used to input values into functions from the user, making for dynamic environments.

In particular, we used widgets to override the `fetch_date` for a survey, so we could have a default value (current day) but the user could select a different date value. 

## Example

```python
import ipywidgets as widgets

w = widgets.IntSlider(value=22)

print(f"You selected {w.value}!")
```

## Use case

```python
dbutils.widgets.text("override","N","1. Override Date?")
dbutils.widgets.text("fetch_date","2021-01-01","2. Fetch From Date")

if getArgument("override") == "Y": # Used to pass data to fragment, and in the Fragment code, you can call getArguments() to get what you passed to it.
  fetch_date = datetime.today().date()
else:
    # split the given datetime value abd convert to datetime
  fetch_date = datetime.strptime(getArgument("fetch_date").split("-")[0]+getArgument("fetch_date").split("-")[1]+getArgument("fetch_date").split("-")[2], "%Y%m%d").date()
  ```
  