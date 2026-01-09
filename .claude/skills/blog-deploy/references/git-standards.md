# Git Commit Standards for Episode Deployment

This document outlines git commit message standards and workflow for episode deployments.

---

## Commit Message Format

### Structure

```
[Action] Episode [XX]: [Title]

[Body with details]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

### Components

**First Line (Subject):**
- **[Action]**: Usually "Add" for new episodes
- **Episode [XX]**: Episode number with two digits (e.g., "Episode 67")
- **[Title]**: Short version of episode title (5-10 words max)
- **Total length**: Keep under 72 characters when possible

**Body:**
- Blank line after subject
- 3-5 bullet points with details
- Each bullet starts with "- "
- Include: guest info, topic, duration, notable features

**Footer:**
- Blank line before footer
- Claude Code attribution link
- Co-authored-by line

---

## Examples

### Example 1: Episode with Transcript

```
Add Episode 67: Flipper Zero Firmware Update

- Add new solo episode
- Topic: Firmware update walkthrough with troubleshooting
- Duration: 15:55
- Full transcript included (~440 lines)
- SEO optimized: 53-char title, 155-char description

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

### Example 2: Episode with Guest

```
Add Episode 66: Flipper Zero Unboxing

- Add new solo episode (unboxing format)
- Topic: Flipper Zero hardware security testing tool
- Duration: 05:30
- Full transcript included (~5,300 words)
- SEO score: 9.5/10

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

### Example 3: Episode with Additional Changes

```
Add Episode 67: Flipper Zero Firmware Update

- Add new solo episode
- Topic: Firmware update walkthrough with troubleshooting
- Duration: 15:55
- Full transcript included (~440 lines)
- Created DaVinci Resolve transcript formatter script
- Updated NEW-EPISODE-DEPLOYMENT.md with improved workflow

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

---

## Bullet Point Guidelines

### Required Information

**Always include:**
- Guest status: "with [Guest Name]" or "solo episode"
- Topic: Brief 1-sentence description
- Duration: HH:MM:SS or MM:SS format

**Include when applicable:**
- Transcript status: "Full transcript included ([X] lines)" or "Full transcript included (~[X] words)"
- SEO details: "SEO optimized: [X]-char title, [X]-char description"
- Special features: "Related episodes manually selected", "New workflow applied"
- Additional changes: "Created [script name]", "Updated [documentation]"

### Writing Style

**Good examples:**
- "Add new solo episode"
- "Topic: Firmware update walkthrough with troubleshooting"
- "Full transcript included (~440 lines)"
- "Created DaVinci Resolve transcript formatter script"

**Bad examples:**
- "This episode is a solo episode" (too verbose)
- "Discusses firmware updates" (vague)
- "Has a transcript" (not specific)
- "Made a script" (unclear what script)

---

## Git Workflow Commands

### Standard Episode Deployment

```bash
# Stage all changes
git add -A

# Commit with formatted message
git commit -m "Add Episode XX: [Title]

- Add new [solo episode/episode with Guest Name]
- Topic: [brief description]
- Duration: [HH:MM:SS]
- [Additional details]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# Push to main branch
git push origin main
```

### Using Heredoc for Multi-line Messages

For better formatting when constructing commit messages:

```bash
git commit -m "$(cat <<'EOF'
Add Episode 67: Flipper Zero Firmware Update

- Add new solo episode
- Topic: Firmware update walkthrough with troubleshooting
- Duration: 15:55
- Full transcript included (~440 lines)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

---

## Commit Best Practices

### When to Commit

**Commit immediately after:**
- Episode markdown file is created and verified
- Episode image is copied to correct location
- Transcript is formatted and embedded (if applicable)
- User has approved the final episode preview

**Never commit:**
- Before user approval
- With failed builds
- With temporary/test files
- With sensitive information

### What to Stage

**Always stage:**
- New episode markdown file: `content/episodes/episode-XX-*.md`
- Episode image: `static/images/episodes/episode-XXX.jpg`
- Any new scripts created: `scripts/*.py`
- Updated documentation: `docs/*.md` (if workflow changed)

**Never stage:**
- Working files: `working/*`
- Build output: `public/*`
- Production packages: `production-deployment-*.zip`
- Temporary files: `*.tmp`, `*.bak`
- SESSION_CONTEXT.md (unless explicitly requested)

### Git Add Command

```bash
# Stage all changes (preferred for episode deployment)
git add -A

# Or stage specific files
git add content/episodes/episode-67-*.md \
        static/images/episodes/episode-067.jpg \
        scripts/format_davinci_transcript.py
```

---

## Verification Steps

### After Commit

```bash
# Verify commit was created
git log -1 --oneline

# Check what was committed
git show --stat

# Verify commit message format
git log -1 --pretty=format:"%B"
```

### After Push

```bash
# Verify push succeeded
git log -1 --oneline

# Check remote status
git status

# Verify branch is up to date
git fetch origin
git status
```

### Expected Output

After successful push:
```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

---

## Error Handling

### Push Rejected (Behind Remote)

**Error:**
```
! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'origin'
```

**Solution:**
```bash
# Pull latest changes
git pull origin main

# Resolve any conflicts (if present)

# Push again
git push origin main
```

### Commit Message Error

**Error:** Commit message doesn't follow format

**Solution:**
```bash
# Amend the commit message
git commit --amend

# Edit message in editor, save and close

# Force push (only if not pushed yet)
git push origin main --force-with-lease
```

**Important:** Only amend commits that haven't been pushed.

### Staged Wrong Files

**Error:** Accidentally staged files that shouldn't be committed

**Solution:**
```bash
# Unstage specific file
git reset HEAD [filename]

# Unstage all files
git reset HEAD .

# Re-stage correct files
git add [correct files]
```

---

## Branch Strategy

### Main Branch

**Usage:** All episode deployments go directly to main branch

**Workflow:**
```bash
# Always work on main
git checkout main

# Pull latest before starting
git pull origin main

# Stage, commit, and push episode
git add -A
git commit -m "[message]"
git push origin main
```

### No Feature Branches

For episode deployments, feature branches are NOT used:
- Changes are straightforward (adding content)
- No code changes that could break the site
- Episodes are reviewed before commit
- Immediate deployment to staging (Netlify)

### When to Use Branches

Only create branches for:
- Major site redesigns
- Breaking changes to templates
- Experimental features
- Structural refactoring

**Not for:**
- Adding episodes
- Updating content
- Minor fixes
- Documentation updates

---

## Integration with Deployment

### Automatic Triggers

**When you push to main:**
- ✅ GitHub repository is updated
- ✅ Netlify automatically deploys staging site
- ❌ GoDaddy production site NOT automatically updated (manual only)

### Staging Deployment

After push, Netlify automatically:
1. Detects new commit on main branch
2. Runs `hugo --minify` build
3. Deploys to staging URL
4. Updates within 1-2 minutes

### Production Deployment

Production deployment is always manual:
1. Run `./scripts/build_production.sh` locally
2. Creates `production-deployment-[timestamp].zip`
3. User uploads to GoDaddy cPanel
4. User extracts in `public_html/`
5. Site updates immediately

---

## Troubleshooting

### Commit Attribution

Verify commits show correct attribution:

```bash
# Check author
git log -1 --format='%an <%ae>'

# Check co-author
git log -1 --pretty=format:"%B" | grep "Co-Authored-By"
```

Expected output:
```
[User Name] <[user@email.com]>
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

### Verify Remote Repository

```bash
# Check remote URL
git remote -v

# Should show GitHub repository
origin  https://github.com/security-cocktail-hour/security-cocktail-hour-website (fetch)
origin  https://github.com/security-cocktail-hour/security-cocktail-hour-website (push)
```

### Check Commit History

```bash
# Last 5 commits
git log -5 --oneline

# Last commit with full message
git log -1

# Commits for specific file
git log --oneline -- content/episodes/episode-67-*.md
```

---

## Summary Checklist

Before every episode deployment commit:

- [ ] User has approved final episode preview
- [ ] Dev server has been stopped
- [ ] All episode files are created and verified
- [ ] Working directory is clean (no temp files staged)
- [ ] Commit message follows format
- [ ] Commit message includes all required details
- [ ] Claude Code attribution is present
- [ ] Ready to push to main branch

After commit and push:

- [ ] Verify commit was created (git log)
- [ ] Verify push succeeded (git status)
- [ ] Note commit hash for SESSION_CONTEXT update
- [ ] Proceed to production build

---

**Last Updated**: December 22, 2025
