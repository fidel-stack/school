# URL Shortener API

A small URL shortener web API in Python using **Flask** and **SQLite** (stdlib
`sqlite3`, no ORM).

## Endpoints

| Method | Path           | Description                              | Success        |
| ------ | -------------- | ---------------------------------------- | -------------- |
| `GET`  | `/`            | Static manual-testing UI (HTML page)     | `200`          |
| `POST` | `/shorten`     | Create (or reuse) a short code for a URL | `201` new / `200` existing |
| `GET`  | `/<code>`      | Redirect to the original URL             | `302`          |
| `GET`  | `/stats/<code>`| Return stored URL and click count        | `200`          |
| `GET`  | `/health`      | Liveness check                           | `200`          |

Errors are always JSON — `{"error": "..."}` with `400`, `404`, `405` or `500` —
including **routing-level** errors (unmatched paths, disallowed methods), which
are handled by blueprint-registered `app_errorhandler`s so they are never Flask's
default HTML pages.

### `POST /shorten`

```console
$ curl -s -X POST localhost:5000/shorten \
    -H 'Content-Type: application/json' \
    -d '{"url": "https://example.com/landing?utm=x"}'
{"code":"xfyKFO5","url":"https://example.com/landing?utm=x"}     # 201 Created
```

The body must be a JSON object containing `url`. A repeat of the same URL
returns the **same code** with `200 OK`.

Rejected with `400`: missing/non-string `url`, non-object or malformed JSON,
any scheme other than `http`/`https` (`ftp:`, `javascript:`, `data:`,
`mailto:` …), schemeless input (`example.com`), missing host (`http:///x`,
`http://:80/` — checked via `parts.hostname`, not `netloc`),
embedded credentials (`user:pass@`), any whitespace or control character,
length over **2048** characters, and unparseable URLs (bad IPv6 literal,
malformed or out-of-range port).

### `GET /<code>`

```console
$ curl -si localhost:5000/xfyKFO5 | head -3
HTTP/1.1 302 FOUND
Location: https://example.com/landing?utm=x
```

Unknown or malformed codes return `404`. Redirects use **302, not 301** — a
cached 301 would stop browsers from re-asking and silently undercount clicks.

### `GET /stats/<code>`

```console
$ curl -s localhost:5000/stats/xfyKFO5
{"code":"xfyKFO5","url":"https://example.com/landing?utm=x","clicks":2}
```

## Dedupe: one URL, one shared counter

`urls(url)` has a `UNIQUE` index, so the table stores **one row per distinct
URL**. Consequences worth knowing:

- Shortening the same URL twice (from anyone, at any time) returns the same
  code. The first request gets `201`, later ones `200`.
- **The click counter is shared.** `clicks` counts hits on that one code for
  that one URL across *all* callers — it is not per-request, per-caller, or
  per-creation. Two people shortening the same URL watch the same number go up.
- Concurrent duplicates are safe: if two requests race, SQLite's unique index
  rejects the second insert, the handler re-SELECTs the winning code and both
  callers receive it.

If you need a distinct code (and an independent counter) per caller, drop the
unique index on `urls(url)` and add a fast-path `SELECT` before inserting.

## How short codes are generated

- 7 characters from `A-Za-z0-9` via `secrets.choice` (CSPRNG), ~4.4×10¹²
  combinations. `random` is never used — it is predictable.
- Uniqueness is *guaranteed by the database* (`code` is the PRIMARY KEY), not
  by the generator: on an `IntegrityError` the handler distinguishes a code
  collision (regenerate) from a URL conflict (re-SELECT and reuse), bounded at
  10 attempts before returning `500` rather than looping forever.
- Paths are validated with `re.fullmatch("[A-Za-z0-9]{1,16}")` before any
  query runs, so junk input never reaches the database.

## SQL safety

Every statement is parameterized (`conn.execute(sql, (param,))`); table and
column names are module constants and are never built from input. Tests cover
payloads like `https://example.com/q?x=';DROP%20TABLE%20urls;--` (stored
verbatim) and `x'; DROP TABLE urls;--` as a code (rejected as `404`).

## Setup

```console
$ python3 -m venv .venv
$ .venv/bin/pip install -r requirements.txt
```

## Run

```console
$ URLSHORT_DB=shortener.db .venv/bin/flask --app "app:create_app()" run
 * Running on http://127.0.0.1:5000
```

The database path comes from `URLSHORT_DB` (default `shortener.db`) and is
created on startup. Set `FLASK_DEBUG=1` for auto-reload.

## Web UI (manual testing)

The app serves a single static page at `GET /` — plain HTML with inline CSS
and vanilla JS, no CDNs and no build step. Start the server as above, then
open <http://127.0.0.1:5000/> in a browser:

- **Shorten a URL** — POSTs the URL to `/shorten` and shows the short link
  built from `window.location.origin` (works on any host/port, not just
  `localhost`), labeled *Newly created (201)* or *Already existed (200)*.
  Short links open in a new tab with `rel="noopener noreferrer"`.
- **Look up stats** — calls `/stats/<code>` and shows the original URL and
  click count.
- **Errors** — 400 and 404 responses display the API's `error` message in
  red.

All API data is rendered with `textContent`/`createElement`; the page never
assigns to `innerHTML`.

## Tests

```console
$ .venv/bin/python -m pytest -q
74 passed in 1.62s
```

Each test gets its own throwaway SQLite file (`tmp_path`), so tests are
isolated and parallel-safe by construction. Coverage includes:

- happy paths for all three endpoints, redirect status **and** `Location` header
- validation matrix (bad schemes, schemeless, no host — including
  `http://:80/` — credentials, whitespace/control chars, >2048 length,
  unparseable URL, wrong types, malformed/form/empty bodies)
- routing-level errors answer JSON: unmatched paths (`/a/b/c`) → 404,
  `POST /health` and `POST /stats/<code>` → 405
- 404s for unknown and malformed codes (including SQL-injection-shaped ones)
- click counting across repeated redirects; initial count is 0
- **forced generator collisions** (monkeypatched `generate_code`): a collision
  retries and succeeds; a permanently colliding generator returns `500` after
  exactly `MAX_GENERATE_ATTEMPTS` calls and stores nothing
- URL conflicts return the pre-existing shared code
- persistence across app instances; parameterized-query payload round-trips

## Project layout

```
app/
  __init__.py     # create_app() factory: config, schema init, blueprint, JSON errors
  db.py           # sqlite3 connection helper + schema (UNIQUE index on url)
  shortener.py    # URL validation (validate_url) + code generation
  routes.py       # /, /shorten, /<code>, /stats/<code>
  static/
    index.html    # manual-testing UI: plain HTML + vanilla JS, no build step
tests/
  conftest.py     # fixtures: per-test app + client
  test_api.py     # main paths and edge cases
requirements.txt
README.md
```
