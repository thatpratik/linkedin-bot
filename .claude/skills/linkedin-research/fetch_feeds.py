#!/usr/bin/env python3
"""
fetch_feeds.py - collect recent items from the enabled RSS/Atom sources.

Reads research/sources.json and config/agent-config.json (lookback_days),
fetches every enabled source of type "rss", and prints the items published
inside the lookback window as JSON. Standard library only. It only issues
GET requests to the feed URLs listed in sources.json; nothing is uploaded.

Sources of type "web" are listed in the output under "web_sources" so the
caller can read them with its own web tools.

Usage (from the repository root)
  python3 .claude/skills/linkedin-research/fetch_feeds.py
  python3 .claude/skills/linkedin-research/fetch_feeds.py --days 7
  python3 .claude/skills/linkedin-research/fetch_feeds.py --check   # validate feeds only
"""

import argparse
import html
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ATOM = "{http://www.w3.org/2005/Atom}"
UA = "Mozilla/5.0 (compatible; feed-reader)"
TAG_RE = re.compile(r"<[^>]+>")


def load_json(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return json.load(fh)


def clean(text, limit=320):
    text = html.unescape(TAG_RE.sub(" ", text or ""))
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[:limit].rsplit(" ", 1)[0] + "..."


def parse_date(raw):
    if not raw:
        return None
    raw = raw.strip()
    try:
        dt = parsedate_to_datetime(raw)
    except (TypeError, ValueError):
        try:
            dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def parse_feed(data):
    """Yield (title, link, date, summary) from RSS 2.0 or Atom."""
    root = ET.fromstring(data)
    for item in root.iter("item"):
        yield (
            item.findtext("title"),
            item.findtext("link"),
            parse_date(item.findtext("pubDate")
                       or item.findtext("{http://purl.org/dc/elements/1.1/}date")),
            item.findtext("description"),
        )
    for entry in root.iter(ATOM + "entry"):
        link = None
        for ln in entry.findall(ATOM + "link"):
            if ln.get("rel") in (None, "alternate"):
                link = ln.get("href")
                break
        yield (
            entry.findtext(ATOM + "title"),
            link,
            parse_date(entry.findtext(ATOM + "published")
                       or entry.findtext(ATOM + "updated")),
            entry.findtext(ATOM + "summary") or entry.findtext(ATOM + "content"),
        )


def main():
    ap = argparse.ArgumentParser(description="Collect recent items from enabled feeds.")
    ap.add_argument("--days", type=int, help="override research.lookback_days")
    ap.add_argument("--check", action="store_true", help="only report whether each feed parses")
    ap.add_argument("--max-per-source", type=int, default=15)
    args = ap.parse_args()

    config = load_json("config/agent-config.json")
    sources = load_json("research/sources.json")["sources"]
    days = args.days or config["research"]["lookback_days"]
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days)

    out = {
        "fetched_at": now.isoformat(timespec="seconds"),
        "lookback_days": days,
        "sources": [],
        "web_sources": [],
        "errors": [],
    }

    if not config["research"].get("rss_enabled", True):
        sources = [s for s in sources if s["type"] != "rss"]

    for src in sources:
        if not src.get("enabled"):
            continue
        if src["type"] != "rss":
            out["web_sources"].append({k: src[k] for k in ("name", "url", "category")})
            continue
        try:
            entries = list(parse_feed(fetch(src["url"])))
        except Exception as exc:  # one broken feed must not stop the run
            out["errors"].append({"source": src["name"], "url": src["url"], "error": str(exc)})
            continue
        dated = [e for e in entries if e[2] is not None]
        recent = sorted((e for e in dated if cutoff <= e[2] <= now + timedelta(days=2)),
                        key=lambda e: e[2], reverse=True)[: args.max_per_source]
        block = {
            "name": src["name"],
            "category": src["category"],
            "url": src["url"],
            "total_items": len(entries),
            "recent_items": len(recent),
        }
        if not args.check:
            block["items"] = [
                {"title": clean(t, 200), "url": (l or "").strip(),
                 "published": d.date().isoformat(), "summary": clean(s)}
                for t, l, d, s in recent
            ]
        out["sources"].append(block)

    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    print()
    sys.exit(1 if out["errors"] and not out["sources"] else 0)


if __name__ == "__main__":
    main()
