---
description: Set up the subscription usage statusline (macOS, Linux, Windows)
argument-hint:
allowed-tools: [Read, Write, Edit, Bash]
---

# Setup Statusline

Configure Claude Code to show subscription usage in the statusline. Works on macOS, Linux, and Windows. Uses Node.js (already installed with Claude Code).

## Steps

### 1. Resolve the plugin root path

The script lives at `${CLAUDE_PLUGIN_ROOT}/scripts/statusline.mjs`. Resolve `${CLAUDE_PLUGIN_ROOT}` to the actual absolute path. Find it by locating this command file's directory and going up one level.

### 2. Read current settings

Read `~/.claude/settings.json` (create it if it doesn't exist).

### 3. Update the statusLine field

Set the `statusLine` field using the resolved path:

```json
{
  "statusLine": {
    "type": "command",
    "command": "node <ABSOLUTE_PLUGIN_ROOT>/scripts/statusline.mjs"
  }
}
```

Preserve all other existing settings.

### 4. Confirm and instruct

Tell the user:
- Statusline has been configured.
- Restart Claude Code for the change to take effect.
- The statusline shows: Model | Git branch | Context usage | 5h usage % (reset timer) | 7d usage % (reset timer)
