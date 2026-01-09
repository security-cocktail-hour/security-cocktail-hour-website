# Security Cocktail Hour Website - Claude Context

**Last Updated**: January 8, 2026
**Hugo Version**: v0.151.0
**Branch**: main

---

## Current Session

**Today's Focus**: Pre-deployment test suite implementation + Configuration documentation audit

### Pre-Deployment Test Suite ✅
- **Test Suite Created:**
  - Comprehensive Playwright-based testing in `scripts/tests/`
  - Smart episode testing strategy: newest 5 + one from each block of 10
  - Coverage: 25+ pages (8 static, 12 episodes, 5 blog posts) in 4-5 minutes
  - Automated failure screenshot capture for debugging
  - Master test runner with CLI options (--static, --episodes, --blog)
- **Documentation Updated:**
  - Added Step 5.5 to NEW-EPISODE-DEPLOYMENT.md (pre-deployment testing workflow)
  - Created comprehensive testing documentation in scripts/tests/README.md
  - Added cleanup step for test screenshots
  - Updated deployment approval workflow
- **Result:** Quality gate between manual review and production deployment - catches technical issues before reaching production

### Configuration Documentation Audit ✅
- **Audited Claude Code Configuration**: Reviewed actual plugin, skill, and MCP server state
- **Updated CLAUDE.md**: Corrected "Claude Code Configuration" section to reflect actual current state
  - document-skills plugin: Enabled globally (16 skills loaded)
  - Playwright MCP: Configured globally (22 tools loaded)
  - Total context usage: 23k tokens (11% of 200k) - efficient and well-balanced
- **Corrected January 4 entry**: Updated to accurately reflect configuration documentation work
- **Renamed SESSION_CONTEXT.md to CLAUDE.md**: Aligned with Claude Code community conventions
  - Used `git mv` to preserve history
  - Updated 11 files with references (ARCHIVE.md, docs/, skills/)
  - Changed header from "Session Context" to "Claude Context"
  - CLAUDE.md is the standard convention for project-specific context
- **Result:** Documentation now accurately reflects actual system state and follows standard conventions

---

## Project Overview

**Production Site**: https://securitycocktailhour.com/ (GoDaddy cPanel - Live)
**Staging Site**: Netlify automatic deployments from GitHub
**GitHub Repository**: https://github.com/security-cocktail-hour/security-cocktail-hour-website
**Local Dev Server**: http://localhost:1313/ (when running `hugo server -D`)

**Current Stats**: 154 pages (67 episodes, 4 blog posts, newsletter page, main pages) | 6.0MB images | 8.2MB production package

---

## Claude Code Configuration

### Current Configuration (Updated: January 8, 2026)

**Context Usage**: ~23k tokens (11% of 200k budget) - Optimized for episode deployment and general website work

**Global Settings** (`~/.claude/settings.json`):
```json
{
  "enabledPlugins": {
    "frontend-design@claude-plugins-official": false,
    "document-skills@anthropic-agent-skills": true
  }
}
```

**MCP Servers** (Global):
- Playwright MCP: Configured and running (`npx -y @playwright/mcp@latest`)
- Provides browser automation for testing and debugging

**Project Settings** (`.claude/settings.local.json`):
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

### What's Currently Loaded

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

### Configuration Notes

- **document-skills enabled globally**: Provides comprehensive document processing capabilities (Word, Excel, PowerPoint, PDF) always available
- **Playwright MCP configured globally**: Essential for pre-deployment testing workflow and visual debugging
- **frontend-design disabled globally**: Available via Skill tool when needed for design mockups
- **Context is not constrained**: With 132k tokens free (66%), the current configuration provides good balance between capability and efficiency
- **Pre-deployment testing**: Current setup supports the automated test suite in `scripts/tests/`

### Modifying Configuration

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

---

## Recent Completed Work (Last 7 Days)

### January 8, 2026 - Pre-Deployment Test Suite Implementation ✅
- **Test Suite Created** - Comprehensive Playwright-based testing for quality assurance before production
- **Test Scripts** (`scripts/tests/`):
  - `test_helpers.py` - Content discovery and validation utilities (360 lines)
  - `test_static_pages.py` - Test 8 static pages (364 lines)
  - `test_episodes.py` - Smart episode testing with block strategy (412 lines)
  - `test_blog.py` - Blog list and post testing (397 lines)
  - `run_all_tests.py` - Master test runner with CLI options (142 lines)
  - `README.md` - Complete testing documentation (179 lines)
- **Testing Strategy**:
  - Smart episode selection: Always test newest 5 + one from each block of 10 older episodes
  - Deterministic and scalable as site grows (currently tests 12 of 67 episodes)
  - Blog posts: Test 5 latest (currently all 4, prepared for growth)
  - Static pages: Test all 8 pages (homepage, about, contact, partnership, resources, newsletter, privacy, terms)
- **Coverage**: 25+ pages tested in 4-5 minutes
- **Validation**: Page loads, SEO metadata, navigation, platform links, forms, search/filter, console errors, transcript sections, related episodes
- **Screenshot Capture**: Automatic failure screenshots for debugging (saved to `scripts/tests/test_screenshots/`)
- **Documentation Updated**:
  - Added Step 5.5 to `docs/NEW-EPISODE-DEPLOYMENT.md` (run pre-deployment tests)
  - Integration workflow: Manual review → Automated tests → Clean up → Production build
  - Added troubleshooting section for test failures
  - Updated Quick Reference with testing commands
- **Git**: Committed 19 files (4,069+ additions) and pushed to GitHub
- Status: ✅ COMPLETE

### January 4, 2026 - Documentation and Configuration Review ✅
- **Configuration Documentation** - Documented Claude Code configuration approach
- **Current Configuration State**:
  - `document-skills@anthropic-agent-skills`: Enabled globally (provides 16 document/design skills)
  - `frontend-design@claude-plugins-official`: Disabled globally (available via Skill tool when needed)
  - Playwright MCP: Configured globally (essential for pre-deployment testing workflow)
- **Context Usage**: Efficient at ~23k tokens (11% of 200k budget) with 132k tokens free (66.2%)
- **Configuration Approach**: Balance between capability and efficiency - core tools always available, specialized tools on-demand
- **Documentation Updated**:
  - Added "Claude Code Configuration" section to CLAUDE.md
  - Updated ARCHIVE.md with historical entries (January 4, 2026 + December entries)
  - Updated scripts/README.md to clarify Playwright Python library vs MCP
  - Verified all other documentation files
  - Archived older entries from CLAUDE.md to ARCHIVE.md
- **Result**: Well-documented configuration optimized for episode deployment, testing, and content work
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

# Run pre-deployment tests (RECOMMENDED before production)
python3 scripts/tests/run_all_tests.py          # All tests (~4-5 min)
python3 scripts/tests/run_all_tests.py --static  # Static pages only (~15 sec)
python3 scripts/tests/run_all_tests.py --episodes # Episodes only (~2-3 min)
python3 scripts/tests/run_all_tests.py --blog    # Blog only (~1 min)

# Clean up after testing
rm -rf scripts/tests/test_screenshots

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
- `CLAUDE.md` - This file (project context and working reference)
- `ARCHIVE.md` - Historical fixes and detailed reference material
- `docs/NEW-EPISODE-DEPLOYMENT.md` - New episode workflow (includes Step 5.5: pre-deployment testing)
- `docs/SEO-TITLE-TAG-STANDARDS.md` - Title tag standards and implementation
- `docs/SEO-META-DESCRIPTION-STANDARDS.md` - Meta description standards
- `GODADDY-DEPLOYMENT-INSTRUCTIONS.md` - Production deployment guide
- `scripts/tests/README.md` - Pre-deployment testing documentation

**Design Documentation:**
- `docs/design_specs/sch_design_spec_v1_3.md` - Master design specification (Art Deco - December 2025)
- `docs/design_specs/blog_page_spec.md` - Blog design specification (v1.2)
- `docs/design_specs/partnership_page_spec.md` - Partnership page specification (v1.1)

**Scripts:**
- `scripts/build_production.sh` - Production build with .htaccess validation
- `scripts/validate_htaccess.py` - Validate .htaccess file integrity
- `scripts/audit_title_tags.py` - Title tag audit tool
- `scripts/audit_meta_descriptions.py` - Meta description audit tool
- `scripts/capture_hero_sections.py` - Playwright automation to capture hero section screenshots
- `scripts/format_transcript.py` - Transcript formatting utility

**Testing Scripts** (`scripts/tests/`):
- `run_all_tests.py` - Master test runner (all, static, episodes, blog)
- `test_static_pages.py` - Test 8 static pages
- `test_episodes.py` - Smart episode testing (newest 5 + block sampling)
- `test_blog.py` - Blog list and post testing
- `test_helpers.py` - Content discovery and validation utilities
- `README.md` - Complete testing documentation

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
