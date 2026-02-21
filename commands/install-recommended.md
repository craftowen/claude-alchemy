---
description: Install recommended plugins for Claude Code power users
argument-hint:
allowed-tools: [Bash]
---

# Install Recommended Plugins

Install the recommended plugin suite for Claude Code power users.

## Plugins

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

## Steps

1. Show the user the plugin list above
2. Run each install command via Bash, one by one:

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

3. Report the result of each installation (success, already installed, or failed)
4. Summarize the results at the end
