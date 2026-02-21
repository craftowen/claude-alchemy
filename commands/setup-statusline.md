---
description: Set up the subscription usage statusline
argument-hint:
allowed-tools: [Read, Write, Edit, Bash]
---

# Setup Statusline Usage

Configure Claude Code to use the subscription usage statusline.

## Steps

1. Read the user's current `~/.claude/settings.json`
2. Update the `statusLine` field to:
```json
{
  "statusLine": {
    "type": "command",
    "command": "python3 ${CLAUDE_PLUGIN_ROOT}/scripts/statusline.py"
  }
}
```
Where `${CLAUDE_PLUGIN_ROOT}` is replaced with the actual absolute path to the plugin's root directory (the `claude-alchemy` repository root).

3. Preserve all other existing settings in the file
4. Confirm to the user that the statusline has been configured
5. Tell the user to restart Claude Code for the change to take effect

**Important:** The plugin root path must be resolved to an absolute path. Find it by locating this command file and going up one directory.
