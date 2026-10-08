"""Shared fixtures: each test gets its own throwaway SQLite database."""

import pytest

from app import create_app


@pytest.fixture
def app(tmp_path):
    application = create_app(database=str(tmp_path / "test.db"))
    application.config.update(TESTING=True)
    return application


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def shorten(client):
    """Helper: POST a URL and return the parsed JSON response."""

    def _shorten(url):
        resp = client.post("/shorten", json={"url": url})
        assert resp.status_code in (200, 201), resp.get_data(as_text=True)
        return resp.get_json()

    return _shorten
