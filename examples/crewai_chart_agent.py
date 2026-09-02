#!/usr/bin/env python3
"""CrewAI-style agent: table in, dashboard_url out. stdlib only."""
import json
import os
import urllib.error
import urllib.request
from pathlib import Path

API = "https://xsbzchiryhqatvrzgyxm.supabase.co/functions/v1/generate-dashboard"


def load_dotenv():
    env = Path(__file__).resolve().parents[1] / ".env"
    if not env.exists():
        return
    for line in env.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def tablecharts_dashboard(rows: list, title: str = "Dashboard") -> str:
    key = os.environ.get("TABLECHARTS_API_KEY", "")
    if not key or key.startswith("tc_live_your_"):
        raise SystemExit("Set TABLECHARTS_API_KEY in .env")
    body = json.dumps({"data": rows, "title": title}).encode()
    req = urllib.request.Request(
        API,
        data=body,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            out = json.loads(res.read().decode())
    except urllib.error.HTTPError as e:
        raise SystemExit(e.read().decode()) from e
    return out.get("dashboard_url") or ""


if __name__ == "__main__":
    load_dotenv()
    rows = json.loads(
        (Path(__file__).with_name("sample_data.json")).read_text()
    )
    print(tablecharts_dashboard(rows, title="Monthly Revenue"))
