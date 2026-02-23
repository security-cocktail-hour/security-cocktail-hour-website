# Security Cocktail Hour Website - Claude Context

**Last Updated**: February 23, 2026
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

**Current Stats**: 252 pages (71 episodes, 8 blog posts, newsletter, main pages) | 9.9MB production package

---

## Recent Completed Work

**February 23, 2026** - Episode 71: Added Apple Podcasts and Amazon Music links. Redeployed to production.

**February 22, 2026** - Blog Post: "OpenClaw turned AI security upside down. That's actually good news." deployed. Featured post (replaced Venezuela post). Related to Episode 51. Store hidden from site (draft: true, removed from nav/footer) — content preserved for future launch.

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

**Latest Package**: `production-deployment-20260223-182907.zip` (9.9MB, 252 pages)

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

**Production**: https://securitycocktailhour.com/ - 252 pages live
- Art Deco design (Red/Navy/Teal, Oswald/PT Serif/Bebas Neue)
- Latest: Episode 71 "Breaking Vulnerability Management's 30-Year Logjam" (Feb 23, 2026), Blog Post "OpenClaw turned AI security upside down" (Feb 22, 2026), Blog Post "OpenClaw's security reputation is well-deserved" (Feb 5, 2026)
- Store hidden (draft: true) — ready to re-enable when store launches
- All features working: search, transcripts, 404 page, 301 redirects, SEO

**For detailed phase history, see ARCHIVE.md**
