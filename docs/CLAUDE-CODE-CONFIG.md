# Claude Code Configuration

**Last Updated**: January 17, 2026

This file documents the Claude Code configuration for this project. Reference this when troubleshooting or modifying settings.

---

## Current Configuration

**Context Usage**: ~23k tokens (11% of 200k budget) - Optimized for episode deployment and general website work

### Global Settings (`~/.claude/settings.json`)

```json
{
  "enabledPlugins": {
    "frontend-design@claude-plugins-official": false,
    "document-skills@anthropic-agent-skills": true
  }
}
```

### MCP Servers (Global)

- Playwright MCP: Configured and running (`npx -y @playwright/mcp@latest`)
- Provides browser automation for testing and debugging

### Project Settings (`.claude/settings.local.json`)

```json
{
  "permissions": {
    "allow": [
      "Bash(curl:*)",
      "Skill(frontend-design)"
    ]
  }
}
```

---

## What's Currently Loaded

**Skills** (1.3k tokens):
- document-skills plugin provides 16 skills: xlsx, docx, pptx, pdf, frontend-design, doc-coauthoring, internal-comms, canvas-design, algorithmic-art, web-artifacts-builder, mcp-builder, theme-factory, brand-guidelines, slack-gif-creator, skill-creator, webapp-testing

**MCP Tools** (3.4k tokens):
- Playwright MCP provides 22 browser automation tools for testing, screenshots, and debugging

**Total Context Breakdown**:
- System prompt: 3.0k tokens (1.5%)
- System tools: 14.8k tokens (7.4%)
- MCP tools: 3.4k tokens (1.7%)
- Skills: 1.3k tokens (0.7%)
- Messages: ~8 tokens (0.0%)
- **Free space: 132k tokens (66.2%)**

---

## Configuration Notes

- **document-skills enabled globally**: Provides comprehensive document processing capabilities (Word, Excel, PowerPoint, PDF) always available
- **Playwright MCP configured globally**: Essential for pre-deployment testing workflow and visual debugging
- **frontend-design disabled globally**: Available via Skill tool when needed for design mockups
- **Context is not constrained**: With 132k tokens free (66%), the current configuration provides good balance between capability and efficiency
- **Pre-deployment testing**: Current setup supports the automated test suite in `scripts/tests/`
- **Global CLAUDE.md**: `~/.claude/CLAUDE.md` contains cross-project standards (skill structure, etc.) - applies to ALL projects automatically

---

## Modifying Configuration

**To disable document-skills globally** (if context becomes constrained):
```bash
# Edit ~/.claude/settings.json
{
  "enabledPlugins": {
    "frontend-design@claude-plugins-official": false,
    "document-skills@anthropic-agent-skills": false
  }
}
```

**To remove Playwright MCP**:
```bash
claude mcp remove playwright
```

**To enable on-demand for a specific project**:
Create `.claude/settings.local.json`:
```json
{
  "enabledPlugins": {
    "document-skills@anthropic-agent-skills": true
  }
}
```

**Note**: Restart Claude Code after changing configuration.
