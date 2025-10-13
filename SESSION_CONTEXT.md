# Security Cocktail Hour Website - Session Context

**Last Updated**: October 13, 2025
**Hugo Version**: v0.151.0
**Session Status**: Deployed to Netlify staging - ready for team review

---

## Project Overview

Building a static website for the Security Cocktail Hour podcast using Hugo static site generator. The site is currently deployed to Netlify for staging/testing and will ultimately be deployed to GoDaddy cPanel hosting as static HTML files.

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
- Netlify staging environment configured
- GitHub repository with automatic deployments
- Netlify build configuration (`netlify.toml`)
- Git workflow established

### ⏳ Pending Integration

**Backend Services (waiting for hosting setup):**
- Newsletter subscription form (needs Mailchimp or similar)
- Contact form submission (needs Formspree or PHP handler)
- Google Analytics (optional, can add anytime)

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

### Current (Team Review Phase)

1. **Review staging site**
   - Test all pages and functionality
   - Check mobile responsiveness
   - Verify content accuracy
   - Test search/filter on episodes page
   - Review episode pages for completeness

2. **Gather feedback**
   - Collect feedback from team members
   - Create list of issues or changes needed
   - Prioritize fixes and enhancements

3. **Make adjustments**
   - Use Git workflow to make changes
   - Test locally before pushing
   - Verify changes on staging after deployment

### Before Production Launch

1. **Integrate backend services**
   - Newsletter: Mailchimp (or alternative)
   - Contact form: Formspree (or alternative)
   - Test both thoroughly on staging

2. **Final testing**
   - Test all pages on staging
   - Verify mobile responsiveness
   - Test in Chrome, Firefox, Safari
   - Check page load speed (< 3 seconds)
   - Verify all images load
   - Test search/filter functionality
   - Proofread all content
   - Test social sharing

3. **Deploy to production**
   - Build with `hugo --minify`
   - Upload `public/` to GoDaddy
   - Test live site
   - Submit sitemap to search engines

### Post-Launch

1. **Monitoring**
   - Set up Google Analytics (optional)
   - Monitor uptime (UptimeRobot, Pingdom)
   - Check Google Search Console for indexing

2. **Content**
   - Add missing episode images (21 episodes)
   - Add episode show notes as time permits
   - Regular episode updates

3. **Features (Phase 2)**
   - Blog/articles section
   - Enhanced search features
   - Additional resources
   - Performance optimizations

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
