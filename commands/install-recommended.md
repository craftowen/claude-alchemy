---
description: Show recommended plugins and install instructions
argument-hint:
allowed-tools: []
---

# Recommended Plugins

Display the recommended plugin suite for Claude Code power users and provide install instructions.

## Response

Tell the user to run each of the following commands to install the recommended plugins:

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

Present them in a table format:

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

Tell the user they can copy and paste each command one by one, or use `/plugin` to browse and install interactively.
