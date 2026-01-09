# Blog Post Input Format

**Security Cocktail Hour Website - Blog Post Deployment Input Specification**
**Version:** 1.0
**Last Updated:** January 9, 2026

---

## Overview

The blog post deployment skill requires content information in a structured format with 9 numbered fields. This document specifies the exact format, requirements, and examples for the `working/blog-answers.txt` file.

---

## Input File Location

**File path:** `working/blog-answers.txt`

**Preparation:**
1. User creates/edits this file with blog post details
2. Skill reads and parses the 9 numbered fields
3. Auto-generates SEO metadata from provided content
4. Builds blog post files and deploys

---

## Field Specifications

### Field 1: Blog Post Title

**Format:** Plain text, single line
**Length:** Target ≤60 characters (flexible for blog posts)
**Requirements:**
- Clear and descriptive
- Front-load important keywords
- Title case (capitalize major words)
- No special formatting (plain text only)

**Examples:**

✅ **Good (58 chars):**
```
1. Blog Post Title
4 Dangerous Job Scams Targeting Professionals in 2025
```

✅ **Good (44 chars):**
```
1. Blog Post Title
Complete Guide to Flipper Zero Firmware Updates
```

✅ **Good (51 chars):**
```
1. Blog Post Title
How CISOs Are Using AI for Threat Detection
```

❌ **Bad - Too long, no keywords:**
```
1. Blog Post Title
Everything You Ever Wanted to Know About the Security Industry But Were Afraid to Ask
```

---

### Field 2: Publication Date

**Format:** YYYY-MM-DD (ISO 8601 date format)
**Requirements:**
- Must be valid date
- Typically current date or scheduled future date
- Hugo will not display posts dated in the future (unless using `-F` flag)

**Examples:**

✅ **Good:**
```
2. Publication Date
2026-01-09
```

✅ **Good (future date for scheduling):**
```
2. Publication Date
2026-01-15
```

❌ **Bad - Wrong format:**
```
2. Publication Date
January 9, 2026
```

❌ **Bad - Invalid date:**
```
2. Publication Date
2026-13-45
```

---

### Field 3: Author Name

**Format:** Plain text name
**Requirements:**
- Must match predefined author profiles (Joe Patti, Adam Roth)
- Or provide custom author with full bio in later fields
- Used to auto-populate author_bio, author_twitter, author_linkedin

**Predefined Authors:**
- **Joe Patti** - Co-host, cybersecurity professional, IT/security operations
- **Adam Roth** - Co-host, cybersecurity professional, network security/threat detection

**Examples:**

✅ **Good:**
```
3. Author Name
Joe Patti
```

✅ **Good:**
```
3. Author Name
Adam Roth
```

✅ **Good (guest author - requires custom bio):**
```
3. Author Name
Dr. Sarah Johnson
```

---

### Field 4: Category

**Format:** One of the predefined categories
**Requirements:**
- Must match episode category list
- Single category only (no multiple categories)
- Used for organization and filtering

**Available Categories:**
- AI Security
- Career
- Cloud Security
- Hardware Security
- Network Security
- Application Security
- Threat Intelligence
- Compliance & Governance
- Security Operations
- General

**Examples:**

✅ **Good:**
```
4. Category
AI Security
```

✅ **Good:**
```
4. Category
Hardware Security
```

❌ **Bad - Not in predefined list:**
```
4. Category
Cybersecurity News
```

❌ **Bad - Multiple categories:**
```
4. Category
AI Security, Career
```

---

### Field 5: Featured

**Format:** `yes` or `no` (case-insensitive)
**Requirements:**
- Maximum 2 featured posts on homepage
- Skill will check existing featured posts and warn if adding 3rd
- `yes` = featured: true in frontmatter
- `no` = featured: false in frontmatter

**Examples:**

✅ **Good:**
```
5. Featured
yes
```

✅ **Good:**
```
5. Featured
no
```

❌ **Bad - Wrong format:**
```
5. Featured
true
```

❌ **Bad - Invalid value:**
```
5. Featured
maybe
```

---

### Field 6: Related Episode

**Format:** Episode filename with .md extension, or "none"
**Requirements:**
- Full filename from `content/episodes/` directory
- Must include `.md` extension
- Episode must exist
- Use "none" if no related episode
- Used to create cross-links between blog and podcast content

**Examples:**

✅ **Good:**
```
6. Related Episode
episode-64-job-scams.md
```

✅ **Good:**
```
6. Related Episode
episode-67-flipper-zero-firmware-update.md
```

✅ **Good (no related episode):**
```
6. Related Episode
none
```

❌ **Bad - Missing .md extension:**
```
6. Related Episode
episode-64-job-scams
```

❌ **Bad - Invalid filename:**
```
6. Related Episode
Episode 64
```

---

### Field 7: Article Content

**Format:** Markdown with multiple paragraphs and H2 headings
**Requirements:**
- Full article content with proper markdown formatting
- At least 2 H2 headings (## Section Title) for content organization
- Opening paragraph that hooks readers
- Multiple paragraphs (target: >500 words)
- Use markdown formatting: **bold**, *italic*, lists, code blocks, blockquotes
- No H1 headings (title is auto-generated as H1)

**Structure recommendations:**
1. **Opening paragraph** - Hook the reader, introduce topic
2. **H2 Section 1** - First main point with supporting content
3. **H2 Section 2** - Second main point with supporting content
4. **H2 Section 3** - Additional points as needed
5. **Conclusion** - Wrap-up paragraph or H2 section

**Examples:**

✅ **Good:**
```
7. Article Content
Cybercriminals are getting smarter, and their latest target is professionals actively searching for new jobs. In 2025, job scams have evolved beyond simple phishing emails into sophisticated operations that can fool even security-aware professionals.

## The Rise of AI-Powered Job Scams

Fake interview processes are becoming increasingly realistic. Scammers now use AI-generated personas with professional headshots, detailed LinkedIn profiles, and even deepfake video interviews. These operations mimic legitimate companies so well that victims often don't realize they've been scammed until it's too late.

The sophistication level has increased dramatically. Scammers create entire fake company websites, complete with employee directories, blog posts, and customer testimonials. They may even conduct multiple rounds of "interviews" to build trust before asking for personal information or money.

## Four Common Scam Types

**1. Fake Interview Schemes**
These scams involve fake job postings and interview processes. Victims go through what seems like a normal hiring process, only to discover the company doesn't exist.

**2. Cryptocurrency "Job Opportunities"**
Scammers promise high-paying remote positions but require victims to purchase cryptocurrency as part of "training" or "equipment."

**3. Data Harvesting Operations**
Disguised as legitimate recruitment, these scams collect personal information, Social Security numbers, and banking details for identity theft.

**4. Check Cashing Scams**
"Employers" send fake checks for equipment purchases, asking victims to deposit and forward funds before the checks bounce.

## How to Protect Yourself

Always verify job opportunities independently through official company websites. Be suspicious of offers that seem too good to be true, especially those requiring upfront payments or personal financial information.

Research the company thoroughly using multiple sources. Check for reviews on Glassdoor, verify the hiring manager on LinkedIn, and call the company's main number to confirm the job posting is legitimate.

Never provide sensitive information like Social Security numbers or banking details until you've verified the company and job offer through independent channels.
```

❌ **Bad - No H2 headings:**
```
7. Article Content
Job scams are bad. Scammers use various techniques to trick people. You should be careful when looking for jobs online. Always verify the company before giving out personal information.
```

❌ **Bad - Too short:**
```
7. Article Content
Job scams are increasing in 2025. Be careful.
```

---

### Field 8: Key Takeaways

**Format:** 3-5 bulleted points
**Requirements:**
- Each takeaway should be 1-2 sentences
- Action-oriented and specific
- Will be formatted in a dedicated "## Key Takeaways" section
- Title case for individual takeaways (optional, can be sentence case)

**Best practices:**
- Summarize main lessons from article
- Provide actionable insights
- Make it valuable for readers who skim
- Focus on practical applications

**Examples:**

✅ **Good:**
```
8. Key Takeaways
- Fake interview processes are becoming increasingly sophisticated, using AI-generated personas and realistic company websites to appear legitimate
- Cryptocurrency-based job scams promise high pay but require victims to purchase crypto as part of "training" or "equipment"
- Data harvesting schemes disguise themselves as legitimate recruitment, collecting personal information and credentials for identity theft
- Always verify job opportunities independently through official company websites and be suspicious of offers that seem too good to be true
```

✅ **Good:**
```
8. Key Takeaways
- Firmware updates unlock new features and fix bugs, making them essential for optimal Flipper Zero performance
- The qFlipper desktop app provides the easiest update method with a graphical interface and automatic firmware detection
- Common update failures are usually caused by USB connection issues or insufficient battery charge—both are easy to fix
```

❌ **Bad - Too vague:**
```
8. Key Takeaways
- Job scams are bad
- You should be careful
- Scammers use techniques
```

❌ **Bad - Not bulleted format:**
```
8. Key Takeaways
Job scams are increasing and you should be careful when looking for jobs online.
```

---

### Field 9: Blog Image Path

**Format:** File path to image, or "none"
**Requirements:**
- Path to JPG, PNG, or WebP image file
- Image will be copied to `static/images/blog/`
- Recommended size: 1200×630px (optimal for social sharing)
- File size: <500KB recommended
- Optional - blog post will use default/fallback if not provided

**Examples:**

✅ **Good:**
```
9. Blog Image Path
working/job-scams-hero.jpg
```

✅ **Good:**
```
9. Blog Image Path
/Users/joe/Desktop/blog-images/flipper-zero-update.png
```

✅ **Good (no image):**
```
9. Blog Image Path
none
```

❌ **Bad - File doesn't exist:**
```
9. Blog Image Path
working/nonexistent-image.jpg
```

❌ **Bad - Not an image file:**
```
9. Blog Image Path
working/blog-content.txt
```

---

## Complete Example

**File:** `working/blog-answers.txt`

```
1. Blog Post Title
4 Dangerous Job Scams Targeting Professionals in 2025

2. Publication Date
2025-11-26

3. Author Name
Joe Patti

4. Category
AI Security

5. Featured
yes

6. Related Episode
episode-64-job-scams.md

7. Article Content
Cybercriminals are getting smarter, and their latest target is professionals actively searching for new jobs. In 2025, job scams have evolved beyond simple phishing emails into sophisticated operations that can fool even security-aware professionals.

## The Rise of AI-Powered Job Scams

Fake interview processes are becoming increasingly realistic. Scammers now use AI-generated personas with professional headshots, detailed LinkedIn profiles, and even deepfake video interviews. These operations mimic legitimate companies so well that victims often don't realize they've been scammed until it's too late.

The sophistication level has increased dramatically. Scammers create entire fake company websites, complete with employee directories, blog posts, and customer testimonials. They may even conduct multiple rounds of "interviews" to build trust before asking for personal information or money.

## Four Common Scam Types

**1. Fake Interview Schemes**

These scams involve fake job postings and interview processes that seem completely legitimate. Victims go through multiple interview rounds, complete skills assessments, and even receive conditional offer letters. The scam is revealed when victims are asked to provide sensitive information or make upfront payments for "background checks" or "equipment."

**2. Cryptocurrency "Job Opportunities"**

Scammers promise high-paying remote positions in cryptocurrency trading, investment management, or blockchain development. The catch? Victims must purchase cryptocurrency as part of their "training program" or "starter kit." Once the funds are transferred, the "employer" disappears.

**3. Data Harvesting Operations**

Disguised as legitimate recruitment efforts, these operations use fake job applications to collect vast amounts of personal information. Victims provide Social Security numbers, bank account details, copies of driver's licenses, and other sensitive data—all of which ends up in the hands of identity thieves.

**4. Check Cashing Scams**

In these schemes, scammers send victims checks to purchase "home office equipment" or "software licenses." Victims are instructed to deposit the checks and forward most of the funds to a third-party vendor. By the time the checks bounce (days or weeks later), the money is gone and victims are liable for the fraudulent deposits.

## Red Flags to Watch For

Several warning signs can help identify job scams before you become a victim. Be wary of job postings with vague job descriptions, unrealistic salary offers, or requests for personal financial information early in the process.

Legitimate employers won't ask you to pay for background checks, training materials, or equipment upfront. They also won't conduct entire interview processes via text message or require you to purchase cryptocurrency as part of the job.

## How to Protect Yourself

Always verify job opportunities independently through official company websites. Don't rely solely on links provided in emails or messages. Look up the company's main phone number and call to verify that the job posting is legitimate.

Research the hiring manager on LinkedIn and other professional networks. Real hiring managers have established profiles, connections, and post history. Be suspicious of profiles that were created recently or have few connections.

Use Glassdoor, Indeed, and other job review sites to research the company and look for warning signs. If you can't find any information about the company online, that's a major red flag.

Never provide sensitive information like Social Security numbers, bank account details, or copies of identification documents until you've thoroughly verified the company and received a legitimate job offer through official channels.

Trust your instincts. If something feels off about a job opportunity—whether it's the communication style, the process, or the requests being made—it's worth taking a step back and investigating further.

## Taking Action If You've Been Scammed

If you believe you've been targeted by a job scam, act quickly. Contact your bank immediately if you've provided financial information or transferred funds. File a report with the Federal Trade Commission (FTC) and the FBI's Internet Crime Complaint Center (IC3).

Change passwords for any accounts that may have been compromised, and consider placing a fraud alert or credit freeze with the major credit bureaus. Monitor your accounts closely for signs of identity theft.

Report the scam to the job board or platform where you found the listing. This helps protect others from falling victim to the same scheme.

## Conclusion

Job scams are becoming more sophisticated, but awareness and due diligence can protect you from becoming a victim. By recognizing the warning signs, verifying opportunities independently, and trusting your instincts, you can navigate the job market safely.

Remember that legitimate employers will never ask you to pay upfront fees or purchase cryptocurrency as part of the hiring process. When in doubt, verify everything through official channels before providing any personal or financial information.

8. Key Takeaways
- Fake interview processes are becoming increasingly sophisticated, using AI-generated personas and realistic company websites to appear legitimate
- Cryptocurrency-based job scams promise high pay but require victims to purchase crypto as part of "training" or "equipment"
- Data harvesting schemes disguise themselves as legitimate recruitment, collecting personal information and credentials for identity theft
- Always verify job opportunities independently through official company websites and be suspicious of offers that seem too good to be true
- Report job scams to the FTC, IC3, and job boards to protect others from falling victim to the same schemes

9. Blog Image Path
working/job-scams-hero.jpg
```

---

## Validation Checklist

Before submitting `blog-answers.txt`, verify:

✅ **Field 1 (Title):**
- Clear and descriptive
- Target ≤60 characters (flexible)
- Title case

✅ **Field 2 (Date):**
- YYYY-MM-DD format
- Valid date

✅ **Field 3 (Author):**
- Valid author name
- Matches predefined profiles (or custom bio ready)

✅ **Field 4 (Category):**
- One of the predefined categories
- Exact match to category list

✅ **Field 5 (Featured):**
- "yes" or "no"
- Check if 2 posts already featured

✅ **Field 6 (Related Episode):**
- Full filename with .md extension
- Episode exists in content/episodes/
- Or "none" if not applicable

✅ **Field 7 (Content):**
- At least 2 H2 headings
- Opening paragraph present
- Target >500 words
- Proper markdown formatting
- Conclusion section/paragraph

✅ **Field 8 (Key Takeaways):**
- 3-5 bullet points
- Each is 1-2 sentences
- Action-oriented and specific

✅ **Field 9 (Image):**
- Valid file path to image
- Image file exists
- Or "none" if not using image

---

## Tips for Writing Good Content

### Opening Paragraph
- Hook the reader immediately
- Introduce the topic clearly
- Explain why the reader should care
- Set expectations for what they'll learn

### H2 Headings
- Use descriptive, keyword-rich headings
- Break content into logical sections
- Make it easy to scan
- Aim for 2-5 H2 sections

### Content Sections
- Start with the most important information
- Use short paragraphs (3-5 sentences)
- Include examples and specifics
- Use lists for readability
- Bold key concepts sparingly

### Key Takeaways
- Focus on actionable insights
- Make them useful for skimmers
- Don't just repeat content
- Synthesize the main lessons

### Conclusion
- Summarize main points
- Provide clear next steps
- Leave the reader with value
- Reinforce the key message

---

**This input format ensures the blog deployment skill has all necessary information to create high-quality, SEO-optimized blog posts.**
