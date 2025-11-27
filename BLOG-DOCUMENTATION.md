# Security Cocktail Hour Blog - Documentation

**Last Updated**: November 25, 2025

---

## Overview

The Security Cocktail Hour blog provides a platform for publishing articles, insights, and analysis related to cybersecurity topics. The blog supports:

- **Mixed content types** - Industry analysis, episode-related content, educational guides
- **Categories and tags** - Organize articles by topic and keywords
- **Featured posts** - Highlight specific articles on the homepage
- **Search and filter** - Client-side search, category, and tag filtering
- **SEO optimization** - Schema.org markup, Open Graph, Twitter Cards

---

## Creating a New Blog Post

### Method 1: Using Hugo Command (Recommended)

```bash
cd "/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website"

hugo new blog/your-article-title-slug.md
```

This creates a new blog post from the archetype template with proper front matter.

### Method 2: Manual Creation

1. Create a new file in `content/blog/` directory
2. Use the format: `article-title-slug.md`
3. Copy the front matter template below

---

## Blog Post Front Matter Template

```yaml
---
title: "Your Article Title"
date: 2025-11-25
draft: false
author: "Joe Patti"
category: "Cloud Security"
tags: ["AWS", "Zero Trust", "Compliance"]
image: "/images/blog/article-image.jpg"
description: "A compelling summary of the article that will appear in search results and social media shares (150-160 characters recommended)."
featured: false
---
```

### Front Matter Fields Explained

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | The article title (shown in headings and meta tags) |
| `date` | Yes | Publication date in YYYY-MM-DD format |
| `draft` | Yes | Set to `false` to publish, `true` to hide |
| `author` | Optional | Author name (e.g., "Joe Patti", "Adam Roth") |
| `category` | Optional | Single category for the article |
| `tags` | Optional | Array of tags for detailed topic classification |
| `image` | Optional | Path to featured image (relative to `/static/`) - **Not currently used** |
| `description` | Recommended | Meta description for SEO and social sharing |
| `featured` | Optional | Set to `true` to show on homepage (max 2 shown) |

---

## Content Structure

After the front matter, write your article content using Markdown:

```markdown
---
# Front matter here
---

Opening paragraph that hooks the reader and introduces the topic.

## Main Section Heading

Content for this section with **bold text** and *italic text* as needed.

### Subsection

- Bullet point 1
- Bullet point 2
- Bullet point 3

## Key Takeaways

- Important point 1
- Important point 2
- Important point 3

## Conclusion

Wrap up the article with final thoughts and call to action.
```

---

## Recommended Categories

Use consistent categories to help readers find related content:

- **AI Security**
- **Cloud Security**
- **CISO Leadership**
- **Compliance & Governance**
- **Cyber Threat Intelligence**
- **Data Protection**
- **Incident Response**
- **Penetration Testing**
- **SOC Operations**
- **Supply Chain Security**
- **Zero Trust**

*You can create new categories as needed, but try to reuse existing ones for consistency.*

---

## Tag Guidelines

Tags provide more granular topic classification:

- Use **lowercase** for consistency (e.g., "aws", "kubernetes", "phishing")
- Keep tags **specific** (e.g., "ransomware" instead of "malware")
- Limit to **3-8 tags** per article
- Reuse existing tags when possible

**Example tags**: `["zero-trust", "aws", "identity-management", "compliance", "nist"]`

---

## Images (Optional)

**Note**: The current blog design does not display featured images on blog cards or article pages. The `image` field in front matter is not currently used but can be left in place for future use.

If you want to add images within your article content, you can use standard Markdown:

```markdown
![Alt text description](/images/blog/inline-image.jpg)
```

Place images in `/static/images/blog/` and they will display inline within the article content.

---

## Featured Posts on Homepage

To feature an article on the homepage:

1. Set `featured: true` in the front matter
2. Maximum 2 featured posts will display
3. Most recent featured posts are shown first
4. Featured section only appears if at least 1 featured post exists

---

## Author Information

### Setting Author

```yaml
author: "Joe Patti"
```

### Optional Author Bio (in front matter)

```yaml
author_bio: "Joe Patti is a cybersecurity executive with over 15 years of experience in incident response, threat intelligence, and security operations."
```

The author bio will display in the sidebar of the blog post.

---

## Markdown Formatting Guide

### Headings

```markdown
## Main Section (H2)
### Subsection (H3)
#### Sub-subsection (H4)
```

### Text Formatting

```markdown
**Bold text**
*Italic text*
`Inline code`
```

### Lists

```markdown
- Unordered list item 1
- Unordered list item 2

1. Ordered list item 1
2. Ordered list item 2
```

### Blockquotes

```markdown
> This is a blockquote. Great for highlighting important statements or quotes.
```

### Code Blocks

````markdown
```python
def example_function():
    print("Hello, world!")
```
````

### Links

```markdown
[Link text](https://example.com)
```

---

## SEO Optimization

### Meta Description

- Length: 150-160 characters
- Include primary keyword
- Make it compelling and actionable
- Shown in search results and social shares

```yaml
description: "Learn how to implement zero trust architecture in AWS with practical examples and security best practices from industry experts."
```

### Title Best Practices

- Length: 50-60 characters
- Include primary keyword
- Make it descriptive and engaging
- Avoid clickbait

---

## Workflow: Adding a New Blog Post

1. **Create the post file**:
   ```bash
   hugo new blog/your-article-slug.md
   ```

2. **Edit front matter** with all required fields

3. **Write content** using Markdown

4. **Add featured image** (optional but recommended)

5. **Test locally**:
   ```bash
   hugo server -D
   # Visit http://localhost:1313/blog
   ```

6. **Review the article**:
   - Check formatting
   - Verify images load
   - Test links
   - Review on mobile view

7. **Publish** by setting `draft: false`

8. **Build site**:
   ```bash
   hugo --minify
   ```

9. **Deploy** via git push (Netlify) or GoDaddy cPanel

---

## Blog URL Structure

- **Blog archive**: `/blog/`
- **Individual post**: `/blog/your-article-slug/`
- **Category filter**: `/blog/?category=Cloud+Security` (via client-side JS)
- **Tag filter**: `/blog/?tag=aws` (via client-side JS)

---

## Related Features

### Newsletter Signup

Every blog post includes a newsletter signup form in the sidebar (Mailchimp integration).

### Social Sharing

Each article has social sharing buttons for:
- Twitter
- LinkedIn
- Email

### Related Articles

The sidebar shows up to 3 related articles based on:
1. Same category (if set)
2. Most recent articles
3. Excludes current article

---

## File Structure

```
/
├── content/
│   └── blog/                    # All blog post markdown files
│       ├── article-1.md
│       ├── article-2.md
│       └── ...
├── layouts/
│   └── blog/
│       ├── list.html            # Blog archive page
│       └── single.html          # Individual blog post page
├── archetypes/
│   └── blog.md                  # Template for new blog posts
├── static/
│   └── images/
│       └── blog/                # Blog post images
└── BLOG-DOCUMENTATION.md        # This file
```

---

## Troubleshooting

### Blog post not appearing

- Check `draft: false` in front matter
- Verify file is in `content/blog/` directory
- Check date is not in the future
- Rebuild site: `hugo --minify`

### Images not loading

- Verify image path starts with `/images/blog/`
- Check file exists in `/static/images/blog/`
- Ensure image filename has no spaces

### Featured post not showing on homepage

- Verify `featured: true` in front matter
- Check maximum 2 posts are featured
- Confirm at least one featured post exists

---

## Examples

### Example 1: Industry Analysis Article

```yaml
---
title: "The Future of Zero Trust in Cloud Environments"
date: 2025-11-25
draft: false
author: "Joe Patti"
category: "Cloud Security"
tags: ["zero-trust", "aws", "azure", "gcp", "identity-management"]
image: "/images/blog/zero-trust-cloud.jpg"
description: "Explore how zero trust architecture is evolving for cloud environments with practical implementation strategies and real-world examples."
featured: true
---
```

### Example 2: Episode Follow-up Article

```yaml
---
title: "Deep Dive: Securing High-Frequency Trading Systems"
date: 2025-11-25
draft: false
author: "Adam Roth"
category: "Financial Security"
tags: ["hft", "fintech", "low-latency", "trading-security"]
image: "/images/blog/hft-security.jpg"
description: "Extended insights from Episode 63 with Jatin Mannepalli on securing nanosecond-speed trading infrastructure."
featured: false
---
```

### Example 3: Educational Guide

```yaml
---
title: "Getting Started with AWS Security Hub"
date: 2025-11-25
draft: false
author: "Joe Patti"
category: "Cloud Security"
tags: ["aws", "security-hub", "compliance", "tutorial"]
image: "/images/blog/aws-security-hub-guide.jpg"
description: "Step-by-step tutorial for implementing AWS Security Hub to centralize and automate security monitoring across your AWS environment."
featured: false
---
```

---

## Quick Command Reference

```bash
# Create new blog post
hugo new blog/article-title.md

# Start development server
hugo server -D

# Build for production
hugo --minify

# Check Hugo version
hugo version

# View all blog posts locally
# Visit: http://localhost:1313/blog/
```

---

**For overall site documentation, see SESSION_CONTEXT.md**
**For deployment instructions, see GODADDY-DEPLOYMENT-INSTRUCTIONS.md**
