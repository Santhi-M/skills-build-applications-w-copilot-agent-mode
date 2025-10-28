from flask import Flask

def create_app():
    """Create and return the Flask application for OctoFit Tracker skeleton."""
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "OctoFit Tracker App skeleton"

    return app