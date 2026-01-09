---
name: episode-deploy
description: "Automate episode deployment for Security Cocktail Hour podcast website with interactive approval gates. Use when the user requests to: (1) Deploy/publish/add a new episode, (2) Release a new episode, (3) Add episode content to the site, (4) Upload/publish episode to production. Handles transcript format detection/conversion, auto-generates SEO metadata (title, description, tags, topics), builds episode files, provides dev preview, commits to git, and creates production package. Maintains human approval checkpoints at: SEO metadata review, dev site preview, and production confirmation. Supports multiple transcript formats and adapts to new formats by creating handler scripts."
---

# Episode Deployment Skill

Streamlined, automated workflow for deploying new podcast episodes to the Security Cocktail Hour website with quality control checkpoints.

## Overview

This skill automates the episode deployment process while maintaining critical approval gates where human review is needed. It handles transcript format detection and conversion, auto-generates SEO-compliant metadata, builds all episode files, provides development preview, and prepares production packages.

## Workflow

The episode deployment follows a 13-step workflow with three key approval checkpoints:

### Phase 1: Content Preparation
1. **Gather episode information** - Read episode details from `working/content-answers.txt`
2. **Detect and format transcript** - Automatically detect format and convert to standard format
3. **Auto-generate SEO metadata** - Create title, description, tags, and topics

### Phase 2: Review and Build (APPROVAL CHECKPOINT 1)
4. **Present metadata for approval** - User reviews and approves/revises SEO metadata
5. **Build episode files** - Create markdown, copy image, embed transcript
6. **Start dev server** - Launch Hugo server with `-D -F` flags

### Phase 3: Final Approval (APPROVAL CHECKPOINT 2)
7. **User approves final episode** - Review on dev site at localhost:1313
8. **Run pre-deployment tests** - Execute automated test suite to validate all pages
9. **Clean up test screenshots** - Remove test artifacts after successful tests

### Phase 4: Production Deployment
10. **Commit to git and push** - Standard git workflow with formatted message
11. **Build production package** - Run `./scripts/build_production.sh` with validation

### Phase 5: Manual Deployment (APPROVAL CHECKPOINT 3)
12. **User deploys to GoDaddy** - Manual upload to cPanel (never automated)
13. **Update CLAUDE.md** - Ask before updating (optional)

**Complete workflow details:** See `references/episode-workflow.md`

## Episode Information Format

User provides episode details in `working/content-answers.txt` with 12 numbered fields:

1. Episode Number
2. Full Episode Title
3. Publication Date (YYYY-MM-DD)
4. Guest Name (or "No guest")
5. Guest Bio
6. Category (AI, Career, Hardware Security, etc.)
7. Duration (HH:MM:SS or MM:SS)
8. Full Description (multiple paragraphs)
9. Platform URLs (YouTube, Spotify, Apple, Amazon)
10. Episode thumbnail image path
11. Transcript file path (optional)
12. Related Episodes (optional, filenames)

Parse this file to extract all information before proceeding.

## Transcript Handling

### Supported Formats

**DaVinci Resolve format:**
```
[HH:MM:SS:FF - HH:MM:SS:FF]
Speaker Name
 Dialogue text...
```

**Generic format:**
```
Speaker Name [MM:SS]
Dialogue text here...
```

**Standard format (target):**
```
*Speaker Name (MM:SS)*
Dialogue text here...
```

### Format Detection and Conversion

When transcript file is provided:

1. **Detect format** by examining file content:
   - DaVinci: Look for `[HH:MM:SS:FF - HH:MM:SS:FF]` pattern
   - Generic: Look for `Speaker [MM:SS]` pattern
   - Standard: Look for `*Speaker (MM:SS)*` pattern

2. **Convert using appropriate script:**
   - DaVinci → `scripts/format_davinci_transcript.py`
   - Generic → `scripts/format_transcript.py`
   - Standard → No conversion needed

3. **Handle unknown formats:**
   - Describe what was found in the file
   - Recommend creating new handler script
   - Ask user how to proceed
   - When creating new handler: Add to `scripts/` directory, document in `references/transcript-formats.md`, copy to skill

**Detailed format specifications:** See `references/transcript-formats.md`

## SEO Metadata Generation

Auto-generate SEO-compliant metadata based on user's full title and description:

### SEO Title (Conditional)
- **Generate only if:** Full title exceeds 60 characters
- **Requirements:** 50-60 chars, keywords first, remove filler words
- **Example:** "AI in Cybersecurity: How CISOs Are Actually Using LLMs" (59 chars)

### Meta Description (Always Required)
- **Requirements:** 120-155 chars, active voice, front-load keywords, no filler phrases
- **Format:** "[Guest name] [action verb] [key topics] with Joe and Adam."
- **Example:** "Learn how to update your Flipper Zero firmware with this complete walkthrough, including troubleshooting tips for common issues." (155 chars)

### Tags (Always Required)
- **Requirements:** 5-8 tags, lowercase with hyphens, mix of specific and general
- **Example:** `flipper-zero`, `firmware-update`, `hardware-security`, `security-tools`, `troubleshooting`

### Topics Discussed (Always Required)
- **Requirements:** 4-7 topics, brief but descriptive (3-8 words), title case
- **Example:** "Flipper Zero Device Overview", "Firmware Update Process", "Troubleshooting Update Issues"

**Complete SEO guidelines:** See `references/seo-standards.md`

## Approval Checkpoints

### Checkpoint 1: SEO Metadata Review

After generating metadata, present to user with character counts:

```
SEO Metadata Generated:

SEO Title: "[Generated Title]" (XX chars) ✓
Meta Description: "[Generated Description]" (XXX chars) ✓

Tags:
- tag1
- tag2
...

Topics Discussed:
- Topic 1
- Topic 2
...

Please review and approve or request revisions.
```

**Wait for explicit approval** before proceeding. Handle revision requests:
- "Make the description more action-oriented"
- "Add '[tag]' as a tag"
- "Change the third topic to '[new topic]'"
- "The SEO title is too long, shorten it"

### Checkpoint 2: Dev Site Preview

After building episode files and starting dev server, inform user:

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

**Wait for explicit approval:**
- "I'm satisfied. Commit and build for production."
- "Looks good, commit and build."

If changes requested, make them and continue in dev mode until approved.

### Pre-Deployment Testing

**After dev site approval, run automated test suite:**

```bash
python3 scripts/tests/run_all_tests.py
```

**Test Coverage:**
- 8 static pages (homepage, about, contact, partnership, resources, newsletter, privacy, terms)
- ~12 episodes (newest 5 + one from each block of 10)
- ~5 latest blog posts
- Total: ~25 pages tested in 4-5 minutes

**Validation checks:**
- Page loads successfully
- Title and navigation correct
- SEO metadata present
- Platform links work
- No console errors
- Forms display correctly
- Search/filter functionality

**If tests pass:**
```
✅ ALL TESTS PASSED - Ready for deployment!
```

Clean up test artifacts:
```bash
rm -rf scripts/tests/test_screenshots
```

Proceed to commit and build.

**If tests fail:**
```
❌ X TEST(S) FAILED - Review errors before deployment

Failed test screenshots saved in: scripts/tests/test_screenshots/
```

- Review error messages and screenshots
- Fix issues in the episode or site files
- Re-run tests until all pass
- Do not proceed to commit/build until tests pass

### Checkpoint 3: Production Deployment

After building production package, inform user:

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

**Wait for user confirmation:**
- "production deployment complete"
- "deployed"
- "live"

## Git Commit Standards

Use formatted commit messages following this structure:

```
Add Episode [XX]: [Title]

- Add new [solo episode/episode with Guest Name]
- Topic: [brief description]
- Duration: [HH:MM:SS]
- [Additional details: transcript lines, SEO details, etc.]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

**Git workflow:**
```bash
git add -A
git commit -m "[formatted message]"
git push origin main
```

Always verify push succeeded and report commit hash to user.

**Complete git standards:** See `references/git-standards.md`

## Production Build

**ALWAYS use the automated build script:**

```bash
./scripts/build_production.sh
```

This script:
- Validates .htaccess file integrity (before and after build)
- Runs `hugo --minify` to build production site
- Ensures all 24 required 301 redirects are present
- Validates 404 error page configuration
- Creates timestamped deployment ZIP
- Prevents broken configurations from reaching production

**NEVER use manual build:**
```bash
hugo --minify  # DON'T USE THIS DIRECTLY
```

If validation fails:
- Script exits with code 1
- DO NOT deploy
- Describe error to user with impact explanation
- Recommend fix
- Wait for user decision

## CLAUDE.md Updates

**Always ask before updating CLAUDE.md**

User may request:
- "Update CLAUDE.md with Episode [XX]"
- "Update session context"

When updating, modify:
1. "Last Updated" date
2. "Recent Completed Work" section (add new episode entry)
3. "Latest Production Package" section
4. "Current Site Status" (increment episode count, update latest episode reference)

## Error Handling

### Pre-Deployment Test Failures

When tests fail:
1. Review the test output to identify which tests failed
2. Check the screenshot files in `scripts/tests/test_screenshots/` for visual debugging
3. Explain the issue to the user with specific details:
   - Which page failed
   - What validation check failed
   - Likely cause (e.g., missing platform link, incorrect frontmatter)
4. Recommend specific fix
5. After fix, re-run tests: `python3 scripts/tests/run_all_tests.py`
6. **DO NOT proceed to commit/build until all tests pass**

**Example:**
```
Pre-deployment tests failed (3 tests):

Episode 67 page:
- Missing Spotify platform link
- Fix: Add spotify URL to episode frontmatter

Homepage:
- New episode card not displaying
- Fix: Check episode date is not in future, or use -F flag with Hugo server

Blog page:
- Search functionality test failed
- Fix: Already known issue, may need template adjustment

Please fix these issues and I'll re-run the tests.
```

### Unknown Transcript Format

When encountering unrecognized format:
1. Describe what was found (show pattern and example)
2. Explain this format is not currently supported
3. Recommend creating new handler script: `scripts/format_[type]_transcript.py`
4. Ask user how they'd like to proceed
5. If creating handler: Document in `references/transcript-formats.md`, copy to skill scripts

### Build Validation Failed

When .htaccess validation fails:
1. Describe the specific validation error
2. Explain the impact (e.g., "This will cause default Apache 404 page instead of custom page")
3. State clearly: "DO NOT DEPLOY THIS PACKAGE"
4. Recommend specific fix
5. Wait for user to fix and run build again

### Missing Required Information

When episode details are incomplete:
1. List all missing fields with field numbers
2. Explain what information is needed for each
3. Wait for user to provide missing information
4. Do not proceed until all required fields are present

## Bundled Resources

### Scripts (`scripts/`)
- **`format_davinci_transcript.py`** - Convert DaVinci Resolve format to standard format
- **`format_transcript.py`** - Convert generic format to standard format

### References (`references/`)
- **`seo-standards.md`** - Complete SEO rules for titles, descriptions, tags, and topics
- **`transcript-formats.md`** - All supported transcript formats and detection logic
- **`episode-workflow.md`** - Detailed 11-step workflow with examples
- **`git-standards.md`** - Git commit message format and workflow commands

## Best Practices

### Communication
- Always show character counts for SEO fields when presenting metadata
- Explain validation errors in plain language with impact assessment
- Provide specific recommendations when errors occur
- Keep user informed at each workflow step

### Quality Control
- Validate all generated metadata before presenting (character counts, format)
- Double-check episode numbering (zero-padded for images: episode-067.jpg)
- Verify file operations succeeded (image copy, transcript conversion)
- Confirm git push succeeded before building production
- Check production package exists and has reasonable size

### User Experience
- Present information in digestible chunks (not overwhelming)
- Wait for explicit approval at each checkpoint (don't batch approvals)
- Don't proceed past approval gates without clear user consent
- Explain what's happening at each step
- Make it easy to request revisions

---

**This skill maintains human oversight while automating repetitive tasks, ensuring quality and consistency in every episode deployment.**
