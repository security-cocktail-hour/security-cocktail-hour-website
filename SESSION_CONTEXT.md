# Security Cocktail Hour Website - Session Context

**Last Updated**: October 8, 2025
**Hugo Version**: v0.151.0
**Session Status**: Ready for staging deployment

---

## Project Overview

Building a static website for the Security Cocktail Hour podcast using Hugo static site generator. The site will be deployed to GoDaddy cPanel hosting as static HTML files.

**Live Dev Server**: http://localhost:1313/
**Hugo Server Processes**:
- Background shell a90180 (running)
- Background shell 23d25d (running)

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

**Technical:**
- SEO optimization (meta tags, Open Graph, schema.org markup)
- Episode number badges on episode pages
- Lazy loading images
- Fallback gradient placeholders for missing episode images
- Client-side search/filter with vanilla JavaScript

### ⏳ Pending Integration

**Backend Services (waiting for hosting setup):**
- Newsletter subscription form (needs Mailchimp or similar)
- Contact form submission (needs Formspree or PHP handler)
- Google Analytics (optional, can add anytime)

### ❌ Known Issues

**Episode 7 Display Problem** (Deferred for later investigation):
- Episode 7 ("The Mandatory AI Security Episode") displays as truncated "Episode ..." on homepage cards
- Markdown file is correct
- Not a browser cache issue
- Attempted fix: Hugo server restart - did not resolve
- Potential causes: Hugo summary generation, character encoding, front matter parsing
- **Action**: Investigate later, possibly check Hugo's `.Summary` generation settings

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
├── hugo.toml                 # Main configuration
├── static/
│   ├── css/
│   │   ├── main.css         # Design system with CSS variables
│   │   └── main.css.backup  # Previous color palette backup
│   └── images/
│       ├── episodes/        # Episode cover images (43 of 64 present)
│       ├── logo.png
│       ├── logo-white.png
│       ├── joe-patti.jpg
│       └── adam-hertzel.jpg
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
- Fixed with batch sed commands:
  ```bash
  sed -i '' 's/^title: "Episode [0-9]*: /title: "/' "$file"
  sed -i '' 's/^guest: ".*"$/guest: ""/' "$file"
  sed -i '' 's/^guest_bio: ".*"$/guest_bio: ""/' "$file"
  ```

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

---

## Hugo Configuration

### hugo.toml Key Settings

```toml
baseURL = 'https://securitycocktailhour.com/'
languageCode = 'en-us'
title = 'Security Cocktail Hour'

[params]
  description = "Expanding cybersecurity knowledge beyond your specialty, one conversation at a time."

[menu]
  [[menu.main]]
    name = "Episodes"
    url = "/episodes/"
    weight = 1
  [[menu.main]]
    name = "About"
    url = "/about/"
    weight = 2
  [[menu.main]]
    name = "Resources"
    url = "/resources/"
    weight = 3
  [[menu.main]]
    name = "Contact"
    url = "/contact/"
    weight = 4

[taxonomies]
  category = 'categories'
  tag = 'tags'
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

### Current Status

Two background processes running:
- Process a90180: Initial server
- Process 23d25d: Restarted server (attempted fix for episode 7 issue)

### Management Commands

**Check running processes:**
```bash
/bashes
```

**View output:**
Use BashOutput tool with bash_id

**Kill process:**
Use KillShell tool with shell_id

**Start server:**
```bash
hugo server -D
```

**Build for production:**
```bash
hugo --minify
```

Output directory: `public/`

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

### Adding Episode Images

1. Add image file to `static/images/episodes/`
2. Update episode markdown: `image: "/images/episodes/episode-XXX.png"`
3. Recommended format: PNG or JPG, optimized for web

---

## Deployment Process

### Build for Production

```bash
cd /Users/joe/Library/CloudStorage/Dropbox/Security\ Cocktail\ Hour/website/redesign\ 2025-10/security-cocktail-hour-website
hugo --minify
```

This generates optimized static files in the `public/` directory.

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

### What NOT to Upload

- `content/` directory (source markdown)
- `layouts/` directory (Hugo templates)
- `static/` directory (pre-build assets)
- `hugo.toml` (configuration)
- `docs/` directory
- `.git/` directory

---

## Staging and Testing

### Recommended Staging Setup

**Option 1: Netlify (Easiest)**
- Free tier
- Automatic builds from Git
- Free SSL
- Custom subdomain
- Deploy previews
- Setup time: 5 minutes

**Option 2: GoDaddy Subdomain**
- Create `staging.securitycocktailhour.com`
- Same environment as production
- Manual deployment
- Setup time: 30 minutes

### Pre-Launch Checklist

- [ ] Test all pages on staging
- [ ] Test contact form (with backend integration)
- [ ] Test newsletter signup (with backend integration)
- [ ] Verify mobile responsiveness
- [ ] Test in Chrome, Firefox, Safari
- [ ] Check page load speed (< 3 seconds)
- [ ] Verify all images load
- [ ] Test search/filter functionality
- [ ] Proofread all content
- [ ] Test social sharing
- [ ] Submit sitemap to Google Search Console

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

---

## File Locations Reference

### Key Files

**Configuration:**
- `hugo.toml` - Main Hugo config

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
- `docs/SESSION_CONTEXT.md` - This file

**Scripts:**
- `convert_episodes.py` - CSV to markdown converter

---

## Next Steps

### Immediate (Before Launch)

1. **Set up staging environment**
   - Recommended: Netlify for easy testing
   - Alternative: GoDaddy subdomain

2. **Integrate backend services**
   - Newsletter: Mailchimp (or alternative)
   - Contact form: Formspree (or alternative)
   - Test both thoroughly on staging

3. **Final testing**
   - Complete pre-launch checklist
   - Test on multiple devices and browsers
   - Fix any issues found

4. **Deploy to production**
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
   - Complete episode show notes (highlights, key takeaways, resources)
   - Regular episode updates

3. **Features (Phase 2)**
   - Blog/articles section
   - Enhanced search features
   - Additional resources
   - Performance optimizations

4. **Resolve Outstanding Issues**
   - Investigate Episode 7 display problem
   - Check for any other similar issues

---

## Important Notes

### Color Palette Changes

The color palette has been changed twice during development:

1. **Original**: Red (#C8534B), Blue (#1E4D8B), Cyan (#3BA0D4), Green (#7BA956)
2. **Attempt 1** (rejected): Charcoal (#333333), Deep Teal (#004D40), Warm Cream (#FEFBF3), Cranberry (#AF3F47), Gold (#E5B800)
3. **Current**: Dark Blue (#192A56), Cool Grey (#8D99AE), Off-white (#F8F9FA), Professional Blue (#436098), Bright Red (#CE1F2C)

Backup of previous palette available in `static/css/main.css.backup`.

### Episode 7 Issue

This issue is **deferred** and does not block launch. Episode 7 shows truncated "Episode ..." on homepage despite correct markdown. Investigate Hugo summary generation settings after launch.

### Form Placeholders

Contact form and newsletter subscriptions are **placeholder forms only**. They display correctly but do not function until backend services are integrated. This is **expected** and will be resolved during staging setup.

---

## Contact Information

**Project Owner**: Joe
**Project Location**: `/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website`
**Hugo Version**: v0.151.0
**Last Session**: October 8, 2025

---

## Quick Reference Commands

```bash
# Start development server
hugo server -D

# Build for production
hugo --minify

# Create new episode
hugo new episodes/episode-XX-title-slug.md

# Check Hugo version
hugo version

# View directory structure
tree -L 2 -I 'public|resources'

# Check running Hugo servers
ps aux | grep hugo
```

---

**Session Context Complete**
**Status**: Ready for staging deployment and backend integration
**Next Action**: Set up staging environment and integrate Mailchimp/Formspree
