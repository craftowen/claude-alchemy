# statusline-usage

A clean, modern statusline for Claude Code that shows real-time subscription usage.

```
Opus 4.6 | main* | 20k/200k | 5h 18% (2h34m) | 7d 32% (3d20h)
```

## Features

- **Model name** — current Claude model
- **Git branch** — clickable link to remote repo, dirty indicator (`*`)
- **Context window** — used/total in k units with color coding
- **5h usage** — 5-hour rolling window utilization % with reset timer
- **7d usage** — 7-day weekly utilization % with reset timer

## How it works

Reads the OAuth token from macOS Keychain and calls the Anthropic usage API (`/api/oauth/usage`) in a non-blocking background subprocess on every statusline refresh. No external dependencies — Python stdlib only.

## Colors

Catppuccin Mocha palette with 24-bit truecolor:
- Usage < 50%: mint green
- Usage 50-89%: warm amber
- Usage >= 90%: soft rose

## Setup

Run `/setup-statusline` in Claude Code, then restart.

## Requirements

- macOS (uses Keychain for OAuth credentials)
- Claude Max or Pro subscription
- Python 3.9+
