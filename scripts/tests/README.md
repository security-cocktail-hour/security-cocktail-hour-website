# Pre-Deployment Testing Suite

Comprehensive Playwright-based testing for the Security Cocktail Hour website before production deployment.

## Quick Start

```bash
# From project root directory
python3 scripts/tests/run_all_tests.py
```

## Test Coverage

- **8 Static Pages**: Homepage, About, Contact, Partnership, Resources, Newsletter, Privacy, Terms
- **Episodes**: List page + 12 individual episodes (newest 5 + 1 from each block of 10)
- **Blog**: List page + 5 latest posts (currently 4)

**Total**: ~25 pages tested in 4-5 minutes

## Usage

### Run All Tests (Recommended)
```bash
python3 scripts/tests/run_all_tests.py
```

### Run Specific Test Suites
```bash
# Static pages only
python3 scripts/tests/run_all_tests.py --static

# Episodes only
python3 scripts/tests/run_all_tests.py --episodes

# Blog only
python3 scripts/tests/run_all_tests.py --blog
```

### Run Individual Test Files
```bash
# Static pages
python3 scripts/tests/test_static_pages.py

# Episodes
python3 scripts/tests/test_episodes.py

# Blog
python3 scripts/tests/test_blog.py
```

## What Gets Tested

### All Pages
- ✅ Page loads successfully
- ✅ Title correct
- ✅ Navigation links present
- ✅ SEO metadata (title, description, og tags)
- ✅ No console errors

### Episode Pages
- ✅ Episode number, date, duration displayed
- ✅ Category badge
- ✅ Platform links (YouTube, Spotify, Apple, Amazon)
- ✅ Episode image
- ✅ Transcript section (if present)
- ✅ Related episodes (if present)
- ✅ Newsletter form

### Blog Posts
- ✅ Author name and date
- ✅ Category and tags
- ✅ Related episode link (if present)
- ✅ Content sections
- ✅ Newsletter sidebar

### List Pages (Episodes/Blog)
- ✅ Search functionality
- ✅ Category filter
- ✅ Tag filter (blog only)
- ✅ Sort dropdown

## Episode Selection Strategy

**Smart block-based testing for scalability:**
- Always test newest 5 episodes (most likely to have issues)
- Test 1 episode from each block of 10:
  - Episodes 1-10: Test episode 5
  - Episodes 11-20: Test episode 15
  - Episodes 21-30: Test episode 25
  - Episodes 31-40: Test episode 35
  - Episodes 41-50: Test episode 45
  - Episodes 51-60: Test episode 55
  - Episodes 61-70: Test episode 61

**Result**: Comprehensive coverage across entire episode history (12 episodes tested for 67 total)

## Output

### Success
```
================================================================================
FINAL TEST SUMMARY
================================================================================
Static Pages:  ✅ PASSED (52/52)
Episodes:      ✅ PASSED (140/140)
Blog:          ✅ PASSED (44/44)

TOTAL: 236 passed, 0 failed
Duration: 4m 18s
================================================================================

✅ ALL TESTS PASSED - Ready for deployment!
```

### Failure
```
❌ 6 TEST(S) FAILED - Review errors before deployment

Failed test screenshots saved in: scripts/tests/test_screenshots/
```

## Screenshot Capture

Screenshots are automatically captured **only on failures** for debugging:
- Location: `scripts/tests/test_screenshots/`
- Format: `{test_name}_{timestamp}_FAILED.png`
- Full page screenshots for visual debugging

## Requirements

```bash
pip install playwright pyyaml
playwright install chromium
```

## Before Running Tests

**Start Hugo dev server:**
```bash
hugo server
```

Tests expect the site to be running at `http://localhost:1313/`

## Integration with Deployment Workflow

```bash
# 1. Start dev server
hugo server

# 2. Run full test suite
python3 scripts/tests/run_all_tests.py

# 3. If all tests pass, build for production
./scripts/build_production.sh

# 4. Deploy to production
```

## Files

- `test_helpers.py` - Shared utilities and content discovery
- `test_static_pages.py` - Static page testing (8 pages)
- `test_episodes.py` - Episode testing with block strategy
- `test_blog.py` - Blog testing (latest 5 posts)
- `run_all_tests.py` - Master test runner

## Maintenance

As the site grows:
- ✅ **New episodes**: Automatically discovered and tested
- ✅ **New blog posts**: Automatically discovered and tested
- ⚠️ **New static pages**: Add test function to `test_static_pages.py`
- ⚠️ **Template changes**: Update validators in `test_helpers.py`

## Exit Codes

- `0` = All tests passed (safe to deploy)
- `1` = One or more tests failed (review before deploying)
