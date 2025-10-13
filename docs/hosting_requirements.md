# Security Cocktail Hour Website - Hosting Requirements

**Date:** October 8, 2025
**Status:** For Implementation

---

## Overview

This document outlines the hosting requirements for the Security Cocktail Hour website, built with Hugo static site generator.

---

## Hosting Requirements

### For Hugo Static Site

The website is a **static site** - no server-side processing is needed for Hugo itself.

**Requirements:**
- **Static file hosting** - HTML, CSS, JavaScript, images
- **File types to serve**: HTML, CSS, JavaScript, images (PNG, JPG), fonts
- **Total size**: ~10-15MB (64 episodes + assets)
- **SSL certificate** (recommended, free via Let's Encrypt or hosting provider)
- **Custom domain support**

**No special requirements:**
- ❌ No database needed
- ❌ No server-side language (PHP, Node.js, Python) for the Hugo site itself
- ❌ No special server configuration

---

## Contact Form & Newsletter Integration

Since Hugo is static, you need **one of these options** for forms:

### Option 1: Use GoDaddy cPanel PHP (if your plan includes it)

**Requirements:**
- PHP 7.4+ for contact form processing
- Mail function enabled
- Can create simple `contact-handler.php` script

**Pros:**
- Uses existing hosting
- No third-party dependencies

**Cons:**
- Requires PHP knowledge
- Need to handle spam prevention
- Email deliverability can be tricky

### Option 2: Use Third-Party Services (Recommended)

**For Contact Form:**
- **Formspree** (https://formspree.io)
  - Free tier: 50 submissions/month
  - Just update form `action` attribute
  - Spam protection included

- **Basin** (https://usebasin.com)
  - Similar to Formspree
  - Simple integration

**For Newsletter:**
- **Mailchimp** (https://mailchimp.com)
  - Free up to 500 subscribers
  - Generate embedded form code
  - Replace `action="#"` with their endpoint

- **ConvertKit** (https://convertkit.com)
  - Built for creators/podcasters
  - Good automation features

- **Buttondown** (https://buttondown.email)
  - Simple, developer-friendly
  - Markdown newsletters

**Pros:**
- Works with pure static sites
- Professional features (analytics, automation)
- Spam protection included
- Reliable email delivery

**Cons:**
- Free tier limitations
- Third-party dependency

---

## Staging Environment Options

### Option A: Netlify (Recommended - Easiest)

**Features:**
- Free tier perfect for staging
- Automatic Hugo builds from Git
- Free SSL certificate
- Can test Formspree/Mailchimp integration
- Custom subdomain (e.g., `staging.securitycocktailhour.com`)
- Deploy previews for every change

**Setup Time:** ~5 minutes

**Steps:**
1. Push code to GitHub repository
2. Connect Netlify to repository
3. Configure build settings: `hugo --minify`
4. Deploy automatically

**URL:** https://netlify.com

### Option B: GitHub Pages

**Features:**
- Free hosting
- Requires manual build (`hugo` command, upload `public/` folder)
- Free SSL certificate
- Custom domain support

**Setup Time:** ~15 minutes

**Limitations:**
- Manual builds required
- No server-side processing

**URL:** https://pages.github.com

### Option C: GoDaddy Subdirectory/Subdomain

**Features:**
- Create `staging.securitycocktailhour.com` or `securitycocktailhour.com/staging/`
- Same environment as production
- Tests exact deployment process

**Setup Time:** ~30 minutes

**Steps:**
1. Create subdomain or subdirectory in cPanel
2. Build site locally: `hugo --minify`
3. Upload `public/` folder contents via FTP or File Manager

**Pros:**
- Exact production environment
- Tests deployment process

**Cons:**
- Manual deployment
- More setup required

---

## Recommended Workflow

### 1. Development (Local)
```bash
hugo server -D
# View at http://localhost:1313/
```

### 2. Staging
**Recommended: Use Netlify**
- Free, automatic deployments
- Test contact form integration (Formspree)
- Test newsletter integration (Mailchimp)
- Share with stakeholders for review
- URL: `something.netlify.app` or custom subdomain

### 3. Production (GoDaddy)
**Build for production:**
```bash
hugo --minify
# Generates optimized files in public/ directory
```

**Deploy to GoDaddy:**
1. Upload entire `public/` directory contents to GoDaddy web root
2. Use FTP client (FileZilla, Cyberduck) or cPanel File Manager
3. Ensure `.htaccess` file is included (if needed for clean URLs)

---

## Files Needed for Deployment

### What to Upload to Production

After running `hugo --minify`, upload the **entire contents** of the `public/` directory:

```
public/
├── index.html
├── episodes/
│   ├── index.html
│   ├── episode-01/
│   ├── episode-02/
│   └── ...
├── about/
│   └── index.html
├── contact/
│   └── index.html
├── resources/
│   └── index.html
├── css/
│   └── main.css
├── images/
│   ├── logo.png
│   ├── episodes/
│   └── ...
├── sitemap.xml
└── robots.txt
```

### What NOT to Upload

**Do not upload these development files:**
- `content/` directory
- `layouts/` directory
- `static/` directory (source)
- `archetypes/` directory
- `hugo.toml` config file
- `docs/` directory
- `.git/` directory
- `node_modules/` (if any)

**Only upload:** The built `public/` directory contents

---

## Domain Configuration

### For Custom Domain

**DNS Settings (configure at your domain registrar or GoDaddy):**

**Option 1: Root domain (securitycocktailhour.com)**
```
A Record
Host: @
Points to: [GoDaddy server IP]
```

**Option 2: WWW subdomain (www.securitycocktailhour.com)**
```
CNAME Record
Host: www
Points to: securitycocktailhour.com
```

**For Staging Subdomain:**
```
CNAME Record
Host: staging
Points to: [Netlify domain] or [GoDaddy staging server]
```

### SSL Certificate

**GoDaddy:**
- Free SSL may be included with hosting plan
- Enable via cPanel under "SSL/TLS Status"

**Netlify:**
- Automatic free SSL via Let's Encrypt
- Enabled by default

---

## Pre-Launch Checklist

### Before Deploying to Production

- [ ] Test all pages on staging environment
- [ ] Test contact form submission (receive test email)
- [ ] Test newsletter signup (verify in Mailchimp/provider)
- [ ] Test all episode links and platform buttons
- [ ] Verify mobile responsiveness on real devices
- [ ] Test in multiple browsers (Chrome, Firefox, Safari)
- [ ] Check page load speed (aim for < 3 seconds)
- [ ] Verify all images load correctly
- [ ] Test search and filter functionality on Episodes page
- [ ] Proofread all content for typos
- [ ] Verify meta tags for SEO (view page source)
- [ ] Test social sharing (Twitter, LinkedIn, Facebook)
- [ ] Set up Google Analytics (if desired)
- [ ] Create XML sitemap (Hugo generates automatically)
- [ ] Submit sitemap to Google Search Console

---

## Post-Launch Tasks

### After Going Live

1. **Submit to Search Engines**
   - Google Search Console: Add property, verify, submit sitemap
   - Bing Webmaster Tools: Similar process

2. **Set Up Monitoring**
   - Google Analytics (if not already done)
   - Uptime monitoring (UptimeRobot, Pingdom)

3. **Update Social Media**
   - Update links on Twitter, LinkedIn, etc.
   - Announce new website

4. **Redirects** (if replacing old site)
   - Set up 301 redirects from old URLs to new URLs
   - Test that old episode links redirect correctly

5. **Backup**
   - Keep backup of `public/` directory
   - Keep source code in Git repository

---

## Troubleshooting Common Issues

### "Page Not Found" Errors

**Problem:** Clean URLs not working (e.g., `/episodes/` shows 404)

**Solution:** Add `.htaccess` file to web root (GoDaddy/Apache):
```apache
# Enable clean URLs
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ /$1/ [L]

# Force HTTPS (optional)
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

### Contact Form Not Working

**Check:**
1. Form `action` attribute points to correct endpoint
2. Method is `POST`
3. Formspree/service is configured correctly
4. Check spam folder for test emails

### Newsletter Signup Not Working

**Check:**
1. Form `action` points to Mailchimp endpoint
2. Field `name` attributes match Mailchimp requirements
3. Test with valid email address
4. Check Mailchimp dashboard for subscribers

### Images Not Loading

**Check:**
1. Image paths are correct (relative URLs)
2. Images exist in `public/images/` directory
3. Case-sensitive filenames (episode-001.png vs Episode-001.png)
4. File permissions (644 for files, 755 for directories)

---

## Support Resources

**Hugo Documentation:** https://gohugo.io/documentation/
**GoDaddy Support:** https://www.godaddy.com/help
**Netlify Documentation:** https://docs.netlify.com/
**Formspree Documentation:** https://help.formspree.io/
**Mailchimp Documentation:** https://mailchimp.com/help/

---

**Document Complete**
*Ready for staging and production deployment*
