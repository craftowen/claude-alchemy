---
description: Show recommended plugins, MCP servers, and CLI tools for Claude Code power users
argument-hint:
allowed-tools: []
---

You are a display-only command. DO NOT use Bash, Write, or any other tool. DO NOT attempt to execute or install anything. Your ONLY job is to display the information below as formatted text to the user.

Present the following recommended tools in three sections, then show install commands for the user to copy and paste manually.

## Plugins (8)

| Plugin | Description |
|--------|-------------|
| agent-browser | Browser automation for AI agents (navigate, fill forms, screenshot, scrape) |
| vercel-react-best-practices | React/Next.js performance optimization guidelines from Vercel |
| supabase-postgres-best-practices | Postgres query optimization and schema design best practices |
| web-design-guidelines | UI/UX design review and accessibility audit |
| code-simplifier | Simplifies and refines code for clarity and maintainability |
| find-skills | Discover and install new skills from the marketplace |
| ui-ux-pro-max | Advanced UI/UX design and prototyping toolkit |
| frontend-design | Frontend design patterns and implementation |

## MCP Servers (1)

| MCP Server | Description |
|------------|-------------|
| context7 | Up-to-date documentation and code examples for any library |

## CLI Tools (2)

| Tool | Description |
|------|-------------|
| vercel | Vercel CLI for deployment and project management |
| supabase | Supabase CLI for local development and database management |

## Install Commands

After showing the tables above, tell the user: "Copy and paste these commands one at a time into your Claude Code prompt:"

Then display the following as a plain text code block (DO NOT execute these):

Plugins:

/plugin install agent-browser@claude-plugins-official
/plugin install vercel-react-best-practices@claude-plugins-official
/plugin install supabase-postgres-best-practices@claude-plugins-official
/plugin install web-design-guidelines@claude-plugins-official
/plugin install code-simplifier@claude-plugins-official
/plugin install find-skills@claude-plugins-official
/plugin install ui-ux-pro-max@claude-plugins-official
/plugin install frontend-design@claude-plugins-official

MCP Server:

/mcp add context7 -- npx -y @upstash/context7-mcp@latest

CLI Tools (run in terminal):

npm install -g vercel
npm install -g supabase
