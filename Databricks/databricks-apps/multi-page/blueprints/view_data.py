from flask import Blueprint, current_app, render_template

view_data_bp = Blueprint("view_data", __name__)


@view_data_bp.route("/")
def index():
    get_connection = current_app.config["GET_CONNECTION"]
    rows = []
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, name, category, created_at"
                    " FROM my_catalog.my_schema.entries"
                    " ORDER BY created_at DESC"
                    " LIMIT 100"
                )
                rows = cursor.fetchall()
    except Exception as exc:
        rows = []
        print(f"Error fetching rows: {exc}")

    return render_template("view_data.html", rows=rows)
