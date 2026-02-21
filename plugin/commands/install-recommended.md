---
description: Install recommended plugins, MCP servers, and CLI tools for Claude Code power users
argument-hint:
allowed-tools: [Bash]
---

# Install Recommended Tools

Install the recommended tool suite for Claude Code power users.

## 1. Plugins

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

## 2. MCP Servers

| MCP Server | Description |
|------------|-------------|
| context7 | Up-to-date documentation and code examples for any library |

## 3. CLI Tools

| Tool | Description |
|------|-------------|
| vercel | Vercel CLI for deployment and project management |
| supabase | Supabase CLI for local development and database management |

## Steps

1. Show the user the full list above (Plugins, MCP Servers, CLI Tools)

2. Install plugins via Bash, one by one:
```bash
claude plugin install agent-browser@claude-plugins-official
claude plugin install vercel-react-best-practices@claude-plugins-official
claude plugin install supabase-postgres-best-practices@claude-plugins-official
claude plugin install web-design-guidelines@claude-plugins-official
claude plugin install code-simplifier@claude-plugins-official
claude plugin install find-skills@claude-plugins-official
claude plugin install ui-ux-pro-max@claude-plugins-official
claude plugin install frontend-design@claude-plugins-official
```

3. Add MCP servers via Bash:
```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp@latest
```

4. Install CLI tools via npm:
```bash
npm install -g vercel
npm install -g supabase
```

5. Report the result of each installation (success, already installed, or failed)
6. Summarize the results at the end
