---
description: Set up the subscription usage statusline (macOS, Linux, Windows)
argument-hint:
allowed-tools: [Read, Write, Edit, Bash]
---

# Setup Statusline

Install the statusline script to `~/.claude/` and configure settings.

## Steps

### 1. Copy the script

Find the statusline.mjs bundled with this plugin and copy it to `~/.claude/statusline.mjs`:

```bash
find ~/.claude/plugins -name "statusline.mjs" -path "*/claude-alchemy/*" 2>/dev/null | head -1 | xargs -I{} cp {} ~/.claude/statusline.mjs
```

If `~/.claude/statusline.mjs` doesn't exist after this, tell the user the plugin might not be installed correctly and stop.

### 2. Update settings.json

Read `~/.claude/settings.json` (create with `{}` if missing). Set the `statusLine` field:

```json
{
  "statusLine": {
    "type": "command",
    "command": "node ~/.claude/statusline.mjs"
  }
}
```

Preserve all other existing settings.

### 3. Confirm

Tell the user:
- Statusline installed to `~/.claude/statusline.mjs`
- Restart Claude Code to apply.
- Shows: Model | Git branch | Context usage | 5h % (reset) | 7d % (reset)
