# Blog Post Deployment Workflow

**Security Cocktail Hour Website - Complete Blog Post Deployment Process**
**Version:** 1.0
**Last Updated:** January 9, 2026

---

## Overview

This document provides a step-by-step workflow for deploying new blog posts to the Security Cocktail Hour website. The process includes content preparation, SEO metadata generation, development preview, automated testing, git management, production build, and manual deployment.

**Total time:** 15-25 minutes (depending on content length and revisions)

---

## Phase 1: Content Preparation

### Step 1: Gather Blog Post Information

**Input file:** `working/blog-answers.txt`

Read and parse the 9 numbered fields:

```
1. Blog Post Title
[Full article title]

2. Publication Date
[YYYY-MM-DD]

3. Author Name
[Joe Patti / Adam Roth / other]

4. Category
[AI Security / Career / Cloud Security / etc.]

5. Featured
[yes / no]

6. Related Episode
[episode-filename.md / none]

7. Article Content
[Full markdown content with H2 headings, paragraphs, lists, etc.]

8. Key Takeaways
[3-5 bulleted points summarizing main lessons]

9. Blog Image Path
[path to image file / none]
```

**Validation:**
- Check all required fields are present (1-4, 7)
- Verify date format is YYYY-MM-DD
- Confirm category matches predefined list
- Validate author name (for bio lookup)

**If validation fails:**
List missing/invalid fields and wait for user to provide correct information.

---

### Step 2: Auto-Generate SEO Metadata

Generate SEO-compliant metadata from user's content:

#### Meta Description
- **Target:** 120-155 characters
- **Strategy:** Combine title + first sentence or opening paragraph
- **Format:** Active voice, front-load keywords, no filler phrases
- **Validation:** Count characters, ensure within range

**Example generation logic:**
```
Title: "4 Dangerous Job Scams Targeting Professionals in 2025"
First sentence: "Cybercriminals are using increasingly sophisticated techniques to target job seekers with fake interviews, cryptocurrency schemes, and data harvesting operations."

Generated description: "Discover 4 dangerous job scams targeting professionals in 2025, including fake interviews, cryptocurrency schemes, and data harvesting operations." (148 chars) ✓
```

#### Tags
- **Target:** 5-8 tags
- **Strategy:** Extract from category + key topics in content + key takeaways
- **Format:** Lowercase with hyphens

**Example generation logic:**
```
Category: "AI Security"
Key topics from content: job scams, social engineering, scam prevention, professional security
Key takeaways topics: fake interviews, cryptocurrency, data harvesting

Generated tags: ["job-scams", "social-engineering", "cybersecurity-awareness", "professional-security", "scam-prevention", "ai-security"]
(6 tags total) ✓
```

#### Author Information
- **Lookup:** Match author name to predefined profiles
- **Auto-populate:** author_bio, author_twitter, author_linkedin

**Joe Patti profile:**
```yaml
author_bio: "Joe Patti is the co-host of Security Cocktail Hour and a cybersecurity professional with extensive experience in IT and security operations. He brings practical insights from years of hands-on security work, helping professionals navigate the complex world of cybersecurity."
author_twitter: "@SecCocktailHour"
author_linkedin: "https://www.linkedin.com/in/joe-patti/"
```

**Adam Roth profile:**
```yaml
author_bio: "Adam Roth is the co-host of Security Cocktail Hour and a cybersecurity professional specializing in network security and threat detection. His background in technical security operations provides valuable perspectives on emerging threats and security best practices."
author_twitter: "@SecCocktailHour"
author_linkedin: "https://www.linkedin.com/in/adam-roth-security/"
```

#### Key Takeaways Structure
- **Source:** Field 8 from blog-answers.txt
- **Format:** Verify it's a bulleted list
- **Validation:** Count bullet points (should be 3-5)
- **Ensure:** Dedicated H2 section `## Key Takeaways` will be added to content

---

### Step 3: Validate Content Structure

Before proceeding, check content structure for SEO best practices:

**Required elements:**
- ✅ Opening paragraph (first paragraph)
- ✅ H2 headings (at least 2 for content organization)
- ✅ Key Takeaways section (from field 8)

**Check for:**
- H2 headings: `grep -c "^## " [content]`
- Article length: Word count (target: >500 words)
- Paragraph length: Flag paragraphs >150 words

**Warning levels:**
- ⚠️ **No H2 headings:** "Consider adding section headers for better SEO."
- ⚠️ **Short content (<500 words):** "Consider expanding for better SEO performance."
- ⚠️ **Long paragraphs:** "Some paragraphs exceed 150 words. Consider breaking into smaller chunks."

**Note:** These are warnings, not blocking errors. User can proceed if desired.

---

### Step 4: Present Metadata for Approval (CHECKPOINT 1)

Present all generated metadata with validation indicators:

```
SEO Metadata Generated:

Title: "[Blog Post Title]" (XX chars) ✓
Meta Description: "[Generated Description]" (XXX chars) ✓

Category: [Category Name]
Featured: [yes/no]
Related Episode: [episode-filename or none]

Author: [Author Name]
Author Bio: "[Auto-populated bio...]"
Author Twitter: @SecCocktailHour
Author LinkedIn: [LinkedIn URL]

Tags:
- tag1
- tag2
- tag3
...

Key Takeaways:
- Takeaway 1
- Takeaway 2
- Takeaway 3
...

Content Structure Check:
✓ H2 headings present (X found)
✓ Key Takeaways section present
✓ Article length: XXX words
⚠ [Any warnings if applicable]

Please review and approve or request revisions.
```

**Wait for explicit approval:**
- "Approved" / "Looks good" / "Perfect" → Proceed to Step 5
- "Change [specific thing]" → Make changes, re-present
- "Add [tag/topic]" → Update metadata, re-present

**Common revision requests:**
- Meta description adjustments (tone, keywords, length)
- Tag additions or removals
- Key takeaway wording changes
- Author bio customization (for guest authors)

---

## Phase 2: Build & Test

### Step 5: Build Blog Post Files

Create markdown file with generated metadata:

**File naming:**
1. Generate slug from title:
   - Convert to lowercase
   - Replace spaces with hyphens
   - Remove special characters
   - Remove leading articles (a, an, the)
   - Limit to 5-8 words

**Example slug generation:**
```
Title: "4 Dangerous Job Scams Targeting Professionals in 2025"
Slug: "dangerous-job-scams-targeting-professionals-2025"
Filename: dangerous-job-scams-targeting-professionals-2025.md
Location: content/blog/dangerous-job-scams-targeting-professionals-2025.md
```

**Front matter format:**
```yaml
---
title: "[Blog Post Title]"
date: [YYYY-MM-DD]
draft: false
author: "[Author Name]"
author_bio: "[Auto-populated author bio]"
author_twitter: "@SecCocktailHour"
author_linkedin: "[Auto-populated LinkedIn URL]"
category: "[Category Name]"
tags: ["tag1", "tag2", "tag3", "tag4", "tag5"]
description: "[Meta description 120-155 chars]"
featured: [true/false]
related_episode: "[episode-filename.md or omit if none]"
---
```

**Content structure:**
1. Opening paragraph
2. H2 sections with content
3. `## Key Takeaways` section (from field 8)
4. Conclusion paragraph/section

**Confirm file created:**
```bash
ls -lh content/blog/[slug].md
```

---

### Step 6: Copy Blog Image (If Provided)

If field 9 contains image path:

**Copy image:**
```bash
cp [source-path] static/images/blog/[original-filename]
```

**Validation:**
```bash
ls -lh static/images/blog/[filename]
file static/images/blog/[filename]  # Verify it's an image
```

**Image requirements:**
- Format: JPG, PNG, or WebP
- Recommended size: 1200×630px (optimal for social sharing)
- File size: <500KB recommended

**If image missing:** Blog post will use default/fallback image (acceptable).

---

### Step 7: Start Dev Server

Launch Hugo development server:

```bash
hugo server -D
```

**Flags:**
- `-D` - Include draft content (in case draft: true is set)

**Confirm server started:**
```
Web Server is available at http://localhost:1313/
```

**Open in browser:**
- Homepage: http://localhost:1313/
- Blog list: http://localhost:1313/blog/
- Blog post: http://localhost:1313/blog/[slug]/

---

### Step 8: User Approves Blog Post (CHECKPOINT 2)

Instruct user to review on dev site:

```
Development server started at http://localhost:1313/

Please review:
1. Blog list page (http://localhost:1313/blog/) shows the new post
2. Blog post displays correctly at http://localhost:1313/blog/[slug]/
3. Title, author, date, category are accurate
4. Content formatting is correct (headings, lists, bold text)
5. Key Takeaways section is formatted properly
6. Related episode link works (if applicable)
7. Blog image displays (if included)
8. SEO metadata appears correctly (right-click > View Page Source)

Let me know when you're satisfied or if you need changes.
```

**Wait for explicit approval:**
- "I'm satisfied" / "Looks good" / "Perfect" → Proceed to Step 9
- "Change [specific thing]" → Make changes, keep server running
- "The [element] looks wrong" → Investigate, fix, ask to refresh browser

**Common issues:**
- Blog post not in list: Check date is not in future
- Formatting off: Check markdown syntax
- Image not displaying: Verify image path in static/images/blog/
- Related episode link 404: Verify episode filename is correct

---

### Step 9: Run Pre-Deployment Tests

After dev site approval, run automated test suite:

```bash
python3 scripts/tests/run_all_tests.py --blog
```

**Test coverage:**
- Blog list page (loads, search works, filter works)
- 5 latest blog posts (currently all 4, scales automatically)
- Validation checks per page:
  - Page loads successfully (200 status)
  - Meta description present (120-155 chars)
  - Title tag present (≤60 chars preferred)
  - No console errors
  - Content renders correctly
  - Related episode link works (if present)

**Expected output:**
```
Testing Blog Pages...
✓ Blog list page loaded successfully
✓ Blog search functionality working
✓ Blog filter functionality working
✓ Blog post: dangerous-job-scams-targeting-professionals-2025
✓ Blog post: [other recent posts...]

All tests passed! (X pages tested in ~XX seconds)
```

**Test duration:** ~1 minute for blog tests

**If tests pass:** Proceed to Step 10

**If tests fail:**
1. Review test output for specific failures
2. Check `scripts/tests/test_screenshots/` for visual debugging
3. Explain issue to user with specifics:
   - Which page failed
   - What validation check failed
   - Likely cause
4. Recommend specific fix
5. After fix, re-run tests: `python3 scripts/tests/run_all_tests.py --blog`
6. **DO NOT proceed until all tests pass**

**Example failure explanation:**
```
Pre-deployment tests failed (1 test):

Blog post page (dangerous-job-scams-targeting-professionals-2025):
- Meta description exceeds 155 chars (currently 168 chars)
- Fix: Edit content/blog/dangerous-job-scams-targeting-professionals-2025.md
  and shorten the description field to ≤155 chars

Screenshot saved to: scripts/tests/test_screenshots/blog_post_dangerous-job-scams-targeting-professionals-2025_failed.png

Please fix this issue and I'll re-run the tests.
```

---

### Step 10: Clean Up Test Screenshots

After tests pass, remove test artifacts:

```bash
rm -rf scripts/tests/test_screenshots
```

**Confirmation:**
```bash
ls scripts/tests/test_screenshots  # Should return: No such file or directory
```

---

## Phase 3: Production Deployment

### Step 11: Commit to Git and Push

Create git commit with standardized message:

**Git workflow:**
```bash
git add -A
git commit -m "$(cat <<'EOF'
Add Blog Post: [Blog Post Title]

Category: [Category Name]
Author: [Author Name]
Date: [Publication Date]
Featured: [yes/no]
Related Episode: [episode-XX-slug or none]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
git push origin main
```

**Example commit:**
```
Add Blog Post: 4 Dangerous Job Scams Targeting Professionals in 2025

Category: AI Security
Author: Joe Patti
Date: 2025-11-26
Featured: yes
Related Episode: episode-64-job-scams

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

**Validation:**
```bash
git log -1 --oneline  # Verify commit exists
git status            # Should show "Your branch is ahead of 'origin/main' by 1 commit"
```

**After push:**
```bash
git status  # Should show "Your branch is up to date with 'origin/main'"
```

**Note:** This triggers Netlify staging deployment automatically (not production).

---

### Step 12: Build Production Package

Run production build script with validation:

```bash
./scripts/build_production.sh
```

**What this does:**
1. Validates `.htaccess` file integrity (before build)
2. Runs `hugo --minify` to build production site
3. Re-validates `.htaccess` in built package (after build)
4. Creates timestamped deployment ZIP: `production-deployment-YYYYMMDD-HHMMSS.zip`
5. Displays validation summary and deployment instructions

**Expected output:**
```
=== Production Build with .htaccess Validation ===

Step 1: Validating .htaccess file integrity...
✓ .htaccess validation passed

Step 2: Building Hugo site...
✓ Hugo build completed (XXX pages)

Step 3: Re-validating .htaccess in build package...
✓ .htaccess validation passed in public/

Step 4: Creating deployment package...
✓ Created: production-deployment-YYYYMMDD-HHMMSS.zip (X.XMB)

=== Build Complete ===
Production package ready for deployment to GoDaddy cPanel.
```

**Exit codes:**
- **0 = Success** - All checks passed, safe to deploy
- **1 = Failure** - Validation failed, DO NOT deploy

**If validation fails:**
1. Explain the specific error
2. State clearly: "DO NOT DEPLOY THIS PACKAGE"
3. Recommend fix
4. Wait for user to fix
5. Re-run build script

**If build succeeds:**
Confirm package exists and has reasonable size:
```bash
ls -lh production-deployment-*.zip
```

---

### Step 13: User Deploys to GoDaddy (CHECKPOINT 3)

Present deployment summary:

```
Production package built: production-deployment-YYYYMMDD-HHMMSS.zip

Changes in this deployment:
- New blog post: "[Blog Post Title]"
- [X] total blog posts on site
- Package size: X.XMB

The package is ready for deployment to GoDaddy cPanel.

Please deploy manually using the instructions in GODADDY-DEPLOYMENT-INSTRUCTIONS.md

Quick Steps:
1. Log into GoDaddy cPanel
2. Navigate to File Manager > public_html/
3. Backup current files (optional but recommended)
4. Delete old files
5. Upload and extract production-deployment-YYYYMMDD-HHMMSS.zip
6. Verify .htaccess permissions are 644
7. Test site at https://securitycocktailhour.com/

Let me know when deployed successfully.
```

**Wait for user confirmation:**
"Deployed successfully" / "Site is live" / "Verified working"

**Why manual deployment:**
- GoDaddy cPanel requires manual file upload (no API)
- Human verification ensures deployment succeeded
- User can check site immediately after deployment

---

### Step 14: Update CLAUDE.md (Optional)

After user confirms deployment, ask:

```
Would you like me to update CLAUDE.md with this deployment? (yes/no)
```

**If yes, update:**

1. **"Recent Completed Work" section** - Add new entry at top:
```markdown
### January [Day], 2026 - Blog Post: [Title] ✅
- **New Blog Post** - "[Blog Post Title]" published
- **Category:** [Category Name]
- **Author:** [Author Name]
- **Publication Date:** [YYYY-MM-DD]
- **Featured:** [yes/no]
- **Related Episode:** [episode-XX or none]
- **SEO Optimizations:**
  - Meta description: XXX chars
  - Tags: X tags (list them)
  - Key takeaways: X bullet points
- **Testing:** Pre-deployment test suite passed (X pages tested)
- **Git:** Committed and pushed to GitHub (commit: [first 7 chars of hash])
- Status: ✅ COMPLETE
```

2. **"Latest Production Package" section:**
```markdown
**Latest Production Package**: `production-deployment-YYYYMMDD-HHMMSS.zip` (X.XMB)
- Contents: XXX pages (XX episodes + X blog posts + newsletter + main pages), XXX files
- Includes: Blog post "[Blog Post Title]" ([Category])
- Status: ✅ DEPLOYED TO PRODUCTION
- Deployed: [Month Day, Year]
```

3. **"Current Site Status" > Production Status:**
```markdown
- **XXX pages live (XX episodes + X blog posts + newsletter + main pages)**
- **Latest blog post:** "[Blog Post Title]" ([Publication Date])
```

**If no:**
Skip update. Document that user declined update in response.

---

## Workflow Summary

### Complete Timeline

**Phase 1: Content Preparation (~5-8 minutes)**
1. Gather blog post information (1 min)
2. Auto-generate SEO metadata (1-2 min)
3. Validate content structure (1 min)
4. Present metadata for approval (2-4 min - depends on revisions)

**Phase 2: Build & Test (~7-12 minutes)**
5. Build blog post files (1 min)
6. Copy blog image (if provided) (<1 min)
7. Start dev server (<1 min)
8. User approves blog post (3-8 min - depends on review time)
9. Run pre-deployment tests (~1 min)
10. Clean up test screenshots (<1 min)

**Phase 3: Production Deployment (~3-5 minutes)**
11. Commit to git and push (1 min)
12. Build production package (1-2 min)
13. User deploys to GoDaddy (varies - manual process)
14. Update CLAUDE.md (optional) (1-2 min)

**Total time:** 15-25 minutes (excluding manual GoDaddy upload time)

---

## Approval Checkpoints

### Checkpoint 1: SEO Metadata Review
- **When:** After generating metadata (Step 4)
- **What:** Review title, description, tags, key takeaways, author info
- **Purpose:** Ensure metadata is accurate and optimized before building

### Checkpoint 2: Dev Site Preview
- **When:** After starting dev server (Step 8)
- **What:** Review blog post on localhost:1313
- **Purpose:** Verify formatting, content, and functionality before testing

### Checkpoint 3: Production Confirmation
- **When:** After building production package (Step 13)
- **What:** Manual deployment to GoDaddy cPanel
- **Purpose:** Human verification that site is live and working

---

## Error Recovery

### Test Failures
1. Review test output
2. Check screenshots in `scripts/tests/test_screenshots/`
3. Fix issue
4. Re-run tests: `python3 scripts/tests/run_all_tests.py --blog`
5. Do not proceed until tests pass

### Build Validation Failures
1. Note specific error from build script
2. DO NOT DEPLOY
3. Fix .htaccess or build issue
4. Re-run: `./scripts/build_production.sh`

### Git Push Failures
1. Check network connection
2. Verify git remote: `git remote -v`
3. Re-run: `git push origin main`

### Hugo Build Failures
1. Check Hugo is installed: `hugo version`
2. Review error message for syntax issues
3. Fix content/template errors
4. Re-run: `hugo --minify` or `./scripts/build_production.sh`

---

**This workflow ensures quality and consistency in every blog post deployment while maintaining human oversight at critical checkpoints.**
