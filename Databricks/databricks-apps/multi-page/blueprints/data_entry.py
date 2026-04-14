from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for

data_entry_bp = Blueprint("data_entry", __name__)


@data_entry_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        category = request.form.get("category", "").strip()

        if not name or not category:
            flash("Both fields are required.", "error")
            return redirect(url_for("data_entry.index"))

        get_connection = current_app.config["GET_CONNECTION"]
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

        return redirect(url_for("data_entry.index"))

    return render_template("data_entry.html")
