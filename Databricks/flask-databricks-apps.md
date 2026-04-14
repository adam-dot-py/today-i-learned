# Flask in Databricks Apps

Databricks Apps supports Python web frameworks like Flask. This means you can build full web applications that run inside your Databricks workspace, with access to Unity Catalog tables via the Databricks SQL connector.

Two common questions answered here:

1. **Can I build a form that inserts data into a Delta table?** Yes.
2. **Can I build multi-page apps?** Yes, using Flask Blueprints.

---

## How Databricks Apps works with Flask

Databricks Apps expects a standard Python web server. For Flask, the app must:

- Listen on the port provided by the `DATABRICKS_APP_PORT` environment variable.
- Use `databricks-sql-connector` (or the Databricks SDK) to talk to a SQL Warehouse.
- Be structured with a `requirements.txt` so Databricks can install dependencies.

Authentication to the SQL Warehouse is handled by passing a personal access token (or service principal token) via an environment variable configured in the App settings.

---

## Single-page data entry app

See [`databricks-apps/single-page/`](databricks-apps/single-page/) for a full working example.

The key pattern is:

```python
# connect to the SQL Warehouse
import os
from databricks import sql

def get_connection():
    return sql.connect(
        server_hostname=os.environ["DATABRICKS_HOST"],
        http_path=os.environ["SQL_WAREHOUSE_HTTP_PATH"],
        access_token=os.environ["DATABRICKS_TOKEN"],
    )
```

Then a standard Flask POST route reads the form values and executes an `INSERT`:

```python
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        category = request.form["category"]
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO my_catalog.my_schema.entries (name, category) VALUES (?, ?)",
                    [name, category],
                )
        flash("Record saved!", "success")
        return redirect(url_for("index"))
    return render_template("index.html")
```

---

## Multi-page app

See [`databricks-apps/multi-page/`](databricks-apps/multi-page/) for a full working example.

Flask Blueprints let you split each page into its own module, keeping the code clean:

```
multi-page/
├── app.py                  # creates the Flask app and registers blueprints
├── requirements.txt
├── blueprints/
│   ├── __init__.py
│   ├── home.py             # "/" — landing page
│   ├── data_entry.py       # "/enter" — form to insert a row
│   └── view_data.py        # "/view" — table showing existing rows
└── templates/
    ├── base.html           # shared nav bar and layout
    ├── home.html
    ├── data_entry.html
    └── view_data.html
```

Each blueprint is registered in `app.py`:

```python
from blueprints.home import home_bp
from blueprints.data_entry import data_entry_bp
from blueprints.view_data import view_data_bp

app.register_blueprint(home_bp)
app.register_blueprint(data_entry_bp, url_prefix="/enter")
app.register_blueprint(view_data_bp, url_prefix="/view")
```

Navigation between pages is just standard HTML links (or `url_for` calls), no special Databricks-specific handling needed.
