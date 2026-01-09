# Title Tag SEO Standards

**Established**: November 28, 2025
**Status**: RECOMMENDED for episodes with long titles

---

## Overview

Title tags (HTML `<title>` element) are one of the most important on-page SEO factors. They appear in:
- Browser tabs
- Google search results (as the clickable headline)
- Social media shares (when Open Graph title not specified)
- Bookmarks

**Impact**: Well-optimized title tags improve click-through rates by 20-40% and help search engines understand page content.

---

## Character Limits

### Hard Limits
- **Target**: 50-60 characters (optimal for all devices)
- **Maximum**: 60 characters (Google truncates around 60-70 depending on character width)
- **Best Practice**: Aim for 50-60 characters to ensure full display

### Why These Limits?

**60 characters**: Google's display limit in search results
- Desktop: Shows ~60-70 characters (600 pixels)
- Mobile: Shows ~50-60 characters (420 pixels)
- Exceeding this causes truncation with "..."

**50-60 characters**: Sweet spot for universal display
- Displays completely on all devices
- Ensures brand name fits after separator
- Better user experience

---

## Implementation: Episode Pages

For episode pages, we use a **dual-title system**:

### Front Matter Fields

```yaml
---
title: "Full Episode Title with Guest Name and All Context"
seo_title: "Shortened Title for Search Engines"
---
```

### Where Each Title Appears

**Full `title` field** (original complete title):
- ✅ Page H1 heading
- ✅ Episode listings (homepage, archive, search results)
- ✅ Schema.org PodcastEpisode "name" field
- ✅ RSS feeds
- ✅ Breadcrumbs

**Shortened `seo_title` field** (when present):
- ✅ HTML `<title>` tag only
- ✅ Falls back to full title if not specified

### Template Implementation

File: `layouts/episodes/single.html`

```go
{{ define "title" }}{{ if .Params.seo_title }}{{ .Params.seo_title }}{{ else }}{{ .Title }}{{ end }} | {{ .Site.Title }}{{ end }}
```

---

## Title Optimization Guidelines

### What to Include
✅ **Primary keywords** - Most important terms first
✅ **Guest name** - If space permits and guest is notable
✅ **Topic/value proposition** - What the episode is about
✅ **Unique identifier** - Episode number (optional, if space)

### What to Remove (for SEO title)
❌ Unnecessary words ("with", "about", "discussion on")
❌ Redundant context that's obvious
❌ Parenthetical asides
❌ Overly long guest titles/credentials

### Examples from Implementation

| Full Title (for display) | SEO Title (for `<title>` tag) | Characters |
|--------------------------|-------------------------------|------------|
| AI in Cybersecurity: How CISOs Are Actually Using LLMs with Myke Lyons (Cribl CISO) | AI in Cybersecurity: How CISOs Are Actually Using LLMs | 59 |
| Cybersecurity at Nanosecond Speed \| Securing High Frequency Trading | Cybersecurity at Nanosecond Speed \| Securing HFT | 58 |
| Building a Successful Cybersecurity Career: Seizing Opportunities and Always Learning with Jen Ellis | Building a Successful Cybersecurity Career | 45 |
| The New Rules of Cyber Incident Response: New Attacks, New Response with Ryan Kovar | The New Rules of Cyber Incident Response | 45 |

---

## When to Use `seo_title`

### Required
- ❌ Not required for any episodes (it's optional)

### Recommended
- ✅ Episode titles over 60 characters
- ✅ Episode titles with long guest credentials/company names
- ✅ Episode titles that don't fit on mobile search results

### Not Needed
- Episodes with titles under 60 characters already
- Episodes where the full title is concise and descriptive

---

## Quality Checklist

Every SEO title should be:

✅ **Concise** - 50-60 characters total (excluding site title)
✅ **Descriptive** - Clearly indicates episode topic
✅ **Keyword-rich** - Primary keywords at the start
✅ **Complete** - No awkward truncation
✅ **Unique** - Different from all other episodes
✅ **Accurate** - Matches the actual episode content

---

## Testing & Verification

### Audit Script
Use the automated audit script to check all title tags:

```bash
python3 scripts/audit_title_tags.py
```

The script will report:
- Titles exceeding 70 characters (likely truncated)
- Titles in acceptable range (61-70 chars)
- Optimal titles (≤60 chars)
- Episodes using SEO titles
- Suggestions for improvement

### Manual Testing
1. Start Hugo server: `hugo server -D`
2. View episode page in browser
3. Check browser tab - should show shortened title
4. View page source - verify `<title>` tag contains SEO title
5. Verify H1 heading still shows full original title

### Command Line Testing
Use browser DevTools or curl:

```bash
curl -s http://localhost:1313/episodes/episode-XX/ | grep -A 2 '<title>'
curl -s http://localhost:1313/episodes/episode-XX/ | grep -A 1 '<h1'
```

Should show:
- `<title>`: Shortened SEO title | Site Title
- `<h1>`: Full original title with guest name

---

## Common Mistakes to Avoid

❌ **Keyword stuffing** - "Cybersecurity cyber security cyber"
❌ **All caps** - "CYBERSECURITY EPISODE"
❌ **Clickbait** - "You Won't Believe This Cyber Trick!"
❌ **Duplicates** - Same title as another episode
❌ **Truncated mid-word** - "Cybersecurity at Nanose..."
❌ **Too short** - "Episode 62" (wastes opportunity)
❌ **Missing context** - "LLMs" (without explaining what it's about)

---

## Episode Archetype Template

When creating new episodes, the archetype includes space for optional SEO title:

```yaml
---
title: "Full Episode Title"
seo_title: ""  # Optional: Add if title > 60 chars
date: {{ .Date }}
draft: false
guest: ""
category: ""
duration: ""
image: ""
description: ""
---
```

---

## Impact & Benefits

### SEO Benefits
- ✅ Better search result appearance
- ✅ Higher click-through rates (CTR)
- ✅ No truncation on any device
- ✅ More effective use of pixel space

### User Benefits
- ✅ Clear, concise information
- ✅ Easier to scan search results
- ✅ Better mobile experience
- ✅ Professional appearance

### Technical Benefits
- ✅ Full titles preserved for context
- ✅ SEO titles optimized for search
- ✅ Easy to revert if needed
- ✅ No impact on existing functionality

---

## Reference

**Current Implementation**: 20 pages with SEO titles (as of November 29, 2025)

- **Episodes**: 17, 29, 37, 39, 40, 42, 43, 47, 48, 49, 50, 53, 55, 60, 61, 62, 63
- **Blog Posts**: when-nanoseconds-matter.md
- **Pages**: _index.md (homepage)

**Template Files**:
- Episodes: `layouts/episodes/single.html:1`
- Blog Posts: `layouts/blog/single.html:1` (uses same baseof.html template)
- Pages: `layouts/_default/baseof.html:4` (fallback for all content)

**Audit Script**: `scripts/audit_title_tags.py` - Comprehensive audit tool for all content types

**Related Documentation**:
- `docs/SEO-META-DESCRIPTION-STANDARDS.md` - Meta description guidelines
- `docs/NEW-EPISODE-DEPLOYMENT.md` - New episode checklist
- `docs/BLOG-SEO-PLAN.md` - Overall SEO strategy

---

**For questions or updates, see CLAUDE.md**
