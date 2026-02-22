---
description: Set up the subscription usage statusline (macOS, Linux, Windows)
argument-hint:
allowed-tools: [Read, Write, Edit, Bash]
---

# Setup Statusline

Configure Claude Code to show subscription usage in the statusline. Works on macOS, Linux, and Windows.

## Steps

### 1. Detect Python

Run this to find which Python command is available:

```bash
python3 --version 2>/dev/null || python --version 2>/dev/null
```

- If `python3` works, use `python3` as the command.
- If only `python` works, verify it is Python 3.x (not 2.x). Use `python` as the command.
- If neither works, Python is not installed. Tell the user to install Python 3 first:
  - **macOS**: `brew install python3` or download from https://www.python.org/downloads/
  - **Windows**: `winget install Python.Python.3` or download from https://www.python.org/downloads/
  - **Linux (Debian/Ubuntu)**: `sudo apt install python3`
  - **Linux (Fedora)**: `sudo dnf install python3`

  After telling the user, STOP and wait. Do not proceed until Python is installed.

### 2. Resolve the plugin root path

The script lives at `${CLAUDE_PLUGIN_ROOT}/scripts/statusline.py`. Resolve `${CLAUDE_PLUGIN_ROOT}` to the actual absolute path. Find it by locating this command file's directory and going up one level.

### 3. Read current settings

Read `~/.claude/settings.json` (create it if it doesn't exist).

### 4. Update the statusLine field

Set the `statusLine` field using the detected Python command and resolved path:

```json
{
  "statusLine": {
    "type": "command",
    "command": "<PYTHON_CMD> <ABSOLUTE_PLUGIN_ROOT>/scripts/statusline.py"
  }
}
```

Preserve all other existing settings.

### 5. Confirm and instruct

Tell the user:
- Statusline has been configured.
- Restart Claude Code for the change to take effect.
- The statusline shows: Model | Git branch | Context usage | 5h usage % (reset timer) | 7d usage % (reset timer)
