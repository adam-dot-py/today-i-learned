import os

from databricks import sql
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", os.urandom(24))


def get_connection():
    """Return a Databricks SQL connection using environment variables."""
    return sql.connect(
        server_hostname=os.environ["DATABRICKS_HOST"],
        http_path=os.environ["SQL_WAREHOUSE_HTTP_PATH"],
        access_token=os.environ["DATABRICKS_TOKEN"],
    )


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        category = request.form.get("category", "").strip()

        if not name or not category:
            flash("Both fields are required.", "error")
            return redirect(url_for("index"))

        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO my_catalog.my_schema.entries (name, category)"
                        " VALUES (?, ?)",
                        [name, category],
                    )
            flash("Record saved successfully!", "success")
        except Exception as exc:
            flash(f"Error saving record: {exc}", "error")

        return redirect(url_for("index"))

    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("DATABRICKS_APP_PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
