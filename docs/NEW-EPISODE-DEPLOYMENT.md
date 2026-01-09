# New Episode Deployment Process

**Last Updated**: January 8, 2026

---

## Overview

This document outlines the process for adding new episodes to the Security Cocktail Hour website and deploying them to production.

---

## What You Need to Provide

### 1. Episode Content File

Place the episode details in a text file (e.g., `working/content-answers.txt`) with the following information:

```
1. Episode Number
2. Full Episode Title (the complete title as you want it displayed)
3. Publication Date (YYYY-MM-DD format)
4. Guest Name (or "No guest" for solo episodes)
5. Guest Bio (short form like "Guest Name, Title, Company")
6. Category (must be one of: AI, Career, Career Bio, Cryptocurrency Security, Educational, General, Hardware Security, Identity, Incident Response, Legal, Operational Technology (OT), Sales, Small Business, Threat Intel, Unboxing, Users)
7. Duration (HH:MM:SS or MM:SS format)
8. Full Description (multiple paragraphs of body content for the episode page - this is where you explain what the episode is about, key topics covered, etc.)
9. Platform URLs:
   YouTube: [URL]
   Spotify: [URL]
   Apple: [URL or note if not yet available]
   Amazon: [URL or note if not yet available]
10. Episode thumbnail image path
11. Transcript file path (optional - if you have a transcript)
12. Related Episodes (optional - filenames like "episode-64-title.md, episode-45-title.md")
```

**Example:**
```
1. 66
2. Unboxing the Device Every Hacker Wants
3. 2025-12-15
4. No guest
5. N/A
6. Unboxing
7. 05:30
8. Pretty much everyone in the cybersecurity business has heard of the Flipper Zero, but many security pros have never actually seen one.

Since not everyone has the time to get their hands on one, we did and are unboxing it in this quick 5-minute episode.

This surprisingly compact hardware can:
- Test RFID systems and vulnerabilities
- Check infrared device security
- Identify wireless protocol weaknesses
- Run custom security testing apps

If you're defending networks, you need tools. This episode is the first in a series where we'll give you a look at the tools you can use to fight the bad guys.

9. Platform URLs:
YouTube: https://youtu.be/1wZTNDO_Yyc
Spotify: https://tinyurl.com/mrxxjz8h
Apple: https://tinyurl.com/jvhb6467
Amazon: https://tinyurl.com/4zuxzk4n
10. working/episode-66-thumbnail.jpg
11. working/transcript-ep-066.txt
12. (none)
```

### Claude Will Auto-Generate SEO Metadata

**You do NOT need to provide these** - Claude will generate them based on your full title and description, then present them for your approval:

1. **SEO Title** (only if full title exceeds 60 characters) - optimized for search results
2. **Meta Description** (120-155 chars) - SEO-compliant description for search snippets
3. **Tags** (5-8 relevant tags) - for categorization and SEO
4. **Topics Discussed** (bulleted list) - extracted from your full description

**Approval Process**: Claude will show you these generated items with character counts, you can approve or request revisions, and once approved, deployment proceeds.

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

### Step 2: Claude Will Generate SEO Metadata

Claude will automatically:
1. Read the episode details from your content file
2. Analyze the full title and description
3. Generate SEO-compliant metadata:
   - **SEO Title** (if full title > 60 chars)
   - **Meta Description** (120-155 chars)
   - **Tags** (5-8 relevant tags)
   - **Topics Discussed** (bulleted list)
4. Present these for your approval with character counts

**Example Output:**
```
SEO Title: "Unboxing the Device Every Hacker Wants" (40 chars) ✓
Meta Description: "Flipper Zero unboxed: RFID testing, infrared capabilities, hardware features, and ethical use of this security testing tool." (128 chars) ✓
Tags: flipper-zero, hardware, security-tools, pentesting, hacking-tools
Topics Discussed:
- RFID and NFC Testing
- Infrared Signal Replay
- Wireless Protocol Testing
- Hardware Security Tools
- Ethical Hacking
```

### Step 3: Review and Approve/Revise

Review the generated metadata:
- Check SEO title length and clarity
- Verify meta description is compelling and accurate
- Ensure tags are relevant
- Confirm topics list is complete

Then either:
- **Approve**: "Looks good, proceed"
- **Revise**: "Make the description more action-oriented" or "Add 'sub-ghz' as a tag"

### Step 4: Claude Builds Episode and Dev Preview

Once you approve the metadata, Claude will:
1. Copy the episode image to `static/images/episodes/episode-XXX.jpg`
2. Copy transcript (if provided) and format it properly
3. Create the episode markdown file with:
   - Approved SEO metadata in front matter
   - Full description as body content
   - Collapsible transcript section (if provided)
   - Related episodes (if specified)
4. Start the Hugo dev server with future posts enabled (`hugo server -D -F`)
5. Let you preview at http://localhost:1313/

### Step 5: Review Dev Site and Approve

Review the episode on the dev site:
- Check the homepage shows the new episode
- Verify the episode page displays correctly
- Check image, description, topics, transcript formatting
- Test platform links
- Verify SEO metadata appears correctly

### Step 5.5: Run Pre-Deployment Tests

After you've reviewed the dev site and are satisfied with the new episode, run the automated test suite to validate everything works correctly:

```bash
python3 scripts/tests/run_all_tests.py
```

**What gets tested:**
- ✅ New episode appears on homepage (latest episode section)
- ✅ Episode page loads correctly with all metadata
- ✅ All platform links present (YouTube, Spotify, Apple, Amazon)
- ✅ SEO metadata valid (title, description, og tags)
- ✅ Navigation working across all pages
- ✅ Related episodes displaying (if specified)
- ✅ Transcript section present (if included)
- ✅ No console errors
- ✅ All static pages still functioning
- ✅ Episodes list page search/filter working
- ✅ Blog page search/filter working

**Expected result:**
```
================================================================================
FINAL TEST SUMMARY
================================================================================
Static Pages:  ✅ PASSED
Episodes:      ✅ PASSED
Blog:          ✅ PASSED

TOTAL: 236+ passed, 0 failed
Duration: 4-5 minutes
================================================================================

✅ ALL TESTS PASSED - Ready for deployment!
```

**If tests fail:**
1. Review error messages in terminal output
2. Check failed test screenshots in `scripts/tests/test_screenshots/`
3. Fix issues in the episode markdown or templates
4. Re-run tests until all pass

**Quick test option (faster):**
If you only want to test the homepage and new episode quickly:
```bash
python3 scripts/tests/run_all_tests.py --static --episodes
```
This runs in ~30 seconds and tests the most critical pages.

**After all tests pass, clean up screenshots:**
```bash
rm -rf scripts/tests/test_screenshots
```
This removes any failure screenshots from previous test runs.

### Step 6: Build and Deploy

Once all tests pass, tell Claude:
> "Tests passed. Commit and build for production."

Claude will:
1. Stop the dev server
2. Commit changes to git with descriptive message
3. Push to GitHub (triggers automatic Netlify staging deployment)
4. Build production site (`hugo --minify`)
5. Create `production-deployment.zip` package

### Step 7: Upload to GoDaddy

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

### SEO Standards (Auto-Generated)

**AUTOMATED COMPLIANCE**: Claude automatically generates SEO-compliant metadata based on your content.

#### Meta Description Standards

Claude generates meta descriptions following these rules:
- **Length**: 120-155 characters (optimal range)
- **Content**: Concise, compelling, action-oriented
- **Structure**: Front-load keywords, include guest name if applicable
- **Voice**: Active voice, no filler words
- **Completeness**: Full sentences, no truncation

**You Review and Approve**: Claude presents the generated description with character count for your approval before proceeding.

**Reference:** See `docs/SEO-META-DESCRIPTION-STANDARDS.md` for complete guidelines.

#### SEO Title Standards

Claude generates optimized SEO titles when needed:
- **When**: Only if full title exceeds 60 characters
- **Length**: 50-60 characters (optimal for search results)
- **Purpose**: Prevents truncation in search results while preserving full title for page display

**Dual-Title System:**
```yaml
---
title: "Full Episode Title with Guest Name and Context"  # For page display, Schema.org
seo_title: "Shortened Title for Search Results"  # For HTML <title> tag only
---
```

**You Review and Approve**: Claude shows the generated SEO title with character count for your approval.

**Reference:** See `docs/SEO-TITLE-TAG-STANDARDS.md` for complete guidelines and examples.

#### Tags and Topics

Claude automatically generates:
- **Tags**: 5-8 relevant tags based on episode content (for SEO and categorization)
- **Topics Discussed**: Bulleted list extracted from your full description

**You Review and Approve**: You can request additions, removals, or revisions to both before proceeding.

### Episode Transcripts (Optional)

**New Feature (December 2, 2025)**: Episode transcripts are now automatically displayed in a collapsible accordion for better user experience while maintaining full SEO benefits.

**How It Works:**
- If your episode markdown includes a section with heading `## Full Episode Transcript`, it will automatically be converted to a collapsible accordion
- Content before the transcript displays normally
- Transcript is collapsed by default, expands when user clicks
- All transcript content remains in HTML DOM for full search engine indexing (SEO-friendly)

**Adding a Transcript:**
```markdown
## Topics Discussed

- Topic 1
- Topic 2

## Full Episode Transcript

**Speaker Name [00:00]:**
Transcript text here...

**Another Speaker [01:30]:**
More transcript text...
```

**SEO Benefits:**
- ✅ Google fully indexes content within `<details>` elements
- ✅ No "hidden content" penalty
- ✅ Transcripts improve keyword ranking
- ✅ Better UX (page not overwhelmingly long)

**Design:**
- Matches current site aesthetic (blue gradient header)
- Mobile responsive (scrollable content area)
- Smooth animations
- Accessible (keyboard navigation, screen readers)

### Related Episodes

**New Feature (December 2, 2025)**: Episodes can now specify custom related episodes instead of using auto-generated recommendations.

**Auto-Generated (Default):**
- By default, related episodes are selected based on matching category
- Shows up to 3 related episodes in sidebar

**Manual Override (Optional):**
If you want to specify which episodes should be shown as related, add this to the episode frontmatter:

```yaml
---
title: "Episode Title"
date: 2025-12-02
category: "Educational"
related_episodes:
  - "episode-61-ai-attacks-need-ai-defense-ransomwares-new-danger-and-how-a-top-cyber-expert-is-.md"
  - "episode-58-travel-router-unboxing-dont-get-hacked-on-vacation.md"
---
```

**How to Find Episode Filenames:**
```bash
ls content/episodes/ | grep -i "topic-keyword"
```

**Use Cases:**
- Episode is part of a series
- Want to link thematically related episodes
- Cross-promote different categories
- Feature flagship episodes

### Episode Content Structure

Episodes are automatically structured with:

**Front Matter (Auto-Generated):**
```yaml
---
title: "Full Episode Title"
seo_title: "SEO Title"  # Only if title > 60 chars
date: 2025-12-21
category: "Category"
duration: "HH:MM:SS"
image: "/images/episodes/episode-XXX.jpg"
description: "SEO meta description (120-155 chars)"
platforms:
  youtube: "URL"
  spotify: "URL"
  apple: "URL"
  amazon: "URL"
tags:
  - tag1
  - tag2
related_episodes:  # Optional
  - "episode-XX-title.md"
---
```

**Body Content:**
- Your full description (multiple paragraphs)
- Additional sections as needed
- Topics Discussed (auto-generated bulleted list)
- Full Episode Transcript (auto-formatted in collapsible accordion)

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

### Test Failures

**If pre-deployment tests fail:**

1. **Review the error output** - Terminal shows which specific test failed
2. **Check screenshots** - Failed tests save screenshots to `scripts/tests/test_screenshots/`
3. **Common issues:**
   - Missing platform links: Add all 4 platform URLs to episode frontmatter
   - Episode not on homepage: Check episode date isn't in the future
   - Broken navigation: Verify Hugo server is still running
   - SEO metadata missing: Ensure `seo_title` and `description` in frontmatter
4. **Fix the issue** in the episode markdown file
5. **Re-run tests** until all pass
6. **Clean up screenshots** with `rm -rf scripts/tests/test_screenshots`

**For detailed test documentation**, see `scripts/tests/README.md`

---

## Quick Reference

**Start new episode:**
```
"We're releasing a new episode. Content is in @working/content-answers.txt"
```

**Review generated SEO metadata:**
Claude will present SEO title, meta description, tags, and topics for your approval.

**Approve metadata:**
```
"Looks good, proceed with the episode"
```

**Request revisions:**
```
"Make the description more action-oriented"
"Add 'ransomware' as a tag"
"The SEO title is too long, shorten it"
```

**Preview on dev site:**
After metadata approval, Claude builds the episode and starts dev server.

**Run pre-deployment tests:**
```
python3 scripts/tests/run_all_tests.py
```

**Clean up after testing:**
```
rm -rf scripts/tests/test_screenshots
```

**Approve final build (after tests pass):**
```
"Tests passed. Commit and build for production."
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
- Session context: `CLAUDE.md`
- GoDaddy deployment: `GODADDY-DEPLOYMENT-INSTRUCTIONS.md`
- Testing documentation: `scripts/tests/README.md`

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
6. **Run tests**: `python3 scripts/tests/run_all_tests.py`
7. **Clean up**: `rm -rf scripts/tests/test_screenshots`
8. **Approve**: "Tests passed. Commit and build for production"
9. **Upload** `production-deployment.zip` to GoDaddy cPanel
10. **Verify** episode appears on https://securitycocktailhour.com/

---

**Need Help?**

Refer to [CLAUDE.md](../CLAUDE.md) for detailed project documentation and technical details.
