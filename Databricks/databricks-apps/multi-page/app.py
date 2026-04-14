import os

from databricks import sql
from flask import Flask

from blueprints.data_entry import data_entry_bp
from blueprints.home import home_bp
from blueprints.view_data import view_data_bp

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", os.urandom(24))

app.register_blueprint(home_bp)
app.register_blueprint(data_entry_bp, url_prefix="/enter")
app.register_blueprint(view_data_bp, url_prefix="/view")


def get_connection():
    """Return a Databricks SQL connection using environment variables."""
    return sql.connect(
        server_hostname=os.environ["DATABRICKS_HOST"],
        http_path=os.environ["SQL_WAREHOUSE_HTTP_PATH"],
        access_token=os.environ["DATABRICKS_TOKEN"],
    )


# Make the connection factory available to all blueprints via app context.
app.config["GET_CONNECTION"] = get_connection


if __name__ == "__main__":
    port = int(os.environ.get("DATABRICKS_APP_PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
