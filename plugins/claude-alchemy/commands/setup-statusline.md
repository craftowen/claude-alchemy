---
description: Set up the subscription usage statusline (macOS, Linux, Windows)
argument-hint:
allowed-tools: [Read, Write, Edit, Bash]
---

# Setup Statusline

Configure Claude Code to show subscription usage in the statusline.

## Steps

### 1. Find the statusline script

Run this command to find the script:

```bash
find ~/.claude/plugins -name "statusline.mjs" -path "*/claude-alchemy/*" 2>/dev/null | head -1
```

Store the result as SCRIPT_PATH. If empty, the plugin may not be installed correctly — tell the user and stop.

### 2. Read current settings

Read `~/.claude/settings.json` (create it with `{}` if it doesn't exist).

### 3. Update the statusLine field

Set the `statusLine` field:

```json
{
  "statusLine": {
    "type": "command",
    "command": "node <SCRIPT_PATH>"
  }
}
```

Where `<SCRIPT_PATH>` is the absolute path found in step 1. Preserve all other existing settings.

### 4. Confirm

Tell the user:
- Statusline configured: `node <SCRIPT_PATH>`
- Restart Claude Code to apply.
- Shows: Model | Git branch | Context usage | 5h % (reset) | 7d % (reset)
