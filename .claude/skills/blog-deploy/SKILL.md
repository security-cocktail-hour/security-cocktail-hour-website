---
name: blog-deploy
description: "Automate blog post deployment for Security Cocktail Hour website with interactive approval gates. Use when the user requests to: (1) Deploy/publish/add a new blog post, (2) Release a new article, (3) Add blog content to the site, (4) Upload/publish blog post to production. Auto-generates SEO metadata (description, tags, key takeaways), builds blog post files, provides dev preview, runs pre-deployment tests, commits to git, and creates production package. Maintains human approval checkpoints at: SEO metadata review, dev site preview, and production confirmation."
---

# Blog Post Deployment Skill

Streamlined, automated workflow for deploying new blog posts to the Security Cocktail Hour website with quality control checkpoints.

## Overview

This skill automates the blog post deployment process while maintaining critical approval gates where human review is needed. It auto-generates SEO-compliant metadata, builds blog post files, validates content structure, provides development preview, runs pre-deployment tests, and prepares production packages.

**Key principle:** This skill provides the *workflow automation*. For content standards and guidelines, it references the authoritative project documentation to ensure consistency.

---

## Workflow

The blog post deployment follows a 10-step workflow with three key approval checkpoints:

### Phase 1: Content Preparation
1. **Gather blog post information** - Read blog post details from `working/blog-answers.txt`
2. **Auto-generate SEO metadata** - Create meta description, tags, and key takeaways structure
3. **Present metadata for approval** (APPROVAL CHECKPOINT 1) - User reviews and approves/revises SEO metadata

### Phase 2: Build & Test
4. **Build blog post files** - Create markdown file in `content/blog/`
5. **Copy blog image** (if provided) - Copy to `static/images/blog/`
6. **Start dev server** - Launch Hugo server with `hugo server -D`
7. **User approves blog post** (APPROVAL CHECKPOINT 2) - Review on dev site at localhost:1313/blog/
8. **Run pre-deployment tests** - Execute blog test suite to validate pages
9. **Clean up test screenshots** - Remove test artifacts after successful tests

### Phase 3: Production Deployment
10. **Commit to git and push** - Standard git workflow with formatted message
11. **Build production package** - Run `./scripts/build_production.sh` with validation
12. **User deploys to GoDaddy** (APPROVAL CHECKPOINT 3) - Manual upload to cPanel (never automated)
13. **Update CLAUDE.md** - Ask before updating (optional)

**Complete workflow details:** See `references/blog-workflow.md` (bundled with skill)

---

## Blog Post Information Format

User provides blog post details in `working/blog-answers.txt` with 8 numbered fields:

1. **Blog Post Title** - Full article title (typically ≤60 chars, no separate SEO title needed)
2. **Publication Date** - YYYY-MM-DD format
3. **Author Name** - "Joe Patti", "Adam Roth", or other
4. **Category** - "AI Security", "Cloud Security", "Hardware Security", "Career", etc.
5. **Featured** - "yes" or "no" (maximum 2 featured posts on homepage)
6. **Related Episode** - Episode filename (e.g., "episode-67-flipper-zero-firmware-update.md") or "none"
7. **Article Content** - Full markdown content with H2 headings, paragraphs, lists
8. **Blog Image Path** - Path to hero image (optional, e.g., `working/blog-image.jpg`)

Parse this file to extract all information before proceeding.

**Input format specification:** See `references/blog-input-format.md` (bundled with skill)
**Template file:** `working/blog-answers.txt.template` (created during skill setup)

---

## SEO Metadata Generation

Auto-generate SEO-compliant metadata based on user's title and content.

### Where to Find Standards

**All SEO standards are documented in the project documentation:**

- **Meta descriptions:** See `docs/SEO-META-DESCRIPTION-STANDARDS.md`
  - 120-155 characters (strict requirement)
  - Active voice, front-load keywords
  - No filler phrases

- **Tags and topics:** See `docs/BLOG-DOCUMENTATION.md`
  - 5-8 tags per post
  - Lowercase with hyphens
  - Mix of specific and general

- **Content structure:** See `docs/BLOG-DOCUMENTATION.md`
  - H2 headings required (minimum 2)
  - Key Takeaways section
  - Opening paragraph guidelines

### Generation Strategy

**Read the project documentation files above using the Read tool to understand current standards, then:**

#### Meta Description (Always Required)
- **Strategy:** Combine title + first sentence or opening paragraph
- **Format:** Action-oriented statement summarizing the article's value
- **Example:** "Discover 4 dangerous job scams targeting professionals in 2025, including fake interviews, cryptocurrency schemes, and data harvesting operations." (148 chars)

#### Tags (Always Required)
- **Strategy:** Extract from category + content topics + key takeaways
- **Example:** `job-scams`, `social-engineering`, `cybersecurity-awareness`, `professional-security`, `scam-prevention`

#### Key Takeaways (Auto-Generated)
- **Strategy:** Analyze the full article content and synthesize 3-5 key takeaways
- **Format:** Markdown bulleted list, each takeaway 1-2 sentences
- **Tone:** Match the author's voice and writing style from the article
- **Focus:** Actionable insights and practical lessons, not just content summaries
- **Presented at Checkpoint 1** for user approval; revise until approved
- **Inserted** as a dedicated `## Key Takeaways` section in the blog post

#### Author Information (Auto-Populated)
- **Lookup:** Match author name to predefined profiles in `docs/BLOG-DOCUMENTATION.md`
- **Auto-populate:** author_bio, author_twitter, author_linkedin

**Author profiles are documented in:** `docs/BLOG-DOCUMENTATION.md`

---

## Content Structure Validation

Before presenting for approval, validate blog post structure according to standards in `docs/BLOG-DOCUMENTATION.md`.

### Required Elements (Read from project docs)
- **Opening paragraph** - Strong introduction that hooks readers
- **H2 headings** - At least 2 section headings for content organization (SEO best practice)
- **Key Takeaways section** - Dedicated section with bulleted list (improves readability)
- **Conclusion** - Wrap-up paragraph or section

### Warnings to User
- **Missing H2 headings:** "No H2 headings found. Consider adding section headers for better SEO."
- **No Key Takeaways section:** "Key Takeaways section not found. This section improves reader engagement."
- **Very short content:** "Article is <500 words. Consider expanding for better SEO performance."
- **Very long paragraphs:** "Some paragraphs exceed 150 words. Consider breaking into smaller chunks."

**Content structure guidelines:** See `docs/BLOG-DOCUMENTATION.md` in project root

---

## Approval Checkpoints

### Checkpoint 1: SEO Metadata Review

After generating metadata, present to user with character counts:

```
SEO Metadata Generated:

Title: "[Blog Post Title]" (XX chars) ✓
Meta Description: "[Generated Description]" (XXX chars) ✓

Category: [Category Name]
Featured: [yes/no]
Related Episode: [episode-filename or none]

Author: [Author Name]
Author Bio: "[Auto-populated bio...]"

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
⚠ [Any warnings]

Please review and approve or request revisions.
```

**Wait for explicit approval** before proceeding.

### Checkpoint 2: Dev Site Preview

After building blog post files and starting dev server, inform user:

```
Development server started at http://localhost:1313/

Please review:
- Blog list page (http://localhost:1313/blog/) shows the new post
- Blog post displays correctly at http://localhost:1313/blog/[slug]/
- Title, author, date, category are accurate
- Content formatting is correct (headings, lists, bold text)
- Key Takeaways section is formatted properly
- Related episode link works (if applicable)
- Blog image displays (if included)
- SEO metadata appears correctly in page source (right-click > View Page Source)

Let me know when you're satisfied or if you need changes.
```

**Wait for explicit approval.**

### Pre-Deployment Testing

**After dev site approval, run automated test suite:**

```bash
python3 scripts/tests/run_all_tests.py --blog
```

**Test Coverage:**
- Blog list page (http://localhost:1313/blog/)
- 5 latest blog posts (currently all 4, prepared for growth)
- Validation: Page loads, SEO metadata, search functionality, filtering

**Test duration:** ~1 minute

If any test fails, explain the issue with screenshot reference and recommend fix. **DO NOT proceed to commit/build until all tests pass.**

After tests pass, clean up:
```bash
rm -rf scripts/tests/test_screenshots
```

**Testing documentation:** See `scripts/tests/README.md` in project root

### Checkpoint 3: Production Confirmation

After committing to git and building production package, present summary and deployment instructions.

**Deployment documentation:** See `GODADDY-DEPLOYMENT-INSTRUCTIONS.md` in project root

---

## Featured Post Management

**Important constraint:** Maximum 2 featured posts on homepage.

When user sets a blog post as featured (`featured: yes`):

1. **Check existing featured posts:**
   ```bash
   grep -l "featured: true" content/blog/*.md | wc -l
   ```

2. **If already 2 featured posts exist:**
   ```
   ⚠️ Warning: There are already 2 featured blog posts on the homepage:
   - [Post 1 Title]
   - [Post 2 Title]

   Setting this post as featured will result in 3 featured posts, which may
   overcrowd the homepage.

   Options:
   1. Remove featured status from one of the existing posts
   2. Keep this post as non-featured
   3. Proceed with 3 featured posts (not recommended)

   What would you like to do?
   ```

3. **Handle user response accordingly**

---

## Git Commit Message Format

Use standardized format for blog post commits (read from `references/git-standards.md` bundled with skill):

```bash
git commit -m "$(cat <<'EOF'
Add Blog Post: [Blog Post Title]

Category: [Category Name]
Author: [Author Name]
Date: [Publication Date]
[Featured: yes/no]
[Related Episode: episode-XX-slug]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

**Git workflow standards:** See `references/git-standards.md` (bundled with skill)

---

## Blog Post Front Matter Template

Generate front matter in this exact format (following standards in `docs/BLOG-DOCUMENTATION.md`):

```yaml
---
title: "[Blog Post Title]"
date: [YYYY-MM-DD]
draft: false
author: "[Author Name]"
author_bio: "[Auto-populated author bio]"
author_twitter: "@SecCocktailHour"
author_linkedin: "[Auto-populated LinkedIn URL or leave empty]"
category: "[Category Name]"
tags: ["tag1", "tag2", "tag3", "tag4", "tag5"]
description: "[Meta description 120-155 chars]"
featured: [true/false]
related_episode: "[episode-filename.md or leave empty]"
---
```

**Front matter standards:** See `docs/BLOG-DOCUMENTATION.md` in project root

---

## Blog Post File Naming

Create markdown file with slug-based naming (following conventions in `docs/BLOG-DOCUMENTATION.md`):

**Format:** `article-title-slug.md`
**Location:** `content/blog/`

**Slug generation rules:**
1. Convert title to lowercase
2. Replace spaces with hyphens
3. Remove special characters (keep hyphens only)
4. Remove articles (a, an, the) from beginning
5. Limit to 5-8 words

**Examples:**
- "4 Dangerous Job Scams Targeting Professionals in 2025" → `dangerous-job-scams-targeting-professionals-2025.md`
- "The Complete Guide to Flipper Zero" → `complete-guide-flipper-zero.md`

**Image naming:** Keep original filename, copy to `static/images/blog/[original-name]`

---

## Error Handling

### Pre-Deployment Test Failures

When tests fail:
1. Review the test output to identify which tests failed
2. Check the screenshot files in `scripts/tests/test_screenshots/` for visual debugging
3. Explain the issue to the user with specific details
4. Recommend specific fix
5. After fix, re-run tests: `python3 scripts/tests/run_all_tests.py --blog`
6. **DO NOT proceed to commit/build until all tests pass**

### Build Validation Failed

When .htaccess validation fails (see `scripts/build_production.sh`):
1. Describe the specific validation error
2. Explain the impact
3. State clearly: "DO NOT DEPLOY THIS PACKAGE"
4. Recommend specific fix
5. Wait for user to fix and run build again

### Missing Required Information

When blog post details are incomplete:
1. List all missing fields with field numbers
2. Explain what information is needed for each
3. Wait for user to provide missing information
4. Do not proceed until all required fields are present

**Required fields:**
- Title (field 1)
- Publication Date (field 2)
- Author Name (field 3)
- Category (field 4)
- Article Content (field 7)

**Optional fields:**
- Featured (defaults to "no")
- Related Episode (defaults to "none")
- Blog Image Path (optional)

---

## Documentation References

### Bundled with This Skill
- **`references/blog-workflow.md`** - Detailed 10-step workflow with examples
- **`references/blog-input-format.md`** - Template and guidelines for working/blog-answers.txt
- **`references/git-standards.md`** - Git commit message format and workflow commands

### Project Documentation (Read Directly)
- **`docs/BLOG-DOCUMENTATION.md`** - Complete blog post standards, front matter, content structure
- **`docs/SEO-META-DESCRIPTION-STANDARDS.md`** - Meta description rules (120-155 chars, active voice, etc.)
- **`docs/SEO-TITLE-TAG-STANDARDS.md`** - Title tag optimization guidelines
- **`docs/NEW-EPISODE-DEPLOYMENT.md`** - Episode deployment process (similar workflow for reference)
- **`GODADDY-DEPLOYMENT-INSTRUCTIONS.md`** - Production deployment guide
- **`scripts/tests/README.md`** - Pre-deployment testing documentation
- **`CLAUDE.md`** - Project context and current status

**Why this approach?**
- Single source of truth for content standards
- Skill stays up-to-date automatically when project docs change
- Easier maintenance (update docs once, not in multiple places)
- Skill focuses on workflow automation, not documentation duplication

---

## Best Practices

### Communication
- Always show character counts for SEO fields when presenting metadata
- Explain validation errors in plain language with impact assessment
- Provide specific recommendations when errors occur
- Keep user informed at each workflow step

### Quality Control
- **Read project documentation first** using the Read tool to understand current standards
- Validate all generated metadata before presenting (character counts, format)
- Check for existing featured posts before setting new one as featured
- Verify file operations succeeded (image copy, slug generation)
- Confirm git push succeeded before building production
- Check production package exists and has reasonable size
- Validate content structure (headings, key takeaways section)

### User Experience
- Present information in digestible chunks (not overwhelming)
- Wait for explicit approval at each checkpoint (don't batch approvals)
- Don't proceed past approval gates without clear user consent
- Explain what's happening at each step
- Make it easy to request revisions
- Provide helpful warnings (not blocking errors) for content structure issues

### Staying Current
- Always read the latest version of project documentation files when generating content
- If standards have changed in project docs, use the new standards
- Report any inconsistencies between skill behavior and project docs to user

---

**This skill maintains human oversight while automating repetitive tasks, ensuring quality and consistency in every blog post deployment.**
