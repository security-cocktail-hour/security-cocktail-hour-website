# Security Cocktail Hour Website - Session Context

**Last Updated**: January 4, 2026
**Hugo Version**: v0.151.0
**Branch**: main

---

## Current Session

**Today's Focus**: Claude Code context optimization and documentation updates
- **Configuration Changes:**
  - Disabled global plugins (frontend-design, document-skills, example-skills) in `~/.claude/settings.json`
  - Removed Playwright MCP from global configuration via `claude mcp remove playwright`
  - Context savings: ~55-65k tokens per session (27-32% of total)
  - Plugins remain installed and available - enable per-project as needed
- **Documentation Updates:**
  - Added "Claude Code Configuration" section to SESSION_CONTEXT.md with complete plugin management guide
  - Updated ARCHIVE.md with January 4, 2026 historical entry
  - Updated scripts/README.md to clarify Playwright Python library vs MCP distinction
  - Verified all other documentation files (NEW-EPISODE-DEPLOYMENT.md, episode-deploy.skill, etc.)
- **Result:** Lean global configuration with on-demand plugin loading for specific tasks

---

## Project Overview

**Production Site**: https://securitycocktailhour.com/ (GoDaddy cPanel - Live)
**Staging Site**: Netlify automatic deployments from GitHub
**GitHub Repository**: https://github.com/security-cocktail-hour/security-cocktail-hour-website
**Local Dev Server**: http://localhost:1313/ (when running `hugo server -D`)

**Current Stats**: 154 pages (67 episodes, 4 blog posts, newsletter page, main pages) | 6.0MB images | 8.2MB production package

---

## Claude Code Configuration

### Context Optimization (Updated: January 4, 2026)

To maximize available context for episode deployment and content work, plugins and MCP servers are disabled globally by default. Enable them on-demand when needed for specific tasks.

**Global Settings** (`~/.claude/settings.json`):
```json
{
  "enabledPlugins": {
    "frontend-design@claude-code-plugins": false,
    "document-skills@anthropic-agent-skills": false,
    "example-skills@anthropic-agent-skills": false
  }
}
```

**MCP Servers**:
- Playwright MCP: Removed from global config (load on-demand when needed)

**Context Savings**: ~55-65k tokens saved per session (27-32% of total context)

### When to Enable Plugins

Plugins are **installed but disabled globally**. Enable per-project as needed:

**Frontend Design Work** (design mockups, visual debugging):
- Enable `frontend-design@claude-code-plugins`
- Use case: Art Deco redesign, hero section mockups, page layouts

**Document Processing** (spreadsheets, presentations, Word docs):
- Enable `document-skills@anthropic-agent-skills` or `example-skills@anthropic-agent-skills`
- Includes: xlsx (Excel), docx (Word), pptx (PowerPoint), pdf
- Use case: Data analysis, report generation, presentation creation

**Web Testing/Screenshots** (requires Playwright MCP):
- Load on-demand: `claude mcp add --scope local --transport stdio playwright -- npx -y @playwright/mcp@latest`
- Use case: Layout debugging, screenshot automation, browser testing

### How to Enable Plugins for a Project

Create or edit `.claude/settings.local.json` in the project directory:

```json
{
  "enabledPlugins": {
    "document-skills@anthropic-agent-skills": true
  }
}
```

This overrides the global `false` setting for that project only.

**Note**: Project-local overrides take priority over global settings. Restart Claude Code after changing plugin configuration.

---

## Recent Completed Work (Last 7 Days)

### January 4, 2026 - Claude Code Context Optimization ✅
- **Context Optimization** - Disabled global plugins and removed Playwright MCP to free up context
- **Plugins Disabled Globally**:
  - `frontend-design@claude-code-plugins`
  - `document-skills@anthropic-agent-skills`
  - `example-skills@anthropic-agent-skills`
- **MCP Servers**: Removed Playwright MCP from global configuration via `claude mcp remove playwright`
- **Context Savings**: ~55-65k tokens per session (27-32% reduction)
- **Configuration Approach**: Plugins remain installed but disabled globally; enable per-project as needed
- **Documentation Updated**:
  - Added "Claude Code Configuration" section to SESSION_CONTEXT.md
  - Updated ARCHIVE.md with historical entries (January 4, 2026 + December entries)
  - Updated scripts/README.md to clarify Playwright Python library vs MCP
  - Verified all other documentation files
  - Archived older entries from SESSION_CONTEXT.md to ARCHIVE.md
- **Result**: Lean global configuration optimized for episode deployment and content maintenance work
- Status: ✅ COMPLETE

**For detailed deployment history, see ARCHIVE.md**

---

## Production Deployment

**Latest Production Package**: `production-deployment-20251227-182404.zip` (8.2MB)
- Contents: 154 pages (67 episodes + 4 blog posts + newsletter + main pages), 367 files
- Includes: Episode 6 (Flipper Zero and Other Totally Legit Hacking Tools) with full 38-minute transcript
- Status: ✅ DEPLOYED TO PRODUCTION
- Deployed: December 27, 2025

**Deployment Process**:
1. Download latest production package
2. Log into GoDaddy cPanel File Manager
3. Navigate to `public_html/`
4. Delete old files (backup first if needed)
5. Upload and extract the production package
6. Verify `.htaccess` permissions are 644
7. Test site at https://securitycocktailhour.com/

**Deployment Documentation**: See `GODADDY-DEPLOYMENT-INSTRUCTIONS.md`

---

## Production Build Process

**STANDARD METHOD: Always use the automated build script**

```bash
./scripts/build_production.sh
```

**What it does:**
1. Validates .htaccess file integrity (before build)
2. Runs `hugo --minify` to build production site
3. Re-validates .htaccess in built package (after build)
4. Creates timestamped deployment ZIP: `production-deployment-YYYYMMDD-HHMMSS.zip`
5. Displays validation summary and deployment instructions

**Why use this instead of manual build:**
- ✓ Prevents broken 404 error pages from reaching production
- ✓ Ensures all 24 required 301 redirects are present
- ✓ Validates security headers and performance config
- ✓ Catches .htaccess errors before deployment
- ✓ Creates properly named, timestamped packages

**Exit codes:**
- 0 = All checks passed, safe to deploy
- 1 = Validation failed, DO NOT deploy (fix errors first)

**When requested to "build for production" or "create production package":**
- Use `./scripts/build_production.sh` (automated, with validation)
- NOT `hugo --minify` (manual, no validation)

---

## Quick Reference Commands

```bash
# Navigate to project
cd "/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website"

# Start development server
hugo server -D
# Access at http://localhost:1313/

# Build for production (RECOMMENDED - with validation)
./scripts/build_production.sh
# Creates: production-deployment-YYYYMMDD-HHMMSS.zip

# Validate .htaccess file integrity
python3 scripts/validate_htaccess.py

# Manual build for production (without validation)
hugo --minify

# Create new episode
hugo new episodes/episode-XX-title-slug.md

# Git workflow
git add -A
git commit -m "Description"
git push origin main  # Triggers Netlify staging deployment

# Run SEO audit scripts
python scripts/audit_title_tags.py
python scripts/audit_meta_descriptions.py

# Capture hero section screenshots (requires Playwright MCP)
# First load Playwright: claude mcp add --scope local --transport stdio playwright -- npx -y @playwright/mcp@latest
python3 scripts/capture_hero_sections.py

# Image optimization (if ImageMagick installed)
magick input.jpg -quality 85 -strip output.jpg
```

---

## Key Documentation Files

**Essential Documentation:**
- `SESSION_CONTEXT.md` - This file (current working context)
- `ARCHIVE.md` - Historical fixes and detailed reference material
- `docs/NEW-EPISODE-DEPLOYMENT.md` - New episode workflow
- `docs/SEO-TITLE-TAG-STANDARDS.md` - Title tag standards and implementation
- `docs/SEO-META-DESCRIPTION-STANDARDS.md` - Meta description standards
- `GODADDY-DEPLOYMENT-INSTRUCTIONS.md` - Production deployment guide

**Design Documentation:**
- `docs/design_specs/sch_design_spec_v1_3.md` - Master design specification (Art Deco - December 2025)
- `docs/design_specs/blog_page_spec.md` - Blog design specification (v1.2)
- `docs/design_specs/partnership_page_spec.md` - Partnership page specification (v1.1)

**Scripts:**
- `scripts/audit_title_tags.py` - Title tag audit tool
- `scripts/audit_meta_descriptions.py` - Meta description audit tool
- `scripts/capture_hero_sections.py` - Playwright automation to capture hero section screenshots
- `scripts/format_transcript.py` - Transcript formatting utility

**Design Prototypes:**
- `temp/hero-redesigns/` - Hero section redesign mockups (remaining files)
  - `index.html` - Gallery view of all 6 initial concepts
  - `home-hero-v2.html` through `home-hero-v5.html` - Home hero iterations
  - `homepage-full-mockup.html` - Full homepage mockup
  - `episodes-page-v2.html` - Episodes page mockup v2
  - Note: Approved mockups and screenshots removed from git after implementation (December 13, 2025)

---

## Current Site Status

**Phase 1 (MVP)**: ✅ Complete
- All core pages live
- All integrations working
- 66 episodes published

**Phase 2 (Blog)**: ✅ Complete
- Blog feature implemented
- 4 blog posts published
- Full SEO optimization

**Phase 3 (SEO)**: ✅ Complete
- Title tags optimized (≤60 chars)
- Meta descriptions optimized (120-155 chars)
- Schema.org markup implemented
- Images optimized (123KB saved)
- Sitemap submitted to Google & Bing

**Phase 3.5 (UX Enhancements)**: ✅ Complete (December 2, 2025)
- Collapsible transcript accordion (SEO-friendly)
- Manual related episodes override
- Episode 64 published with full transcript
- Episode number display on all cards
- Episode number search functionality

**Phase 4 (Art Deco Redesign)**: ✅ COMPLETE - All Pages Live in Production
- ✅ Logo design DNA analysis complete
- ✅ 6 initial design concepts created and reviewed
- ✅ Premium Art Deco aesthetic selected and finalized
- ✅ Design system established (Oswald/PT Serif/Bebas Neue typography, Red/Navy/Teal palette)
- ✅ Episodes page mockup complete (v3 - approved)
- ✅ About page mockup complete (approved)
- ✅ Contact page mockup complete (approved)
- ✅ Blog page mockup complete (approved)
- ✅ Homepage full mockup complete (v2 with PT Serif)
- ✅ Partnership page mockup complete (approved)
- ✅ **Homepage hero Hugo integration COMPLETE** (December 8, 2025)
  - All layout issues resolved using Playwright MCP debugging
  - Grid overflow fixed (percentage to fr units)
  - Episode badge positioning fixed (floating effect)
  - Newsletter alignment fixed (flexbox + CSS specificity)
  - Design matches approved mockup
- ✅ **All page Hugo integrations COMPLETE**
  - Episodes archive page - Art Deco design applied
  - About page - Art Deco design applied
  - Blog archive page - Art Deco design applied
  - Contact page - Art Deco design applied
  - Partnership page - Art Deco design applied
- ✅ **Complete Art Deco redesign deployed to production**
- ✅ **All changes pushed to GitHub**

**Production Status**: ✅ LIVE (Latest Deployment: December 27, 2025)
- Site: https://securitycocktailhour.com/
- **Complete Art Deco design system live across ALL pages** (Red/Navy/Teal palette, Oswald/PT Serif/Bebas Neue typography)
  - Homepage with redesigned hero section
  - Episodes archive page
  - About page
  - Blog archive page
  - Contact page
  - Partnership page
  - Newsletter page
  - All individual episode and blog post pages
- **Episode 67 live and accessible** (Flipper Zero Firmware Update - December 22, 2025) - Latest Episode
- **Episode 6 full transcript added** (Flipper Zero and Other Totally Legit Hacking Tools - December 27, 2025) - 38-minute transcript with collapsible accordion
- Episode 66 live and accessible (Flipper Zero Unboxing - December 15, 2025)
- Episode 65 live and accessible (Job Scams - December 8, 2025)
- Blog post "4 Dangerous Job Scams Targeting Professionals in 2025" featured on homepage
- Episode numbers displayed on all episode cards (Episodes page and Homepage)
- **Search functionality working correctly** - Episodes and blog page filters now function properly (fixed December 16, 2025)
- **404 Error Page working correctly** - Custom branded 404 page with navigation and 5-second auto-redirect (fixed December 17, 2025)
- **301 Redirects active** - All 24 legacy URL redirects working (verified December 17, 2025)
- Collapsible transcript accordion working across all episode pages
- Manual related episodes feature active
- All SEO optimizations active
- Cache-busting implemented (CSS updates load properly)
- Submitted to search engines (Google & Bing)
- **154 pages live (67 episodes + 4 blog posts + newsletter + main pages)**
- **GitHub repository synchronized** (Episode 6 transcript pushed December 27, 2025 - commit `df14c75`)

---

**For detailed historical information, see ARCHIVE.md**
