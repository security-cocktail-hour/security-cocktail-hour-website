# Security Cocktail Hour Website - Session Context

**Last Updated**: October 21, 2025
**Hugo Version**: v0.151.0
**Session Status**: LIVE IN PRODUCTION - DNS cutover complete, all features functional

---

## Project Overview

Building a static website for the Security Cocktail Hour podcast using Hugo static site generator. The site is deployed to both Netlify (staging) and GoDaddy cPanel (production).

**Production Site**: https://securitycocktailhour.com/ (GoDaddy cPanel - awaiting DNS cutover)
**Staging Site**: https://[your-site-name].netlify.app/
**GitHub Repository**: https://github.com/security-cocktail-hour/security-cocktail-hour-website
**Local Dev Server**: http://localhost:1313/ (when running `hugo server -D`)

---

## Current Status

### ✅ Completed Features

**Core Functionality:**
- Homepage with hero section, latest episode, recent episodes grid
- Episode library/archive with search and filter functionality
- Individual episode pages with full show notes
- About page with host photos and bios
- Contact page (form placeholder - needs backend integration)
- Resources page (basic structure)
- Responsive navigation with mobile menu
- Footer with site links and platform icons

**Design System:**
- Complete CSS design system with CSS variables
- Responsive design (mobile, tablet, desktop)
- Professional blue/grey color palette (see Color Palette section below)
- System font stack for performance
- Consistent spacing, shadows, border radius

**Content:**
- 64 episodes migrated from CSV to Hugo markdown
- All episode metadata (title, date, guest, category, duration, description)
- Episode images (43 of 64 present, graceful fallbacks for missing)
- Host photos (Joe Patti, Adam Roth)
- Logo and branding assets
- Placeholder sections removed from episode pages (Key Takeaways, Resources Mentioned)

**Technical:**
- SEO optimization (meta tags, Open Graph, schema.org markup)
- Episode number badges on episode pages
- Lazy loading images
- Fallback gradient placeholders for missing episode images
- Client-side search/filter with vanilla JavaScript
- Relative URLs for internal navigation (works on any domain)
- Absolute URLs preserved for SEO/social sharing

**Deployment:**
- **Production**: GoDaddy cPanel hosting with static HTML files
- **Staging**: Netlify with automatic deployments from GitHub
- GitHub repository with automatic deployments to staging
- Netlify build configuration (`netlify.toml`)
- GoDaddy deployment via production-deployment.zip file
- Git workflow established

**Newsletter Integration:**
- Mailchimp account created with audience
- Newsletter forms integrated on key pages:
  - Homepage newsletter section
  - Episode page sidebar
  - About page
  - Resources page
- Forms include honeypot field for bot protection
- Submissions open in new tab for Mailchimp confirmation
- **Note**: Footer newsletter form removed per user request (newsletter should only be on specific pages)

**Contact Form Integration:**
- Formspree account created and configured
- Contact form integrated with AJAX submission
- Form endpoint: https://formspree.io/f/mrbyrgrv
- Features:
  - Name, email, subject dropdown, message fields
  - Real-time success/error messages
  - Loading state during submission
  - No page redirect (stays on same page)
  - Proper error handling with fallback to direct email

**Google Analytics:**
- GA4 tracking implemented (Measurement ID: G-8QL8F8JKNR)
- Added to baseof.html template
- Tracks all pages across the site

**Legal Pages:**
- Privacy Policy page created (GDPR/CCPA compliant)
- Terms of Service page created (Governing law: New Jersey)
- Both accessible via footer links

**Cookie Consent:**
- GDPR-compliant cookie consent banner implemented
- Accept/Decline buttons
- Integrates with Google Analytics (enables/disables tracking)
- User choice stored for 365 days
- Links to Privacy Policy

**Performance Optimization:**
- Episode images optimized: PNG to JPG conversion (episodes 18, 20, 24, 32, 36-46, 48-50, 52, 54-55, 57-61)
- Episodes 1-13 share single optimized image (episode-001-013.png, 35KB)
- Bio page images optimized (adam-roth.jpg: 34KB, joe-patti.jpg: 25KB)
- Total site size reduced from 49MB to 7.7MB (84% reduction!)
- Pages load virtually instantly

### ✅ Fixed Issues

**Episode 7 Display Problem** (RESOLVED - October 13, 2025):
- **Issue**: Episode 7 description was not truncating on homepage/episode list
- **Root Cause**: Episode 7's description (104 chars) was shorter than the 120-char truncation limit, plus templates were using Hugo's auto-generated `.Summary` instead of explicit `.Params.description`
- **Fix**: Changed templates to use `.Params.description` (from front matter) instead of `.Summary`
- **Files Changed**:
  - `layouts/episodes/list.html:64`
  - `layouts/index.html:52,85`
  - `layouts/episodes/single.html:161-162`

**Absolute URL Problem** (RESOLVED - October 13, 2025):
- **Issue**: Internal navigation links used `.Permalink` (absolute URLs with production domain), causing 404s on staging
- **Fix**: Changed internal navigation to `.RelPermalink` (relative URLs) while keeping absolute URLs for SEO/social sharing
- **Result**: Site now works on any domain (staging, production, localhost)

**Placeholder Content** (RESOLVED - October 13, 2025):
- **Issue**: 55 episode pages had placeholder sections for "Key Takeaways" and "Resources Mentioned"
- **Fix**: Removed all placeholder sections using batch script
- **Preserved**: 4 episodes with actual Key Takeaways content (episodes 53, 59, 60, 61)
- **Result**: 715 lines of placeholder content removed

**Newsletter Integration** (COMPLETED - October 14, 2025):
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

**Contact Form Integration** (COMPLETED - October 14, 2025):
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

**Google Analytics Integration** (COMPLETED - October 14, 2025):
- **Task**: Add GA4 tracking to all pages
- **Implementation**: Added Google Analytics script to baseof.html template
- **Measurement ID**: G-8QL8F8JKNR
- **Location**: [layouts/_default/baseof.html](layouts/_default/baseof.html) in <head> section
- **Result**: All pages tracked with GA4

**Legal Pages** (COMPLETED - October 14, 2025):
- **Task**: Create Privacy Policy and Terms of Service pages
- **Implementation**: Created comprehensive legal pages
- **Files**:
  - [content/privacy.md](content/privacy.md) - GDPR/CCPA compliant privacy policy
  - [content/terms.md](content/terms.md) - Complete terms of service (Governing law: New Jersey)
- **Result**: Legal pages accessible via footer links

**Cookie Consent Banner** (COMPLETED - October 14, 2025):
- **Task**: Add GDPR-compliant cookie consent banner
- **Implementation**: Added consent banner to baseof.html
- **Location**: [layouts/_default/baseof.html](layouts/_default/baseof.html)
- **Features**:
  - Accept/Decline buttons
  - Integrates with Google Analytics (enables/disables tracking based on choice)
  - Stores user choice in cookie for 365 days
  - Links to Privacy Policy
- **Result**: GDPR-compliant cookie consent implemented

**Production Deployment** (COMPLETED - October 15, 2025):
- **Task**: Deploy to GoDaddy cPanel hosting
- **Implementation**: Created production-deployment.zip with complete built site
- **Deployment Method**: Manual upload via cPanel File Manager
- **Documentation**: [GODADDY-DEPLOYMENT-INSTRUCTIONS.md](GODADDY-DEPLOYMENT-INSTRUCTIONS.md)
- **Domain**: securitycocktailhour.com (with SSL)
- **Result**: Site deployed and tested on production, awaiting DNS cutover

**Episode 41 Date Bug** (FIXED - October 15, 2025):
- **Issue**: Episode 41 showing as latest episode instead of Episode 61
- **Root Cause**: Episode 41 had date `2025-10-15` (today) instead of actual publication date
- **Fix**: Updated date to `2024-10-15` (correct year)
- **File**: [content/episodes/episode-41-everybody-makes-mistakes-including-cybersecurity-pros.md](content/episodes/episode-41-everybody-makes-mistakes-including-cybersecurity-pros.md)
- **Result**: Episode 61 now correctly displays as latest episode

**Image Optimization - Episodes 1-13** (COMPLETED - October 15, 2025):
- **Task**: Reduce page load time for episode images
- **Implementation**: Created single shared optimized image for episodes 1-13
- **File**: episode-001-013.png (300x300px, 35KB, reduced from 2.7MB per image)
- **Updates**: Updated episodes 01-13 to reference shared image
- **Savings**: ~32MB reduction in total page load

**Image Optimization - PNG to JPG Conversion** (COMPLETED - October 15, 2025):
- **Task**: Further reduce page load time by converting large PNG files to JPG
- **Implementation**: Converted 27 episode PNGs to optimized JPG format
- **Episodes Converted**: 18, 20, 24, 32, 36-46, 48-50, 52, 54-55, 57-61
- **Original Size Range**: 217KB to 1.2MB per PNG
- **Optimized Size**: Significantly smaller JPG files
- **Total Reduction**: Site deployment size reduced from 49MB to 7.7MB (84% reduction!)
- **Result**: Episodes page and About page load virtually instantly

**Episode 43 Image Reference Bug** (FIXED - October 15, 2025):
- **Issue**: Episode 43 image not displaying on production
- **Root Cause**: Markdown file still referenced .png instead of .jpg
- **Fix**: Updated image reference from episode-043.png to episode-043.jpg
- **File**: [content/episodes/episode-43-cybersecurity-for-emts-and-first-responders-protecting-patients-and-professional.md:8](content/episodes/episode-43-cybersecurity-for-emts-and-first-responders-protecting-patients-and-professional.md#L8)
- **Result**: Episode 43 image now displays correctly

**Mobile Hamburger Menu Fix** (FIXED - October 15, 2025):
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

**Episodes Page Category Filter Fix** (FIXED - October 21, 2025):
- **Issue**: Category filter dropdown only showed "All Topics" with no other options
- **Root Cause**: Template was trying to use Hugo's taxonomy system (`.Site.Taxonomies.categories`), but episodes use singular `category` field in front matter
- **Fix**: Updated template to collect categories directly from episode pages and display alphabetically
- **File Changed**: [layouts/episodes/list.html:26-37](layouts/episodes/list.html#L26-L37)
- **Result**: Dropdown now shows all 16 categories: AI, Career, Career Bio, Cryptocurrency Security, Educational, General, Hardware Security, Identity, Incident Response, Legal, Operational Technology (OT), Sales, Small Business, Threat Intel, Unboxing, Users
- **Deployed**: Pushed to GitHub/Netlify staging, production package updated

**SEO Optimization for Cybersecurity Podcast Keywords** (COMPLETED - October 21, 2025):
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

---

## Git & Netlify Workflow

### Repository Information

**GitHub Repository**: https://github.com/security-cocktail-hour/security-cocktail-hour-website
**Branch**: `main`
**Remote**: `origin`

### Making Changes & Deploying

Netlify is configured for **automatic deployments**. Every push to the `main` branch triggers a new build and deployment.

**Workflow:**

1. **Make changes locally**:
   ```bash
   # Navigate to project directory
   cd "/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website"

   # Start dev server to preview changes
   hugo server -D
   # View at http://localhost:1313/
   ```

2. **Test changes locally**:
   - Browse the site at http://localhost:1313/
   - Test all pages, navigation, search/filter
   - Check responsive design (resize browser)

3. **Commit and push changes**:
   ```bash
   # Stage all changes
   git add -A

   # Commit with descriptive message
   git commit -m "Your descriptive commit message"

   # Push to GitHub
   git push
   ```

4. **Automatic deployment**:
   - Netlify detects the push automatically
   - Builds site using `hugo --minify` (from `netlify.toml`)
   - Deploys to staging URL
   - Takes ~1-2 minutes

5. **Verify deployment**:
   - Go to https://app.netlify.com/
   - Check deployment status (Building → Published)
   - Test staging site

### Netlify Dashboard Access

**URL**: https://app.netlify.com/
**Site**: Security Cocktail Hour Website

**Dashboard features:**
- View deployment history
- See build logs
- Configure custom domain
- Monitor site analytics
- Manage environment variables

### Useful Git Commands

```bash
# Check current status
git status

# View commit history
git log --oneline -10

# See what changed in a file
git diff path/to/file

# Undo local changes (before commit)
git checkout -- path/to/file

# View remote URL
git remote -v

# Pull latest changes
git pull
```

### Build Configuration

**File**: `netlify.toml`

```toml
[build]
  command = "hugo --minify"
  publish = "public"

[build.environment]
  HUGO_VERSION = "0.151.0"
  HUGO_ENV = "production"
```

This file tells Netlify:
- How to build the site (`hugo --minify`)
- Which directory to deploy (`public/`)
- Which Hugo version to use (0.151.0)

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

## Current Color Palette

**Applied**: October 8, 2025

### New Palette (Current)

```
Primary (Dark Blue):      #192A56
- Usage: Main text, navigation, footers, headings
- Very readable on light backgrounds

Secondary (Cool Grey):    #8D99AE
- Usage: Category tags, secondary text, borders, dividers
- Subtle, professional

Background (Off-white):   #F8F9FA
- Usage: Main page background
- Cleaner than pure white

Action (Professional Blue): #436098
- Usage: Most buttons, CTAs, gradients
- Distinct and professional
- Darker gradient variant: #6A8CC7

Accent (Bright Red):      #CE1F2C
- Usage: "Listen Now" button only, key highlights
- Used sparingly for emphasis
```

### CSS Variable Mapping

```css
--color-primary: #192A56           /* Dark Blue */
--color-secondary: #8D99AE         /* Cool Grey */
--color-background: #F8F9FA        /* Off-white */
--color-action: #436098            /* Professional Blue */
--color-accent: #CE1F2C            /* Bright Red */

/* Legacy mappings for compatibility */
--color-security-red: #CE1F2C      /* Mapped to Accent */
--color-deep-blue: #436098         /* Mapped to Action */
--color-charcoal: #192A56          /* Mapped to Primary */
```

### Button Classes

- `.btn-primary` - Blue action buttons (#436098)
- `.btn-secondary` - Outlined blue buttons
- `.btn-accent` - Red accent button (#CE1F2C) - used for "Listen Now" header button only

### Color Backup

Previous color palette saved in: `static/css/main.css.backup`

---

## Project Structure

```
/
├── .git/                    # Git repository
├── .gitignore               # Git ignore file
├── netlify.toml             # Netlify build configuration
├── hugo.toml                # Main Hugo configuration
├── static/
│   ├── css/
│   │   ├── main.css         # Design system with CSS variables
│   │   └── main.css.backup  # Previous color palette backup
│   └── images/
│       ├── episodes/        # Episode cover images (43 of 64 present)
│       ├── logo.png
│       ├── logo-white.png
│       ├── joe-patti.jpg
│       └── adam-roth.jpg
├── layouts/
│   ├── _default/
│   │   ├── baseof.html      # Master template
│   │   ├── about.html
│   │   ├── contact.html
│   │   └── resources.html
│   ├── partials/
│   │   ├── header.html
│   │   └── footer.html
│   ├── index.html           # Homepage
│   └── episodes/
│       ├── list.html        # Episode archive with search/filter
│       └── single.html      # Individual episode page
├── content/
│   └── episodes/            # All episode markdown files (64 total)
├── archetypes/
│   └── episodes.md          # Template for new episodes
├── docs/
│   ├── sch_design_spec.md
│   ├── sch_website_requirements.md
│   ├── hosting_requirements.md
│   └── SESSION_CONTEXT.md   # This file
├── public/                  # Generated site (ignored by git)
└── convert_episodes.py      # Python script for CSV to markdown conversion
```

---

## Episode Content Structure

### Episode Front Matter Format

```yaml
---
title: "Episode Title"
date: YYYY-MM-DD
draft: false
guest: "Guest Name"
category: "Category"
duration: "HH:MM:SS"
image: "/images/episodes/episode-XXX.png"
description: >-
  Episode description (uses YAML block scalar for quotes)
platforms:
  youtube: "URL"
  spotify: "URL"
  apple: "URL"
  amazon: "URL"
guest_bio: "Bio text"
---
```

### Episode File Naming Convention

```
episode-[number]-[title-slug].md
```
- Number: Two digits with leading zero (01, 02, ... 64)
- Title slug: Lowercase, hyphenated, max 80 chars total filename

### Missing Episode Images

21 episodes currently using gradient fallback placeholders. Fallbacks are automatic via CSS/JavaScript - no manual intervention needed. Add actual images to `/static/images/episodes/` when available.

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

## Key Features Implementation

### 1. Episode Number Display

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

### 2. Missing Image Handling

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

### 3. Search and Filter

Client-side JavaScript on episode list page:
- Text search across title, description, guest
- Category filter dropdown
- Date sorting (newest/oldest)

Location: `layouts/episodes/list.html`

### 4. SEO Optimization

- Open Graph meta tags for social sharing
- Schema.org PodcastEpisode markup on individual episodes
- Descriptive page titles and meta descriptions
- Semantic HTML structure

### 5. Relative vs Absolute URLs

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

---

## Hugo Configuration

### hugo.toml Key Settings

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

## Hugo Server Management

### Start Development Server

```bash
cd "/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website"
hugo server -D
```

Server runs at: http://localhost:1313/

### Build for Production

```bash
hugo --minify
```

Output directory: `public/`

### Check Hugo Version

```bash
hugo version
```

Current: `hugo v0.151.0+extended+withdeploy darwin/arm64`

---

## Content Workflow

### Creating New Episodes

Use the archetype:
```bash
hugo new episodes/episode-XX-title-slug.md
```

This creates a new episode file with the correct front matter template.

### Editing Episodes

1. Edit markdown file in `content/episodes/`
2. Hugo dev server auto-reloads
3. Check changes at http://localhost:1313/
4. When satisfied, commit and push to deploy to staging

### Adding Episode Images

1. Add image file to `static/images/episodes/`
2. Update episode markdown: `image: "/images/episodes/episode-XXX.png"`
3. Recommended format: PNG or JPG, optimized for web
4. Commit and push changes

---

## Deployment Options

### Staging (Current - Netlify)

**Automatic deployment from GitHub:**
1. Push changes to GitHub `main` branch
2. Netlify automatically builds and deploys
3. View at staging URL
4. Build time: ~1-2 minutes

**Manual deployment from local:**
1. Build site: `hugo --minify`
2. Use Netlify CLI: `netlify deploy --prod` (requires setup)

### Production (Future - GoDaddy)

**Build for Production:**
```bash
hugo --minify
```

**What to Upload to GoDaddy:**

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

---

## Third-Party Integrations (To Do)

### Newsletter Subscription

**Recommended: Mailchimp**
- Free up to 500 subscribers
- Generate embedded form code
- Update form `action` in these files:
  - `layouts/index.html` (homepage)
  - `layouts/_default/about.html` (about page)
  - `layouts/_default/resources.html` (resources page)
  - `layouts/episodes/single.html` (episode sidebar)

**Current forms have:** `action="#"` (placeholder)

### Contact Form

**Option 1: Formspree (Easiest)**
- Free tier: 50 submissions/month
- Update form `action` in `layouts/_default/contact.html`
- No backend code needed

**Option 2: PHP Handler (if GoDaddy supports)**
- Create `contact-handler.php`
- Update form `action` to point to PHP file
- Handle email sending and spam prevention

### Google Analytics (Optional)

Add tracking code to `layouts/_default/baseof.html` in `<head>` section:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

Replace `GA_MEASUREMENT_ID` with your actual ID.

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

## File Locations Reference

### Key Files

**Configuration:**
- `hugo.toml` - Main Hugo config
- `netlify.toml` - Netlify build config
- `.gitignore` - Git ignore rules

**Templates:**
- `layouts/_default/baseof.html` - Master template
- `layouts/index.html` - Homepage
- `layouts/episodes/list.html` - Episode archive
- `layouts/episodes/single.html` - Episode page
- `layouts/partials/header.html` - Header/navigation
- `layouts/partials/footer.html` - Footer

**Styles:**
- `static/css/main.css` - All styles (design system)
- `static/css/main.css.backup` - Previous color palette

**Content:**
- `content/episodes/` - All episode markdown files

**Documentation:**
- `docs/sch_design_spec.md` - Design specification
- `docs/sch_website_requirements.md` - Requirements
- `docs/hosting_requirements.md` - Hosting and deployment guide
- `SESSION_CONTEXT.md` - This file (in root)

**Scripts:**
- `convert_episodes.py` - CSV to markdown converter

---

## Next Steps

### ✅ SITE LIVE IN PRODUCTION (Updated October 21, 2025)

**Current Status:**
- ✅ All MVP features completed and tested
- ✅ Site deployed to GoDaddy cPanel production hosting
- ✅ DNS cutover complete - Live at https://securitycocktailhour.com/
- ✅ All backend services integrated and functional:
  - ✅ Mailchimp newsletter forms
  - ✅ Formspree contact form
  - ✅ Google Analytics GA4
  - ✅ Privacy Policy & Terms of Service
  - ✅ Cookie consent banner
- ✅ Performance optimized (7.7MB total, pages load instantly)
- ✅ Mobile hamburger menu working on all devices
- ✅ Category filter dropdown showing all 16 topics
- ✅ SEO optimized for "cybersecurity podcast" keyword
- ✅ PodcastSeries schema markup implemented
- ✅ Tested and verified on production

**Production Deployment File:**
- Location: `production-deployment.zip` in project root
- Size: 7.7 MB (optimized, includes category filter fix and SEO improvements)
- Ready for deployment via cPanel File Manager
- Last Updated: October 21, 2025

**Recent Updates (October 21, 2025):**
1. Fixed category filter dropdown on Episodes page
2. Implemented Phase 1 SEO optimizations for cybersecurity podcast keywords
3. Added PodcastSeries structured data markup
4. Optimized meta titles and descriptions across all key pages

**Ready for Production Deployment:**
- Changes tested on staging (Netlify)
- Production package prepared
- Awaiting upload to GoDaddy cPanel

### Post-Launch (Future)

1. **Monitoring**
   - Monitor Google Analytics for traffic and behavior
   - Check Google Search Console for indexing and SEO
   - Monitor uptime and performance

2. **Content Updates**
   - Add new episodes as they're released
   - Optionally add missing episode images for older episodes
   - Update show notes and resources as needed

3. **Future Enhancements (Phase 2)**
   - Blog/articles section
   - Enhanced search features (filters, categories)
   - Additional resources and content
   - Further performance optimizations
   - Additional podcast platforms

---

## Important Notes

### Color Palette Changes

The color palette has been changed twice during development:

1. **Original**: Red (#C8534B), Blue (#1E4D8B), Cyan (#3BA0D4), Green (#7BA956)
2. **Attempt 1** (rejected): Charcoal (#333333), Deep Teal (#004D40), Warm Cream (#FEFBF3), Cranberry (#AF3F47), Gold (#E5B800)
3. **Current**: Dark Blue (#192A56), Cool Grey (#8D99AE), Off-white (#F8F9FA), Professional Blue (#436098), Bright Red (#CE1F2C)

Backup of previous palette available in `static/css/main.css.backup`.

### Form Placeholders

Contact form and newsletter subscriptions are **placeholder forms only**. They display correctly but do not function until backend services are integrated. This is **expected** and will be resolved before production launch.

### Git Best Practices

- Always test changes locally before pushing
- Write descriptive commit messages
- Commit related changes together
- Push to GitHub when ready to deploy to staging
- Don't push broken code (test first!)

---

## Contact Information

**Project Owner**: Joe
**Project Location**: `/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website`
**Hugo Version**: v0.151.0
**Last Session**: October 13, 2025

---

## Quick Reference Commands

```bash
# Navigate to project
cd "/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website"

# Start development server
hugo server -D

# Build for production
hugo --minify

# Create new episode
hugo new episodes/episode-XX-title-slug.md

# Check Hugo version
hugo version

# Git workflow
git status                    # Check what changed
git add -A                    # Stage all changes
git commit -m "Description"   # Commit changes
git push                      # Push to GitHub (triggers Netlify deploy)

# Check running Hugo servers
ps aux | grep hugo

# Install/update Netlify CLI
npm install -g netlify-cli

# Login to Netlify
netlify login
```

---

**Session Context Complete**
**Status**: Deployed to Netlify staging - awaiting team review
**Next Action**: Team reviews staging site, provides feedback for any adjustments needed
