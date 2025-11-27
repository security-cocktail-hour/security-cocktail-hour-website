# Blog Pages Design Specification

**Version**: 1.0
**Date**: November 26, 2025
**Status**: Implemented
**Parent Design System**: [sch_design_spec_v1_2.md](./sch_design_spec_v1_2.md)

---

## 1. Overview

### 1.1 Purpose
The Blog section provides a platform for publishing cybersecurity insights, analysis, and deep dives that complement the podcast episodes. The blog serves to:
- Establish thought leadership in cybersecurity
- Improve SEO with keyword-rich content
- Provide written content for users who prefer reading
- Drive newsletter signups and engagement
- Create shareable content for social media

### 1.2 Pages Covered
This specification covers three blog-related implementations:

1. **Blog Archive Page** (`/blog/`) - Main listing page with search and filters
2. **Individual Blog Post Pages** (`/blog/[post-slug]/`) - Single post view with full content
3. **Featured Posts Section** - Homepage integration showing up to 2 featured posts

### 1.3 URLs
- Blog Archive: `https://securitycocktailhour.com/blog/`
- Individual Posts: `https://securitycocktailhour.com/blog/[post-slug]/`
- Category Pages: `https://securitycocktailhour.com/categories/[category]/`
- Tag Pages: `https://securitycocktailhour.com/tags/[tag]/`

---

## 2. Navigation Integration

### 2.1 Main Navigation
- **Menu Item**: "Blog"
- **Position**: Between "Episodes" and "Resources" (weight: 15)
- **Configuration**: Defined in `hugo.toml`
- **Style**: Inherits from main design system navigation

### 2.2 Footer Navigation
- **Section**: "Browse"
- **Position**: Second item (after "All Episodes", before "Resources")
- **Implementation**: `layouts/partials/footer.html` (line 13)

### 2.3 Breadcrumb Navigation
Individual blog posts include breadcrumb navigation:
- Home > Blog > [Post Title]
- Style: Light text on gradient background (rgba(255, 255, 255, 0.8))
- Separator: " > "

---

## 3. Blog Archive Page (`/blog/`)

### 3.1 Page Header
**Background**: Linear gradient (135deg, #436098 0%, #6A8CC7 100%)
**Text Color**: White
**Padding**: 3rem vertical, responsive horizontal via container

**Content**:
- **Heading**: "Blog" (H1, white)
- **Subheading**: "Insights, analysis, and deep dives into cybersecurity topics from the Security Cocktail Hour team."
  - Font size: 1.125rem
  - Max width: 600px
  - Color: White

### 3.2 Search and Filter Toolbar
**Background**: White
**Border**: Bottom 1px solid #E5E5E5
**Padding**: 1rem vertical
**Layout**: Flexbox with space-between alignment

**Components**:

#### 3.2.1 Search Input
- **Type**: Text search with SVG icon
- **Icon**: Magnifying glass (14×14px, positioned absolute left 10px)
- **Placeholder**: "Search..."
- **Style**:
  - Width: 100%
  - Padding: 6px 10px 6px 32px
  - Font size: 0.8125rem
  - Border: None (border-bottom only)
  - Border-bottom: 1px solid #E5E5E5
  - Background: Transparent
  - Focus state: Border-bottom color changes to #436098
- **Container**:
  - Flex: 1
  - Min-width: 200px
  - Max-width: 320px

#### 3.2.2 Filter Dropdowns
Three dropdowns in a row:

**Category Filter**:
- Default option: "Category"
- Dynamic options from all published blog posts
- Sorted alphabetically

**Tag Filter**:
- Default option: "Tag"
- Dynamic options from all published blog posts
- Sorted alphabetically

**Sort Filter**:
- Options: "Newest" (default), "Oldest"
- Controls date-based sorting

**Shared Dropdown Styles**:
- Padding: 6px 24px 6px 10px
- Font size: 0.8125rem
- Border: None (border-bottom only)
- Border-bottom: 1px solid #E5E5E5
- Background: Transparent
- Color: #192A56
- Custom dropdown arrow: SVG data URI (10×6px, #8D99AE)
- Arrow position: Right 6px center
- Cursor: Pointer
- Appearance: None (custom styling)

**Responsive Behavior**:
- Desktop: Search on left, filters on right
- Mobile: Stack vertically with gap
- Flex-wrap: Wrap

### 3.3 Main Content Layout
**Grid System**:
- Mobile: 1 column
- Desktop (900px+): 2 columns (2fr main content, 1fr sidebar)
- Gap: 2rem

#### 3.3.1 Blog Post Grid
**Layout**:
- Mobile: 1 column
- Desktop (900px+): 2 columns (within main content area)
- Gap: Standard grid gap from design system

**Post Cards**:
- **Component**: `.card` (from design system)
- **Class**: `.blog-card`
- **Data Attributes**:
  - `data-title`: Lowercase title for search
  - `data-category`: Category name
  - `data-tags`: Comma-separated tags
  - `data-date`: ISO format date (YYYY-MM-DD)

**Card Content**:
1. **Category Tag**:
   - Component: `.category-tag` (from design system)
   - Color: Secondary (#8D99AE)

2. **Title**:
   - Element: H3
   - Class: `.card-title`
   - Full post title (no truncation)

3. **Metadata**:
   - Class: `.card-meta`
   - Format: "[Author] | [Date]"
   - Date format: "January 2, 2006"

4. **Tag Pills** (first 3 tags):
   - Font size: 0.75rem
   - Color: #8D99AE
   - Background: rgba(141, 153, 174, 0.1)
   - Padding: 0.25rem 0.5rem
   - Border-radius: 4px
   - Display: Flex with gap 0.5rem

5. **Description**:
   - Class: `.card-description`
   - Content: Post description or summary
   - Truncated to 120 characters

6. **CTA Button**:
   - Text: "Read More"
   - Style: `.btn .btn-primary` (Professional Blue #436098)

#### 3.3.2 No Results Message
- Display: Hidden by default
- Trigger: When search/filter returns zero results
- Style:
  - Text align: Center
  - Padding: 3rem vertical
  - Message font size: 1.25rem
  - Message color: rgba(45, 45, 45, 0.6)
- Content: "No blog posts found matching your search."
- Action: "Clear Filters" button (`.btn .btn-secondary`)

### 3.4 Sidebar
**Position**: Sticky (top: 2rem)
**Background**: Linear gradient (135deg, #436098 0%, #6A8CC7 100%)
**Component**: `.card` with gradient background

**Content**:
1. **Heading**: "Join Our Newsletter" (H4, white)
2. **Description**: "Get exclusive insights, show news and more delivered to your inbox."
   - Font size: 0.875rem
   - Margin bottom: 1rem
3. **Newsletter Form**:
   - Action: Mailchimp subscribe endpoint
   - Method: POST
   - Target: _blank
   - Fields:
     - Email input (type: email, required)
     - Honeypot field (hidden, absolute positioned left -5000px)
     - Submit button: "Subscribe"
       - Style: White background, professional blue text (#436098)
       - Width: 100%

### 3.5 Client-Side Functionality
**JavaScript Features**:

1. **Search Filter**:
   - Triggers on input event
   - Matches against lowercase title
   - Case-insensitive search

2. **Category Filter**:
   - Triggers on change event
   - Exact match on category value
   - Empty value shows all

3. **Tag Filter**:
   - Triggers on change event
   - Matches tag in comma-separated list
   - Case-insensitive matching

4. **Sort Function**:
   - Triggers on change event
   - Sorts by date (newest/oldest)
   - Reorders DOM elements

5. **Reset Function**:
   - Clears all filter values
   - Resets to newest sort
   - Shows all posts
   - Triggered by "Clear Filters" button

6. **No Results Display**:
   - Hides grid when visibleCount === 0
   - Shows no results message
   - Reverses when filters changed

---

## 4. Individual Blog Post Page (`/blog/[post-slug]/`)

### 4.1 Page Header
**Background**: Linear gradient (135deg, #436098 0%, #6A8CC7 100%)
**Text Color**: White
**Padding**: 2rem vertical

**Content Sections**:

1. **Breadcrumb Navigation**:
   - Margin bottom: 1rem
   - Font size: 0.875rem
   - Link color: rgba(255, 255, 255, 0.8)
   - Current page color: White
   - Format: Home > Blog > [Post Title]

2. **Category and Tags**:
   - Display: Flex with gap 0.5rem
   - Category background: rgba(255, 255, 255, 0.3)
   - Tag background: rgba(255, 255, 255, 0.2)
   - Tag prefix: "#"
   - Limit: First 3 tags shown

3. **Title**:
   - Element: H1
   - Color: White
   - Margin bottom: 1rem

4. **Metadata**:
   - Font size: 1rem
   - Opacity: 0.95
   - Format: "[Author] | [Publish Date] | Updated [Modified Date]"
   - Date format: "January 2, 2006"
   - Updated date shown only if different from publish date

### 4.2 Main Content Layout
**Grid System**:
- Mobile: 1 column
- Desktop (900px+): 2 columns (2fr main content, 1fr sidebar)
- Gap: 2rem
- Scoping: `.section .container > div` to avoid footer conflicts

#### 4.2.1 Article Description Box
**Conditional Display**: Only if post has description parameter

**Style**:
- Background: #F5F5F5
- Padding: 1.5rem
- Border-left: 4px solid #436098
- Margin bottom: 2rem
- Border-radius: 4px

**Content**:
- Font size: 1.125rem
- Font weight: 500
- Color: #192A56 (Primary Dark Blue)
- Margin: 0

#### 4.2.2 Article Content
**Container**: `.article-content`
**Margin bottom**: 2rem

**Typography Styles**:

**H2**:
- Color: #192A56
- Margin-top: 2rem
- Margin-bottom: 1rem
- Font size: 1.75rem

**H3**:
- Color: #192A56
- Margin-top: 1.5rem
- Margin-bottom: 0.75rem
- Font size: 1.5rem

**H4**:
- Color: #192A56
- Margin-top: 1.25rem
- Margin-bottom: 0.5rem
- Font size: 1.25rem

**Paragraphs**:
- Margin-bottom: 1rem
- Line-height: 1.7

**Lists (ul, ol)**:
- Margin-bottom: 1rem
- Padding-left: 2rem
- List items:
  - Margin-bottom: 0.5rem
  - Line-height: 1.7

**Blockquotes**:
- Border-left: 4px solid #436098
- Padding-left: 1.5rem
- Margin: 1.5rem 0
- Font-style: Italic
- Color: rgba(45, 45, 45, 0.8)

**Code**:
- Inline code:
  - Background: #F5F5F5
  - Padding: 0.2rem 0.4rem
  - Border-radius: 4px
  - Font-size: 0.9em
  - Font-family: Monospace
- Code blocks (pre):
  - Background: #F5F5F5
  - Padding: 1rem
  - Border-radius: 8px
  - Overflow-x: Auto
  - Margin: 1.5rem 0
  - Nested code: Transparent background, no padding

**Images**:
- Max-width: 100%
- Height: Auto
- Border-radius: 8px
- Margin: 1.5rem 0

#### 4.2.3 Tags Section
**Conditional Display**: Only if post has tags

**Style**:
- Border-top: 1px solid #E5E5E5
- Padding-top: 1.5rem
- Margin-top: 2rem
- Margin-bottom: 2rem

**Content**:
1. **Heading**: "Tags" (H4, margin-bottom: 1rem)
2. **Tag Links**:
   - Display: Flex with gap 0.5rem, wrap
   - Each tag links to: `/blog/?tag=[tag]`
   - Style:
     - Font size: 0.875rem
     - Color: #436098
     - Background: rgba(67, 96, 152, 0.1)
     - Padding: 0.5rem 1rem
     - Border-radius: 20px
     - Text decoration: None
     - Transition: All 0.2s
   - Prefix: "#"

#### 4.2.4 Social Sharing Section
**Style**:
- Border-top: 1px solid #E5E5E5
- Padding-top: 1.5rem
- Margin-top: 2rem

**Content**:
1. **Heading**: "Share This Post" (H4)
2. **Share Buttons** (Flexbox, gap: 1rem):
   - Twitter: Intent tweet with title and URL
   - LinkedIn: Share offsite with URL
   - Email: Mailto with subject and body
   - Style: `.btn .btn-secondary` for all buttons
   - Target: `_blank` with `rel="noopener"` for external links

### 4.3 Sidebar
**Grid column**: 2 (on desktop)

**Components**:

1. **Newsletter Signup Card**:
   - Component: `.card`
   - Background: Linear gradient (135deg, #436098 0%, #6A8CC7 100%)
   - Color: White
   - Margin-bottom: 2rem
   - Content:
     - Heading: "Join Our Newsletter" (H4, white)
     - Description: "Get exclusive insights, show news and more delivered to your inbox."
       - Font size: 0.875rem
       - Margin bottom: 1rem
     - Form: Same Mailchimp integration as blog list page
       - Email input (white background)
       - Honeypot field (hidden)
       - Submit button: White background, #436098 text, full width

2. **View All Posts Button**:
   - Text: "View All Posts"
   - Link: `/blog/`
   - Style: `.btn .btn-secondary`
   - Width: 100%
   - Text-align: Center

---

## 5. Featured Posts Section (Homepage)

### 5.1 Conditional Display
**Logic**: Only displays if there are posts with `featured: true` parameter
**Limit**: Maximum 2 featured posts shown
**Query**: `where (where .Site.RegularPages "Type" "blog") ".Params.featured" true | first 2`

### 5.2 Section Header
**Background**: #F5F5F5 (alternating section background)
**Container**: Standard `.container`

**Content**:
- **Layout**: Flexbox with space-between and center alignment
- **Left**: "Featured Blog Posts" (H2, margin: 0)
- **Right**: "View All →" link
  - Color: #436098
  - Font-weight: 600
  - Text-decoration: None
  - Links to: `/blog/`
- **Margin-bottom**: 2rem

### 5.3 Post Grid
**Layout**: `.grid .grid-2` (2 columns on desktop, 1 on mobile)

**Post Cards**:
1. **Category Tag**: If present, displayed at top
2. **Title**: H3 with `.card-title`
3. **Metadata**:
   - Format: "[Author] | [Date]"
   - Date format: "January 2, 2006"
4. **Description**:
   - Truncated to 120 characters
   - Uses description parameter or summary
5. **CTA Button**:
   - Text: "Read More"
   - Style: `.btn .btn-primary`

---

## 6. SEO & Metadata

### 6.1 Blog Archive Page SEO

**Meta Description**:
```html
<meta name="description" content="Browse our complete archive of cybersecurity insights, analysis, and practical guidance. Blog posts from Security Cocktail Hour covering industry trends, security operations, and practitioner perspectives.">
```

**Schema.org Markup** (JSON-LD):
- **Type**: `Blog`
- **Properties**:
  - name: "Security Cocktail Hour Blog"
  - description: "Cybersecurity insights, analysis, and practical guidance from industry practitioners"
  - url: Page permalink
  - publisher: Organization object with site title and base URL
  - blogPost: Array of first 10 posts with BlogPosting objects
    - Each post includes: headline, url, datePublished, description

**Open Graph Tags**:
- `og:type`: "website"
- `og:url`: Page permalink
- `og:title`: "Blog | Security Cocktail Hour"
- `og:description`: Archive description
- `og:site_name`: Site title

**Twitter Card Tags**:
- `twitter:card`: "summary"
- `twitter:url`: Page permalink
- `twitter:title`: "Blog | Security Cocktail Hour"
- `twitter:description`: Archive description

### 6.2 Individual Blog Post SEO

**Schema.org Markup** (JSON-LD):
- **Type**: `BlogPosting`
- **Properties**:
  - headline: Post title
  - datePublished: ISO format date
  - dateModified: ISO format modified date
  - author: Person object (uses author parameter or "Security Cocktail Hour")
  - publisher: Organization object
  - description: Post description or summary
  - url: Post permalink
  - image: Optional post image (absolute URL)

**Open Graph Tags**:
- `og:type`: "article"
- `og:url`: Post permalink
- `og:title`: Post title
- `og:description`: Post description or summary
- `og:image`: Optional post image (absolute URL)

**Twitter Card Tags**:
- `twitter:card`: "summary_large_image"
- `twitter:url`: Post permalink
- `twitter:title`: Post title
- `twitter:description`: Post description or summary
- `twitter:image`: Optional post image (absolute URL)

**Title Tag**:
```
{{ .Title }} | {{ .Site.Title }}
```

---

## 7. Content Architecture

### 7.1 Blog Post Front Matter
```yaml
---
title: "Post Title"
date: YYYY-MM-DD
draft: false
author: "Author Name"  # Optional, defaults to "Security Cocktail Hour"
category: "Category Name"
tags: ["tag1", "tag2", "tag3"]
description: >-
  Post summary/description for meta tags and card display.
  Uses YAML block scalar for multi-line content.
featured: true  # Optional, includes in homepage featured section
image: "/images/blog/image.jpg"  # Optional, for social sharing
---
```

### 7.2 Taxonomy Support
**Categories**:
- Single category per post
- Used for filtering on archive page
- Archive pages generated at `/categories/[category]/`

**Tags**:
- Multiple tags per post
- Used for filtering on archive page
- Archive pages generated at `/tags/[tag]/`
- First 3 tags shown on cards and post headers

### 7.3 File Structure
```
content/
└── blog/
    ├── post-one-slug.md
    ├── post-two-slug.md
    └── ...

layouts/
├── blog/
│   ├── list.html      # Blog archive page
│   └── single.html    # Individual post page
└── _default/
    ├── taxonomy.html  # Category/tag list pages
    └── term.html      # Individual category/tag pages

archetypes/
└── blog.md           # Template for new blog posts
```

---

## 8. Design System References

### 8.1 Colors
All colors reference the main design system (`sch_design_spec_v1_2.md`):

- **Primary (Dark Blue)**: #192A56 - Headings, body text
- **Secondary (Cool Grey)**: #8D99AE - Tags, meta text, borders
- **Background (Off-white)**: #F8F9FA - Page backgrounds
- **Action (Professional Blue)**: #436098 - Buttons, CTAs, gradients
- **Accent (Bright Red)**: #CE1F2C - Not used in blog (reserved for "Listen Now")

**Gradient Usage**:
- Headers: `linear-gradient(135deg, #436098 0%, #6A8CC7 100%)`
- Newsletter cards: Same gradient

### 8.2 Typography
Referenced from main design system:

- **Font Family**: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif
- **Base Font Size**: 16px (1rem)
- **Line Height**: 1.6 (body), 1.7 (article content)
- **Headings**: Uses design system heading sizes and weights

### 8.3 Components
All components inherit from main design system:

- **Buttons**: `.btn`, `.btn-primary`, `.btn-secondary`
- **Cards**: `.card`, `.card-content`, `.card-title`, `.card-meta`, `.card-description`
- **Category Tags**: `.category-tag`
- **Grid**: `.grid`, `.grid-2`, `.grid-3`
- **Container**: `.container`
- **Section**: `.section`

### 8.4 Spacing
Uses design system spacing scale:
- Standard section padding
- Card padding
- Grid gaps
- Component margins

---

## 9. Responsive Breakpoints

### 9.1 Desktop (900px and above)
**Blog Archive Page**:
- Main layout: 2fr (content) + 1fr (sidebar)
- Blog post grid: 2 columns
- Search/filter toolbar: Horizontal layout
- Sidebar: Sticky positioning

**Blog Single Page**:
- Main layout: 2fr (article) + 1fr (sidebar)
- Article max-width: Natural flow within grid
- Sidebar: Fixed width via grid

**Homepage Featured Posts**:
- Grid: 2 columns

### 9.2 Mobile (below 900px)
**Blog Archive Page**:
- Main layout: 1 column (stacked)
- Blog post grid: 1 column
- Search/filter toolbar: Wraps with flex
- Sidebar: Full width, below content

**Blog Single Page**:
- Main layout: 1 column (stacked)
- Article: Full width
- Sidebar: Full width, below article

**Homepage Featured Posts**:
- Grid: 1 column

### 9.3 CSS Implementation
**Media Query**:
```css
@media (min-width: 900px) {
  .section .container > div {
    grid-template-columns: 2fr 1fr !important;
  }
  #blog-grid.grid-3 {
    grid-template-columns: repeat(2, 1fr) !important;
  }
}
```

**Scoping Note**: The selector `.section .container > div` specifically targets blog section layouts and prevents conflicts with footer layout, which also uses `.container > div` structure.

---

## 10. Implementation Notes

### 10.1 Key Technical Decisions

**Text-Focused Design**:
- Blog posts do not require images
- Cards work with or without images
- Social sharing images are optional
- Gradient backgrounds provide visual interest

**Client-Side Filtering**:
- No server-side processing required
- Fast, responsive filtering
- Works without JavaScript (posts still display)
- Simple vanilla JavaScript implementation

**SEO Priority**:
- Full Schema.org markup on all pages
- Comprehensive Open Graph and Twitter Card tags
- Semantic HTML structure
- Descriptive meta descriptions

**Mailchimp Integration**:
- Same newsletter form as used on Episodes and other pages
- Includes honeypot spam protection
- Opens in new tab to preserve user's place

**CSS Scoping Fix**:
- Initial implementation used `.container > div` selector
- Caused layout conflicts with footer (also uses `.container > div`)
- Fixed by changing to `.section .container > div`
- Limits scope to blog section content areas only

### 10.2 Content Guidelines

**Writing Style**:
- Professional but conversational
- Focused on practical insights
- Complementary to podcast content
- 800-2000 words ideal length

**Categories**:
- Keep focused and limited in number
- Use for broad topic areas
- Examples: "Security Operations", "Leadership", "Technical Deep Dives"

**Tags**:
- Use for specific topics
- Enable cross-content discovery
- Examples: "AI", "CISO", "Incident Response", "Cloud Security"

**Featured Posts**:
- Limit to 2 on homepage
- Choose timely, high-quality content
- Update regularly to keep homepage fresh

### 10.3 Maintenance Considerations

**Adding New Posts**:
1. Use archetype: `hugo new blog/post-slug.md`
2. Fill in all front matter fields
3. Write content using markdown
4. Set `draft: false` when ready
5. Optionally add `featured: true` for homepage

**Taxonomy Management**:
- Categories and tags auto-generate from posts
- No manual configuration needed
- Archive pages created automatically

**SEO Updates**:
- All meta tags pull from front matter
- Update description for better search snippets
- Add images for richer social sharing

**Performance**:
- No images required reduces page weight
- Client-side JS is minimal (~30 lines)
- Static generation ensures fast loads
- Newsletter form loads from CDN

---

## 11. Testing Checklist

### 11.1 Visual Testing
- [ ] Blog archive page displays correctly on desktop (900px+)
- [ ] Blog archive page displays correctly on mobile (<900px)
- [ ] Individual post page layout works on desktop
- [ ] Individual post page layout works on mobile
- [ ] Featured posts section appears on homepage (when featured posts exist)
- [ ] Featured posts section hidden when no featured posts
- [ ] All gradient backgrounds render correctly
- [ ] Newsletter forms display properly
- [ ] Social sharing buttons aligned correctly
- [ ] Typography follows design system

### 11.2 Functional Testing
- [ ] Search filters posts by title (case-insensitive)
- [ ] Category filter shows only matching posts
- [ ] Tag filter shows posts with matching tags
- [ ] Sort toggles between newest and oldest
- [ ] Multiple filters work together correctly
- [ ] Clear filters button resets all filters
- [ ] No results message appears when appropriate
- [ ] Newsletter form submits to Mailchimp
- [ ] Social sharing links work correctly
- [ ] Breadcrumb navigation links work
- [ ] Tag links on posts filter correctly
- [ ] View All Posts button works from single pages

### 11.3 SEO Testing
- [ ] Schema.org markup validates (Google Rich Results Test)
- [ ] Open Graph tags present on all pages
- [ ] Twitter Card tags present on all pages
- [ ] Meta descriptions unique and descriptive
- [ ] Title tags follow proper format
- [ ] Blog archive appears in sitemap
- [ ] Individual posts appear in sitemap
- [ ] Category pages indexed properly
- [ ] Tag pages indexed properly

### 11.4 Responsive Testing
- [ ] Search toolbar wraps properly on mobile
- [ ] Filter dropdowns accessible on mobile
- [ ] Sidebar appears below content on mobile
- [ ] Grid switches to single column on mobile
- [ ] All touch targets minimum 44×44px
- [ ] Text remains readable at all sizes
- [ ] Newsletter form usable on mobile

### 11.5 Accessibility Testing
- [ ] Headings follow proper hierarchy (H1 > H2 > H3)
- [ ] Form inputs have labels/placeholders
- [ ] Links have descriptive text
- [ ] Color contrast meets WCAG AA standards
- [ ] Keyboard navigation works throughout
- [ ] Focus states visible on interactive elements
- [ ] Honeypot field properly hidden from screen readers

### 11.6 Cross-Browser Testing
- [ ] Chrome/Edge (Chromium)
- [ ] Firefox
- [ ] Safari (desktop)
- [ ] Safari (iOS)
- [ ] Chrome (Android)

### 11.7 Integration Testing
- [ ] Blog link appears in main navigation
- [ ] Blog link appears in footer
- [ ] Featured posts integrate with homepage
- [ ] Newsletter form connects to Mailchimp
- [ ] Social sharing generates correct URLs
- [ ] Category/tag taxonomy pages work
- [ ] No layout conflicts with other pages

---

## 12. File Reference

### 12.1 Template Files
- `layouts/blog/list.html` - Blog archive page template
- `layouts/blog/single.html` - Individual blog post template
- `layouts/index.html` - Homepage (includes featured posts section)
- `layouts/_default/taxonomy.html` - Category/tag list pages
- `layouts/_default/term.html` - Individual category/tag pages
- `layouts/partials/footer.html` - Footer with Blog link

### 12.2 Content Files
- `content/blog/` - Directory containing all blog post markdown files
- `archetypes/blog.md` - Template for creating new blog posts

### 12.3 Configuration
- `hugo.toml` - Main menu configuration (Blog menu item, weight: 15)

### 12.4 Documentation
- `BLOG-DOCUMENTATION.md` - User guide for creating and managing blog posts
- `BLOG-SEO-PLAN.md` - SEO strategy and implementation plan
- `docs/design_specs/blog_page_spec.md` - This specification document

---

## 13. Version History

**Version 1.0** (November 26, 2025)
- Initial specification created
- Documented implemented blog feature
- Covers blog archive, single posts, and homepage integration
- Includes Priority 1 SEO enhancements
- Documents CSS scoping fix for footer conflicts
- Terminology standardized to "blog post" throughout

---

**End of Blog Pages Design Specification**
