# Security Cocktail Hour Website - Claude Context

**Last Updated**: February 2, 2026
**Hugo Version**: v0.151.0
**Branch**: main

---

## Current Session

*Use this section for active work. Clear when complete.*

---

## Project Overview

**Production Site**: https://securitycocktailhour.com/ (GoDaddy cPanel)
**Staging Site**: Netlify automatic deployments from GitHub
**GitHub Repository**: https://github.com/security-cocktail-hour/security-cocktail-hour-website
**Local Dev Server**: http://localhost:1313/ (when running `hugo server -D`)

**Current Stats**: 219 pages (70 episodes, 6 blog posts, newsletter, main pages) | 8.8MB production package

---

## Recent Completed Work

**February 2, 2026** - Episode 70: "Securing Mars Rovers and Space Stations with NASA's Former CIO Renee Wynn" deployed to production.

**For detailed history, see ARCHIVE.md**

---

## Production Workflow

**Build & Deploy**:
```bash
./scripts/build_production.sh    # Validates .htaccess, builds, creates ZIP
```
- Creates: `production-deployment-YYYYMMDD-HHMMSS.zip`
- Validates: 301 redirects, 404 page, security headers
- Exit 0 = safe to deploy, Exit 1 = fix errors first

**Deploy to GoDaddy**: Upload ZIP to `public_html/`, extract, verify `.htaccess` permissions (644). See `GODADDY-DEPLOYMENT-INSTRUCTIONS.md`.

**Latest Package**: `production-deployment-20260202-194707.zip` (8.8MB, 219 pages)

---

## Quick Reference

```bash
# Development
hugo server -D                              # Start dev server at localhost:1313

# Production build
./scripts/build_production.sh               # Build with validation

# Pre-deployment tests
python3 scripts/tests/run_all_tests.py      # All tests
python3 scripts/tests/run_all_tests.py --static   # Static pages only
python3 scripts/tests/run_all_tests.py --episodes # Episodes only
python3 scripts/tests/run_all_tests.py --blog     # Blog only

# Git
git add -A && git commit -m "Description" && git push origin main

# Utilities
python3 scripts/validate_htaccess.py        # Validate .htaccess
python scripts/audit_title_tags.py          # SEO audit
python scripts/audit_meta_descriptions.py   # SEO audit
```

---

## Key Documentation

| File | Purpose |
|------|---------|
| `CLAUDE.md` | This file - project context |
| `ARCHIVE.md` | Historical fixes and reference |
| `docs/NEW-EPISODE-DEPLOYMENT.md` | Episode workflow |
| `docs/SEO-TITLE-TAG-STANDARDS.md` | Title tag standards |
| `docs/SEO-META-DESCRIPTION-STANDARDS.md` | Meta description standards |
| `docs/CLAUDE-CODE-CONFIG.md` | Claude Code configuration |
| `GODADDY-DEPLOYMENT-INSTRUCTIONS.md` | Production deployment |
| `scripts/tests/README.md` | Testing documentation |

**Custom Skills** (`.claude/skills/`):
- `episode-deploy` - Automated episode deployment (transcript processing, SEO, testing, git)
- `blog-deploy` - Automated blog deployment (SEO, validation, testing, git)
- `cpanel-deploy` - **NOT FUNCTIONAL** - GoDaddy SSH auth issues; use manual deployment

---

## Current Site Status

**All Phases Complete**: MVP | Blog | SEO | UX Enhancements | Art Deco Redesign

**Production**: https://securitycocktailhour.com/ - 219 pages live
- Art Deco design (Red/Navy/Teal, Oswald/PT Serif/Bebas Neue)
- Latest: Episode 70 "Securing Mars Rovers and Space Stations" (Feb 2, 2026), Blog Post "The SLA Wake-Up Call" (Jan 22, 2026)
- All features working: search, transcripts, 404 page, 301 redirects, SEO

**For detailed phase history, see ARCHIVE.md**
