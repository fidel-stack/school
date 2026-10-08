"""HTTP endpoints: GET /, POST /shorten, GET /<code>, GET /stats/<code>."""

import sqlite3
from pathlib import Path

from flask import Blueprint, current_app, jsonify, redirect, request, send_from_directory

from .db import connect
from .shortener import (
    MAX_GENERATE_ATTEMPTS,
    InvalidURL,
    generate_code,
    is_valid_code_format,
    validate_url,
)

bp = Blueprint("shortener", __name__)


def _db() -> sqlite3.Connection:
    """Open a connection to the database configured for this app."""
    return connect(current_app.config["DATABASE"])


def _error(status: int, message: str):
    return jsonify({"error": message}), status


def _classify_conflict(conn: sqlite3.Connection, url: str, exc: sqlite3.IntegrityError) -> str:
    """Tell a urls(code) collision apart from a urls(url) conflict.

    Returns "code" (we drew an already-used code: regenerate),
    "url" (this URL was already shortened: reuse its code),
    or "unknown" (unexpected constraint message - ask the database).
    """
    message = str(exc)
    if "urls.code" in message:
        return "code"
    if "urls.url" in message:
        return "url"
    row = conn.execute("SELECT code FROM urls WHERE url = ?", (url,)).fetchone()
    return "url" if row is not None else "unknown"


# Path(__file__) is app/routes.py, so this is <project>/app/static regardless
# of the process working directory - no reliance on CWD or Flask's root_path.
STATIC_DIR = Path(__file__).resolve().parent / "static"


@bp.get("/")
def index():
    """Serve the manual-testing UI (one static HTML page, no build step)."""
    return send_from_directory(STATIC_DIR, "index.html")


@bp.post("/shorten")
def shorten():
    """Accept {"url": "..."} and return a short code for it.

    Idempotent: shortening the same URL twice returns the same code (200
    the second time, 201 on first creation).
    """
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return _error(400, "request body must be a JSON object")

    if "url" not in data:
        return _error(400, "missing required field: url")
    try:
        url = validate_url(data["url"])
    except InvalidURL as exc:  # InvalidURL subclasses ValueError
        return _error(400, str(exc))

    conn = _db()
    try:
        # Uniqueness is enforced by the PRIMARY KEY on code and the UNIQUE
        # index on url; on any violation we decide which one fired and act
        # accordingly, with a bounded number of retries for code collisions.
        for _ in range(MAX_GENERATE_ATTEMPTS):
            code = generate_code()
            try:
                conn.execute("INSERT INTO urls (code, url) VALUES (?, ?)", (code, url))
            except sqlite3.IntegrityError as exc:
                conflict = _classify_conflict(conn, url, exc)
                if conflict == "code":
                    continue  # drew an existing code: draw another one
                if conflict == "url":
                    # Another request shortened this URL first; hand back
                    # that shared code instead of creating a second row.
                    row = conn.execute(
                        "SELECT code FROM urls WHERE url = ?", (url,)
                    ).fetchone()
                    if row is None:
                        return _error(500, "url conflict could not be resolved")
                    return jsonify({"code": row["code"], "url": url}), 200
                return _error(500, "unexpected database constraint violation")
            conn.commit()
            return jsonify({"code": code, "url": url}), 201
        # Should be unreachable with a real CSPRNG - but never loop forever.
        return _error(500, "could not allocate a unique short code")
    finally:
        conn.close()


@bp.get("/<code>")
def resolve(code: str):
    """Redirect to the original URL, counting the click."""
    if not is_valid_code_format(code):
        return _error(404, "short code not found")

    conn = _db()
    try:
        row = conn.execute("SELECT url FROM urls WHERE code = ?", (code,)).fetchone()
        if row is None:
            return _error(404, "short code not found")
        # 302 (not 301): browsers must re-ask us, or click counts skew.
        conn.execute("UPDATE urls SET clicks = clicks + 1 WHERE code = ?", (code,))
        conn.commit()
        return redirect(row["url"], code=302)
    finally:
        conn.close()


@bp.get("/stats/<code>")
def stats(code: str):
    """Return the stored URL and its click count."""
    if not is_valid_code_format(code):
        return _error(404, "short code not found")

    conn = _db()
    try:
        row = conn.execute(
            "SELECT code, url, clicks FROM urls WHERE code = ?", (code,)
        ).fetchone()
        if row is None:
            return _error(404, "short code not found")
        return jsonify({"code": row["code"], "url": row["url"], "clicks": row["clicks"]})
    finally:
        conn.close()


# app_errorhandler (not plain errorhandler): registers on the *app*, so errors
# raised by the routing layer - unmatched paths, disallowed methods - are JSON
# too, not just errors from views in this blueprint.
@bp.app_errorhandler(404)
def not_found(_error):
    return jsonify({"error": "not found"}), 404


@bp.app_errorhandler(405)
def method_not_allowed(_error):
    return jsonify({"error": "method not allowed"}), 405
