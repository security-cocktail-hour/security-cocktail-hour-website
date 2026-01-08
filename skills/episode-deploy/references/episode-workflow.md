# Episode Deployment Workflow

This document outlines the complete workflow for deploying new episodes to the Security Cocktail Hour website.

---

## Workflow Overview

1. **Gather episode information** from user
2. **Detect and format transcript** (if provided)
3. **Auto-generate SEO metadata** (title, description, tags, topics)
4. **Present metadata for approval** (user reviews and approves/revises)
5. **Build episode files** (markdown, image, transcript)
6. **Start dev server** for preview
7. **User approves** final episode
8. **Commit to git** and push to GitHub
9. **Build production package** with validation
10. **User deploys to GoDaddy** manually

---

## Step 1: Gather Episode Information

User provides episode details in `working/content-answers.txt` with the following format:

```
1. Episode Number
2. Full Episode Title (the complete title as you want it displayed)
3. Publication Date (YYYY-MM-DD format)
4. Guest Name (or "No guest" for solo episodes)
5. Guest Bio (short form like "Guest Name, Title, Company")
6. Category (must be one of: AI, Career, Career Bio, Cryptocurrency Security, Educational, General, Hardware Security, Identity, Incident Response, Legal, Operational Technology (OT), Sales, Small Business, Threat Intel, Unboxing, Users)
7. Duration (HH:MM:SS or MM:SS format)
8. Full Description (multiple paragraphs of body content for the episode page)
9. Platform URLs:
   YouTube: [URL]
   Spotify: [URL]
   Apple: [URL or note if not yet available]
   Amazon: [URL or note if not yet available]
10. Episode thumbnail image path
11. Transcript file path (optional)
12. Related Episodes (optional - filenames like "episode-64-title.md")
```

### Read and Parse Content File

- Read `working/content-answers.txt`
- Parse each numbered field
- Extract all information into structured data
- Validate required fields are present
- Check category is valid

---

## Step 2: Detect and Format Transcript

If transcript file path is provided (field 11):

### Detect Transcript Format

Use detection logic to identify format:
- **DaVinci Resolve format**: `[HH:MM:SS:FF - HH:MM:SS:FF]`
- **Generic format**: `Speaker [MM:SS]`
- **Standard format**: `*Speaker (MM:SS)*`

See `references/transcript-formats.md` for detailed format specifications.

### Convert Transcript

Based on detected format:
- **DaVinci**: Use `scripts/format_davinci_transcript.py`
- **Generic**: Use `scripts/format_transcript.py`
- **Standard**: No conversion needed
- **Unknown**: Report error, ask user for guidance

### Conversion Command

```bash
python3 scripts/format_[type]_transcript.py working/input.txt working/ep[XX]-transcript-formatted.txt
```

### Verify Output

- Check formatted transcript exists
- Verify format matches standard: `*Speaker (MM:SS)*`
- Confirm line count is reasonable
- Report success to user

---

## Step 3: Auto-Generate SEO Metadata

Based on the full title and description provided by user, automatically generate:

### SEO Title (Conditional)

**When to generate:**
- Only if full title exceeds 60 characters

**Requirements:**
- 50-60 characters target
- Primary keywords at start
- Remove unnecessary words ("with", "about", guest credentials)
- Maintain clarity and accuracy

**Example:**
```
Full title: "AI in Cybersecurity: How CISOs Are Actually Using LLMs with Myke Lyons (Cribl CISO)"
SEO title: "AI in Cybersecurity: How CISOs Are Actually Using LLMs" (59 chars)
```

### Meta Description (Always Required)

**Requirements:**
- 120-155 characters (target 120 for mobile)
- Active voice, compelling
- Front-load keywords
- No filler phrases ("In this episode", "Join us")
- Specific and descriptive

**Format for episodes:**
```
[Guest name] [action verb] [key topics] with Joe and Adam.
```

**Example:**
```
"Learn how to update your Flipper Zero firmware with this complete walkthrough, including troubleshooting tips for common issues during the update process."
(155 chars)
```

### Tags (Always Required)

**Requirements:**
- 5-8 relevant tags
- Lowercase with hyphens
- Mix of specific and general terms
- Include tool/technology names when applicable

**Example:**
```yaml
tags:
  - flipper-zero
  - firmware-update
  - hardware-security
  - security-tools
  - troubleshooting
  - device-maintenance
  - pentesting
```

### Topics Discussed (Always Required)

**Requirements:**
- 4-7 key topics
- Brief but descriptive (3-8 words)
- Extracted from full description
- Title case
- Most important topics first

**Example:**
```markdown
## Topics Discussed

- Flipper Zero Device Overview
- Flipper Desktop App Setup
- Firmware Update Process
- Troubleshooting Update Issues
- Device Recovery Methods
- Keeping Security Tools Updated
```

---

## Step 4: Present Metadata for User Approval

Display generated metadata to user with character counts:

```
SEO Metadata Generated:

SEO Title: "Flipper Zero Firmware Update: Complete Walkthrough" (53 chars) ✓
Meta Description: "Learn how to update your Flipper Zero firmware with this complete walkthrough, including troubleshooting tips for common issues during the update process." (155 chars) ✓

Tags:
- flipper-zero
- firmware-update
- hardware-security
- security-tools
- troubleshooting
- device-maintenance
- pentesting

Topics Discussed:
- Flipper Zero Device Overview
- Flipper Desktop App Setup
- Firmware Update Process
- Troubleshooting Update Issues
- Device Recovery Methods
- Keeping Security Tools Updated

Please review and approve or request revisions.
```

### Handle User Response

**If approved:**
- Proceed to Step 5

**If revisions requested:**
- Make requested changes
- Re-present metadata
- Wait for approval

### Common Revision Requests

- "Make the description more action-oriented"
- "Add '[tag]' as a tag"
- "Change the third topic to '[new topic]'"
- "The SEO title is too long, shorten it"
- "Remove the '[word]' from the description"

---

## Step 5: Build Episode Files

Once metadata is approved, build all episode files:

### Copy Episode Image

```bash
cp [source-image-path] static/images/episodes/episode-[XXX].jpg
```

- Use zero-padded 3-digit episode number (e.g., `episode-067.jpg`)
- Always use `.jpg` extension (even if source is PNG)
- Verify copy succeeded

### Create Episode Markdown File

**File path:** `content/episodes/episode-[XX]-[title-slug].md`

**Title slug rules:**
- Convert to lowercase
- Replace spaces with hyphens
- Remove special characters (except hyphens)
- Keep reasonably short (5-8 words max)

**Front matter template:**

```yaml
---
title: "[Full Episode Title]"
seo_title: "[SEO Title]"  # Only if title > 60 chars
date: YYYY-MM-DD
guest: "[Guest Name]"  # Or omit if no guest
category: "[Category]"
duration: "HH:MM:SS"
image: "/images/episodes/episode-XXX.jpg"
description: "[Meta Description]"
platforms:
  youtube: "[URL]"
  spotify: "[URL]"
  apple: "[URL]"
  amazon: "[URL]"
tags:
  - tag1
  - tag2
  - tag3
related_episodes:  # Optional
  - "episode-XX-title.md"
---
```

**Body content:**

1. Full description (as provided by user)
2. Topics Discussed section (auto-generated)
3. Full Episode Transcript section (if transcript provided)

**Example body:**

```markdown
[Full description paragraphs here]

## Topics Discussed

- Topic 1
- Topic 2
- Topic 3

## Full Episode Transcript

[Formatted transcript content here]
```

### Handle Related Episodes

If user provided related episodes (field 12):
- Parse the filenames
- Add to `related_episodes:` array in front matter
- Verify files exist (optional validation)

If no related episodes provided:
- Omit `related_episodes:` field
- Hugo will auto-generate based on matching category

---

## Step 6: Start Dev Server for Preview

Start Hugo development server with future posts enabled:

```bash
hugo server -D -F
```

**Flags:**
- `-D`: Show draft posts
- `-F`: Show future-dated posts

Inform user:
```
Development server started at http://localhost:1313/

Please review:
- Homepage shows the new episode
- Episode page displays correctly
- Image, description, topics are accurate
- Transcript formatting is correct (if included)
- Platform links work
- SEO metadata appears correctly in page source

Let me know when you're satisfied or if you need changes.
```

---

## Step 7: User Approves Final Episode

Wait for user approval:

**Possible responses:**
- "I'm satisfied. Commit and build for production."
- "Looks good, commit and build."
- "Change [X] to [Y]" (make changes, continue in dev mode)
- "The date should be [date]" (update date, rebuild)

**If changes requested:**
- Make the requested changes
- Hugo auto-reloads
- Wait for next approval

**If approved:**
- Stop dev server
- Proceed to Step 8

---

## Step 8: Commit to Git and Push

### Stop Dev Server

```bash
# Kill the Hugo server process
```

### Git Workflow

```bash
git add -A
git commit -m "[commit message]"
git push origin main
```

**Commit message format:**

```
Add Episode [XX]: [Title]

- Add new episode with [guest name or "solo episode"]
- Topic: [brief topic description]
- [Additional changes made, e.g., "Add DaVinci transcript formatter"]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

**Example:**

```
Add Episode 67: Flipper Zero Firmware Update

- Add new episode solo episode
- Topic: Firmware update walkthrough with troubleshooting
- Duration: 15:55
- Full transcript included (~440 lines)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

See `references/git-standards.md` for complete git commit standards.

### Verify Push

Confirm push succeeded:
```bash
git log -1 --oneline
```

Report commit hash and success to user.

---

## Step 9: Build Production Package

### Use Automated Build Script

**ALWAYS use the automated build script:**

```bash
./scripts/build_production.sh
```

**Why this is mandatory:**
- Validates .htaccess file integrity (before build)
- Runs `hugo --minify` to build production site
- Re-validates .htaccess in built package (after build)
- Creates timestamped deployment ZIP
- Prevents broken 404 pages and missing redirects

**Never use manual build:**
```bash
hugo --minify  # DON'T USE THIS DIRECTLY
```

### Build Script Output

Script will display:
- Validation status for .htaccess
- All 24 required 301 redirects verified
- 404 error page configuration verified
- Security headers verified
- Build completion status
- Package filename and size

**Example output:**
```
✓ .htaccess validation passed
✓ Hugo build completed
✓ Production package created: production-deployment-20251222-105612.zip (8.2MB, 367 files)

Ready for deployment to GoDaddy cPanel.
```

### Handle Build Errors

If validation fails:
- Script exits with code 1
- DO NOT deploy
- Review error messages
- Fix issues
- Run build script again

---

## Step 10: User Deploys to GoDaddy

**This step is ALWAYS manual** - never attempt to automate GoDaddy deployment.

### Inform User

```
Production package ready: production-deployment-[timestamp].zip

Please deploy manually to GoDaddy:
1. Log into GoDaddy cPanel
2. Navigate to File Manager → public_html
3. Delete old files (backup first if needed)
4. Upload and extract production-deployment-[timestamp].zip
5. Verify .htaccess permissions are 644
6. Test site at https://securitycocktailhour.com/

See GODADDY-DEPLOYMENT-INSTRUCTIONS.md for detailed instructions.
```

### Wait for Confirmation

User will respond with:
- "production deployment complete"
- "deployed"
- "live"

Once confirmed, proceed to update SESSION_CONTEXT.md.

---

## Step 11: Update SESSION_CONTEXT.md (Optional)

**Important:** Always ask before updating SESSION_CONTEXT.md.

User may respond:
- "Update SESSION_CONTEXT with Episode [XX]"
- "Update session context"

**What to update:**

1. **Recent Completed Work section:**
   - Add new entry for the episode
   - Include episode number, title, date
   - Note key details (duration, category, transcript included)
   - Include commit hash
   - Include production package filename and size
   - Mark as "DEPLOYED TO PRODUCTION"

2. **Latest Production Package:**
   - Update filename and timestamp
   - Update file count if changed
   - Update deployment date
   - Update "Includes" line with new episode

3. **Current Site Status:**
   - Increment episode count
   - Increment page count
   - Update "Latest Episode" reference
   - Update "Episode XX live and accessible" line

4. **Last Updated date:**
   - Update to current date

---

## Error Handling

### Transcript Format Not Recognized

**Error:** Unknown transcript format

**Response:**
1. Describe what was found in the transcript file
2. Recommend creating a new handler script
3. Ask user how they'd like to proceed

**Example:**
```
I've detected a new transcript format in [file]:
- Lines appear to match: [pattern]
- Example: [show example]

This format is not currently supported. I recommend:
1. Create a new handler script: scripts/format_[type]_transcript.py
2. Add detection logic for this format
3. Copy handler to skill for future use

Would you like me to create a handler script for this format?
```

### Build Validation Failed

**Error:** .htaccess validation failed

**Response:**
1. Describe validation error
2. Explain impact
3. DO NOT proceed with deployment
4. Recommend fix

**Example:**
```
Build validation failed:
- Missing 404 error directive in .htaccess
- This will cause default Apache 404 page to show instead of custom page
- Impact: Poor user experience, Google indexing issues

DO NOT DEPLOY THIS PACKAGE.

Recommended fix:
1. Add "ErrorDocument 404 /404.html" to static/.htaccess
2. Run build script again
```

### Missing Required Information

**Error:** User content file missing required fields

**Response:**
1. List missing fields
2. Ask user to provide missing information
3. Do not proceed until all required fields are present

**Example:**
```
Missing required information in content-answers.txt:
- Field 6: Category
- Field 7: Duration

Please provide:
- Category (one of: AI, Career, Hardware Security, etc.)
- Duration (HH:MM:SS or MM:SS format)
```

---

## Best Practices

### Communication
- Always show character counts for SEO fields
- Present metadata clearly for easy review
- Explain validation errors in plain language
- Provide specific recommendations when errors occur

### File Handling
- Always use UTF-8 encoding
- Verify files exist before reading
- Check file operations succeeded
- Clean up temporary files when done

### Quality Control
- Validate all generated metadata before presenting
- Double-check episode numbering
- Verify image copy succeeded
- Confirm git push succeeded
- Check production package exists and has reasonable size

### User Experience
- Present information in digestible chunks
- Wait for explicit approval at checkpoints
- Don't batch multiple approvals into one
- Keep user informed of progress
- Explain what's happening at each step

---

**Last Updated**: December 22, 2025
