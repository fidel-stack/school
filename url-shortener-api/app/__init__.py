"""Application factory for the URL shortener API."""

import os

from flask import Flask, jsonify

from .db import init_db
from .routes import bp as shortener_bp


def create_app(database: str | None = None) -> Flask:
    """Build a configured app instance.

    ``database`` overrides the SQLite path (tests pass a tmp file);
    otherwise ``URLSHORT_DB`` or ``shortener.db`` is used.
    """
    app = Flask(__name__)
    app.config["DATABASE"] = database or os.environ.get("URLSHORT_DB") or "shortener.db"

    init_db(app.config["DATABASE"])
    # The blueprint installs app-wide 404/405 JSON handlers via
    # bp.app_errorhandler, so routing-level errors are JSON too.
    app.register_blueprint(shortener_bp)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    return app


