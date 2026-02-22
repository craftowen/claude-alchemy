#!/usr/bin/env python3
"""
Claude Code Statusline — subscription usage tracker
Model | Git branch | 20k/200k | 5h 18% (2h34m) | 7d 32% (3d20h)

Cross-platform: macOS, Linux, Windows.
Reads OAuth token from:
  1. CLAUDE_CODE_OAUTH_TOKEN env var
  2. macOS Keychain (macOS only)
  3. ~/.claude/.credentials.json (all platforms)
No external dependencies — Python stdlib only.
"""

import json
import sys
import os
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path

CACHE_FILE = Path.home() / ".claude" / "statusline_cache.json"
CREDS_FILE = Path.home() / ".claude" / ".credentials.json"


def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


class C:
    RST = "\033[0m"
    BOLD = "\033[1m"
    DIM = rgb(108, 112, 134)       # muted gray
    TEXT = rgb(205, 214, 244)       # soft white
    BRANCH = rgb(137, 180, 250)    # soft blue
    DIRTY = rgb(250, 179, 135)     # peach
    GREEN = rgb(166, 227, 161)     # mint
    YELLOW = rgb(249, 226, 175)    # warm amber
    RED = rgb(243, 139, 168)       # soft rose


def pcolor(p):
    return C.GREEN if p < 50 else C.YELLOW if p < 90 else C.RED


def ftok(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1000:
        return f"{n // 1000}k"
    return str(n)


def osc8(url, text):
    return f"\033]8;;{url}\a{text}\033]8;;\a"


def load_json(path):
    try:
        return json.loads(path.read_text()) if path.exists() else {}
    except Exception:
        return {}


def git_info(d):
    try:
        r = subprocess.run(["git", "branch", "--show-current"],
                           capture_output=True, text=True, cwd=d, timeout=2)
        br = r.stdout.strip()
        if not br:
            r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                               capture_output=True, text=True, cwd=d, timeout=2)
            br = r.stdout.strip()[:7] if r.stdout else ""
        if not br:
            return "", False, ""
        r = subprocess.run(["git", "status", "--porcelain"],
                           capture_output=True, text=True, cwd=d, timeout=2)
        dirty = bool(r.stdout.strip())
        r = subprocess.run(["git", "remote", "get-url", "origin"],
                           capture_output=True, text=True, cwd=d, timeout=2)
        url = r.stdout.strip()
        if url.startswith("git@github.com:"):
            url = url.replace("git@github.com:", "https://github.com/")
        if url.endswith(".git"):
            url = url[:-4]
        return br, dirty, url
    except Exception:
        return "", False, ""


def _fetch_script():
    """Self-contained background script for usage fetch. Cross-platform."""
    return f'''
import json, os, platform, subprocess, urllib.request
from pathlib import Path
from datetime import datetime, timezone

OUT = Path({json.dumps(str(CACHE_FILE))})
CREDS = Path({json.dumps(str(CREDS_FILE))})

token = None

# 1. Env var
token = os.environ.get("CLAUDE_CODE_OAUTH_TOKEN")

# 2. macOS Keychain
if not token and platform.system() == "Darwin":
    try:
        r = subprocess.run(
            ["security", "find-generic-password", "-s", "Claude Code-credentials", "-w"],
            capture_output=True, text=True, timeout=3)
        if r.returncode == 0 and r.stdout.strip():
            token = json.loads(r.stdout.strip()).get("claudeAiOauth", {{}}).get("accessToken")
    except Exception:
        pass

# 3. Credentials file (~/.claude/.credentials.json)
if not token:
    try:
        if CREDS.exists():
            token = json.loads(CREDS.read_text()).get("claudeAiOauth", {{}}).get("accessToken")
    except Exception:
        pass

if not token:
    raise SystemExit(1)

try:
    req = urllib.request.Request("https://api.anthropic.com/api/oauth/usage", headers={{
        "Authorization": f"Bearer {{token}}",
        "anthropic-beta": "oauth-2025-04-20",
        "anthropic-version": "2023-06-01"}})
    with urllib.request.urlopen(req, timeout=5) as r:
        data = json.loads(r.read())

    cache = {{"cached_at": datetime.now(timezone.utc).isoformat()}}
    for key in ("five_hour", "seven_day"):
        if data.get(key):
            cache[key] = data[key]
    OUT.write_text(json.dumps(cache))
except Exception:
    pass
'''


def fetch_usage():
    """Fetch usage data. Sync on first run (no cache), background thereafter."""
    script = _fetch_script()
    kwargs = dict(stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # Windows needs CREATE_NO_WINDOW to avoid popup
    if platform.system() == "Windows":
        kwargs["creationflags"] = 0x08000000
    if not CACHE_FILE.exists():
        subprocess.run([sys.executable, "-c", script], timeout=10, **kwargs)
    else:
        subprocess.Popen([sys.executable, "-c", script], **kwargs)


def main():
    try:
        data = json.loads(sys.stdin.read())
    except Exception:
        print("No data")
        return

    fetch_usage()
    cache = load_json(CACHE_FILE)

    D = C.DIM
    SEP = f" {D}|{C.RST} "
    parts = []

    # Model
    model = data.get("model", {})
    name = model.get("display_name", model.get("id", "?")).replace("Claude ", "")
    parts.append(f"{C.TEXT}{name}{C.RST}")

    # Git branch
    cwd = data.get("workspace", {}).get("current_dir", os.getcwd())
    br, dirty, remote = git_info(cwd)
    if br:
        bd = f"{br}*" if dirty else br
        bc = C.DIRTY if dirty else C.BRANCH
        parts.append(f"{bc}{osc8(remote, bd)}{C.RST}" if remote else f"{bc}{bd}{C.RST}")

    # Context: 20k/200k
    ctx = data.get("context_window", {})
    cs = ctx.get("context_window_size", 200000)
    cp = ctx.get("used_percentage", 0) or 0
    ut = int(cs * cp / 100)
    parts.append(f"{pcolor(cp)}{ftok(ut)}{D}/{ftok(cs)}{C.RST}")

    # 5h / 7d usage with reset timer
    now = datetime.now(timezone.utc)
    for label, key in [("5h", "five_hour"), ("7d", "seven_day")]:
        period = cache.get(key, {})
        util = period.get("utilization")
        resets_at = period.get("resets_at")
        if util is not None:
            txt = f"{D}{label} {pcolor(util)}{util:.0f}%"
            if resets_at:
                try:
                    secs = max(0, int((datetime.fromisoformat(resets_at) - now).total_seconds()))
                    h, m = secs // 3600, (secs % 3600) // 60
                    if h > 24:
                        txt += f" {D}({h // 24}d{h % 24}h)"
                    elif h > 0:
                        txt += f" {D}({h}h{m}m)"
                    else:
                        txt += f" {D}({m}m)"
                except Exception:
                    pass
            parts.append(f"{txt}{C.RST}")
        else:
            parts.append(f"{D}{label} {C.TEXT}--{C.RST}")

    print(SEP.join(parts))


if __name__ == "__main__":
    main()
