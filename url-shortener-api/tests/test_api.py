"""End-to-end tests for the three endpoints plus their edge cases."""

import re

import pytest

from app.shortener import MAX_GENERATE_ATTEMPTS

CODE_RE = re.compile(r"^[A-Za-z0-9]{7}$")
VALID_URL = "https://example.com/some/path?x=1"
URL_LENGTH_CAP = 2048


# ---------------------------------------------------------------------------
# POST /shorten - happy path
# ---------------------------------------------------------------------------


def test_shorten_returns_code(client):
    resp = client.post("/shorten", json={"url": VALID_URL})
    assert resp.status_code == 201
    data = resp.get_json()
    assert CODE_RE.match(data["code"]), data["code"]
    assert data["url"] == VALID_URL


def test_shorten_accepts_http_and_https(client):
    for url in ("http://example.com", "https://example.com/a/b?c=d#frag"):
        resp = client.post("/shorten", json={"url": url})
        assert resp.status_code == 201, url
        assert CODE_RE.match(resp.get_json()["code"])


def test_dedupe_returns_201_then_200_with_same_code(client):
    """A duplicate URL hits the UNIQUE index, gets re-SELECTed, returns 200."""
    first = client.post("/shorten", json={"url": VALID_URL})
    second = client.post("/shorten", json={"url": VALID_URL})
    assert first.status_code == 201
    assert second.status_code == 200
    assert CODE_RE.match(first.get_json()["code"])
    assert first.get_json()["code"] == second.get_json()["code"]
    # Only one row exists for this URL.
    third = client.post("/shorten", json={"url": VALID_URL})
    assert third.status_code == 200
    assert third.get_json()["code"] == first.get_json()["code"]


def test_shorten_makes_distinct_codes_for_distinct_urls(client):
    a = client.post("/shorten", json={"url": "https://example.com/a"})
    b = client.post("/shorten", json={"url": "https://example.com/b"})
    assert a.get_json()["code"] != b.get_json()["code"]


def test_url_at_length_cap_accepted(client):
    prefix = "https://example.com/"
    url = prefix + "a" * (URL_LENGTH_CAP - len(prefix))
    assert len(url) == URL_LENGTH_CAP
    assert client.post("/shorten", json={"url": url}).status_code == 201


def test_url_over_length_cap_rejected(client):
    prefix = "https://example.com/"
    url = prefix + "a" * (URL_LENGTH_CAP - len(prefix) + 1)
    assert len(url) == URL_LENGTH_CAP + 1
    resp = client.post("/shorten", json={"url": url})
    assert resp.status_code == 400
    assert "2048" in resp.get_json()["error"]


# ---------------------------------------------------------------------------
# POST /shorten - validation
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "bad_url",
    [
        "ftp://example.com/file",          # wrong scheme
        "file:///etc/passwd",              # wrong scheme
        "javascript:alert(1)",             # dangerous scheme
        "data:text/html,<script>",         # dangerous scheme
        "mailto:a@example.com",            # not a web URL
        "example.com/path",                # schemeless
        "//example.com/path",              # protocol-relative
        "http://",                         # no host
        "https:///path",                   # no host
        "",                                # empty
        "   https://example.com  ",        # surrounding whitespace
        "https://example.com/a b",         # internal whitespace
        "https://example.com/a\nb",        # newline
        "http://ex\tample.com",            # tab (whitespace branch)
        "https://example.com/\x00",        # NUL - control char, not whitespace
        "https://example.com/\x07",        # BEL - control char, not whitespace
        "https://example.com/\x7f",        # DEL - control char, not whitespace
        12345,                             # not a string
        None,
        True,
        ["https://example.com"],
        {"url": "https://example.com"},
    ],
)
def test_shorten_rejects_bad_urls(client, bad_url):
    resp = client.post("/shorten", json={"url": bad_url})
    assert resp.status_code == 400, (bad_url, resp.get_data(as_text=True))
    assert "error" in resp.get_json()


@pytest.mark.parametrize(
    "unparseable",
    [
        "http://[::1",        # unmatched IPv6 bracket -> urlsplit ValueError
        "http://[",           # bare unmatched bracket
        "http://[not-an-ip]", # malformed IPv6 literal
        "http://example.com:notaport/",  # bad port -> .port ValueError
        "http://example.com:99999/",     # port out of range
    ],
)
def test_unparseable_url_returns_400(client, unparseable):
    resp = client.post("/shorten", json={"url": unparseable})
    assert resp.status_code == 400, (unparseable, resp.get_data(as_text=True))
    assert "error" in resp.get_json()


def test_shorten_rejects_missing_url_field(client):
    resp = client.post("/shorten", json={})
    assert resp.status_code == 400
    assert "url" in resp.get_json()["error"]


def test_shorten_rejects_non_object_body(client):
    resp = client.post("/shorten", json=["https://example.com"])
    assert resp.status_code == 400


def test_shorten_rejects_malformed_json(client):
    resp = client.post("/shorten", data="{not json", content_type="application/json")
    assert resp.status_code == 400


def test_shorten_rejects_form_encoded_body(client):
    resp = client.post(
        "/shorten",
        data={"url": VALID_URL},
        content_type="application/x-www-form-urlencoded",
    )
    assert resp.status_code == 400


def test_shorten_rejects_empty_body(client):
    resp = client.post("/shorten")
    assert resp.status_code == 400


def test_empty_host_with_port_is_rejected(client):
    """http://:80/ has a non-empty netloc but no hostname."""
    resp = client.post("/shorten", json={"url": "http://:80/"})
    assert resp.status_code == 400
    assert "host" in resp.get_json()["error"]


@pytest.mark.parametrize(
    "credentialed",
    [
        "https://user:pass@example.com/",
        "https://user@example.com/",
        "http://user:pass@example.com:8080/a?b=c",
    ],
)
def test_credentials_in_url_are_rejected(client, credentialed):
    resp = client.post("/shorten", json={"url": credentialed})
    assert resp.status_code == 400, (credentialed, resp.get_data(as_text=True))
    assert "credential" in resp.get_json()["error"]


def test_whitespace_is_rejected_with_specific_error(client):
    """Whitespace (space/newline/tab) hits the whitespace branch."""
    for url in (
        "https://example.com/a b",
        "https://example.com/\n",
        "https://example.com/\t",
    ):
        resp = client.post("/shorten", json={"url": url})
        assert resp.status_code == 400, url
        assert "whitespace" in resp.get_json()["error"], url


def test_control_characters_are_rejected_with_specific_error(client):
    """Non-whitespace control chars (NUL/BEL/DEL) hit the control branch."""
    for url in (
        "https://example.com/\x00",
        "https://example.com/\x07",
        "https://example.com/\x7f",
    ):
        resp = client.post("/shorten", json={"url": url})
        assert resp.status_code == 400, repr(url)
        assert "control character" in resp.get_json()["error"], repr(url)


def test_unmatched_route_returns_json_404(client):
    """Routing-level 404s (no rule matches at all) must be JSON too."""
    for path in ("/deep/path/here", "/a/b/c", "/stats/a/b"):
        resp = client.get(path)
        assert resp.status_code == 404, path
        assert resp.is_json, resp.content_type
        assert "error" in resp.get_json()

    resp = client.post("/no/such/route", json={})
    assert resp.status_code == 404
    assert resp.is_json


def test_method_not_allowed_returns_json_405(client):
    """Routing-level 405s (including blueprint paths) must be JSON too."""
    resp = client.post("/health")
    assert resp.status_code == 405
    assert resp.is_json, resp.content_type
    assert "error" in resp.get_json()

    code = client.post("/shorten", json={"url": VALID_URL}).get_json()["code"]
    resp = client.post(f"/stats/{code}")
    assert resp.status_code == 405
    assert resp.is_json
    assert "error" in resp.get_json()


# ---------------------------------------------------------------------------
# GET /<code> - redirect
# ---------------------------------------------------------------------------


def test_redirects_to_original_url_with_302(client):
    code = client.post("/shorten", json={"url": VALID_URL}).get_json()["code"]
    resp = client.get(f"/{code}")
    assert resp.status_code == 302
    assert resp.headers["Location"] == VALID_URL


def test_redirect_not_301_so_counts_stay_accurate(client):
    """A cached 301 would stop browsers from re-asking us, undercounting."""
    code = client.post("/shorten", json={"url": VALID_URL}).get_json()["code"]
    assert client.get(f"/{code}").status_code == 302


def test_redirect_unknown_code_is_404(client):
    resp = client.get("/zzzzzzz")
    assert resp.status_code == 404
    assert "error" in resp.get_json()


@pytest.mark.parametrize(
    "bad_code",
    [
        "../etc/passwd",
        "abc/../../../etc",
        "has space",
        "has'quote",
        "semi;colon",
        "a" * 17,  # longer than any code we generate
        "%41%42",  # percent-encoded
        "....",
        "x'; DROP TABLE urls;--",
    ],
)
def test_redirect_malformed_code_is_404(client, bad_code):
    resp = client.get(f"/{bad_code}")
    assert resp.status_code in (404, 400), resp.get_data(as_text=True)


def test_unknown_code_does_not_create_rows(client, app):
    client.get("/nosuch1")
    with app.app_context():
        from app.db import connect

        conn = connect(app.config["DATABASE"])
        try:
            assert conn.execute("SELECT COUNT(*) AS n FROM urls").fetchone()["n"] == 0
        finally:
            conn.close()


# ---------------------------------------------------------------------------
# GET /stats/<code>
# ---------------------------------------------------------------------------


def test_stats_initial_click_count_is_zero(client):
    code = client.post("/shorten", json={"url": VALID_URL}).get_json()["code"]
    resp = client.get(f"/stats/{code}")
    assert resp.status_code == 200
    assert resp.get_json() == {"code": code, "url": VALID_URL, "clicks": 0}


def test_stats_counts_each_redirect(client):
    code = client.post("/shorten", json={"url": VALID_URL}).get_json()["code"]
    for _ in range(3):
        assert client.get(f"/{code}").status_code == 302
    assert client.get(f"/stats/{code}").get_json()["clicks"] == 3


def test_stats_unknown_code_is_404(client):
    resp = client.get("/stats/nope123")
    assert resp.status_code == 404
    assert "error" in resp.get_json()


@pytest.mark.parametrize("bad_code", ["bad code", "a" * 17, "x' OR '1'='1"])
def test_stats_malformed_code_is_404(client, bad_code):
    resp = client.get(f"/stats/{bad_code}")
    assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Collision handling: forced generator collisions (change 6)
# ---------------------------------------------------------------------------


def test_forced_code_collision_regenerates(client, monkeypatch):
    """First draw collides with an existing row; second draw must win."""
    taken = client.post("/shorten", json={"url": VALID_URL}).get_json()["code"]
    draws = [taken, "fresh99"]

    def collide_first(length=7):
        return draws.pop(0)

    monkeypatch.setattr("app.routes.generate_code", collide_first)
    resp = client.post("/shorten", json={"url": "https://example.com/other"})
    assert resp.status_code == 201
    assert resp.get_json()["code"] == "fresh99"
    # The pre-existing row is untouched.
    stats = client.get(f"/stats/{taken}").get_json()
    assert stats["url"] == VALID_URL


def test_forced_collision_exhausts_retry_limit(client, app, monkeypatch):
    """A generator that always returns a used code must fail loudly, not loop."""
    taken = client.post("/shorten", json={"url": VALID_URL}).get_json()["code"]
    calls = []

    def always_taken(length=7):
        calls.append(length)
        return taken

    monkeypatch.setattr("app.routes.generate_code", always_taken)
    resp = client.post("/shorten", json={"url": "https://example.com/other"})
    assert resp.status_code == 500
    assert "error" in resp.get_json()
    assert len(calls) == MAX_GENERATE_ATTEMPTS
    # The URL that could not get a code was not stored half-way.
    with app.app_context():
        from app.db import connect

        conn = connect(app.config["DATABASE"])
        try:
            stored = conn.execute(
                "SELECT COUNT(*) AS n FROM urls WHERE url = ?",
                ("https://example.com/other",),
            ).fetchone()["n"]
        finally:
            conn.close()
    assert stored == 0


def test_forced_url_conflict_returns_existing_code(client, monkeypatch):
    """Even with a fresh random code each try, a duplicate URL shares one code."""
    first = client.post("/shorten", json={"url": VALID_URL}).get_json()["code"]
    # Generator is never consulted for the conflict path's *result*: the
    # insert fails on urls(url) and the handler re-SELECTs the stored code.
    monkeypatch.setattr(
        "app.routes.generate_code", lambda length=7: "zzzzz99"
    )
    second = client.post("/shorten", json={"url": VALID_URL})
    assert second.status_code == 200
    assert second.get_json()["code"] == first


# ---------------------------------------------------------------------------
# Safety / correctness properties
# ---------------------------------------------------------------------------


def test_codes_are_random_not_sequential(client):
    """Two URLs shortened back-to-back must not get predictable codes."""
    first = client.post("/shorten", json={"url": "https://example.com/1"}).get_json()
    second = client.post("/shorten", json={"url": "https://example.com/2"}).get_json()
    assert first["code"] != second["code"]


def test_sql_injection_in_url_is_stored_not_executed(client):
    # Percent-encoded so it is a legal URL; the raw quotes/semicolons are
    # what a naive f-string query would trip over.
    nasty = "https://example.com/q?x=';DROP%20TABLE%20urls;--"
    resp = client.post("/shorten", json={"url": nasty})
    assert resp.status_code == 201
    code = resp.get_json()["code"]
    # Table still exists and the payload round-trips verbatim.
    stats = client.get(f"/stats/{code}")
    assert stats.status_code == 200
    assert stats.get_json()["url"] == nasty


def test_sql_injection_in_code_is_rejected(client):
    assert client.get("/x' OR '1'='1").status_code == 404
    assert client.get("/stats/x'; DROP TABLE urls;--").status_code == 404


def test_data_persists_across_app_instances(tmp_path):
    from app import create_app

    db = str(tmp_path / "persist.db")
    with create_app(database=db).test_client() as c:
        code = c.post("/shorten", json={"url": VALID_URL}).get_json()["code"]

    with create_app(database=db).test_client() as c:
        assert c.get(f"/stats/{code}").get_json()["url"] == VALID_URL


def test_health_endpoint(client):
    assert client.get("/health").get_json() == {"status": "ok"}


def test_root_serves_html_page(client):
    """GET / must serve the static testing UI as HTML."""
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.content_type.startswith("text/html"), resp.content_type
    body = resp.get_data(as_text=True)
    assert "<!DOCTYPE html>" in body
    assert "shorten-form" in body


def test_unknown_route_is_json_404(client):
    resp = client.get("/nope")
    assert resp.status_code == 404
    assert "error" in resp.get_json()
