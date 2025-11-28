# New Episode Deployment Process

**Last Updated**: November 27, 2025

---

## Overview

This document outlines the process for adding new episodes to the Security Cocktail Hour website and deploying them to production.

---

## What You Need to Provide

### 1. Episode Content File

Place the episode details in a text file (e.g., `working/content-answers.txt`) with the following information:

```
1. [Episode Number]
2. [Full Episode Title]
3. [Publication Date in YYYY-MM-DD format]
4. [Guest Name]
5. [Guest Bio - can be short form like "Guest Name, Title, Company"]
6. [Category - must be one of: AI, Career, Career Bio, Cryptocurrency Security, Educational, General, Hardware Security, Identity, Incident Response, Legal, Operational Technology (OT), Sales, Small Business, Threat Intel, Unboxing, Users]
7. [Duration in HH:MM:SS or MM:SS format]
8. [Episode Description - SEO-optimized meta description, 120-155 characters maximum]

9. Platform URLs:
YouTube: [URL]
Spotify: [URL]
Apple: [URL or note if not yet available]
Amazon: [URL or note if not yet available]

10. [Path to episode thumbnail image]
```

**Example:**
```
1. 62
2. AI in Cybersecurity: How CISOs Are Actually Using LLMs with Myke Lyons (Cribl CISO)
3. 2025-11-03
4. Myke Lyons
5. Myke Lyons, CISO, Cribl
6. AI
7. 57:50
8. Join Security Cocktail Hour hosts Joe Patti and Adam Roth for an in-depth conversation with Myke Lyons...

00:00 Intro
00:38 Welcome Myke Lyons
[timestamps]

#AI #LLM #Cybersecurity [hashtags]

9.
YouTube: https://youtu.be/lnbMS2B8lWk
Spotify: https://open.spotify.com/episode/...
Apple and Amazon URLs won't be available until it's published.
10. "working/episode-thumbnail.jpg"
```

### 2. Episode Thumbnail Image

- Place the image file in the `working/` directory
- Format: JPG preferred (smaller file size)
- Recommended size: 300x300px or larger
- File naming doesn't matter (it will be renamed during processing)

---

## Deployment Process

### Step 1: Provide Content to Claude

Simply tell Claude Code:
> "We're releasing a new episode. The content is in @working/content-answers.txt and the image is at [path]."

Or if you want to preview first:
> "We're releasing a new episode. I have the copy and graphics. I want to preview it on the dev site before creating the production package."

### Step 2: Claude Will Process

Claude will automatically:
1. Read the episode details from your content file
2. Copy the episode image to `static/images/episodes/episode-XXX.jpg`
3. Create the episode markdown file with proper formatting:
   - Bulleted timestamps (not plain text)
   - Bulleted topics (no hashtags)
   - Proper front matter with all metadata
4. Start the Hugo dev server with future posts enabled (`hugo server -D -F`)
5. Let you preview at http://localhost:1313/

### Step 3: Review and Approve

Review the episode on the dev site:
- Check the homepage shows the new episode
- Verify the episode page displays correctly
- Check image, timestamps, topics formatting
- Test platform links

### Step 4: Build and Deploy

Once approved, tell Claude:
> "I'm satisfied with this. Commit and build for production."

Claude will:
1. Stop the dev server
2. Commit changes to git with descriptive message
3. Push to GitHub (triggers automatic Netlify staging deployment)
4. Build production site (`hugo --minify`)
5. Create `production-deployment.zip` package

### Step 5: Upload to GoDaddy

Manually upload `production-deployment.zip` to GoDaddy cPanel:
1. Log into GoDaddy cPanel
2. Navigate to File Manager → public_html
3. Upload and extract `production-deployment.zip`
4. Verify deployment

See [GODADDY-DEPLOYMENT-INSTRUCTIONS.md](../GODADDY-DEPLOYMENT-INSTRUCTIONS.md) for detailed instructions.

---

## Important Notes

### Publication Dates and Visibility

**Hugo doesn't display future-dated episodes by default.**

- If episode date is **today or earlier**: Shows immediately on production
- If episode date is **tomorrow or future**: Won't show until that date arrives

**Options:**

1. **Publish immediately**: Set date to today or earlier (e.g., 2025-11-02)
2. **Schedule for future**: Set date to publication date (e.g., 2025-11-03)
   - Episode is included in deployment package
   - Will automatically appear on the specified date
   - No need to redeploy

**Development Preview:**
- Claude always starts dev server with `-F` flag to show future posts
- You can preview future-dated episodes locally before they go live

### Meta Description SEO Standards

**CRITICAL REQUIREMENT**: All episode descriptions must comply with SEO standards.

**Character Limits:**
- **Target**: 120 characters (optimal for mobile)
- **Maximum**: 155 characters (hard limit - Google truncates beyond this)

**Requirements:**
- ✅ Concise and compelling
- ✅ Include guest name if applicable
- ✅ Mention key topics covered
- ✅ Active voice, action-oriented
- ✅ Front-load important keywords
- ✅ Complete sentences (no truncation)
- ❌ No filler words or redundant phrases
- ❌ Never exceed 155 characters

**Good Example (127 chars):**
> "Jatin Mannepalli explores high-frequency trading security challenges, incident response, and custom hardware with Joe and Adam."

**Bad Example (656 chars - WAY too long):**
> "In this episode of the Security Cocktail Hour, guest Jatin Mannepalli introduces co-hosts Joe Patti and Adam Roth the high-speed, high stakes world of high frequency trading (HFT) and its many security challenges..."

**Tools Available:**
- Run `python3 scripts/audit_meta_descriptions.py` to check all descriptions
- See `reports/meta-description-audit-2025-11-27.md` for complete audit results

### Episode Format Standards

All episodes follow the standardized format documented in [SESSION_CONTEXT.md](../SESSION_CONTEXT.md#episode-content-structure):

**Episode Timestamps:**
```markdown
## Episode Timestamps

- 00:00 Intro
- 00:38 Welcome Guest Name
- 02:42 Topic description
```

**Topics Discussed:**
```markdown
## Topics Discussed

- AI
- Cybersecurity
- CISO
- Data Security
```

**Key Rules:**
- Use **bullet points** (dashes) for both sections
- Do NOT use hashtags (#) in Topics Discussed
- Homepage shows only description field
- Individual episode pages show all sections

### Platform URLs

If Apple Podcasts or Amazon Music URLs aren't available yet:
- Use the show's home page as placeholder:
  - Apple: `https://podcasts.apple.com/us/podcast/security-cocktail-hour/id1679376200`
  - Amazon: `https://music.amazon.com/podcasts/d11e431a-f7b1-4bb0-8671-024afce9ade6/security-cocktail-hour`
- Update later if needed (requires new deployment)

### Git Workflow

All changes are automatically:
1. Committed to git with descriptive message
2. Pushed to GitHub main branch
3. Deployed to Netlify staging (automatic)
4. Available for manual GoDaddy production deployment

Commit messages follow this format:
```
Add Episode XX: [Title]

- Add new episode with [guest name]
- Topic: [brief topic description]
- [other changes made]

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## Troubleshooting

### Episode Not Showing on Homepage

**Check the date:**
- Hugo doesn't show future-dated episodes
- Change episode date to today or earlier
- Rebuild and redeploy

### Image Not Displaying

**Check these:**
- Image exists at `static/images/episodes/episode-XXX.jpg`
- Episode markdown references correct image path
- Image is valid JPG/PNG format
- Hard refresh browser (Cmd+Shift+R / Ctrl+Shift+R)

### Formatting Issues

**Common fixes:**
- Timestamps not as bullets: Add `- ` before each timestamp
- Hashtags showing: Convert to plain text list without `#`
- Description too long on homepage: Check `layouts/index.html` template

### Deployment Package Size

Current package size: ~7.8MB (optimized)
- Episodes use JPG images (smaller than PNG)
- Images optimized for web
- Hugo minifies HTML/CSS/JS

---

## Quick Reference

**Start new episode:**
```
"We're releasing a new episode. Content is in @working/content-answers.txt"
```

**Preview first:**
```
"I want to see it on the dev site before building for production."
```

**Approve and deploy:**
```
"I'm satisfied. Commit and build for production."
```

**Change episode date:**
```
"Change the episode date to [date] so it shows immediately."
```

---

## Files and Locations

**Episode Content:**
- Markdown: `content/episodes/episode-XX-title-slug.md`
- Image: `static/images/episodes/episode-XXX.jpg`

**Production Package:**
- Location: `production-deployment.zip` (project root)
- Contents: Complete built site from `public/` directory

**Documentation:**
- This file: `NEW-EPISODE-DEPLOYMENT.md`
- Session context: `SESSION_CONTEXT.md`
- GoDaddy deployment: `GODADDY-DEPLOYMENT-INSTRUCTIONS.md`

**Staging Sites:**
- Netlify: Auto-deploys from GitHub
- Local dev: http://localhost:1313/ (when Hugo server running)

**Production:**
- GoDaddy cPanel: Manual upload of production-deployment.zip
- Live site: https://securitycocktailhour.com/

---

## Example Workflow

1. **Record and publish episode**
2. **Prepare content file** with episode details in `working/content-answers.txt`
3. **Add thumbnail image** to `working/` directory
4. **Tell Claude**: "We're releasing a new episode. Content in @working/content-answers.txt"
5. **Preview** at http://localhost:1313/
6. **Approve**: "Commit and build for production"
7. **Upload** `production-deployment.zip` to GoDaddy cPanel
8. **Verify** episode appears on https://securitycocktailhour.com/

---

**Need Help?**

Refer to [SESSION_CONTEXT.md](../SESSION_CONTEXT.md) for detailed project documentation and technical details.
