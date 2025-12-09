# Partnership Page Design Specification
## Security Cocktail Hour Website

**Version:** 1.1
**Date:** December 9, 2025
**Status:** Implemented & Deployed (Art Deco Design Update)
**Page Type:** Static Marketing Page
**URL:** `/partnership` or `/sponsorship`
**Parent Design System:** [sch_design_spec_v1_3.md](./sch_design_spec_v1_3.md)  

---

## 1. Page Overview

### Purpose
Present partnership and sponsorship opportunities for the Security Cocktail Hour podcast. Convert potential sponsors and partners by clearly communicating value proposition, package tiers, and audience reach.

### Key Goals
- Showcase partnership tiers and benefits
- Communicate podcast reach and audience demographics
- Drive potential sponsors to contact page
- Professional presentation that conveys competence and credibility

---

## 2. Navigation Integration

### Top Navigation Menu
**CRITICAL:** Add "Partnership" link to the main navigation menu.

**Navigation Structure:**
```
[Logo] [Episodes] [About] [Resources] [Partnership] [Contact] [Listen Now Button]
```

**Placement:** Between "Resources" and "Contact"

**Link Properties:**
- Text: "Partnership"
- URL: `/partnership` (or `/sponsorship` - use same URL structure as other pages)
- Font Size: 1rem (16px)
- Font Weight: 500
- Color: Primary (#192A56)
- Hover: Action Blue (#436098)
- Active state: Action Blue (#436098) with appropriate indicator

---

## 3. Page Structure

### Section Breakdown

1. **Navigation** (reuse existing site navigation component)
2. **Hero Section** - Page title and subtitle
3. **About & Audience Section** - Two-column layout
4. **Partnership Levels Section** - Three-card tier comparison
5. **Why Support Section** - Four benefit cards
6. **Metrics Section** - Three stat cards
7. **CTA Section** - Call to action with contact button
8. **Footer** (reuse existing site footer component)

---

## 4. Content Sections - Detailed Specifications

### 4.1 Hero Section

**Layout:**
- Full-width section
- Centered content
- Maximum width: 900px
- Padding: 4rem 1.5rem 3rem

**Background:**
- Linear gradient: Action Blue (#436098) to Light Action Blue (#6A8CC7)
- Direction: 135deg diagonal

**Content:**
```
H1: "Partnership Opportunities"
- Font size: 2.5rem (desktop), 2rem (mobile)
- Font weight: 700
- Color: White
- Margin bottom: 1rem

Subtitle: "Support the Podcast that Supports You"
- Font size: 1.25rem (desktop), 1.125rem (mobile)
- Font weight: 400
- Font style: italic
- Color: White
- Opacity: 0.95
- Margin bottom: 2rem
```

---

### 4.2 About & Audience Section

**Layout:**
- Two-column grid (1fr 1fr)
- Gap: 3rem
- Section padding: 3rem 0
- Background: #F8F9FA

**Responsive:** Single column on mobile (< 968px)

#### About Box (Left Column)

**Container:**
- Background: White
- Padding: 2rem
- Border radius: 12px
- Box shadow: 0 2px 8px rgba(0, 0, 0, 0.1)

**Content:**
```
H2: "About the Podcast"
- Font size: 2rem
- Font weight: 700
- Color: Primary (#192A56)
- Margin bottom: 1rem

Paragraph 1:
"Hosted by Joe Patti and Adam Roth, the Security Cocktail Hour features candid, in-depth discussions about the latest security topics and current events with expert guests from across the industry."

Paragraph 2:
"With 62+ episodes, we've built a dedicated community of security practitioners who trust our insights and recommendations."

- Line height: 1.7
- Margin bottom: 1rem per paragraph
```

#### Audience Box (Right Column)

**Container:**
- Background: White
- Padding: 2rem
- Border radius: 12px
- Box shadow: 0 2px 8px rgba(0, 0, 0, 0.1)

**Content:**
```
H2: "Our Audience"
- Font size: 2rem
- Font weight: 700
- Color: Primary (#192A56)
- Margin bottom: 1rem

Bulleted List (custom bullets):
• "Cybersecurity professionals (CISOs, Security Engineers, SOC Analysts)"
• "Technology leaders and decision-makers"
• "Cybersecurity vendors and consultants"
• "IT professionals and others transitioning into security"

Bullet styling:
- Custom bullet: "•" (large dot)
- Bullet color: Action Blue (#436098)
- Bullet font size: 1.5rem
- Bullet font weight: bold
- List item padding: 0.75rem 0
- List item padding-left: 1.5rem
- Line height: 1.6

Closing note (below list):
"Highly engaged professionals who value deep discussions"
- Font style: italic
- Color: Accent Red (#CE1F2C)
- Margin top: 1rem
- Font weight: 500
```

---

### 4.3 Partnership Levels Section

**Layout:**
- Section padding: 3rem 0
- Background: White

**Header:**
```
H2: "Partnership Levels"
- Font size: 2.5rem (desktop), 2rem (mobile)
- Font weight: 700
- Color: Primary (#192A56)
- Text align: center
- Margin bottom: 3rem
```

**Three-Column Card Grid:**
- Grid: repeat(3, 1fr)
- Gap: 2rem
- Responsive: Single column on mobile (< 968px)

**IMPORTANT:** Cards must use flexbox to ensure buttons align to bottom regardless of content length.

#### Card Structure (All Three Cards)

**Container:**
- Background: White
- Border radius: 12px
- Box shadow: 0 4px 16px rgba(0, 0, 0, 0.12)
- Display: flex
- Flex direction: column
- Transition: all 0.3s

**Hover State:**
- Transform: translateY(-4px)
- Box shadow: 0 8px 24px rgba(0, 0, 0, 0.15)

**Card Header Section:**
- Padding: 2rem
- Text align: center
- Color: White

**Card Body:**
- Padding: 2rem
- Display: flex
- Flex direction: column
- Height: 100%

**List Container:**
- List style: none
- Margin bottom: 2rem
- Flex-grow: 1 (pushes button to bottom)

**List Items:**
- Padding: 0.75rem 0
- Padding-left: 1.5rem
- Line height: 1.5
- Border bottom: 1px solid #F8F9FA
- Position: relative

**List Item Checkmark:**
- Content: "✓"
- Position: absolute
- Left: 0
- Color: Action Blue (#436098)
- Font weight: bold

**Button (All Cards):**
- Text: "Learn More"
- Link: `/contact`
- Width: 100%
- Border radius: 8px
- Padding: 0.75rem 1.5rem
- Font weight: 600
- Transition: all 0.2s

#### Card 1: Supporter - $500

**Header Background:**
- Linear gradient: Action Blue (#436098) to lighter variant (#6A8CC7)
- Direction: 135deg

**Content:**
```
Tier: "SUPPORTER"
- Font size: 1.5rem
- Font weight: 700
- Text transform: uppercase
- Margin bottom: 0.5rem

Price: "$500"
- Font size: 2.5rem
- Font weight: 700

Benefits (bulleted list):
• "Company mention during episode"
• "Link & CTA in episode description"
• "Social media recognition"

Button:
- Background: Action Blue (#436098)
- Text: White
- Hover background: Darken 10% (#3A5282)
- Hover effect: translateY(-2px)
- Hover shadow: 0 4px 12px rgba(67, 96, 152, 0.3)
```

#### Card 2: Featured Partner - $1,000

**Header Background:**
- Linear gradient: Primary (#192A56) to Action Blue (#436098)
- Direction: 135deg

**Content:**
```
Tier: "FEATURED PARTNER"
- Font size: 1.5rem
- Font weight: 700
- Text transform: uppercase
- Margin bottom: 0.5rem

Price: "$1,000"
- Font size: 2.5rem
- Font weight: 700

Benefits (bulleted list):
• "Everything in Supporter"
• "15-second ad read"
• "Featured paragraph in episode description"

Button:
- Background: Action Blue (#436098)
- Text: White
- Hover background: Darken 10% (#3A5282)
- Hover effect: translateY(-2px)
- Hover shadow: 0 4px 12px rgba(67, 96, 152, 0.3)
```

#### Card 3: Episode Sponsor - $2,500

**Header Background:**
- Linear gradient: Accent Red (#CE1F2C) to darker red (#B41A26)
- Direction: 135deg

**Content:**
```
Tier: "EPISODE SPONSOR"
- Font size: 1.5rem
- Font weight: 700
- Text transform: uppercase
- Margin bottom: 0.5rem

Price: "$2,500"
- Font size: 2.5rem
- Font weight: 700

Benefits (bulleted list):
• "Everything in Featured Partner"
• "60-second ad read"
• "Logo featured in episode intro"
• "Dedicated social media post"

Button:
- Background: Accent Red (#CE1F2C)
- Text: White
- Hover background: Darken 10% (#B41A26)
- Hover effect: translateY(-2px)
- Hover shadow: 0 4px 12px rgba(206, 31, 44, 0.3)
```

**Custom Packages Note (Below Cards):**
```
Text: "Custom packages available — let's discuss what works for your team."
- Font style: italic
- Color: Secondary (#8D99AE)
- Text align: center
- Margin top: 2rem
- Padding: 1.5rem
- Background: #F8F9FA
- Border radius: 8px
```

---

### 4.4 Why Support Section

**Layout:**
- Section padding: 3rem 0
- Background: #F8F9FA

**Header:**
```
H2: "Why Support Your Team Member's Appearance?"
- Font size: 2rem
- Font weight: 700
- Color: Primary (#192A56)
- Text align: center
- Margin bottom: 2rem
```

**Four-Item Grid:**
- Grid: repeat(2, 1fr)
- Gap: 2rem
- Max width: 900px
- Margin: 0 auto
- Responsive: Single column on mobile (< 968px)

#### Benefit Cards (All Four)

**Container:**
- Background: White
- Padding: 2rem
- Border radius: 8px
- Box shadow: 0 2px 8px rgba(0, 0, 0, 0.1)
- Text align: left

**Content Structure:**
```
H3: Benefit Title
- Color: Action Blue (#436098)
- Margin bottom: 0.5rem
- Font weight: 600

P: Description
- Color: Primary (#192A56)
- Line height: 1.6
```

**Card 1:**
```
Title: "Professional Development Visibility"
Description: "Showcase your team members as industry thought leaders and support their professional growth."
```

**Card 2:**
```
Title: "Industry Thought Leadership Positioning"
Description: "Position your organization at the forefront of cybersecurity conversations and innovations."
```

**Card 3:**
```
Title: "Authentic Connection with Security Practitioners"
Description: "Build genuine relationships with cybersecurity professionals through meaningful content."
```

**Card 4:**
```
Title: "Support for Cybersecurity Education"
Description: "Contribute to the advancement of cybersecurity knowledge and help elevate the entire industry."
```

---

### 4.5 Metrics Section

**Layout:**
- Section padding: 3rem 0
- Background: White
- Text align: center

**Header:**
```
H2: "Podcast Metrics"
- Font size: 2rem
- Font weight: 700
- Color: Primary (#192A56)
- Text align: center
- Margin bottom: 2rem
```

**Three-Column Grid:**
- Grid: repeat(3, 1fr)
- Gap: 2rem
- Max width: 900px
- Margin: 0 auto 2rem
- Responsive: Single column on mobile (< 968px)

#### Metric Cards (All Three)

**Container:**
- Background: Linear gradient Action Blue (#436098) to lighter (#6A8CC7)
- Direction: 135deg
- Color: White
- Padding: 2rem
- Border radius: 12px
- Box shadow: 0 2px 8px rgba(0, 0, 0, 0.1)

**Content:**
```
Number Display:
- Font size: 2.5rem
- Font weight: 700
- Margin bottom: 0.5rem

Label:
- Font size: 1rem
- Opacity: 0.9
```

**Metric 1:**
```
Number: "44,000"
Label: "Total Views"
```

**Metric 2:**
```
Number: "81,000"
Label: "Impressions"
```

**Metric 3:**
```
Number: "407"
Label: "Subscribers"
```

**Stats Note (Below Cards):**
```
Text: "Stats for YouTube, 11/7/2024-11/7/2025"
- Font size: 0.875rem
- Color: Secondary (#8D99AE)
- Font style: italic
```

---

### 4.6 CTA Section

**Layout:**
- Section padding: 4rem 0
- Background: Linear gradient Action Blue (#436098) to Light Action Blue (#6A8CC7)
- Direction: 135deg
- Color: White
- Text align: center

**Content:**
```
H2: "Ready to Partner With Us?"
- Font size: 2rem (desktop), 1.75rem (mobile)
- Font weight: 700
- Margin bottom: 1rem

Paragraph:
"Let's discuss how we can work together to support cybersecurity education and connect with engaged professionals."
- Font size: 1.125rem
- Margin bottom: 2rem
- Opacity: 0.95

Button:
Text: "Contact Us"
Link: `/contact`
Style:
- Background: White
- Color: Primary (#192A56)
- Padding: 0.875rem 2rem
- Border radius: 8px
- Font weight: 600
- Text decoration: none
- Display: inline-block
- Transition: all 0.2s

Hover State:
- Background: #F8F9FA
- Transform: translateY(-2px)
- Box shadow: 0 4px 12px rgba(255, 255, 255, 0.3)
```

---

## 5. SEO & Metadata

### Page Metadata
```html
<title>Partnership Opportunities - Security Cocktail Hour Podcast</title>
<meta name="description" content="Support the Security Cocktail Hour podcast through partnership opportunities. Connect with cybersecurity professionals and support cybersecurity education.">
```

### Schema.org Structured Data
Consider adding:
- Organization schema
- WebPage schema
- Offer schema for each partnership tier

---

## 6. Responsive Breakpoints

### Mobile (< 768px)
- Hide navigation links (show hamburger menu if implemented)
- Hero H1: 2rem
- Hero subtitle: 1.125rem
- All grid layouts: Single column
- Partnership header H2: 2rem
- CTA H2: 1.75rem

### Tablet (768px - 968px)
- About/Audience: Single column
- Partnership cards: Single column
- Benefits grid: Single column
- Metrics: Single column
- Maintain most desktop styling

### Desktop (> 968px)
- Full multi-column layouts
- All hover effects active
- Maximum content width: 1200px

---

## 7. Implementation Notes for Claude Code

### Integration Requirements

1. **Navigation Update:**
   - Add "Partnership" link to main navigation component
   - Update navigation array/menu data structure
   - Ensure active state styling works correctly

2. **URL Routing:**
   - Create route for `/partnership` (or `/sponsorship`)
   - Ensure URL is consistent with site routing pattern

3. **Reusable Components:**
   - Use existing navigation component
   - Use existing footer component
   - Use existing button styles (btn-primary, btn-secondary, btn-white)
   - Use existing container/section patterns

4. **Content Management:**
   - Consider if partnership tiers should be data-driven
   - Consider if metrics should be updatable via config/data file
   - Maintain content in easily editable format

5. **Template Structure:**
   - Use same template system as other pages
   - Ensure proper semantic HTML
   - Include all accessibility features (ARIA labels, alt text, etc.)

6. **Performance:**
   - No images on this page (uses gradients and icons)
   - Minimal external dependencies
   - Fast load time priority

### Testing Checklist

- [ ] Navigation link appears in correct position
- [ ] Navigation link highlights on active page
- [ ] All buttons link to `/contact` page
- [ ] Partnership cards align properly with varying content
- [ ] All hover effects work
- [ ] Responsive layouts work on mobile, tablet, desktop
- [ ] Typography matches design spec exactly
- [ ] Colors match production palette exactly
- [ ] Page loads quickly
- [ ] No console errors
- [ ] Semantic HTML structure
- [ ] Accessibility (keyboard navigation, screen readers)

---

## 8. Color Reference (Art Deco Palette)

**Updated: December 9, 2025** - Aligned with Design Spec v1.3

```css
/* Art Deco Primary Colors */
--red: #D74444                     /* Art Deco Accent - primary CTAs, highlights */
--red-dark: #A63333                /* Red Dark - hover states */
--navy: #2B4D7D                    /* Navy - main text, headers, backgrounds */
--navy-light: #3A5F99              /* Navy Light - lighter accents */
--navy-dark: #1F3859               /* Navy Dark - darker accents */
--teal: #4A9B9B                    /* Teal - links, interactive elements */
--teal-light: #6BB8B8              /* Teal Light - hover states */
--cream: #F5F1E8                   /* Cream - main background */
--cream-dark: #E8E0D0              /* Cream Dark - subtle backgrounds */
--white: #FFFFFF                   /* White - pure white elements */

/* Gradients (135deg diagonal) */
/* Note: These gradients are documented in Design Spec v1.3 */
Navy Gradient: linear-gradient(135deg, #1F3859, #2B4D7D, #3A5F99)
Red Gradient: linear-gradient(135deg, #A63333, #D74444)
Teal Gradient: linear-gradient(135deg, #4A9B9B, #6BB8B8)
```

**Partnership Page Usage:**
- **Hero Section**: Navy gradient background
- **Featured Partner Card**: Navy to Navy Light gradient header
- **Episode Sponsor Card**: Red gradient header (premium tier)
- **Supporter Card**: Navy gradient header (base tier)
- **Metrics Cards**: Navy gradient backgrounds
- **CTA Section**: Navy gradient background
- **Buttons**: Red (primary), Navy (secondary)

---

## 9. Typography Reference (Art Deco Fonts)

**Updated: December 9, 2025** - Aligned with Design Spec v1.3

Referenced from main design system (Art Deco fonts):

```css
/* Google Fonts - Art Deco Typography */
--font-heading: 'Oswald', sans-serif;        /* Headings, titles */
--font-body: 'PT Serif', serif;              /* Body text, descriptions */
--font-ui: 'Bebas Neue', cursive;            /* UI elements, badges */

/* Font Weights */
Oswald: 600 (semi-bold), 700 (bold)
PT Serif: 400 (regular), 700 (bold)
Bebas Neue: 400 (regular)

/* Typography Scale */
H1: 2.5rem (desktop), 2rem (mobile) - Oswald Bold (700)
H2: 2rem (desktop), 1.75rem (mobile) - Oswald Bold (700)
H3: 1.5rem - Oswald Semi-bold (600)
Body: 1rem, line-height 1.7 - PT Serif Regular (400)
Buttons/Links: 1rem, font-weight 600 - Oswald Semi-bold

/* Line Height */
Headings: 1.2-1.3
Body Text: 1.7 (serif requires more spacing)
UI Elements: 1.5
```

**Partnership Page Usage:**
- **Hero Title**: Oswald Bold, 2.5rem (desktop)
- **Section Headings**: Oswald Bold, 2rem
- **Card Titles**: Oswald Semi-bold, 1.5rem
- **Body Text**: PT Serif Regular, 1rem with 1.7 line-height
- **Buttons**: Oswald Semi-bold, 1rem
- **Tier Labels**: Bebas Neue Regular (uppercase)

---

## 10. Files to Reference

When implementing this page, reference these existing project files:
- `sch_design_spec_v1_3.md` - Main design system (Art Deco)
- `sch_website_requirements.md` - Technical requirements
- Existing navigation component
- Existing footer component
- Existing button components
- Existing container/section patterns

---

## 11. Questions for Implementation

1. **Static vs. Data-Driven:** Should partnership tiers be hardcoded or pulled from data file?
2. **Metrics Updates:** How will podcast metrics be updated over time?
3. **Form Integration:** Should there be a contact form on this page, or is link to contact page sufficient?
4. **A/B Testing:** Any plans to test different CTAs or layouts?

---

## 12. Version History

**Version 1.1** (December 9, 2025)
- Updated color palette to Art Deco scheme
- Updated typography to Google Fonts (Oswald, PT Serif, Bebas Neue)
- Updated parent design system reference to v1.3
- All color and typography references updated throughout document
- Added detailed color usage documentation for partnership page

**Version 1.0** (November 8, 2025)
- Initial specification
- Original color scheme and system fonts

---

**End of Specification**
