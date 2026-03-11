# Security Cocktail Hour Website - Claude Context

**Last Updated**: March 11, 2026
**Hugo Version**: v0.151.0
**Branch**: main

---

## Current Session

*Use this section for active work. Clear when complete.*

**Pending**: Google Search Console re-crawl in progress (Validate Fix initiated Mar 11, 2026). Check back in a few days to confirm 404 count drops.

---

## Project Overview

**Production Site**: https://securitycocktailhour.com/ (GoDaddy cPanel)
**Staging Site**: Netlify automatic deployments from GitHub
**GitHub Repository**: https://github.com/security-cocktail-hour/security-cocktail-hour-website
**Local Dev Server**: http://localhost:1313/ (when running `hugo server -D`)

**Current Stats**: 274 pages (72 episodes, 9 blog posts, newsletter, main pages) | 10MB production package

---

## Recent Completed Work

**March 11, 2026** - Fixed Google Search Console 404 indexing errors (25 URLs). Converted `Redirect 301` to `RewriteRule` directives to fix double-redirect conflict with trailing slash rule. Added 5 missing redirects. Deployed to production, GSC Validate Fix initiated.

**March 11, 2026** - Episode 72 & blog post deployed.

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

**Latest Package**: `production-deployment-20260311-154056.zip` (10MB, 274 pages)

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

**Production**: https://securitycocktailhour.com/ - 274 pages live
- Art Deco design (Red/Navy/Teal, Oswald/PT Serif/Bebas Neue)
- Latest: Episode 72 "Drones Are the Next Cyber Weapon" (Mar 11, 2026), Blog Post "Drones Are Already Being Used as Cyberweapons" (Mar 10, 2026)
- Store hidden (draft: true) — ready to re-enable when store launches
- All features working: search, transcripts, 404 page, 301 redirects, SEO

**For detailed phase history, see ARCHIVE.md**
