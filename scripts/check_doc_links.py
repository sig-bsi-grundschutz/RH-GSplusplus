#!/usr/bin/env python3
"""Verify that documentation URLs in mappings/{product}/docs.json respond successfully."""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_hrefs(docs_path: Path) -> list[tuple[str, str]]:
    raw = json.loads(docs_path.read_text(encoding="utf-8"))
    hrefs: list[tuple[str, str]] = []
    for key, value in raw.items():
        if isinstance(value, str):
            hrefs.append((key, value))
        elif isinstance(value, dict) and value.get("href"):
            hrefs.append((key, value["href"]))
    return hrefs


def check_url(key: str, url: str, timeout: float) -> tuple[bool, str]:
    req = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            code = resp.status
            if 200 <= code < 400:
                return True, str(code)
            return False, f"HTTP {code}"
    except urllib.error.HTTPError as exc:
        if exc.code in (403, 405):
            # Some doc hosts block HEAD; retry with GET and range.
            get_req = urllib.request.Request(
                url,
                headers={"Range": "bytes=0-0"},
                method="GET",
            )
            try:
                with urllib.request.urlopen(get_req, timeout=timeout) as resp:
                    code = resp.status
                    if 200 <= code < 400:
                        return True, f"{code} (GET fallback)"
            except urllib.error.HTTPError as get_exc:
                return False, f"HTTP {get_exc.code} (GET fallback)"
            except urllib.error.URLError as get_exc:
                return False, str(get_exc.reason)
        return False, f"HTTP {exc.code}"
    except urllib.error.URLError as exc:
        return False, str(exc.reason)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--product", default="rhel9")
    parser.add_argument("--timeout", type=float, default=30.0)
    args = parser.parse_args()

    docs_path = _repo_root() / "mappings" / args.product / "docs.json"
    if not docs_path.is_file():
        print(f"Missing {docs_path}", file=sys.stderr)
        return 1

    failures: list[str] = []
    for key, url in load_hrefs(docs_path):
        ok, detail = check_url(key, url, args.timeout)
        status = "OK" if ok else "FAIL"
        print(f"[{status}] {key}: {url} ({detail})")
        if not ok:
            failures.append(f"{key}: {url} ({detail})")

    if failures:
        print("\nBroken documentation links:", file=sys.stderr)
        for line in failures:
            print(f"  - {line}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
