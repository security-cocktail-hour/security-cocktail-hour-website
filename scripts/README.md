# Scripts Directory

Utility scripts for the Security Cocktail Hour Website project.

---

## Production Deployment Scripts

### `build_production.sh`

**Purpose:** Automated production build with .htaccess validation

**Usage:**
```bash
./scripts/build_production.sh
```

**What it does:**
1. Validates `.htaccess` file integrity (before build)
2. Builds production site with `hugo --minify`
3. Re-validates built `.htaccess` file (after build)
4. Creates timestamped deployment ZIP package
5. Displays deployment summary

**Output:**
- Production package: `production-deployment-YYYYMMDD-HHMMSS.zip`
- Exit code 0: Success (safe to deploy)
- Exit code 1: Validation failed (DO NOT deploy)

**When to use:**
- Before every production deployment
- Ensures .htaccess file is not broken
- Prevents broken redirects and 404 pages

---

### `validate_htaccess.py`

**Purpose:** Validates .htaccess file integrity

**Usage:**
```bash
python3 scripts/validate_htaccess.py
```

**What it checks:**
- ✓ File exists in `static/` and `public/` directories
- ✓ File is not empty
- ✓ ErrorDocument 404 directive present
- ✓ All 24 required 301 redirects present
- ✓ No duplicate redirects
- ✓ RewriteEngine enabled
- ✓ HTTPS redirect configured
- ✓ Trailing slash rules configured
- ✓ Security headers (X-Frame-Options, X-XSS-Protection, X-Content-Type-Options)
- ✓ Performance optimizations (mod_expires, mod_deflate)
- ✓ `static/.htaccess` matches `public/.htaccess`

**Exit codes:**
- 0: All checks passed
- 1: One or more checks failed

**When to use:**
- Before deploying to production
- After modifying `.htaccess` file
- When debugging redirect or 404 issues
- Automatically called by `build_production.sh`

---

## SEO Audit Scripts

### `audit_title_tags.py`

**Purpose:** Audits title tags across all pages for SEO compliance

**Usage:**
```bash
python scripts/audit_title_tags.py
```

**What it checks:**
- Title tag length (≤60 characters recommended)
- Missing title tags
- Duplicate title tags
- Title tag format consistency

**Output:**
- Summary report with warnings and errors
- Lists pages that need attention

---

### `audit_meta_descriptions.py`

**Purpose:** Audits meta descriptions across all pages for SEO compliance

**Usage:**
```bash
python scripts/audit_meta_descriptions.py
```

**What it checks:**
- Meta description length (120-155 characters recommended)
- Missing meta descriptions
- Duplicate meta descriptions
- Meta description quality

**Output:**
- Summary report with warnings and errors
- Lists pages that need attention

---

## Development Scripts

### `capture_hero_sections.py`

**Purpose:** Captures screenshots of hero sections using Playwright automation

**Usage:**
```bash
python3 scripts/capture_hero_sections.py
```

**Requirements:**
- Playwright installed: `pip install playwright`
- Playwright browsers installed: `playwright install`

**What it does:**
- Launches local development server
- Captures screenshots of hero sections
- Saves to specified output directory

**When to use:**
- Documenting design changes
- Creating mockup comparisons
- Visual regression testing

---

### `format_transcript.py`

**Purpose:** Formats podcast transcripts for Hugo markdown files

**Usage:**
```bash
python scripts/format_transcript.py input.txt output.md
```

**What it does:**
- Cleans up transcript formatting
- Adds proper markdown structure
- Formats speaker names
- Removes extra whitespace

**When to use:**
- Processing new episode transcripts
- Converting raw transcripts to markdown

---

## Quick Reference

### Production Deployment Workflow

```bash
# 1. Validate and build production package (recommended)
./scripts/build_production.sh

# 2. Manual validation (if needed)
python3 scripts/validate_htaccess.py

# 3. Manual build (if not using automated script)
hugo --minify

# 4. Manual deployment package creation
zip -r production-deployment-$(date +%Y%m%d-%H%M%S).zip public/
```

### SEO Auditing Workflow

```bash
# Run both SEO audits
python scripts/audit_title_tags.py
python scripts/audit_meta_descriptions.py

# Fix any issues found in markdown frontmatter
# Re-run audits to verify fixes
```

---

## Script Requirements

### Python Scripts
- Python 3.6 or higher
- No external dependencies for validation scripts
- Playwright required for `capture_hero_sections.py`

### Bash Scripts
- Bash 3.2 or higher (macOS default)
- Hugo CLI installed
- zip command (pre-installed on macOS/Linux)

---

## Exit Codes

All scripts follow standard Unix exit code conventions:
- `0` - Success
- `1` - General error or validation failure
- `2` - Command usage error

---

## Adding New Scripts

When adding new scripts to this directory:

1. Add appropriate shebang line
2. Add usage documentation in comments
3. Follow naming convention: `verb_noun.py` or `verb_noun.sh`
4. Make executable: `chmod +x scripts/your_script.sh`
5. Update this README with documentation
6. Test thoroughly before committing

---

**Last Updated:** December 17, 2025
