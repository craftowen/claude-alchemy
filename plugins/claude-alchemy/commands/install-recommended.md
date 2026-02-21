---
description: Show recommended plugins, MCP servers, and CLI tools for Claude Code power users
argument-hint:
allowed-tools: []
---

# Recommended Tools

Show the recommended tool suite for Claude Code power users and provide install instructions.

## Response

Present the following tools in three sections with tables, then show the install commands the user should copy and paste.

### Plugins (8개)

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

### MCP Servers (1개)

| MCP Server | Description |
|------------|-------------|
| context7 | Up-to-date documentation and code examples for any library |

### CLI Tools (2개)

| Tool | Description |
|------|-------------|
| vercel | Vercel CLI for deployment and project management |
| supabase | Supabase CLI for local development and database management |

## Install Commands

Tell the user to copy and paste these commands one by one:

**Plugins:**
```
/plugin install agent-browser@claude-plugins-official
/plugin install vercel-react-best-practices@claude-plugins-official
/plugin install supabase-postgres-best-practices@claude-plugins-official
/plugin install web-design-guidelines@claude-plugins-official
/plugin install code-simplifier@claude-plugins-official
/plugin install find-skills@claude-plugins-official
/plugin install ui-ux-pro-max@claude-plugins-official
/plugin install frontend-design@claude-plugins-official
```

**MCP Server:**
```
/mcp add context7 -- npx -y @upstash/context7-mcp@latest
```

**CLI Tools (터미널에서 직접 실행):**
```bash
npm install -g vercel
npm install -g supabase
```
