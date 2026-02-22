---
description: Set up the subscription usage statusline (macOS, Linux, Windows)
argument-hint:
allowed-tools: [Read, Write, Edit, Bash]
---

# Setup Statusline

Configure Claude Code to show subscription usage in the statusline. Works on macOS, Linux, and Windows. Uses Node.js (already installed with Claude Code).

## Steps

### 1. Find the statusline script path

The script is located relative to THIS command file. Use these steps to resolve the absolute path:

1. This command file is at: `<this file's absolute path>`
2. Go up one directory from `commands/` to reach the plugin root
3. The script is at `<plugin root>/scripts/statusline.mjs`

For example, if this command file is at `/Users/owen/.claude/plugins/cache/claude-alchemy/xyz/plugins/claude-alchemy/commands/setup-statusline.md`, then the script is at `/Users/owen/.claude/plugins/cache/claude-alchemy/xyz/plugins/claude-alchemy/scripts/statusline.mjs`.

To verify the resolved path, run: `ls <resolved path>` using Bash. If the file doesn't exist, try finding it:
```
find ~/.claude/plugins -name "statusline.mjs" -path "*/claude-alchemy/*" 2>/dev/null
```

### 2. Read current settings

Read `~/.claude/settings.json` (create it with `{}` if it doesn't exist).

### 3. Update the statusLine field

Set the `statusLine` field using the resolved absolute path:

```json
{
  "statusLine": {
    "type": "command",
    "command": "node <RESOLVED_ABSOLUTE_PATH>/scripts/statusline.mjs"
  }
}
```

Preserve all other existing settings. Only update the `statusLine` field.

### 4. Confirm and instruct

Tell the user:
- Statusline has been configured.
- The path set: `<the actual path used>`
- Restart Claude Code for the change to take effect.
- The statusline shows: Model | Git branch | Context usage | 5h usage % (reset timer) | 7d usage % (reset timer)
