#!/usr/bin/env python3
"""LangGraph-style node: table in, dashboard_url out. stdlib only."""
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


def chart_node(state: dict) -> dict:
    key = os.environ.get("TABLECHARTS_API_KEY", "")
    if not key or key.startswith("tc_live_your_"):
        raise SystemExit("Set TABLECHARTS_API_KEY in .env")
    body = json.dumps(
        {"data": state["rows"], "title": state.get("title", "Dashboard")}
    ).encode()
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
    return {
        "dashboard_url": out.get("dashboard_url"),
        "embed_iframe": out.get("embed_iframe"),
        "chart_type": out.get("chart_type"),
    }


if __name__ == "__main__":
    load_dotenv()
    rows = json.loads(
        (Path(__file__).with_name("sample_data.json")).read_text()
    )
    result = chart_node({"rows": rows, "title": "Monthly Revenue"})
    print(result["dashboard_url"])
