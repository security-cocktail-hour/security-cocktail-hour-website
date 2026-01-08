# SEO Standards for Episode Deployment

**Source Documentation:**
- `docs/SEO-TITLE-TAG-STANDARDS.md`
- `docs/SEO-META-DESCRIPTION-STANDARDS.md`

**IMPORTANT:** This is a consolidated version of the source documents above. If those source files change, this consolidated version must be updated accordingly.

---

## Title Tag Standards

### Character Limits
- **Target**: 50-60 characters (optimal for all devices)
- **Maximum**: 60 characters (Google truncates beyond this)
- **Best Practice**: Aim for 50-60 characters to ensure full display

### Dual-Title System

Episode pages use a dual-title system when needed:

```yaml
---
title: "Full Episode Title with Guest Name and All Context"  # For display
seo_title: "Shortened Title for Search Engines"  # For <title> tag only
---
```

**Full `title` field** appears in:
- Page H1 heading
- Episode listings (homepage, archive)
- Schema.org markup
- RSS feeds
- Breadcrumbs

**Shortened `seo_title` field** (when present):
- HTML `<title>` tag only
- Falls back to full title if not specified

### When to Use `seo_title`

**Recommended:**
- Episode titles over 60 characters
- Episode titles with long guest credentials/company names
- Episode titles that don't fit on mobile search results

**Not Needed:**
- Episodes with titles under 60 characters already
- Episodes where the full title is concise and descriptive

### Title Optimization Guidelines

**What to Include:**
- Primary keywords (most important terms first)
- Guest name (if space permits and guest is notable)
- Topic/value proposition (what the episode is about)

**What to Remove (for SEO title):**
- Unnecessary words ("with", "about", "discussion on")
- Redundant context that's obvious
- Parenthetical asides
- Overly long guest titles/credentials

### Examples

| Full Title (for display) | SEO Title (for `<title>` tag) | Characters |
|--------------------------|-------------------------------|------------|
| AI in Cybersecurity: How CISOs Are Actually Using LLMs with Myke Lyons (Cribl CISO) | AI in Cybersecurity: How CISOs Are Actually Using LLMs | 59 |
| Cybersecurity at Nanosecond Speed \| Securing High Frequency Trading | Cybersecurity at Nanosecond Speed \| Securing HFT | 58 |
| Building a Successful Cybersecurity Career: Seizing Opportunities and Always Learning with Jen Ellis | Building a Successful Cybersecurity Career | 45 |

---

## Meta Description Standards

### Character Limits
- **Target**: 120 characters (optimal for mobile display)
- **Maximum**: 155 characters (Google truncates beyond this)
- **Absolute Rule**: NEVER exceed 155 characters

### Why These Limits?

**155 characters**: Google's cutoff point in search results
- Desktop: Shows ~155 characters
- Mobile: Shows ~120 characters
- Exceeding this causes awkward truncation with "..."

**120 characters**: Sweet spot for mobile-first indexing
- Displays completely on all devices
- Ensures full message delivery
- Better user experience

### Requirements Checklist

Every meta description MUST be:
- ✅ Concise (120-155 characters total)
- ✅ Compelling (entices clicks, shows value)
- ✅ Complete (no awkward sentence breaks)
- ✅ Keyword-rich (primary keywords at start)
- ✅ Active voice (action-oriented language)
- ✅ Unique (different from all other pages)
- ✅ Specific (describes actual content)

Every meta description MUST NOT:
- ❌ Exceed 155 characters
- ❌ Use filler phrases ("In this episode", "Join us to learn")
- ❌ Be generic or vague
- ❌ Duplicate other descriptions
- ❌ End mid-sentence
- ❌ Include hashtags or special characters unnecessarily

### Writing Guidelines

**Front-Load Keywords:**
Put the most important information first.

**Good**: "High-frequency trading security with Jatin Mannepalli. Nanosecond-level challenges and custom hardware solutions."

**Bad**: "In this episode, we discuss the world of high-frequency trading security challenges with guest Jatin Mannepalli."

**Use Active Voice:**
Make it action-oriented.

**Good**: "Paul Asadoorian explores firmware vulnerabilities, supply chain risks, and hardware attack surfaces."

**Bad**: "Firmware vulnerabilities and supply chain risks are explored in this discussion with Paul Asadoorian."

**Be Specific:**
Generic descriptions don't perform.

**Good**: "Trevor Marcotte reveals how six-figure security deals get done through trust, relationships, and solving client problems."

**Bad**: "Learn about security sales best practices and how to close deals in the cybersecurity industry."

**Cut Filler Words:**
Every character counts.

**Phrases to Avoid:**
- "In this episode/article/post"
- "Join us as we"
- "Learn how to"
- "This post covers"
- "We discuss"
- "You'll discover"

**Better Alternatives:**
- Start with guest name or topic
- Lead with the problem/solution
- State the benefit directly

### Format Standards for Episodes

**Structure**: [Guest name] [action verb] [key topics] with Joe and Adam.

**Examples:**

```yaml
description: "Jatin Mannepalli explores high-frequency trading security challenges, incident response, and custom hardware with Joe and Adam."
# 127 characters ✅

description: "Jason Luttrell shares hacking stories from pen testing banks, data centers, and more. Learn why physical security matters."
# 139 characters ✅

description: "Is agentic AI a security nightmare? Kevin O'Connor discusses autonomous AI security with Joe and Adam."
# 102 characters ✅
```

---

## Tag Selection Guidelines

### Tag Requirements
- **Count**: 5-8 relevant tags per episode
- **Format**: Lowercase with hyphens (e.g., `flipper-zero`, `hardware-security`)
- **Purpose**: Categorization and SEO

### Tag Selection Principles
- Select tags that represent core topics discussed
- Include technology/tool names when applicable
- Add security domain tags (e.g., `pentesting`, `incident-response`)
- Include general category tags (e.g., `hardware-security`, `ai-security`)
- Balance specificity with discoverability

### Common Tags to Consider
- **Tools**: `flipper-zero`, `burp-suite`, `metasploit`
- **Domains**: `hardware-security`, `incident-response`, `threat-intel`, `identity`
- **Techniques**: `pentesting`, `red-teaming`, `vulnerability-assessment`
- **Concepts**: `zero-trust`, `ransomware`, `supply-chain-security`
- **General**: `security-tools`, `cybersecurity`, `ethical-hacking`

---

## Topics Discussed Guidelines

### Purpose
Provide a bulleted list of main topics covered in the episode for quick reference.

### Format
```markdown
## Topics Discussed

- Topic 1 (brief, descriptive)
- Topic 2 (brief, descriptive)
- Topic 3 (brief, descriptive)
- Topic 4 (brief, descriptive)
- Topic 5 (brief, descriptive)
```

### Extraction Guidelines
- Extract 4-7 key topics from the full description
- Make each topic brief but descriptive (3-8 words)
- Use title case
- Start with the most important/interesting topics
- Balance technical specificity with accessibility
- Include both "what" and "why" topics when applicable

### Examples

**Episode Description:**
> "Learn how to update your Flipper Zero firmware with this complete walkthrough, including troubleshooting tips for common issues during the update process."

**Topics Discussed:**
- Flipper Zero Device Overview
- Flipper Desktop App Setup
- Firmware Update Process
- Troubleshooting Update Issues
- Device Recovery Methods
- Keeping Security Tools Updated

---

## Quality Checklist

Before finalizing any episode, verify:

**SEO Title (if used):**
- ✅ 50-60 characters
- ✅ Primary keywords at start
- ✅ No awkward truncation
- ✅ Unique from other episodes
- ✅ Accurately represents content

**Meta Description:**
- ✅ 120-155 characters
- ✅ Active voice, compelling
- ✅ Front-loaded keywords
- ✅ Complete sentences
- ✅ No filler phrases
- ✅ Unique from other episodes

**Tags:**
- ✅ 5-8 tags total
- ✅ Lowercase with hyphens
- ✅ Relevant to episode content
- ✅ Mix of specific and general

**Topics Discussed:**
- ✅ 4-7 topics listed
- ✅ Brief but descriptive
- ✅ Extracted from full description
- ✅ Most important topics first

---

## Common Mistakes to Avoid

### SEO Title Mistakes
- ❌ Keyword stuffing
- ❌ All caps
- ❌ Clickbait language
- ❌ Duplicating other episodes
- ❌ Truncated mid-word
- ❌ Too short (wastes opportunity)
- ❌ Missing context

### Meta Description Mistakes
- ❌ Exceeding 155 characters
- ❌ Using passive voice
- ❌ Generic/vague descriptions
- ❌ Filler phrases ("In this episode...")
- ❌ Incomplete sentences
- ❌ Keyword stuffing

### Tag Mistakes
- ❌ Too many tags (>8)
- ❌ Too few tags (<5)
- ❌ Inconsistent formatting
- ❌ Overly broad tags only
- ❌ Overly specific tags that won't be reused

---

**Last Updated**: December 22, 2025
