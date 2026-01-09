# Security Cocktail Hour Website - Archive

**Purpose**: This file contains historical fixes, detailed troubleshooting information, and reference material that is not needed for day-to-day work but is preserved for future reference.

**Last Updated**: January 4, 2026

---

## Table of Contents

1. [Fixed Issues - Chronological](#fixed-issues---chronological)
2. [Data Migration History](#data-migration-history)
3. [Design System Details](#design-system-details)
4. [Color Palette Evolution](#color-palette-evolution)
5. [Troubleshooting Guide](#troubleshooting-guide)
6. [Deployment Details](#deployment-details)

---

## Fixed Issues - Chronological

### January 4, 2026 - Claude Code Context Optimization ✅

**Context Optimization Changes:**
- Disabled global plugins to free up context for episode deployment work
- Removed Playwright MCP from global configuration
- Total context savings: ~55-65k tokens per session (27-32% of total context)

**Plugins Disabled Globally:**
- `frontend-design@claude-code-plugins` - Frontend design work (mockups, visual debugging)
- `document-skills@anthropic-agent-skills` - Document processing (xlsx, docx, pptx, pdf)
- `example-skills@anthropic-agent-skills` - Duplicate of document-skills

**MCP Servers:**
- Playwright MCP - Removed from global config (used during Art Deco redesign for browser debugging)

**Configuration Approach:**
- Plugins remain **installed** but **disabled globally** by default
- Enable per-project as needed via `.claude/settings.local.json`
- Load Playwright MCP on-demand: `claude mcp add --scope local --transport stdio playwright -- npx -y @playwright/mcp@latest`

**Impact:**
- Lean context for typical episode deployment and content maintenance work
- Plugins available when needed for design work, document processing, or browser testing
- No impact on `scripts/capture_hero_sections.py` (uses Playwright Python library, not MCP)

**Documentation Updated:**
- CLAUDE.md - Added "Claude Code Configuration" section
- scripts/README.md - Clarified Playwright Python library vs MCP distinction
- ARCHIVE.md - This entry

**See:** CLAUDE.md for complete configuration details and usage instructions.

---

### December 27, 2025 - Episode 6 Full Transcript Addition ✅

**Episode 6** full transcript added to production:
- **Title**: "Flipper Zero and Other Totally Legit Hacking Tools"
- **Transcript**: Complete 38-minute transcript (~411 lines of dialogue)
- **Conversion**: Converted from DaVinci Resolve format using `format_davinci_transcript.py`
- **Episode Highlights**: Updated with 5 key topic bullets:
  - White hat vs. black hat: The ethics of security tools
  - Responsible disclosure: When and how to report vulnerabilities
  - Why Amazon banned it (and why that misses the point)
  - Real stakes: Cars, building systems, and IoT vulnerabilities
  - Debunking the hype: What the Flipper Zero CAN'T do
- **Display**: Transcript displayed in collapsible accordion (SEO-friendly)
- **Bug Fix**: Fixed name typo (Joe Patty → Joe Patti) in opening line
- **Commit**: `df14c75`
- **Production Package**: `production-deployment-20251227-182404.zip` (8.2MB, 367 files)
- **Status**: ✅ DEPLOYED TO PRODUCTION

---

### December 22, 2025 - Episode 67 Platform URL Updates ✅

**Episode 67** platform URLs updated:
- Replaced Apple Podcasts tinyurl with full episode URL
- Replaced Amazon Music tinyurl with full episode URL
- URLs now point directly to episode on each platform

**Episode Deployment Skill Created**:
- `episode-deploy.skill` - Automated episode deployment workflow (23KB)
- Includes transcript format detection and conversion
- Auto-generates SEO metadata (title, description, tags, topics)
- Three interactive approval checkpoints (SEO review, dev preview, production confirmation)
- References: seo-standards.md, transcript-formats.md, episode-workflow.md, git-standards.md
- Scripts: format_davinci_transcript.py, format_transcript.py

**Commit**: `1529046`
**Production Package**: `production-deployment-20251222-131949.zip` (8.2MB, 367 files)
**Status**: ✅ DEPLOYED TO PRODUCTION

---

### December 22, 2025 - Episode 67: Flipper Zero Firmware Update ✅

**Episode 67** deployed to production:
- **Title**: "Flipper Zero Firmware Update: If at first you don't succeed..."
- **Topic**: Firmware update walkthrough with troubleshooting
- **Duration**: 15:55
- **Category**: Hardware Security
- **Full Transcript**: Included (~440 lines)
- **SEO**: 53-char title, 155-char description

**New Tools Created**:
- `scripts/format_davinci_transcript.py` - Converts DaVinci Resolve transcript format to episode format
- Handles timecode conversion from `[HH:MM:SS:FF]` to `(MM:SS)`

**Episode Workflow Improvement**:
- Updated `docs/NEW-EPISODE-DEPLOYMENT.md` with new auto-generation workflow
- Claude now auto-generates SEO title, meta description, tags, and topics
- User reviews and approves generated metadata before deployment
- Streamlines episode creation process

**Related Episodes**: Episode 66 (Flipper Zero Unboxing), Episode 6
**Commit**: `4405873`
**Production Package**: `production-deployment-20251222-105612.zip` (8.2MB, 367 files)
**Status**: ✅ DEPLOYED TO PRODUCTION

---

### December 17, 2025 - 404 Error Page, Validation System & cPanel Cleanup ✅

**404 Error Handling**:
- Added `ErrorDocument 404 /404.html` directive to .htaccess
- Fixed Google indexing issue where Apache default 404 was shown instead of custom page
- Users now see branded 404 page with navigation and 5-second auto-redirect

**301 Redirects Verified**:
- All 24 existing redirects working correctly (from Google Search Console report)
- 6 transcript page redirects
- 8 episode list page redirects
- 3 info page redirects
- 1 support page redirect
- 6 store/merchandise redirects

**Validation System Created**:
- `scripts/validate_htaccess.py` - Validates all 24 redirects, 404 config, security headers
- `scripts/build_production.sh` - Automated build with validation (now standard method)
- Updated deployment documentation with validation requirements
- Created `scripts/README.md` with complete documentation

**cPanel Server Cleanup**:
- Removed leftover `.htaccess` file from home directory
- Issue: Production ZIP was accidentally extracted in home directory instead of `public_html/`
- Removed: `.htaccess` file from `/home/nfgitkw863go/` (should only exist in `public_html/`)
- Impact: None - production site in `public_html/` was unaffected
- Note for future: Always extract production packages directly into `public_html/`

**Commits**: `1770355` (404 fix), `42e3058` (validation system), `b4f1786` (SESSION_CONTEXT update)
**Production Package**: `production-deployment-20251217-214752.zip` (8.1MB, 352 files)
**Status**: ✅ DEPLOYED TO PRODUCTION

---

### December 16, 2025 - Search Functionality Bug Fixes ✅

**Episodes page search** - Fixed large gap issue when filtering results
**Blog page search** - Fixed same layout issue

**Root Cause**: JavaScript was hiding `.episode-card` instead of `.episode-card-link` wrappers

**Also Fixed**: Centered no-results messages with proper width constraints

**Commits**: `d938b75` (episodes), `33ef736` (blog)
**Production Package**: `production-deployment-20251216-151412.zip` (8.1MB, 352 files)
**Status**: ✅ DEPLOYED TO PRODUCTION

---

### December 15, 2025 - Episode 66: Flipper Zero Unboxing - PRODUCTION DEPLOYED ✅

**✅ STATUS: PRODUCTION DEPLOYMENT COMPLETE**

**Deployment Package**: `production-deployment-20251215-140357.zip` (8.1MB)

**Episode Details**:
- **Title**: "Unboxing the Device Every Hacker Wants"
- **Episode Number**: 66
- **Date**: December 15, 2025
- **Duration**: 05:30
- **Category**: Unboxing (2nd unboxing episode - first was Episode 58)
- **Topic**: Flipper Zero hardware security testing tool

**SEO Optimization**:
- **Title Tag**: "Unboxing the Device Every Hacker Wants" (40 chars - excellent)
- **Meta Description**: "Flipper Zero unboxed: RFID testing, infrared capabilities, hardware features, and ethical use of this security testing tool." (128 chars)
- **SEO Score**: 9.5/10
  - Front-loaded keywords (✅ "Flipper Zero" at position 0)
  - Active voice (✅ "unboxed")
  - Specific content (✅ lists exact features)
  - No filler phrases (✅)
  - Mobile-friendly (✅ displays completely on all devices)

**Content Summary**:
- Unboxing of Flipper Zero security testing device
- Overview of hardware features: RFID, NFC, infrared, Sub-GHz, GPIO pins
- Demonstration of capabilities (Tesla charging port access, IR signal replay, breadboard testing)
- Emphasis on ethical use as legitimate security testing tool
- Full transcript included (~5,300 words)

**Platform Links**:
- YouTube: https://youtu.be/1wZTNDO_Yyc
- Spotify: https://tinyurl.com/mrxxjz8h
- Apple Podcasts: https://tinyurl.com/jvhb6467
- Amazon Music: https://tinyurl.com/4zuxzk4n

**Tags**:
- flipper-zero
- hardware
- security-tools
- pentesting
- hacking-tools

**Files Created**:
- `content/episodes/episode-66-unboxing-device-every-hacker-wants.md`
- `static/images/episodes/episode-66-unboxing-device-every-hacker-wants.jpg`

**Build Statistics**:
- Pages: 145 (up from 134)
- Non-page files: 23
- Static files: 63
- Build time: 217ms
- Minified: Yes
- Production package: 8.1MB

**Production Deployment**: ✅ Successfully deployed December 15, 2025

---

### December 13, 2025 - Repository Cleanup and GitHub Sync ✅

**✅ CURRENT STATUS: ALL CHANGES PUSHED TO GITHUB**

**Git Push Completed**:
- Pushed 5 pending commits to GitHub (commits `9dfaae4` through `e14d8a6`)
- Netlify staging deployment triggered automatically
- Repository now fully synchronized with local development

**Repository Cleanup**:
- **Git Commit**: `3aaa538` - "Clean up temporary files and update .gitignore"
- **Files Removed**: 16 temporary files (4,659 lines deleted)
  - Old deployment package: `production-deployment-20251206-154540.zip`
  - Hero redesign mockups: 5 HTML files from `temp/hero-redesigns/`
  - Hero screenshots: 6 PNG files from `temp/hero-screenshots/`
  - Temp test files: `episode-number-options.html`, `transcript-accordion-demo.html`
  - Temp data files: `404_urls_for_redirect.csv`, `episodes.pdf`

**Updated .gitignore**:
- Added `*.zip` to exclude deployment packages
- Added `.playwright-mcp/` to exclude Playwright MCP directory
- Current deployment package (`production-deployment-20251210-124818.zip`) now properly ignored

**Git Status**: ✅ Working tree clean
**Branch**: main (up to date with origin/main)

---

### December 10, 2025 - Episode 65 & Job Scams Blog Post - PRODUCTION DEPLOYED ✅

**✅ STATUS: PRODUCTION DEPLOYMENT COMPLETE**

**Deployment Package**: `production-deployment-20251210-124818.zip` (7.9MB)
**Git Commits**:
- `9dfaae4` - Add Episode 65 blog post on job scams and update featured posts
- `59877b8` - Optimize SEO metadata for Episode 65 and job scams blog post

**Content Additions**:

1. **Episode 65: Job Scams Are Getting Worse | Four of the Most Dangerous**
   - **File**: `content/episodes/episode-65-job-scams-are-getting-worse-four-of-the-most-dangerous.md`
   - **Date**: December 8, 2025
   - **Duration**: 31:58
   - **Category**: Educational
   - **Description**: "AI deepfakes, malware, and crypto scams are targeting job seekers. Learn to spot these 4 dangerous employment scams in 2025 and protect yourself." (158 chars)
   - **Platform Links**: YouTube, Spotify, Apple Podcasts, Amazon Music
   - **Full Transcript**: Included (~5,000 words)
   - **Topics Covered**:
     - AI-Enhanced Interview Fraud with deepfakes
     - Package Reshipping/Processing Scams
     - Mystery Shopper Check Scams
     - Gamified Cryptocurrency Task Scams

2. **Blog Post: 4 Dangerous Job Scams Targeting Professionals in 2025**
   - **File**: `content/blog/dangerous-job-scams-2025-complete-guide.md`
   - **Date**: December 10, 2025
   - **Author**: Joe Patti
   - **Category**: Scam Awareness
   - **Featured**: Yes (first featured post)
   - **Related Episode**: episode-65
   - **Word Count**: ~5,800 words
   - **SEO Optimizations**:
     - Title: "4 Dangerous Job Scams Targeting Professionals in 2025: A Complete Guide" (71 chars)
     - SEO Title: "4 Dangerous Job Scams Targeting Professionals in 2025" (55 chars - optimized)
     - Description: "AI deepfakes, malware, and crypto scams are targeting job seekers. Learn to spot these 4 dangerous employment scams in 2025 and protect yourself." (158 chars - optimized)
   - **Content Sections**:
     1. AI-Enhanced Interview Fraud: The Deepfake Nightmare
     2. Packaging and Processing Scams: Becoming an Unwitting Accomplice
     3. Secret Shopper Check Scams: The Bounced Check Trap
     4. Gamified Task Scams: The Fastest-Growing Threat
     5. Conclusion: Universal Protection Measures
   - **Tags**: job-scams, employment-fraud, AI-deepfakes, cryptocurrency-scams, malware, interview-fraud, reshipping-scams, mystery-shopper-scams, career-safety, cybersecurity-awareness
   - **External Authority Links**: FTC, FBI IC3, VirusTotal, Better Business Bureau
   - **Schema Markup**: BlogPosting, BreadcrumbList, Open Graph, Twitter Cards

3. **Featured Posts Update**
   - **File**: `content/blog/when-nanoseconds-matter.md`
   - **Change**: Updated `featured: true` to `featured: false`
   - **Reason**: Made room for new job scams blog post as featured content on homepage

**SEO Optimizations Applied**:

| File | Field | Before | After | Reason |
|------|-------|--------|-------|--------|
| Episode 65 | description | 124 chars | 158 chars | Extended to optimal length for search snippets |
| Blog Post | seo_title | 69 chars | 55 chars | Shortened to prevent truncation in Google results |
| Blog Post | description | 124 chars | 158 chars | Extended to optimal length for better CTR |

**SEO Compliance Review Results**:
- Episode 65: 8.5/10 (excellent, minor description length improvement)
- Blog Post: 8/10 → 9/10 after optimizations (title length fixed, description extended)

**Cleanup Actions**:
- Removed temporary test files from `static/` directory:
  - `static/test-hero.html`
  - `static/test-hero-with-main.html`
  - `static/episode-number-options.html`
  - `static/css/main.css.backup`
- Static files reduced from 66 to 62 in production build

**Build Statistics**:
- Pages: 134
- Non-page files: 23
- Static files: 62
- Build time: 185ms
- Minified: Yes
- Production package: 7.9MB

**Files Modified for Production**:
- `content/episodes/episode-65-job-scams-are-getting-worse-four-of-the-most-dangerous.md` (created)
- `content/blog/dangerous-job-scams-2025-complete-guide.md` (created)
- `content/blog/when-nanoseconds-matter.md` (featured status removed)

**Production Deployment Ready**: ✅ `production-deployment-20251210-124818.zip`

---

### December 9, 2025 - UX Improvements: Card Interaction Patterns & Blog Page Fixes

**✅ CURRENT STATUS: UX CONSISTENCY IMPROVEMENTS IMPLEMENTED**

**Objective**: Standardize card interaction patterns across all pages following UX best practices, fix blog page layout issues, and update individual blog pages with Art Deco design.

**Key Changes**:

1. **Blog Page Column Layout Fix**
   - **Problem**: Blog cards displayed with inconsistent column widths and wasted space at various browser widths
   - **Root Cause**: CSS using `repeat(auto-fill, minmax(320px, 1fr))` created too many narrow columns
   - **Solution**: Changed to `repeat(auto-fit, minmax(min(100%, 400px), 1fr))`
   - **File**: `static/css/main.css` (lines 2377-2380)
   - **Result**: Cards now properly fill available space without awkward gaps

2. **Episode Card Hover Behavior Standardization**
   - **Problem**: Hero Latest Episode card had image zoom on hover; Recent Episodes cards didn't
   - **Reason**: Inconsistency creates confusing user experience
   - **Solution**: Removed image scale effect from hero card to match simpler hover behavior
   - **File**: `static/css/main.css` (lines 1739-1746)
   - **Result**: All episode cards now have consistent jump + outline + shadow behavior

3. **Entire Card Clickability Implementation** (UX Best Practice)
   - **Problem**: Cards showed hover effects but only "Listen Now"/"Read More" button was clickable (false affordance)
   - **Analysis**: Violates UX principles (Fitts's Law, Principle of Least Surprise)
   - **Industry Standard**: Material Design, Apple HIG, YouTube, Netflix all use fully clickable cards for single-action items
   - **Implementation**:
     - **Homepage** (`layouts/index.html`):
       - Lines 122-150: Wrapped hero latest episode card in `<a class="episode-card-link">`
       - Lines 175-194: Wrapped recent episodes cards in `<a class="episode-card-link">`
       - Lines 212-227: Wrapped featured blog cards in `<a class="blog-card-link">`
       - Changed nested `<a>` to `<span>` for "Listen Now" and "Read More"
     - **Blog Archive Page** (`layouts/blog/list.html`):
       - Lines 137-163: Wrapped blog cards in `<a class="blog-card-link">`
       - Changed `<a class="read-more-btn">` to `<span class="read-more-btn">`
     - **Episodes Archive Page** (`layouts/episodes/list.html`):
       - Lines 88-120: Wrapped episode cards in `<a class="episode-card-link">`
       - Removed platform buttons (YouTube, Spotify, etc.) to avoid nested links
       - Changed `<a class="listen-btn">` to `<span class="episode-cta">`
     - **CSS Updates** (`static/css/main.css`):
       - Lines 1004-1030: Added `.episode-card-link` wrapper styles with hover states
       - Lines 1492-1512: Added `.hero .episode-card-link` hover states
       - Lines 1721-1725: Added `.episode-card-link:hover .episode-card` for archive page
       - Lines 1862-1895: Added `.episode-cta` button styles with hover effects
       - Lines 2404-2450: Added `.blog-card-link` wrapper styles with hover states
   - **Result**: Entire cards now clickable, matching user expectations and industry standards

4. **Featured Blog Posts Styling Fix**
   - **Problem**: After making cards clickable, "Read More" lost styling and margins disappeared
   - **Root Cause**: Used `.episode-cta` class which didn't exist in CSS; missing `.blog-content` wrapper
   - **Solution**:
     - Changed class from `episode-cta` to `read-more-btn` (line 223)
     - Added `.blog-content` wrapper div (lines 214-225)
   - **File**: `layouts/index.html`
   - **Result**: Proper button styling and internal padding restored

5. **Blog Single Pages Art Deco Update**
   - **Problem**: Individual blog pages still using old blue color scheme
   - **Solution**: Updated all color references to Art Deco palette
   - **File**: `layouts/blog/single.html`
   - **Changes**:
     - Line 81: Hero gradient changed to `linear-gradient(135deg, var(--navy) 0%, #3A6199 100%)`
     - Line 126: Description callout - teal border, cream background
     - Line 135: Related episode component - teal accents, cream gradient
     - Line 188: Newsletter card - replaced inline blue styles with `.newsletter-card` class (proper red gradient)
     - Line 166: Tags section - updated to teal color
     - Lines 238-325: Article content styling - navy-dark headings, teal blockquotes, cream code blocks
   - **Result**: Blog single pages now match Art Deco design system

**Files Modified**:
- `layouts/index.html` - Homepage card clickability
- `layouts/blog/list.html` - Blog archive card clickability
- `layouts/blog/single.html` - Art Deco color updates
- `layouts/episodes/list.html` - Episodes archive card clickability
- `static/css/main.css` - Card wrapper styles, hover states, button styles, grid fixes

**UX Improvements Summary**:
- ✅ Consistent card interaction patterns across all pages
- ✅ Entire cards clickable (following industry best practices)
- ✅ Standardized hover behavior (jump + outline + shadow)
- ✅ Removed false affordances
- ✅ Better adherence to Fitts's Law (larger click targets)
- ✅ Blog page layout properly responsive
- ✅ Art Deco design consistently applied to all blog pages

**Testing Status**:
- ✅ Homepage episode cards: Clickable with proper hover
- ✅ Homepage blog cards: Clickable with proper hover
- ✅ Blog archive page: Clickable with proper hover
- ✅ Episodes archive page: Clickable with proper hover
- ✅ Blog single pages: Art Deco styling applied
- ✅ Newsletter card visibility: Fixed on blog single pages
- ✅ All pages render correctly at various viewport widths

---

### December 9, 2025 - Design Specification Documentation Updated to v1.3

**✅ CURRENT STATUS: DESIGN DOCUMENTATION SYNCHRONIZED WITH ART DECO REDESIGN**

**Documentation Updates**: All design specifications updated to reflect the Art Deco redesign work completed in December 2025.

**Files Created**:

1. **docs/design_specs/sch_design_spec_v1_3.md** (NEW - 2333 lines)
   - Comprehensive master design system specification documenting Art Deco redesign
   - Complete color palette section (Art Deco: Red #D74444, Navy #2B4D7D, Teal #4A9B9B, Cream #F5F1E8)
   - Extended palette documented (Red Dark, Navy Light/Dark, Teal Light, Cream Dark, Silver)
   - Complete typography section (Google Fonts: Oswald 600/700, PT Serif 400/700, Bebas Neue 400)
   - Typography scale with responsive clamp() values
   - Detailed Art Deco hero section design specifications
   - Art deco pattern CSS implementation
   - Episode badge positioning fix documentation (floating effect)
   - "Recent Implementation Fixes" section documenting December 8, 2025 fixes

**Files Updated**:

2. **docs/design_specs/blog_page_spec.md** (v1.1 → v1.2)
   - Updated header: version to 1.2, date to December 9, 2025
   - Updated parent design system reference to v1.3
   - Section 8.1 Colors: Complete Art Deco palette with gradient documentation
   - Section 8.2 Typography: Complete Google Fonts documentation
   - Added version history section

3. **docs/design_specs/partnership_page_spec.md** (v1.0 → v1.1)
   - Updated header: version to 1.1, date to December 9, 2025
   - Added parent design system reference to v1.3
   - Section 8 Color Reference: Complete Art Deco palette with gradients
   - Added "Partnership Page Usage" subsection documenting color application
   - Section 9 Typography Reference: Complete Google Fonts documentation with usage examples
   - Section 10: Updated reference from v1.2 to v1.3
   - Added version history section

4. **docs/README.md** (Documentation Index)
   - Updated "Last Updated" date to December 9, 2025
   - Updated master design system reference: v1.2 → v1.3 (line 55)
   - Added Art Deco details to design system description
   - Updated file organization tree with version numbers (line 138)
   - Updated quick reference section (line 190, 194)
   - Added deprecation warnings for old color palette files (lines 91-92)

5. **docs/color palette 2025-10-08.md** (DEPRECATED)
   - Added prominent deprecation notice at top of file
   - Documented deprecation date: December 9, 2025
   - Added reference to current Art Deco palette in v1.3
   - Listed current Art Deco colors for quick reference
   - Preserved original content as "Historical Reference: Original Color Palette (October 2025)"

**Version Summary**:
- Master Design Spec: v1.2 → **v1.3** (Art Deco)
- Blog Page Spec: v1.1 → **v1.2**
- Partnership Page Spec: v1.0 → **v1.1**
- Color Palette (October 2025): **DEPRECATED** (replaced by Art Deco palette in v1.3)

**Git Commit**:
- Commit: 29aa6c4 - "Update design specifications to v1.3 documenting Art Deco redesign"
- Files changed: 5 files, 2487 insertions(+), 63 deletions(-)
- Status: ✅ Committed and pushed to GitHub

**Documentation Status**:
- ✅ All design specifications synchronized with Art Deco implementation
- ✅ Color palette fully documented (primary + extended colors)
- ✅ Typography system fully documented (3 Google Fonts with weights)
- ✅ All gradient patterns documented (135deg diagonal)
- ✅ Recent fixes documented in v1.3
- ✅ Old color palette deprecated with migration path
- ✅ All cross-references updated to v1.3

---

### December 8, 2025 - Homepage Hero Redesign Implementation (COMPLETE)

**✅ CURRENT STATUS: SUCCESSFULLY IMPLEMENTED**

**Goal**: Implement the art deco hero redesign from mockup to live site

**Branch**: `hero-redesign`

**Implementation Summary**: Successfully implemented the premium art deco hero redesign using Playwright MCP tools for browser-based debugging. All layout issues resolved through targeted CSS fixes.

**Files Modified**:
1. **layouts/_default/baseof.html** (lines 27-30)
   - Added Google Fonts preconnect and stylesheet
   - Fonts: Oswald (600/700), PT Serif (400/700), Bebas Neue

2. **layouts/index.html** (completely rewritten - 379 lines)
   - Bypassed Hugo's base template inheritance
   - Created standalone HTML document with full `<head>` and `<body>`
   - Includes all metadata, analytics, schema markup from baseof.html
   - Hero section HTML structure matches working mockup exactly
   - Added cache-busting parameter to CSS: `?v={{ now.Unix }}`
   - Preserves all dynamic Hugo content (episodes, blog posts, etc.)

3. **static/css/main.css** (multiple additions and fixes)
   - Added art deco CSS variables (lines 6-72): colors, fonts, spacing
   - Updated button styles with art deco design (lines 274-365)
   - Added extensive hero section CSS (lines 638-877)
   - **Key Fixes Applied**:
     - **Line 724**: Changed grid columns from `55% 45%` to `1.1fr 0.9fr` (CRITICAL FIX - percentage columns don't account for gap)
     - **Line 733**: Changed `.hero .hero-grid > *` overflow from `hidden !important` to `visible !important` (allows badge to extend beyond card)
     - **Line 1483**: Changed `.hero .episode-card` overflow from `hidden` to `visible`
     - **Line 1495**: Added `max-width: 100%` to episode image and `border-radius: 8px 8px 0 0`
     - **Line 1513-1514**: Repositioned badge with `top: -1rem; right: -1rem` for floating effect
     - **Line 1190-1191**: Added `margin-left: auto; margin-right: auto` to `.newsletter-section p` (centers paragraphs with max-width constraint)
     - **Line 1198**: Added `align-items: center` to `.newsletter-form` (vertical alignment)
     - **Line 1201**: Increased specificity from `.newsletter-input` to `input.newsletter-input` (overrides general input styles)

**Issues Resolved**:

1. **Grid Overflow Problem** (80px overflow)
   - Root Cause: Percentage-based grid columns (55% + 45% = 100%) don't account for 80px gap
   - Fix: Changed to fractional units `1.1fr 0.9fr` which properly distribute space after gap
   - File: static/css/main.css (line 724)

2. **Episode Badge Clipping**
   - Root Cause: Multiple overflow constraints at different levels (card, wrapper, grid children)
   - Fix: Changed overflow from `hidden` to `visible` on all three levels, with !important rule on grid children being the key fix
   - Files: static/css/main.css (lines 733, 1483, 1524)
   - Badge Position: `top: -1rem; right: -1rem` for floating effect extending beyond card boundaries

3. **Newsletter Input/Button Misalignment**
   - Root Cause 1: Missing `align-items: center` on flex container
   - Root Cause 2: General `input[type="email"]` selector overriding newsletter input padding
   - Fix 1: Added `align-items: center` to `.newsletter-form`
   - Fix 2: Increased specificity to `input.newsletter-input` to override general input styles
   - Files: static/css/main.css (lines 1198, 1201)

4. **Newsletter Text Not Centered**
   - Root Cause: Global `p` selector applies `max-width: 70ch` but paragraphs lacked auto margins
   - Fix: Added `margin-left: auto; margin-right: auto` to `.newsletter-section p`
   - File: static/css/main.css (lines 1190-1191)

**Debugging Approach**:
- Used Playwright MCP browser automation for live debugging
- Inspected computed styles and bounding boxes to identify root causes
- Applied targeted CSS fixes based on browser inspection data
- Verified fixes visually with screenshots

**Results**:
- ✅ Hero section grid layout correct (no overflow)
- ✅ Episode badge positioned correctly (floating at upper-right)
- ✅ Newsletter form elements vertically aligned
- ✅ Newsletter text properly centered
- ✅ All responsive behavior maintained
- ✅ Design matches approved mockup

**Git Status**:
- Branch: `hero-redesign`
- Modified: CLAUDE.md, layouts/index.html, layouts/_default/baseof.html, static/css/main.css

**Hugo Server**: Running on http://localhost:1313/

---

### Episode 7 Display Problem (RESOLVED - October 13, 2025)
- **Issue**: Episode 7 description was not truncating on homepage/episode list
- **Root Cause**: Episode 7's description (104 chars) was shorter than the 120-char truncation limit, plus templates were using Hugo's auto-generated `.Summary` instead of explicit `.Params.description`
- **Fix**: Changed templates to use `.Params.description` (from front matter) instead of `.Summary`
- **Files Changed**:
  - `layouts/episodes/list.html:64`
  - `layouts/index.html:52,85`
  - `layouts/episodes/single.html:161-162`

### Absolute URL Problem (RESOLVED - October 13, 2025)
- **Issue**: Internal navigation links used `.Permalink` (absolute URLs with production domain), causing 404s on staging
- **Fix**: Changed internal navigation to `.RelPermalink` (relative URLs) while keeping absolute URLs for SEO/social sharing
- **Result**: Site now works on any domain (staging, production, localhost)

### Placeholder Content (RESOLVED - October 13, 2025)
- **Issue**: 55 episode pages had placeholder sections for "Key Takeaways" and "Resources Mentioned"
- **Fix**: Removed all placeholder sections using batch script
- **Preserved**: 4 episodes with actual Key Takeaways content (episodes 53, 59, 60, 61)
- **Result**: 715 lines of placeholder content removed

### Newsletter Integration (COMPLETED - October 14, 2025)
- **Task**: Integrate Mailchimp newsletter subscription functionality
- **Implementation**: Updated all newsletter forms across the site with Mailchimp form action URL
- **Locations Updated**:
  - Homepage newsletter section ([layouts/index.html:132](layouts/index.html#L132))
  - Footer newsletter form ([layouts/partials/footer.html:39](layouts/partials/footer.html#L39))
  - Episode page sidebar ([layouts/episodes/single.html:140](layouts/episodes/single.html#L140))
  - About page ([layouts/_default/about.html:161](layouts/_default/about.html#L161))
  - Resources page ([layouts/_default/resources.html:204](layouts/_default/resources.html#L204))
- **Features Added**:
  - Mailchimp form action with audience ID
  - Honeypot field for bot protection
  - Forms open in new tab for confirmation
  - Email field name changed to "EMAIL" (Mailchimp standard)
- **Result**: All newsletter forms now fully functional with Mailchimp
- **Note**: Footer newsletter form later removed per user request (newsletter should only be on specific pages)

### Contact Form Integration (COMPLETED - October 14, 2025)
- **Task**: Integrate Formspree for contact form submissions
- **Implementation**: Updated contact form with Formspree endpoint and AJAX submission handler
- **Location**: Contact page ([layouts/_default/contact.html:22](layouts/_default/contact.html#L22))
- **Features Added**:
  - Formspree form action (https://formspree.io/f/mrbyrgrv)
  - AJAX submission with fetch API
  - Real-time success/error messages displayed on page
  - Loading state ("Sending...") during submission
  - Form stays on same page (no redirect)
  - Proper error handling with user-friendly messages
  - Fallback message with direct email if submission fails
- **Form Fields**: Name, Email, Subject (dropdown with 6 options), Message
- **Result**: Contact form fully functional with professional UX

### Google Analytics Integration (COMPLETED - October 14, 2025)
- **Task**: Add GA4 tracking to all pages
- **Implementation**: Added Google Analytics script to baseof.html template
- **Measurement ID**: G-8QL8F8JKNR
- **Location**: [layouts/_default/baseof.html](layouts/_default/baseof.html) in <head> section
- **Result**: All pages tracked with GA4

### Legal Pages (COMPLETED - October 14, 2025)
- **Task**: Create Privacy Policy and Terms of Service pages
- **Implementation**: Created comprehensive legal pages
- **Files**:
  - [content/privacy.md](content/privacy.md) - GDPR/CCPA compliant privacy policy
  - [content/terms.md](content/terms.md) - Complete terms of service (Governing law: New Jersey)
- **Result**: Legal pages accessible via footer links

### Cookie Consent Banner (COMPLETED - October 14, 2025)
- **Task**: Add GDPR-compliant cookie consent banner
- **Implementation**: Added consent banner to baseof.html
- **Location**: [layouts/_default/baseof.html](layouts/_default/baseof.html)
- **Features**:
  - Accept/Decline buttons
  - Integrates with Google Analytics (enables/disables tracking based on choice)
  - Stores user choice in cookie for 365 days
  - Links to Privacy Policy
- **Result**: GDPR-compliant cookie consent implemented

### Production Deployment (COMPLETED - October 15, 2025)
- **Task**: Deploy to GoDaddy cPanel hosting
- **Implementation**: Created production-deployment.zip with complete built site
- **Deployment Method**: Manual upload via cPanel File Manager
- **Documentation**: [GODADDY-DEPLOYMENT-INSTRUCTIONS.md](GODADDY-DEPLOYMENT-INSTRUCTIONS.md)
- **Domain**: securitycocktailhour.com (with SSL)
- **Result**: Site deployed and tested on production, awaiting DNS cutover

### Episode 41 Date Bug (FIXED - October 15, 2025)
- **Issue**: Episode 41 showing as latest episode instead of Episode 61
- **Root Cause**: Episode 41 had date `2025-10-15` (today) instead of actual publication date
- **Fix**: Updated date to `2024-10-15` (correct year)
- **File**: [content/episodes/episode-41-everybody-makes-mistakes-including-cybersecurity-pros.md](content/episodes/episode-41-everybody-makes-mistakes-including-cybersecurity-pros.md)
- **Result**: Episode 61 now correctly displays as latest episode

### Image Optimization - Episodes 1-13 (COMPLETED - October 15, 2025)
- **Task**: Reduce page load time for episode images
- **Implementation**: Created single shared optimized image for episodes 1-13
- **File**: episode-001-013.png (300x300px, 35KB, reduced from 2.7MB per image)
- **Updates**: Updated episodes 01-13 to reference shared image
- **Savings**: ~32MB reduction in total page load

### Image Optimization - PNG to JPG Conversion (COMPLETED - October 15, 2025)
- **Task**: Further reduce page load time by converting large PNG files to JPG
- **Implementation**: Converted 27 episode PNGs to optimized JPG format
- **Episodes Converted**: 18, 20, 24, 32, 36-46, 48-50, 52, 54-55, 57-61
- **Original Size Range**: 217KB to 1.2MB per PNG
- **Optimized Size**: Significantly smaller JPG files
- **Total Reduction**: Site deployment size reduced from 49MB to 7.7MB (84% reduction!)
- **Result**: Episodes page and About page load virtually instantly

### Episode 43 Image Reference Bug (FIXED - October 15, 2025)
- **Issue**: Episode 43 image not displaying on production
- **Root Cause**: Markdown file still referenced .png instead of .jpg
- **Fix**: Updated image reference from episode-043.png to episode-043.jpg
- **File**: [content/episodes/episode-43-cybersecurity-for-emts-and-first-responders-protecting-patients-and-professional.md:8](content/episodes/episode-43-cybersecurity-for-emts-and-first-responders-protecting-patients-and-professional.md#L8)
- **Result**: Episode 43 image now displays correctly

### Mobile Hamburger Menu Fix (FIXED - October 15, 2025)
- **Issue**: Hamburger menu on iPhone/mobile devices did not respond to taps
- **Root Cause**: JavaScript existed but CSS was missing for `.site-nav.active` state
- **Fix Applied**:
  - Added JavaScript to toggle menu visibility ([layouts/_default/baseof.html](layouts/_default/baseof.html))
  - Added CSS for `.site-nav.active` to display mobile menu ([static/css/main.css](static/css/main.css))
  - Menu appears as fixed dropdown below header with proper styling
  - Click handlers to close menu when tapping outside or on nav links
  - Accessibility improvements with aria-expanded attribute
- **Files Changed**:
  - [layouts/_default/baseof.html](layouts/_default/baseof.html) - Added mobile menu toggle JavaScript
  - [layouts/partials/header.html](layouts/partials/header.html) - Added aria-expanded attribute
  - [static/css/main.css](static/css/main.css) - Added mobile menu CSS styles
- **Result**: Mobile hamburger menu now fully functional on all mobile devices including iPhone/iPad
- **Deployed**: Tested on staging, deployed to production successfully

### Episodes Page Category Filter Fix (FIXED - October 21, 2025)
- **Issue**: Category filter dropdown only showed "All Topics" with no other options
- **Root Cause**: Template was trying to use Hugo's taxonomy system (`.Site.Taxonomies.categories`), but episodes use singular `category` field in front matter
- **Fix**: Updated template to collect categories directly from episode pages and display alphabetically
- **File Changed**: [layouts/episodes/list.html:26-37](layouts/episodes/list.html#L26-L37)
- **Result**: Dropdown now shows all 16 categories: AI, Career, Career Bio, Cryptocurrency Security, Educational, General, Hardware Security, Identity, Incident Response, Legal, Operational Technology (OT), Sales, Small Business, Threat Intel, Unboxing, Users
- **Deployed**: Pushed to GitHub/Netlify staging, production package updated

### SEO Optimization for Cybersecurity Podcast Keywords (COMPLETED - October 21, 2025)
- **Task**: Optimize site for target keywords "cybersecurity podcast" and "data breach prevention"
- **Implementation**: Phase 1 SEO improvements across key pages
- **Changes Made**:
  1. **Homepage Meta Optimization**:
     - Title: "Cybersecurity Podcast | Security Cocktail Hour - Expert Interviews & Insights"
     - Description: 160-char description including target keywords
     - File: [content/_index.md](content/_index.md)
  2. **Episodes Page Meta Optimization**:
     - Title: "Cybersecurity Podcast Episodes | Security Cocktail Hour"
     - Description: Mentions data breach prevention, AI security, incident response
     - Files: [content/episodes/_index.md](content/episodes/_index.md), [layouts/episodes/list.html:1](layouts/episodes/list.html#L1)
  3. **About Page Meta Optimization**:
     - Title: "About the Cybersecurity Podcast | Security Cocktail Hour"
     - Description: Emphasizes podcast format and practitioner interviews
     - File: [content/about.md](content/about.md)
  4. **PodcastSeries Schema Markup**:
     - Added structured data to homepage for search engines
     - Includes podcast name, description, authors, RSS feed
     - File: [layouts/index.html:1-23](layouts/index.html#L1-L23)
  5. **Title Logic Fix**:
     - Prevented duplicate site title appending on SEO-optimized pages
     - File: [layouts/_default/baseof.html:8](layouts/_default/baseof.html#L8)
- **Keyword Coverage**:
  - "cybersecurity podcast" now in all page titles, descriptions, and schema markup
  - "data breach prevention" in homepage/episodes descriptions and schema
- **Expected Impact**:
  - Improved search visibility for cybersecurity podcast queries
  - Better click-through rates from enhanced meta descriptions
  - Google properly categorizes site as podcast
  - Foundation for podcast-related search ranking
- **Deployed**: Pushed to GitHub/Netlify staging, production package updated (7.7MB)

### Episode 62 Updates (November 2-3, 2025)

**November 2, 2025 - Added Episode 62:**
- Added Episode 62: "AI in Cybersecurity: How CISOs Are Actually Using LLMs with Myke Lyons"
- Fixed homepage template to show only description for latest episode (no timestamps/topics)
- Standardized episode format documentation (bulleted timestamps and topics)
- Created NEW-EPISODE-DEPLOYMENT.md with complete deployment workflow
- Updated CLAUDE.md with episode content structure

**November 3, 2025 - Episode 62 Fixes:**
- Updated Episode 62 platform URLs (Apple and Amazon episode-specific links)
- Fixed Episode 62 visibility issue - rebuilt site to make episode appear on production
- Episode 62 now live and visible on https://securitycocktailhour.com/
- All platform links functional (YouTube, Spotify, Apple, Amazon)

### Design Specification Update (November 6, 2025)
1. Updated Design Specification to v1.1 with current color palette
2. Verified color palette consistency across documentation files:
   - docs/color palette 2025-10-08.png (correct)
   - docs/color palette 2025-10-08.md (correct)
   - docs/sch_design_spec_v1.1.md (NOW UPDATED - was outdated)
3. Replaced outdated color scheme in design spec:
   - OLD: Security Red (#C8534B), Deep Security Blue (#1E4D8B), Spotlight Cyan (#3BA0D4), etc.
   - NEW: Primary (#192A56), Secondary (#8D99AE), Action (#436098), Accent (#CE1F2C), Background (#F8F9FA)
4. Updated all color references throughout design spec document (35+ locations)
5. Renamed design spec file: sch_design_spec.md → sch_design_spec_v1.1.md
6. Design specification now matches production site colors (October 8, 2025 palette)

### Partnership Page Implementation (November 8, 2025)

**1. Added Partnership/Sponsorship Page**
   - Created new Partnership page with three sponsorship tiers ($500, $1,000, $2,500)
   - Includes podcast metrics (44K views, 81K impressions, 407 subscribers)
   - Features audience demographics and "Why Support" benefits section
   - All "Learn More" buttons link to Contact page
   - Added to main navigation between Resources and Contact
   - Files: `content/partnership.md`, `layouts/_default/partnership.html`
   - Design spec: `docs/partnership page/partnership_page_spec.md`

**2. Updated Contact Page**
   - Added LinkedIn link to Social Media section
   - LinkedIn appears above Twitter/X link
   - URL: https://www.linkedin.com/company/security-cocktail-hour/
   - File: `layouts/_default/contact.html:77`

**3. Navigation Menu Update**
   - Added "Partnership" link to main navigation
   - Positioned between Resources (weight 30) and Contact (weight 40)
   - Weight: 35 for proper ordering
   - File: `hugo.toml:27-29`

**4. Color Consistency Fix**
   - Corrected Partnership page hero and CTA sections to use standard site gradient
   - Changed from: `#192A56 to #436098` (darker)
   - Changed to: `#436098 to #6A8CC7` (standard Action Blue gradient)
   - Updated design spec to reflect correct gradient

**5. Production Build**
   - Built with `hugo --minify`
   - Total pages: 76 (up from 75)
   - Build time: 132ms
   - All pages validated and minified

**6. Footer Navigation Update**
   - Added Partnership link to footer "About" section
   - Positioned between Contact and Resources for consistency
   - Link appears on all pages site-wide
   - File: `layouts/partials/footer.html:22`

**7. Production Deployment**
   - First deployment: Partnership page without footer link (deployed successfully)
   - Second deployment: Added footer Partnership link (deployed successfully)
   - All Partnership page features live and accessible
   - Site URL: https://securitycocktailhour.com/partnership

**8. Design Specification Documentation**
   - Created new `docs/design_specs/` folder for centralized design documentation
   - Master design spec: `sch_design_spec_v1_2.md` (1,474 lines, updated from v1.1)
   - Page-specific spec: `partnership_page_spec.md` (693 lines)
   - Updated gradient documentation with all three production gradients:
     - Professional Blue gradient (primary - general use)
     - Dark Blue gradient (emphasis - featured items)
     - Red gradient (premium - accent items)
   - Both documents cross-reference each other
   - Partnership spec references master design system v1.2
   - Master spec lists Partnership as "Implemented & Deployed"
   - Documentation matches production implementation

### Episode 51 Content Enhancement (November 12, 2025)

**1. Episode 51 Content Enhancement**
   - Added comprehensive "Episode Highlights" section with bullet-point summary
   - Added "Shadow AI" thought leadership content section
   - Added complete 56-minute formatted transcript with timestamps and section headers
   - Transcript formatted with bold timestamps and H3 section headers for readability
   - All content properly formatted in markdown with line breaks
   - File: `content/episodes/episode-51-agentic-ai-security-full-speed-into-the-unknown.md`
   - Source files: `temp/shadow ai post.txt`, `temp/transcript-ep-051.txt`

**2. Production Build & Deployment**
   - Built site with `hugo --minify` (161ms build time)
   - Created production-deployment.zip (7.8MB)
   - Deployed to GoDaddy cPanel successfully
   - Episode 51 live at: https://securitycocktailhour.com/episodes/episode-51-agentic-ai-security-full-speed-into-the-unknown/

---

## Data Migration History

### CSV to Markdown Conversion

Created `convert_episodes.py` to batch convert 7 CSV files to Hugo markdown format.

**Challenges Solved:**
- YAML parsing errors with quotes → Used YAML block scalar syntax (`description: >-`)
- Long filenames → Truncated slugs to 80 characters
- All 64 episodes successfully converted

### Episode-Specific Fixes

**Episode 46**: Title/description swapped in CSV
- Corrected title: "Securing AI: Misbehavior Even the Experts Couldn't Predict"
- Guest: "Alec Crawford" (was "Alec Crawfrord")
- Renamed file to match corrected title

**Episodes 1-10**: CSV had empty title column, guest field contained actual title
- Removed "Episode X:" prefix from titles
- Cleared guest and guest_bio fields for episodes without guests
- Fixed with batch sed commands

**Episode 8**: Guest field incorrect
- Changed from "Small Business Security" to "Sal Toner"

**Episode 31**: Image reference was empty despite image existing
- Updated to: `image: "/images/episodes/episode-031.jpg"`

---

## Design System Details

### Typography

**Font Stack:**
```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

**Scale:**
- H1: 2.5rem (40px) desktop, 2rem (32px) mobile
- H2: 2rem (32px) desktop, 1.75rem (28px) mobile
- H3: 1.5rem (24px) desktop, 1.375rem (22px) mobile
- H4: 1.25rem (20px)
- Body: 1rem (16px)
- Small: 0.875rem (14px)

### Spacing System (8px base)

```css
--space-xs: 0.25rem;   /* 4px */
--space-sm: 0.5rem;    /* 8px */
--space-md: 1rem;      /* 16px */
--space-lg: 1.5rem;    /* 24px */
--space-xl: 2rem;      /* 32px */
--space-2xl: 3rem;     /* 48px */
--space-3xl: 4rem;     /* 64px */
```

### Border Radius

```css
--radius-sm: 4px;   /* Tags, badges */
--radius-md: 8px;   /* Cards, buttons, inputs */
--radius-lg: 12px;  /* Large cards, modals */
```

### Shadows

```css
--shadow-light: 0 2px 8px rgba(0, 0, 0, 0.1);
--shadow-medium: 0 4px 16px rgba(0, 0, 0, 0.12);
--shadow-strong: 0 8px 24px rgba(0, 0, 0, 0.15);
```

### Responsive Breakpoints

```
Mobile (Portrait):        0px - 599px
Mobile (Landscape):       600px - 899px
Tablet:                   900px - 1199px
Desktop:                  1200px+
```

---

## Color Palette Evolution

### Current Palette (October 8, 2025)

```
Primary (Dark Blue):      #192A56  - Main text, navigation, footers, headings
Secondary (Cool Grey):    #8D99AE  - Category tags, secondary text, borders
Background (Off-white):   #F8F9FA  - Main page background
Action (Professional Blue): #436098  - Most buttons, CTAs, gradients
Accent (Bright Red):      #CE1F2C  - "Listen Now" button only
```

### Previous Color Schemes

**Attempt 1** (rejected):
- Charcoal (#333333)
- Deep Teal (#004D40)
- Warm Cream (#FEFBF3)
- Cranberry (#AF3F47)
- Gold (#E5B800)

**Original**:
- Security Red (#C8534B)
- Deep Security Blue (#1E4D8B)
- Spotlight Cyan (#3BA0D4)
- Eco Green (#7BA956)

Backup of previous palette available in `static/css/main.css.backup`.

---

## Troubleshooting Guide

### Common Issues

**"Page Not Found" Errors on GoDaddy**

Add `.htaccess` to web root:
```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ /$1/ [L]
```

**Images Not Loading**

Check:
- Image paths are correct (case-sensitive)
- Images exist in `public/images/`
- File permissions (644 for files, 755 for directories)

**Hugo Server Not Updating**

- Check Hugo server is running
- Hard refresh browser (Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows)
- Restart Hugo server if needed

**Forms Not Submitting**

- Verify form `action` points to correct endpoint
- Check `method="POST"`
- Test with valid email address
- Check service dashboard (Formspree, Mailchimp)

**Netlify Build Failing**

- Check Netlify dashboard for build logs
- Verify Hugo version in `netlify.toml` matches local
- Check for syntax errors in templates
- Verify all file paths are correct

---

## Deployment Details

### Key Features Implementation

#### 1. Episode Number Display

Episode numbers extracted from filenames and displayed as badges:

```html
{{ with .File }}
  {{ $filename := .BaseFileName }}
  {{ if strings.HasPrefix $filename "episode-" }}
    {{ $parts := split $filename "-" }}
    {{ $epNum := index $parts 1 }}
    <span class="category-tag">Episode {{ $epNum }}</span>
  {{ end }}
{{ end }}
```

Location: `layouts/episodes/single.html`

#### 2. Missing Image Handling

Episodes without images display gradient placeholders:

```html
{{ with .Params.image }}
  <img src="{{ . | relURL }}" alt="{{ $.Title }}" class="card-image"
       onerror="this.style.display='none'; this.nextElementSibling.style.display='block';">
  <div class="card-image" style="background: linear-gradient(135deg, #436098 0%, #6A8CC7 100%); display: none;"></div>
{{ else }}
  <div class="card-image" style="background: linear-gradient(135deg, #436098 0%, #6A8CC7 100%);"></div>
{{ end }}
```

#### 3. Search and Filter

Client-side JavaScript on episode list page:
- Text search across title, description, guest
- Category filter dropdown
- Date sorting (newest/oldest)

Location: `layouts/episodes/list.html`

#### 4. SEO Optimization

- Open Graph meta tags for social sharing
- Schema.org PodcastEpisode markup on individual episodes
- Descriptive page titles and meta descriptions
- Semantic HTML structure

#### 5. Relative vs Absolute URLs

**Internal Navigation** (uses `.RelPermalink`):
- Episode list "Listen Now" buttons
- Homepage episode cards
- Related episodes links
- Navigation menu links

**SEO/Social Sharing** (uses `.Permalink`):
- Open Graph `og:url` tags
- Canonical links
- Schema.org JSON-LD
- Social share buttons (Twitter, LinkedIn, Email)

This ensures the site works on any domain (staging, production, localhost) while maintaining proper SEO.

### Hugo Configuration Reference

#### hugo.toml Key Settings

```toml
baseURL = 'https://securitycocktailhour.com/'
languageCode = 'en-us'
title = 'Security Cocktail Hour Podcast'

[params]
  description = "Cybersecurity pros talking shop at the virtual bar."
  author = "Joe Patti and Adam Roth"

[menu]
  [[menu.main]]
    name = 'Episodes'
    pageRef = '/episodes'
    weight = 10
  [[menu.main]]
    name = 'About'
    pageRef = '/about'
    weight = 20
  [[menu.main]]
    name = 'Resources'
    pageRef = '/resources'
    weight = 30
  [[menu.main]]
    name = 'Contact'
    pageRef = '/contact'
    weight = 40

[taxonomies]
  category = 'categories'
  tag = 'tags'

[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true
```

### What to Upload to GoDaddy

Upload **only** the contents of the `public/` directory to your web root:

```
public/
├── index.html
├── episodes/
├── about/
├── contact/
├── resources/
├── css/
├── images/
├── sitemap.xml
└── robots.txt
```

**What NOT to Upload:**
- `content/` directory (source markdown)
- `layouts/` directory (Hugo templates)
- `static/` directory (pre-build assets)
- `hugo.toml` (configuration)
- `docs/` directory
- `.git/` directory
- `netlify.toml` (Netlify-specific)

### Rollback Procedure

If a deployment breaks something:

1. **Via Netlify Dashboard**:
   - Go to https://app.netlify.com/
   - Click "Deploys" tab
   - Find the last good deployment
   - Click "Publish deploy" to roll back

2. **Via Git**:
   ```bash
   # View recent commits
   git log --oneline -10

   # Revert to previous commit (creates new commit)
   git revert HEAD
   git push

   # Or reset to specific commit (rewrite history - use with caution)
   git reset --hard <commit-hash>
   git push --force
   ```

---

## Git Best Practices

- Always test changes locally before pushing
- Write descriptive commit messages
- Commit related changes together
- Push to GitHub when ready to deploy to staging
- Don't push broken code (test first!)

---

## Third-Party Integrations Reference

### Newsletter Subscription - Mailchimp

**Status**: Implemented and fully functional

**Locations**:
- Homepage newsletter section
- Episode page sidebar
- About page
- Resources page

**Features**:
- Mailchimp form action with audience ID
- Honeypot field for bot protection
- Forms open in new tab for confirmation
- Email field name: "EMAIL" (Mailchimp standard)

### Contact Form - Formspree

**Status**: Implemented and fully functional

**Endpoint**: https://formspree.io/f/mrbyrgrv

**Features**:
- AJAX submission with fetch API
- Real-time success/error messages
- Loading state during submission
- No page redirect
- Proper error handling
- Fallback to direct email if submission fails

**Form Fields**: Name, Email, Subject (dropdown), Message

### Google Analytics

**Measurement ID**: G-8QL8F8JKNR

**Implementation**: Added to `layouts/_default/baseof.html` in `<head>` section

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-8QL8F8JKNR"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-8QL8F8JKNR');
</script>
```

**Tracks**: All pages across the site

### Cookie Consent Banner

**Status**: GDPR-compliant implementation

**Features**:
- Accept/Decline buttons
- Integrates with Google Analytics (enables/disables tracking)
- User choice stored for 365 days
- Links to Privacy Policy

---

### Episode 53 Content Enhancement (November 12, 2025)

**1. Episode 53 Content Enhancement**
   - Added comprehensive "Episode Highlights" section with bullet-point summary
   - Added complete formatted transcript with timestamps and section headers
   - Transcript formatted with bold timestamps and H3 section headers for readability
   - All content properly formatted in markdown with line breaks
   - File: `content/episodes/episode-53-the-new-rules-of-cyber-incident-response-new-attacks-new-response.md`

### November 28, 2025 - SEO Title Tag Optimization Complete
- **Implemented dual-title system** for search engines
  - `title`: Full title for Schema.org, RSS feeds, page display
  - `seo_title`: Shortened version (≤60 chars) for search engine `<title>` tag
- **Optimized 17 episode pages**: Episodes 17, 29, 37, 39, 40, 42, 43, 47, 48, 49, 50, 53, 55, 60, 61, 62, 63
- **Created comprehensive documentation**: `docs/SEO-TITLE-TAG-STANDARDS.md`
- **Updated templates**: Episodes use `seo_title` if available, fallback to `title`
- **Commits**: 8c26e4d, 9f4172e, 8fdc3ab
- **Status**: Complete - All episode pages have optimal title tags for search engines

### November 28, 2025 - About Page Meta Description & URL Generation Fix
- **Fixed**: About page meta description exceeded 155 char limit (was 197 chars)
- **New**: "Meet Joe Patti and Adam Roth, the cybersecurity pros behind Security Cocktail Hour podcast. Real conversations about security challenges." (143 chars)
- **Fixed**: URL generation filter `urlize` compatibility issue
- **Solution**: Used `anchorize` filter (Hugo-native) instead
- **Commit**: a80e2f5 - "Fix About page meta description and URL generation"
- **Status**: ✅ All pages now 100% compliant with SEO standards

### November 28, 2025 - Trailing Slash SEO Fix Implemented
- **Issue**: Pages accessible with/without trailing slash (duplicate content for SEO)
- **Solution**: Added .htaccess rules to enforce trailing slashes with 301 redirects
- **File**: `static/.htaccess` - Apache rules for GoDaddy cPanel
- **Commit**: e73d5e9 - "Implement trailing slash SEO fix"
- **Status**: ✅ Enforced on production, prevents duplicate content issues

### November 28, 2025 - SEO Audit Complete + Documentation Cleanup
- **Documentation Reorganization**:
  - Moved SEO-related docs to `docs/` for better organization
  - Created `docs/reports/` for audit records
  - Archived temporary reports from temp/
- **Commit**: d5a7993 - "Complete site-wide SEO optimization and documentation reorganization"

### November 29, 2025 - Title Tag Audit Script and Additional SEO Title Optimizations
- **Created Title Tag Audit Script**: `scripts/audit_title_tags.py`
  - Comprehensive audit tool for all content types (episodes, blog posts, pages)
  - Checks both `title` and optional `seo_title` fields
  - Only validates effective title (what appears in HTML `<title>` tag) against 60/70 char limits
  - Detects identical titles (wasteful duplication)
  - Shows both full and SEO titles side-by-side in summary for easy comparison
  - Provides suggestions for shortening overly long titles
- **Extended SEO Title Support**: Added `seo_title` to non-episode content
  - Homepage: `seo_title: "Security Cocktail Hour Podcast"` (36 chars)
  - Episode 40: Updated to `seo_title: "Fighting Cybersecurity Threats Together"` (39 chars)
  - Episode 53: Updated to `seo_title: "New Rules of Cyber Incident Response | Lisa Landau,Tim Shipp"` (67 chars)
  - Episode 55: Updated to `seo_title: "Firmware, Fire & the Future of Cyber | Paul Asadoorian"` (60 chars)
  - Blog post (when-nanoseconds-matter): `seo_title: "When Nanoseconds Matter: Securing High-Performance Environments"` (64 chars)
- **Documentation Updated**:
  - Updated `docs/SEO-TITLE-TAG-STANDARDS.md` reference section with current implementation (20 pages)
  - Added audit script reference to tools list
  - Updated `docs/README.md` to document new audit script
- **Status**: 20 pages now have optimized SEO titles (17 episodes, 1 blog post, 1 homepage, 1 other page)

### November 29, 2025 - Image Optimization with ImageMagick
- **Image Optimization Implemented**: Optimized all episode images using ImageMagick
- **Backup Created**: Full backup to `image-backups/backup-2025-11-29/` (6.4MB)
- **PNG to JPG Conversion Testing**:
  - episode-017.png → episode-017.jpg (217K → 61K, 72% savings) ✅ Kept
  - episode-047.png → episode-047.jpg (430K → 354K, 18% savings) ✅ Kept
  - episode-053.png → episode-053.jpg (39K → 116K) ❌ Restored to PNG (increased size)
  - episode-056.png → episode-056.jpg (36K → 108K) ❌ Restored to PNG (increased size)
- **JPG Optimization with ImageMagick** (quality 85, -strip for metadata removal):
  - episode-025.jpg: 0.5KB saved
  - episode-029.jpg: 7.5KB saved
  - episode-047.jpg: 107.3KB saved (largest improvement!)
  - episode-058.jpg: 7.7KB saved
  - episode-059.jpg: 0.3KB saved
- **PNG Optimization Attempted**: All 3 PNG files already optimally compressed (no improvement possible)
- **Total Results**:
  - 51 images processed (48 JPG + 3 PNG)
  - ~123KB total savings (6.0MB → 5.9MB)
  - All optimizations non-destructive (files only replaced if smaller)
  - High quality maintained (85% JPG quality, 95% PNG quality)
- **Tools Used**: ImageMagick 7.1.2-8 (via Homebrew on macOS)
- **Status**: All episode images optimized and ready for production deployment

### November 29, 2025 - Production Deployment Fixes
- **Issue 1: 403 Forbidden Error on Production**
  - Cause: .htaccess file had restrictive permissions (600) preventing Apache from reading it
  - Fix: Changed static/.htaccess permissions to 644 (rw-r--r--)
  - Rebuilt production-deployment.zip with correct permissions
  - Commit: eeb748b - "Fix .htaccess file permissions for production deployment"
  - Status: ✅ Resolved - production site accessible
- **Issue 2: Episode Page Footer Layout Broken**
  - Cause: Overly broad CSS selector (.container > div) affecting footer layout
  - Symptoms: Footer displayed in malformed single-column layout instead of 4-column grid
  - Fix: Made episode page grid styles more specific (.section .container > div)
  - This prevents episode 2-column layout from interfering with footer 4-column grid
  - Commit: d75379d - "Fix episode page footer CSS conflict"
  - Status: ✅ Resolved - footer displays correctly on all pages
- **Production Deployment Package**: Updated production-deployment.zip (7.6MB)
  - Includes all fixes: .htaccess permissions, footer CSS, image optimizations
  - Deployed to GoDaddy cPanel production successfully

### November 29, 2025 - Search Engine Submission
- **Sitemap Submitted to Search Engines**
  - Sitemap URL: `https://securitycocktailhour.com/sitemap.xml`
  - Google Search Console: ✅ Submitted
  - Bing Webmaster Tools: ✅ Submitted
  - Contains all 110 pages (episodes, blog posts, main pages)
- **Expected Timeline**:
  - Google: Initial crawling within 24-48 hours, full indexing 1-4 weeks
  - Bing: Initial crawling within 3-7 days
- **SEO Benefits Now Active**:
  - Optimized title tags (≤60 chars) for better click-through rates
  - Meta descriptions (120-155 chars) for compelling search snippets
  - Schema.org markup for rich results (podcast episodes, blog posts)
  - Image optimization (123KB saved) for faster page loads
  - Clean URLs with trailing slashes (no duplicate content issues)
- **Status**: Production site live with full SEO optimization, submitted to search engines

### December 2, 2025 - Episode 64 + Enhanced Features Deployment

**Episode 64 Published**: "Bonus: Holiday Scams Unwrapped: Tips to Stay Safe this Season"
- **Published**: December 2, 2025
- **Category**: Educational
- **Duration**: 32:38
- **Description**: Holiday scam protection tips: gift card fraud, phone payments for teens, seasonal cybersecurity threats
- **SEO Optimized**:
  - Title: 53 characters (optimized with `seo_title`)
  - Description: 145 characters (within 120-155 range)
- **Features**: Full transcript with collapsible accordion
- **Related Episodes**: Manually specified (Episodes 61 & 58)

**🆕 Feature 1: Collapsible Transcript Accordion**
- **File**: `layouts/episodes/single.html` (lines 93-176)
- **Implementation**: Native HTML `<details>` element
- **Functionality**:
  - Auto-detects episodes with "Full Episode Transcript" heading
  - Renders transcript in collapsible accordion (collapsed by default)
  - Blue gradient header matching site design
  - Max height with scroll (600px desktop, 400px mobile)
  - Smooth animations, hover effects
  - Episodes without transcripts unaffected
- **SEO Benefits**:
  - ✅ Content remains in DOM for full indexing
  - ✅ Google officially supports `<details>` (no hidden content penalty)
  - ✅ All transcript text searchable and rankable
  - ✅ Direct link available: `#transcript`
- **UX Benefits**:
  - ✅ Page not overwhelmingly long on load
  - ✅ User controls when to view transcript
  - ✅ Accessible (keyboard nav, screen readers)
  - ✅ Mobile-friendly

**🆕 Feature 2: Manual Related Episodes**
- **File**: `layouts/episodes/single.html` (lines 162-174)
- **Functionality**:
  - Episodes can specify custom related episodes via frontmatter
  - Uses `related_episodes` array field
  - Falls back to auto-generated category matching if not specified
- **Use Cases**:
  - Series episodes
  - Thematic connections across categories
  - Cross-promotion
  - Featured episodes
- **Example**:
  ```yaml
  related_episodes:
    - "episode-61-ai-attacks-need-ai-defense.md"
    - "episode-58-travel-router-unboxing.md"
  ```

**🆕 Episode 64 Platform Links Update + Homepage Fix** (December 2, 2025 - Later)
- **Updated Episode 64 Platform URLs**:
  - YouTube: https://youtu.be/BdiHfxcg1P4 (unchanged)
  - Spotify: https://tinyurl.com/3dzccabe (updated to tinyurl)
  - Apple: https://tinyurl.com/3emej8hy (updated to tinyurl)
  - Amazon: https://tinyurl.com/3w3cfke9 (updated to tinyurl)
- **Fixed Homepage "Listen Now" Button**:
  - Changed from hardcoded YouTube channel link to episode-specific YouTube URL
  - File: `layouts/index.html` (line 74-76)
  - Now uses `{{ .Params.platforms.youtube }}` for dynamic episode links
  - Applies to all current and future episodes automatically

**Commits**:
- `07c1c90` - Publish Episode 64: Holiday Scams Unwrapped bonus episode
- `a9b7612` - Add collapsible transcript accordion for episode pages
- `1f43f64` - Update documentation for Episode 64 and new features
- `f1a29d6` - Update design spec with collapsible transcript and manual related episodes
- `6d64a53` - Update Episode 64 platform links and fix homepage Listen Now button
- `546abf8` - Update production deployment package

**Production Package**: `production-deployment.zip` (7.7MB)
- ✅ Deployed to GoDaddy production (December 2, 2025)
- ✅ Episode 64 live with updated platform links
- ✅ Homepage "Listen Now" button links to episode-specific YouTube URLs
- ✅ Collapsible transcript accordion active
- ✅ Manual related episodes feature active
- ✅ All 111 pages built and minified

### December 3, 2025 - Hero Redesign Page Mockups + Font Selection Complete

**Hero Redesign Work**: Completed full-page mockups for all major pages (Episodes, About, Contact, Blog, Home) and finalized typography system with PT Serif selection

**Design System Finalized**:
- **Typography**:
  - **Oswald** (sans-serif, weights 600/700) - Main headings, page titles, section titles (uppercase, bold)
  - **PT Serif** (serif, weights 400/700) - Body text, descriptions, paragraphs (confident, readable, substantial feel)
  - **Bebas Neue** (sans-serif condensed) - Labels, buttons, UI elements (uppercase, compact)
- **Color Palette** (updated from initial exploration):
  - **Primary Red**: #D74444 (brand color, CTAs, accents)
  - **Navy**: #2B4D7D (primary dark), #3A5F99 (light), #1F3859 (darker)
  - **Teal**: #4A9B9B (primary accent), #6BB8B8 (light) - replaced gold/cyan from initial concepts
  - **Silver**: #C0C0C0 (secondary accent)
  - **Cream**: #F5F1E8 (backgrounds), #E8E0D0 (darker variant)
- **Design Principles**:
  - Premium art deco aesthetic (1950s-60s retro badge style)
  - Compact hero sections (learned from Episodes page feedback)
  - Art deco geometric patterns and corner accents
  - Gradient backgrounds (navy, red) with teal accents
  - Circular badge motifs from logo
  - Consistent visual language across all pages

**Font Selection Process**:
- **Initial Font**: Crimson Pro (serif body font)
- **User Feedback**: "Hard to read", "too ornate", "too dainty" - needed more confident, substantial feel
- **Requirements**: Better readability, less ornate, still distinctive (avoid generic AI look), complements art deco aesthetic
- **Fonts Tested**:
  1. **Lora** - Traditional serif, too similar to Crimson Pro
  2. **Source Serif Pro** - Better readability, user feedback: "It's better"
  3. **Merriweather** - Screen-optimized serif, user feedback: "best so far", "easiest to read", "less dainty", "more confident"
  4. **PT Serif** - Substantial, grounded, screen-designed - user feedback: "I like it"
  5. **Bitter** - Slab serif, bold geometric (shown for comparison)
  6. **Spectral** - Google's digital reading font (shown for comparison)
- **Final Selection**: **PT Serif** - Selected for confident, substantial feel with excellent screen readability
- **All Mockups Updated**: All 5 HTML mockup files updated from Crimson Pro to PT Serif
- **Font Test Files Created**: 6 test files created for side-by-side comparison

**Pages Completed**:

1. **Episodes Page v3** (`temp/hero-redesigns/episodes-page-v3.html`)
   - **User Feedback Addressed**:
     - Reduced hero height dramatically (episode thumbnails now immediately visible)
     - Removed all icons/emojis from platform buttons (YouTube, Spotify, Apple, Amazon)
   - **Features**:
     - Compact hero with stats bar (65 Episodes, 50+ Guests, 60hrs Content)
     - Search input + Category/Sort dropdowns
     - Vertical episode cards with 16:9 thumbnail aspect ratio
     - Episode number badges, category tags, platform buttons
     - Two-column responsive grid
   - **Status**: ✅ Approved ("satisfactory")

2. **About Page** (`temp/hero-redesigns/about-page-mockup.html`)
   - **Sections**:
     - Compact hero with tagline
     - Our Story section (centered narrative)
     - Meet Your Hosts (Joe Patti & Adam Roth) - two-column card layout
     - What You'll Get (3 benefits with icon circles)
     - Stats section (65+ Episodes, 50+ Guests, 60hrs Content)
     - Newsletter signup (red gradient background)
   - **Features**:
     - Square host images with "Co-Host" badges
     - Icon circles with double-border treatment
     - LinkedIn links for hosts
     - Responsive grid layouts
   - **Status**: ✅ Approved ("satisfactory")

3. **Contact Page** (`temp/hero-redesigns/contact-page-mockup.html`)
   - **Layout**: Two-column (contact form left, info cards right)
   - **Features**:
     - Compact hero section
     - Full contact form (Name, Email, Subject dropdown, Message textarea)
     - Formspree integration with AJAX submission
     - Success/error status messages
     - Contact info cards (Email, Social Media, Response Time)
     - "Interested in Being a Guest?" section with red left border
   - **Form Fields**: 6 subject options (Guest Submission, Partnership, Consulting, Sponsorship, Press, General)
   - **Status**: ✅ Approved ("acceptable")

4. **Blog Page** (`temp/hero-redesigns/blog-page-mockup.html`)
   - **Layout**: Two-column (blog grid left, newsletter sidebar right)
   - **Controls**: Search + Category dropdown + Tag dropdown + Sort dropdown
   - **Features**:
     - Compact hero section
     - Blog cards with vertical left accent bar (appears on hover)
     - Red category tags (vs teal for episodes)
     - Tag pills below metadata
     - "Read More" buttons with arrow animation
     - Sticky newsletter sidebar (red gradient)
   - **Sample Content**: 6 blog posts across different categories
   - **Status**: ✅ Approved ("acceptable")

5. **Homepage** (`temp/hero-redesigns/homepage-full-mockup-v2.html`)
   - **Sections**:
     - Full hero with animated accents, stats badges, platform links
     - Featured Episodes section (3 episode cards)
     - Featured Blog Posts section (3 blog cards)
     - About teaser section
     - Newsletter signup (red gradient)
   - **Features**:
     - Premium art deco hero with geometric patterns
     - Consistent card styling across sections
     - Episode/blog cards with hover effects
     - Platform links with underline animations
   - **Status**: ✅ Complete (updated to PT Serif)

**Files Created**:
- `temp/hero-redesigns/episodes-page-v3.html` (updated to PT Serif)
- `temp/hero-redesigns/about-page-mockup.html` (updated to PT Serif)
- `temp/hero-redesigns/contact-page-mockup.html` (updated to PT Serif)
- `temp/hero-redesigns/blog-page-mockup.html` (updated to PT Serif)
- `temp/hero-redesigns/homepage-full-mockup-v2.html` (updated to PT Serif)
- Font test files (for comparison): 6 test HTML files

**Typography Reference**:
- Display/Headers: Oswald (uppercase, bold, geometric art deco feel)
- Body/Content: PT Serif (sentence case, confident serif, substantial readability)
- UI Elements: Bebas Neue (uppercase, condensed, utilitarian)

### December 5, 2025 - Newsletter Signup Page Created

**New Feature: Dedicated Newsletter Signup Page**
- **Purpose**: Clean landing page for social media newsletter promotion
- **URL**: `/newsletter/` (https://securitycocktailhour.com/newsletter/)
- **Design**: Simplified, focused conversion-optimized layout
- **Content**:
  - Blue gradient hero section with title and description
  - Opening paragraph about joining the community
  - Three bullet points: Early episode notifications, Exclusive insights, No spam
  - Streamlined blue signup box with email field + Subscribe button only
  - Privacy statement below the form (outside blue box for visual balance)
  - Trust signals section: 64+ Episodes, 50+ Expert Guests, 60+ Hours of Content
- **Integration**:
  - Mailchimp signup form (same as homepage)
  - Added to footer "About" section (between "About the Show" and "Contact")
  - Not added to header navigation (keeping header simple)
- **Files Created**:
  - `content/newsletter.md` - Page content
  - `layouts/_default/newsletter.html` - Custom template
- **Files Modified**:
  - `layouts/partials/footer.html` - Added newsletter link

**Status**: ✅ DEPLOYED TO PRODUCTION (December 6, 2025)
- Clean, professional landing page for social media sharing at https://securitycocktailhour.com/newsletter/
- Functional Mailchimp integration
- Accessible from footer on all pages
- Production package: 7.7MB (112 pages)

### December 5, 2025 - Episode Number Display + Transcript Accordion Fixes

**Feature: Episode Number Display on Episode Cards**
- **Problem**: Episode numbers only visible in thumbnails (when present), making it hard to find episodes by number
- **Solution**: Added episode number to date line on all episode cards across the site
- **Display Format**: "Episode X | Date" (e.g., "Episode 62 | November 3, 2025")
- **Locations Updated**:
  - Episodes page (all episode cards)
  - Homepage "Latest Episode" section
  - Homepage "Recent Episodes" grid
- **Files Modified**: `layouts/episodes/list.html`, `layouts/index.html`
- **Implementation**: Extracts episode number from filename pattern `episode-XX-...` using Hugo template logic

**Enhancement: Episode Number Search**
- **Problem**: Searching for episode numbers returned no results
- **Solution**: Added episode number to searchable data attributes
- **Functionality**: Users can now search by:
  - Episode number (e.g., "47", "64", "01")
  - Episode title (existing)
  - Guest name (existing)
- **File Modified**: `layouts/episodes/list.html` (JavaScript search function)

**Bug Fix: Collapsible Transcript Accordion**
- **Problem**: 6 episodes with transcripts didn't show collapsible accordion (Episodes 21, 51, 53, 59, 60, 61)
- **Root Cause**: Episodes used heading "## Full Transcript" or "## Transcript" instead of "## Full Episode Transcript"
- **Template Requirement**: `layouts/episodes/single.html` looks for exact heading "Full Episode Transcript"
- **Solution**: Updated transcript headings in all 6 episodes to "## Full Episode Transcript"
- **Files Modified**:
  - `content/episodes/episode-21-medical-devices-halloween-and-whiskey-with-gabrielle-hempel.md`
  - `content/episodes/episode-51-agentic-ai-security-full-speed-into-the-unknown.md`
  - `content/episodes/episode-53-the-new-rules-of-cyber-incident-response-new-attacks-new-response.md`
  - `content/episodes/episode-59-wifi-pineapple-unboxing-the-hacker-device-from-tv-shows.md`
  - `content/episodes/episode-60-crypto-kidnappings-lost-keys-and-million-dollar-bug-bounties.md`
  - `content/episodes/episode-61-ai-attacks-need-ai-defense-ransomwares-new-danger-and-how-a-top-cyber-expert-is-.md`
- **Result**: All episodes with transcripts now show collapsible accordion with blue gradient header

**Commits**:
- `94bcf9d` - Add episode numbers to cards and fix transcript headings for collapsible feature
- `733e1a4` - Update CLAUDE.md documentation
- `e837062` - Add 301 redirects for old URLs from previous site

**Status**: ✅ DEPLOYED TO PRODUCTION (December 5, 2025)
- Episode numbers displayed consistently across all episode cards
- Search functionality enhanced with episode number support
- All transcript accordions working correctly
- 23 301 redirects active for old URLs to fix Google Search Console 404 errors
- Production package: 7.7MB (111 pages)
- Pushed to GitHub and auto-deployed to Netlify staging

### December 8, 2025 - Episode 65 Published + Homepage/Episode Page Fixes

**✅ CURRENT STATUS: EPISODE 65 DEPLOYED TO PRODUCTION + MULTIPLE PAGE FIXES COMPLETE**

**Episode 65: "Job Scams Are Getting Worse | Four of the Most Dangerous"**
- **Published**: December 8, 2025
- **Category**: Educational
- **Duration**: 31:58
- **Description**: "AI deepfakes, malware, and crypto scams are targeting job seekers. Learn to spot these 4 dangerous employment scams in 2025."
- **Full Description**: Job scams are getting scary good. We're talking AI deepfakes, fake recruiters, and cryptocurrency traps that are fooling even tech-savvy professionals. In this Security Cocktail Hour holiday special, Joe and Adam break down four of the most dangerous job scams hitting people right now.
- **Platforms**:
  - YouTube: https://youtu.be/OfOjvn8KfdQ
  - Spotify: https://tinyurl.com/2cyespeb
  - Apple: https://tinyurl.com/4dxufbmj
  - Amazon: https://tinyurl.com/bdd3nx4h
- **Related Episodes**: Episode 64 (Holiday Scams), Episode 45 (Holiday Scams 2023)
- **Features**: Full transcript with collapsible accordion
- **File Created**: `content/episodes/episode-65-job-scams-are-getting-worse-four-of-the-most-dangerous.md`
- **Image**: `static/images/episodes/episode-065.jpg` (copied from temp folder)

**CSS Fixes Implemented**:

1. **Newsletter Signup Box on Episode Single Page** (`layouts/episodes/single.html`)
   - **Problem**: Newsletter box on individual episode pages had white background (from `.card` and `.card-content` classes), making white text invisible
   - **Root Cause**: Both `.card` (line 387 in CSS) and `.card-content` (line 413 in CSS) had white/cream background gradients that needed to be overridden
   - **Solution**: Added inline styles with `!important` to force red gradient background on both card and card-content divs
   - **Changes**:
     - Card div: `background: linear-gradient(135deg, #B33333 0%, #D74444 100%) !important`
     - Card-content div: Same red gradient with `!important`
     - Email input: White background with proper padding, borders, and dark text color
     - Button: White background with red text (#D74444)
   - **File Modified**: `layouts/episodes/single.html` (lines 214-236)

2. **About Section Text Visibility** (`static/css/main.css`)
   - **Problem**: About section on homepage had unreadable text (light text on light background)
   - **Root Cause**: Duplicate `.about-section` definition at line 2964 was overriding the correct navy gradient background (line 1111) with white background
   - **Solution**: Removed `background: var(--white)` from duplicate definition
   - **File Modified**: `static/css/main.css` (line 2966 - removed background property)
   - **Result**: Navy gradient background now shows correctly with white/cream text visible

3. **Episode Content Background Layering** (`static/css/main.css`)
   - **Problem**: Episode cards had unnecessary background gradient on content area
   - **Root Cause**: `.episode-content` class (line 1763) had `background: linear-gradient(180deg, var(--white) 0%, var(--cream) 100%)` that was redundant since parent card already has white background
   - **Solution**: Removed background gradient from `.episode-content` class
   - **File Modified**: `static/css/main.css` (line 1763 - removed background property)

4. **Episode Card Images on Homepage** (`static/css/main.css`)
   - **Problem**: Episode card images in "Recent Episodes" section didn't fill full width, leaving white space on right side and making cards unbalanced
   - **Root Cause**: `.episode-card-small .episode-image` (line 1019) only had `height: 180px`, causing images to crop top/bottom and not fill width
   - **Solution**: Changed to `width: 100%; height: auto; display: block;` to show full images at natural aspect ratio
   - **File Modified**: `static/css/main.css` (lines 1020-1022)
   - **Result**: Images now display at full aspect ratio without cropping, cards adjust height to accommodate images

5. **Homepage Recent Episodes** (`layouts/index.html`)
   - **Change**: Reduced from 5 to 4 episodes in "Recent Episodes" section
   - **Reason**: Better layout balance on homepage
   - **File Modified**: `layouts/index.html` (line 164: changed `first 6` to `first 5`)

6. **CSS Cache-Busting Fix** (`layouts/_default/baseof.html`, `layouts/index.html`)
   - **Problem**: Production site showed old design in regular browsers but worked in incognito mode
   - **Root Cause**: Browsers cached old CSS files, serving outdated styles
   - **Solution**: Added `?v={{ now.Unix }}` timestamp parameter to CSS file links
   - **Files Modified**:
     - `layouts/_default/baseof.html` (line 33)
     - `layouts/index.html` (line 33)
   - **Result**: Each build generates unique CSS URL, forcing browsers to fetch updated files instead of using cache

**All Files Modified**:
1. `content/episodes/episode-65-job-scams-are-getting-worse-four-of-the-most-dangerous.md` (created)
2. `static/images/episodes/episode-065.jpg` (created)
3. `layouts/episodes/single.html` (newsletter box styling - lines 214-236)
4. `static/css/main.css` (4 CSS fixes):
   - Line 1020-1022: Episode card image sizing
   - Line 1763: Removed episode content background
   - Line 2966: Removed about section white background
5. `layouts/index.html` (homepage recent episodes count + cache-busting)
6. `layouts/_default/baseof.html` (cache-busting)

**Git Workflow**:
- Worked on `hero-redesign` branch
- Merged to `main` branch (fast-forward merge)
- Pushed to GitHub (triggers Netlify staging deployment)
- All changes committed with proper commit messages

**Production Deployment Package**:
- **File**: `production-deployment-20251208-143839.zip`
- **Size**: 7.9MB
- **Pages**: 113 pages
- **Location**: Project root directory

**Status**:
- ✅ Episode 65 DEPLOYED TO PRODUCTION (https://securitycocktailhour.com/)
- ✅ Newsletter box rendering correctly on episode pages (red background, white text)
- ✅ About section text readable on homepage (navy background)
- ✅ Episode cards displaying correctly on homepage (full images, no cropping)
- ✅ Homepage shows 4 episodes in Recent Episodes section
- ✅ Cache-busting implemented (browsers will fetch new CSS on each deployment)
- ✅ All changes committed to `main` branch and pushed to GitHub
- ✅ Production package deployed to GoDaddy
- ✅ Cache-busting fix verified (works in both regular and incognito browsers after hard refresh)
- ✅ Production site live with all fixes

**Production Package Deployed**:
- File: `production-deployment-20251208-143839.zip` (7.9MB)
- Deployed: December 8, 2025
- Status: ✅ LIVE on https://securitycocktailhour.com/

---

**End of Archive**
**Last Updated**: December 12, 2025
**For current working context, see CLAUDE.md**
