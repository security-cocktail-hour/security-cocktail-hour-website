# GoDaddy cPanel Deployment Instructions
## Security Cocktail Hour Website - Production Deployment

**Domain:** https://securitycocktailhour.com
**Date Prepared:** October 15, 2025
**Deployment Method:** cPanel File Manager

---

## Files Ready for Deployment

**Location:** `/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website/production-deployment.zip`

**Contents:** Complete production website (73 pages)
- All HTML pages
- CSS stylesheets
- Images (episode covers, logos, host photos)
- JavaScript files
- Sitemap.xml
- Transcripts

---

## Step-by-Step Deployment Instructions

### Step 1: Backup Existing Site (IMPORTANT!)

1. In cPanel, go to **File Manager**
2. Navigate to `public_html` directory
3. Select all files and folders
4. Click **Compress** → Choose **Zip Archive**
5. Name it: `backup-old-site-2025-10-15.zip`
6. Click **Download** to save backup to your computer
7. **Keep this backup safe!**

### Step 2: Clear Old Website Files

1. In cPanel File Manager, still in `public_html`
2. Select **all** existing files and folders
3. Click **Delete**
4. Confirm deletion
5. Verify `public_html` is now empty

### Step 3: Upload New Website

#### Option A: Upload ZIP file (Recommended)

1. In cPanel File Manager, make sure you're in `public_html`
2. Click **Upload** button (top menu)
3. Click **Select File**
4. Navigate to: `/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website/`
5. Select `production-deployment.zip`
6. Click **Open** and wait for upload to complete (may take 2-5 minutes)
7. Once uploaded, go back to File Manager
8. Find `production-deployment.zip` in `public_html`
9. Right-click → **Extract**
10. Extract to current directory
11. **Important:** The files will be in a `public/` subfolder
12. Move all files from `public/` to `public_html`:
    - Open the `public/` folder
    - Select all files/folders inside it
    - Click **Move**
    - Change path from `/public_html/public/` to `/public_html/`
    - Click **Move Files**
13. Delete the empty `public/` folder
14. Delete `production-deployment.zip`

#### Option B: Upload Individual Files (Alternative)

If the ZIP method doesn't work:
1. On your Mac, open Finder
2. Navigate to: `/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website/public/`
3. Select all files and folders
4. In cPanel File Manager, click **Upload**
5. Drag all files/folders from Finder to the upload area
6. Wait for all files to upload (may take 10-15 minutes)

### Step 4: Verify File Structure

Your `public_html` directory should now contain:
```
public_html/
├── index.html (homepage)
├── sitemap.xml
├── about/
├── contact/
├── episodes/
├── resources/
├── privacy/
├── terms/
├── css/
├── images/
└── js/
```

### Step 5: Set File Permissions

1. In cPanel File Manager, still in `public_html`
2. Select all files and folders
3. Click **Permissions** (or **Change Permissions**)
4. Set:
   - **Folders:** 755
   - **Files:** 644
5. Check **Recurse into subdirectories**
6. Click **Change Permissions**

### Step 6: Verify SSL Certificate

1. In cPanel main dashboard, find **SSL/TLS Status**
2. Verify **securitycocktailhour.com** has a green checkmark
3. If not, click **Run AutoSSL** and wait for it to complete
4. This may take 5-10 minutes

### Step 7: Test Your Website

1. Open browser (use Incognito/Private mode to avoid cache)
2. Visit: **https://securitycocktailhour.com**
3. Verify homepage loads correctly
4. Test these key pages:
   - https://securitycocktailhour.com/episodes/
   - https://securitycocktailhour.com/about/
   - https://securitycocktailhour.com/contact/
   - https://securitycocktailhour.com/privacy/
   - https://securitycocktailhour.com/terms/
   - https://securitycocktailhour.com/resources/

5. Test functionality:
   - Newsletter signup form (try subscribing)
   - Contact form (send test message)
   - Cookie consent banner (should appear on first visit)
   - Episode search and filtering
   - Social sharing buttons

### Step 8: Clear DNS Cache (If Needed)

If the site doesn't load:
1. Wait 10-15 minutes for DNS propagation
2. Clear your browser cache
3. Try different browser
4. Check on mobile device

---

## Important Files & Features Included

### Core Pages (73 total)
- Homepage with latest episodes
- Episode library (64 episodes) with search/filter
- Individual episode pages
- About page (host bios)
- Contact page (working Formspree form)
- Resources page
- Privacy Policy
- Terms of Service

### Integrations
✅ **Mailchimp Newsletter** - Forms on homepage, episodes, about, resources pages
✅ **Formspree Contact Form** - Working contact form
✅ **Google Analytics** - GA4 tracking (ID: G-8QL8F8JKNR)
✅ **Cookie Consent Banner** - GDPR compliant
✅ **XML Sitemap** - Located at /sitemap.xml

### SEO Features
- Schema.org podcast markup
- Open Graph meta tags
- Twitter Card meta tags
- Canonical URLs
- XML sitemap
- Clean URLs (no .html extensions)

---

## Troubleshooting

### Issue: Homepage shows directory listing instead of website
**Solution:** Rename `index.html` to make sure it's exactly `index.html` (lowercase, no spaces)

### Issue: CSS not loading (site looks unstyled)
**Solution:** Check file permissions - folders should be 755, files should be 644

### Issue: Images not displaying
**Solution:**
1. Check `/images/` folder exists
2. Verify file permissions
3. Check browser console for 404 errors

### Issue: Forms not working
**Solution:** Forms use external services:
- Newsletter: Mailchimp (should work immediately)
- Contact: Formspree (should work immediately)
- If issues, check browser console for errors

### Issue: SSL certificate error
**Solution:**
1. Go to cPanel → SSL/TLS Status
2. Click **Run AutoSSL**
3. Wait 5-10 minutes
4. If still failing, contact GoDaddy support

### Issue: Old site still showing
**Solution:**
1. Clear browser cache (Cmd+Shift+R on Mac)
2. Try incognito/private browsing
3. Wait 15 minutes for DNS propagation
4. Check on different device/network

---

## Post-Deployment Checklist

After deployment, verify:
- [ ] Homepage loads at https://securitycocktailhour.com
- [ ] All 64 episodes are accessible
- [ ] Newsletter signup works (test with your email)
- [ ] Contact form works (send test message)
- [ ] Cookie banner appears on first visit
- [ ] Google Analytics is tracking (check GA dashboard in 24 hours)
- [ ] Site works on mobile devices
- [ ] SSL certificate shows green padlock in browser
- [ ] All images display correctly
- [ ] Search and filter work on episodes page
- [ ] Privacy Policy and Terms pages are accessible

---

## Support Contacts

**If you need help:**
- GoDaddy Support: (480) 505-8877 (24/7)
- Formspree: support@formspree.io
- Mailchimp: https://mailchimp.com/contact/

**Website Source:**
- GitHub: https://github.com/security-cocktail-hour/security-cocktail-hour-website
- Local: `/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website/`

---

## Future Updates

To update the website in the future:
1. Edit files in the Hugo project locally
2. Test with `hugo server -D`
3. Build production: `hugo --cleanDestinationDir`
4. Upload new files from `public/` folder to cPanel
5. Or use this same ZIP method with new production-deployment.zip

---

**Deployment prepared by Claude Code**
**Date:** October 15, 2025
