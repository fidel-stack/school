"""URL validation and safe short-code generation."""

import re
import secrets
from urllib.parse import urlsplit

# 62**7 ~= 4.4e12 combinations; collisions are still caught by the DB's
# PRIMARY KEY, this only makes them improbable.
CODE_LENGTH = 7
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

MAX_URL_LENGTH = 2048  # common practical cap (browsers/servers enforce one too)

# Shape of a code accepted from a URL path: 1-16 alphanumerics.
CODE_PATTERN = re.compile(r"[A-Za-z0-9]{1,16}")

MAX_GENERATE_ATTEMPTS = 10


class InvalidURL(ValueError):
    """Raised when a candidate URL is not an acceptable http/https URL."""


def validate_url(value) -> str:
    """Return *value* if it is an acceptable absolute http/https URL.

    Rejects non-strings, over-long URLs, whitespace/control characters,
    non-http(s) schemes (ftp:, javascript:, data:, mailto:, ...), schemeless
    input ("example.com/x"), URLs with no host ("http:///path"), and URLs
    carrying credentials.
    """
    if not isinstance(value, str):
        raise InvalidURL("url must be a string")
    if not value:
        raise InvalidURL("url must be a non-empty string")
    if len(value) > MAX_URL_LENGTH:
        raise InvalidURL(f"url must be at most {MAX_URL_LENGTH} characters")
    if any(ch.isspace() for ch in value):
        raise InvalidURL("url must not contain whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in value):
        raise InvalidURL("url must not contain control characters")

    try:
        parts = urlsplit(value)
        _ = parts.port  # raises ValueError on a malformed or out-of-range port
    except ValueError as exc:  # e.g. invalid IPv6 brackets, bad port
        raise InvalidURL("url could not be parsed") from exc

    if parts.scheme.lower() not in ("http", "https"):
        raise InvalidURL("url scheme must be http or https")
    if not parts.hostname:
        raise InvalidURL("url must include a host")
    if parts.username or parts.password:
        raise InvalidURL("url must not include credentials")
    return value


def generate_code(length: int = CODE_LENGTH) -> str:
    """Return a cryptographically random alphanumeric code.

    Uses ``secrets`` (CSPRNG) rather than ``random``, which is predictable.
    """
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


def is_valid_code_format(code: str) -> bool:
    """True if *code* could plausibly be one of ours (cheap path check)."""
    return isinstance(code, str) and CODE_PATTERN.fullmatch(code) is not None
