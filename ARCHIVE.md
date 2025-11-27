# Security Cocktail Hour Website - Archive

**Purpose**: This file contains historical fixes, detailed troubleshooting information, and reference material that is not needed for day-to-day work but is preserved for future reference.

**Last Updated**: November 25, 2025

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
- Updated SESSION_CONTEXT.md with episode content structure

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

**End of Archive**
**Last Updated**: November 25, 2025
**For current working context, see SESSION_CONTEXT.md**
