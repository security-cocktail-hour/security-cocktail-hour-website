# Security Cocktail Hour Website
## Design Specification v1.1

**Date:** November 6, 2025
**Status:** For Implementation
**Based On:** Requirements Document v1.0
**Updated:** Color palette updated to current production colors (October 8, 2025 palette)

---

## 1. Design Philosophy

### Core Principles

**Retro-Modern Fusion**
- Draw from the logo's vintage badge aesthetic
- Apply modern web design principles for usability
- Balance nostalgia with contemporary functionality

**Professional but Approachable**
- Convey cybersecurity expertise without intimidation
- Welcome both technical and non-technical audiences
- Maintain professionalism while being engaging

**Content-First Design**
- Prioritize episode discovery and consumption
- Clear information hierarchy
- Minimal friction to podcast platforms

**Performance-Oriented**
- Clean, efficient design that loads fast
- Mobile-first responsive approach
- Progressive enhancement

---

## 2. Visual Design System

### 2.1 Color Palette

**Updated: October 8, 2025**

**Primary Colors**

```
Primary (Dark Blue)
- Hex: #192A56
- RGB: 25, 42, 86
- Use: Main text, primary navigation, footers, dark backgrounds
- Accessibility: Very readable on light backgrounds (AAA compliant with white)

Secondary (Cool Grey)
- Hex: #8D99AE
- RGB: 141, 153, 174
- Use: Secondary text, borders, dividers, subtle backgrounds, category tags
- Accessibility: Subtle, professional

Base/Background (Off-white)
- Hex: #F8F9FA
- RGB: 248, 249, 250
- Use: Main page background
- Accessibility: Cleaner than pure white

Action/Button (Professional Blue)
- Hex: #436098
- RGB: 67, 96, 152
- Use: Most buttons, CTAs, gradients, interactive elements
- Accessibility: Distinct and professional (AA compliant with white text)

Accent/Highlight (Bright Red)
- Hex: #CE1F2C
- RGB: 206, 31, 44
- Use: "Listen Now" button only, key highlights (used sparingly for emphasis)
- Accessibility: Use with white text (AA compliant)
```

**CSS Variable Mapping**

```css
--color-primary: #192A56           /* Dark Blue */
--color-secondary: #8D99AE         /* Cool Grey */
--color-background: #F8F9FA        /* Off-white */
--color-action: #436098            /* Professional Blue */
--color-accent: #CE1F2C            /* Bright Red */
```

**Gradient Options**

```
Professional Blue Gradient (for cards, hero sections)
- Linear gradient: Action Blue (#436098) → Lighter variant (#6A8CC7)
- Use: Headers, hero sections, featured content cards, missing image placeholders

Subtle Background
- Linear gradient: White → Base/Background (#F8F9FA)
- Use: Page backgrounds, subtle depth
```

### 2.2 Typography

**Font Strategy**
Use system font stack for performance and reliability:

**Headings Font Stack**
```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", 
             Roboto, "Helvetica Neue", Arial, sans-serif;
font-weight: 700 (Bold) for H1-H2
font-weight: 600 (Semi-bold) for H3-H6
```

**Body Font Stack**
```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", 
             Roboto, "Helvetica Neue", Arial, sans-serif;
font-weight: 400 (Regular) for body
font-weight: 500 (Medium) for emphasis
```

**Typography Scale**

```
H1 (Page Titles)
- Size: 2.5rem (40px) desktop, 2rem (32px) mobile
- Weight: 700
- Line Height: 1.2
- Color: Primary (#192A56) or Accent (#CE1F2C)
- Usage: Page headlines, hero titles

H2 (Section Headings)
- Size: 2rem (32px) desktop, 1.75rem (28px) mobile
- Weight: 700
- Line Height: 1.3
- Color: Primary (#192A56)
- Usage: Major sections

H3 (Subsection Headings)
- Size: 1.5rem (24px) desktop, 1.375rem (22px) mobile
- Weight: 600
- Line Height: 1.4
- Color: Primary (#192A56)
- Usage: Episode titles, card headings

H4 (Minor Headings)
- Size: 1.25rem (20px)
- Weight: 600
- Line Height: 1.4
- Color: Primary (#192A56)
- Usage: Sidebar headings, metadata labels

Body Text
- Size: 1rem (16px)
- Weight: 400
- Line Height: 1.6
- Color: Primary (#192A56)
- Max width: 70ch for readability

Small Text
- Size: 0.875rem (14px)
- Weight: 400
- Line Height: 1.5
- Color: Primary (#192A56) or Secondary (#8D99AE) at 70% opacity
- Usage: Metadata, captions, footnotes
```

### 2.3 Spacing System

**Base Unit: 8px**

```
xs: 4px   (0.25rem)  - Tight spacing
sm: 8px   (0.5rem)   - Compact elements
md: 16px  (1rem)     - Default spacing
lg: 24px  (1.5rem)   - Section spacing
xl: 32px  (2rem)     - Major sections
2xl: 48px (3rem)     - Page sections
3xl: 64px (4rem)     - Hero sections
```

**Application:**
- Padding: Use multiples of 8px
- Margins: Use multiples of 8px
- Grid gaps: 16px (mobile), 24px (tablet), 32px (desktop)

### 2.4 Border Radius

```
sm: 4px   - Small elements (tags, badges)
md: 8px   - Cards, buttons, inputs
lg: 12px  - Large cards, modals
full: 50% - Circular elements (avatars)
```

### 2.5 Shadows

```
Light (cards, hover states):
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);

Medium (elevated cards, dropdowns):
box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);

Strong (modals, prominent elements):
box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
```

---

## 3. Component Design

### 3.1 Buttons

**Primary Button (Main CTAs)**
```
Background: Action Blue (#436098)
Text: White
Padding: 12px 24px
Border Radius: 8px
Font Weight: 600
Font Size: 1rem (16px)

Hover State:
- Background: Darken 10% (#3A5282)
- Box Shadow: 0 4px 12px rgba(67, 96, 152, 0.3)
- Transform: translateY(-2px)
- Transition: all 0.2s ease

Active State:
- Transform: translateY(0)
- Box Shadow: 0 2px 8px rgba(67, 96, 152, 0.3)

Examples: "Subscribe", "Join Newsletter", "View All Episodes"
```

**Accent Button ("Listen Now" only)**
```
Background: Accent Red (#CE1F2C)
Text: White
Padding: 12px 24px
Border Radius: 8px
Font Weight: 600
Font Size: 1rem (16px)

Hover State:
- Background: Darken 10% (#B41A26)
- Box Shadow: 0 4px 12px rgba(206, 31, 44, 0.3)
- Transform: translateY(-2px)
- Transition: all 0.2s ease

Active State:
- Transform: translateY(0)
- Box Shadow: 0 2px 8px rgba(206, 31, 44, 0.3)

Examples: "Listen Now" (header button only - used sparingly)
```

**Secondary Button (Alternative Actions)**
```
Background: Transparent
Border: 2px solid Action Blue (#436098)
Text: Action Blue (#436098)
Padding: 10px 24px (adjusted for border)
Border Radius: 8px
Font Weight: 600
Font Size: 1rem (16px)

Hover State:
- Background: Action Blue (#436098)
- Text: White
- Transition: all 0.2s ease

Examples: "Learn More", "Browse Resources"
```

**Tertiary Button (Subtle Actions)**
```
Background: Transparent
Text: Action Blue (#436098)
Font Weight: 600
Font Size: 1rem (16px)

Hover State:
- Text: Primary (#192A56)
- Text Decoration: underline
- Transition: all 0.2s ease

Examples: "Read More", "See Details"
```

### 3.2 Cards

**Episode Card (Primary Content)**
```
Structure:
┌─────────────────────────────────────┐
│  [Episode Cover Image - 16:9]       │
│─────────────────────────────────────│
│  Category Tag                       │
│  H3: Episode Title                  │
│  Guest Name | Duration              │
│  Brief description (2 lines)        │
│  [Listen Now Button]                │
└─────────────────────────────────────┘

Style:
- Background: White
- Border: 1px solid #E5E5E5
- Border Radius: 8px
- Padding: 0 (image full bleed), 20px bottom content
- Box Shadow: Light (on hover: Medium)
- Hover: Lift effect (translateY(-4px))
- Transition: all 0.3s ease

Cover Image:
- Aspect Ratio: 16:9 or 1:1
- Object Fit: cover
- Border Radius: 8px 8px 0 0

Category Tag:
- Background: Secondary Grey (#8D99AE) (or other color by category)
- Text: White
- Padding: 4px 12px
- Border Radius: 4px
- Font Size: 0.75rem (12px)
- Font Weight: 600
- Text Transform: uppercase
```

**Resource Card (Secondary Content)**
```
Structure:
┌─────────────────────────────────────┐
│  Icon | Resource Type               │
│  H4: Resource Title                 │
│  Brief description (1-2 lines)      │
│  [Link/CTA]                         │
└─────────────────────────────────────┘

Style:
- Background: Light Gray (#F5F5F5)
- Border: None or subtle
- Border Radius: 8px
- Padding: 20px
- Hover: Background lightens, slight lift
```

### 3.3 Forms

**Input Fields**
```
Style:
- Border: 1px solid #D0D0D0
- Border Radius: 4px
- Padding: 12px 16px
- Font Size: 1rem (16px)
- Background: White

Focus State:
- Border: 2px solid Action Blue (#436098)
- Box Shadow: 0 0 0 3px rgba(67, 96, 152, 0.1)
- Outline: none

Error State:
- Border: 2px solid Accent Red (#CE1F2C)
- Box Shadow: 0 0 0 3px rgba(206, 31, 44, 0.1)

Labels:
- Font Size: 0.875rem (14px)
- Font Weight: 600
- Color: Primary (#192A56)
- Margin Bottom: 8px
```

**Email Signup Form**
```
Layout Options:

Inline (for header/footer):
[Email Input Field] [Subscribe Button]

Stacked (for modals/dedicated sections):
[Email Input Field]
[Subscribe Button (full width)]

Style:
- Group elements visually
- Clear label or placeholder
- Privacy note (small text below)
- Success/error messages clearly visible
```

### 3.4 Navigation

**Desktop Navigation**
```
Structure:
[Logo] [Episodes] [About] [Resources] [Contact] [Listen Now Button]

Style:
- Background: White or slight gradient
- Height: 80px
- Sticky on scroll
- Logo: 60px height
- Navigation Links:
  - Font Size: 1rem (16px)
  - Font Weight: 500
  - Color: Primary (#192A56)
  - Hover: Accent Red (#CE1F2C)
  - Active: Accent Red (#CE1F2C) with underline
- Listen Now Button: Accent button style (red)
```

**Mobile Navigation**
```
Structure:
[Logo] [Hamburger Menu Icon]

Expanded State:
- Full screen overlay
- Close button (X) top right
- Large, tappable links
- Social icons at bottom

Style:
- Background: Primary Blue (#192A56)
- Links: White text
- Font Size: 1.25rem (20px)
- Padding: 16px between links
```

### 3.5 Footer

```
Structure (Desktop):
┌─────────────────────────────────────────────────────┐
│  [Logo]          [Episodes]      [Social]           │
│                  - Recent        - LinkedIn         │
│  Tagline         - Popular       - Twitter          │
│                  - All           - YouTube          │
│                                                      │
│  [About]         [Resources]     [Newsletter]       │
│  - Hosts         - Tools         [Email Signup]     │
│  - Mission       - Guides                           │
│  - Contact       - Organizations                    │
│                                                      │
│  ───────────────────────────────────────────────    │
│  © 2025 Security Cocktail Hour  [Privacy] [Terms]  │
└─────────────────────────────────────────────────────┘

Style:
- Background: Primary Blue (#192A56)
- Text: White (80% opacity for links)
- Padding: 48px 0
- Link Hover: Full white opacity
- Divider: White (20% opacity)
```

---

## 4. Page Layouts

### 4.1 Homepage Layout

```
┌─────────────────────────────────────────────────────┐
│  [NAVIGATION BAR - Sticky]                          │
├─────────────────────────────────────────────────────┤
│                                                      │
│  HERO SECTION (with spotlight gradient background)  │
│  ┌───────────────────────────────────────────────┐  │
│  │  [Logo - Large]                               │  │
│  │  H1: Podcast Tagline/Value Proposition        │  │
│  │  Subtitle: Brief description                  │  │
│  │  [Listen Now Button] [Subscribe Button]       │  │
│  │                                                │  │
│  │  Platform Icons: [YouTube] [Spotify] [Apple]  │  │
│  └───────────────────────────────────────────────┘  │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  LATEST EPISODE SECTION                             │
│  H2: Latest Episode                                 │
│  ┌───────────────────────────────────────────────┐  │
│  │  [Featured Episode Card - Larger than others] │  │
│  │  - Cover image                                │  │
│  │  - Title, guest, description                  │  │
│  │  - [Listen Now] [Show Notes]                  │  │
│  └───────────────────────────────────────────────┘  │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  RECENT EPISODES GRID                               │
│  H2: Recent Episodes                                │
│  ┌────────┐  ┌────────┐  ┌────────┐               │
│  │Episode │  │Episode │  │Episode │               │
│  │ Card   │  │ Card   │  │ Card   │               │
│  └────────┘  └────────┘  └────────┘               │
│                                                      │
│  [View All Episodes Button]                         │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ABOUT/VALUE SECTION (2-column on desktop)          │
│  ┌─────────────────────┐  ┌────────────────────┐   │
│  │ H2: About the Show  │  │ [Host Photos]      │   │
│  │ Description         │  │ Joe Patti          │   │
│  │ What listeners get  │  │ Adam Roth          │   │
│  │ [Learn More]        │  │ Brief credentials  │   │
│  └─────────────────────┘  └────────────────────┘   │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  EMAIL SIGNUP CTA (Full width, colored background)  │
│  H2: Join Our Newsletter                            │
│  Value proposition bullet points                    │
│  [Email Signup Form]                                │
│                                                      │
├─────────────────────────────────────────────────────┤
│  [FOOTER]                                           │
└─────────────────────────────────────────────────────┘

Mobile Adaptation:
- Stack all sections vertically
- Hero: Reduce logo size, stack buttons
- Episode grid: Single column or 2-column
- About section: Stack images above text
```

### 4.2 Episode Library Layout

```
┌─────────────────────────────────────────────────────┐
│  [NAVIGATION BAR]                                   │
├─────────────────────────────────────────────────────┤
│                                                      │
│  HEADER SECTION                                     │
│  H1: All Episodes                                   │
│  Subtitle: Browse our complete archive              │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  FILTERS & SEARCH BAR (Horizontal layout)           │
│  ┌──────────────────────────────────────────────┐   │
│  │ [Search: 🔍 Search episodes...]              │   │
│  └──────────────────────────────────────────────┘   │
│  [All Topics ▼] [Sort: Newest ▼] [View: Grid ⊞]    │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  EPISODES GRID (3-column desktop, 2-col tablet)     │
│  ┌────────┐  ┌────────┐  ┌────────┐               │
│  │Episode │  │Episode │  │Episode │               │
│  │ Card   │  │ Card   │  │ Card   │               │
│  └────────┘  └────────┘  └────────┘               │
│  ┌────────┐  ┌────────┐  ┌────────┐               │
│  │Episode │  │Episode │  │Episode │               │
│  │ Card   │  │ Card   │  │ Card   │               │
│  └────────┘  └────────┘  └────────┘               │
│                                                      │
│  [Load More] or [Pagination: 1 2 3 ... 10]         │
│                                                      │
├─────────────────────────────────────────────────────┤
│  [FOOTER]                                           │
└─────────────────────────────────────────────────────┘

Alternative List View:
┌────────────────────────────────────────────────────┐
│ [Cover] Episode Title - Guest Name                 │
│         Category | Duration | Date                 │
│         Brief description...                       │
│         [Listen Now]                               │
├────────────────────────────────────────────────────┤
│ [Cover] Episode Title - Guest Name                 │
│         ...                                        │
└────────────────────────────────────────────────────┘
```

### 4.3 Individual Episode Page Layout

```
┌─────────────────────────────────────────────────────┐
│  [NAVIGATION BAR]                                   │
├─────────────────────────────────────────────────────┤
│                                                      │
│  EPISODE HEADER (Full-width colored background)     │
│  ┌───────────────────────────────────────────────┐  │
│  │  Breadcrumb: Home > Episodes > [Episode]      │  │
│  │                                                │  │
│  │  [Category Tag]                               │  │
│  │  H1: Episode Title                            │  │
│  │  Guest Name | Date | Duration                 │  │
│  │                                                │  │
│  │  [Listen on YouTube] [Spotify] [Apple]        │  │
│  └───────────────────────────────────────────────┘  │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  MAIN CONTENT (2-column on desktop)                 │
│  ┌──────────────────────────┐  ┌──────────────────┐│
│  │ EPISODE CONTENT          │  │ SIDEBAR          ││
│  │                          │  │                  ││
│  │ [Episode Cover Image]    │  │ GUEST BIO CARD   ││
│  │                          │  │ [Photo]          ││
│  │ DESCRIPTION              │  │ Name             ││
│  │ Full episode description │  │ Title/Org        ││
│  │ with keywords            │  │ Brief bio        ││
│  │                          │  │ [Links]          ││
│  │ CHAPTER MARKERS          │  │                  ││
│  │ 00:00 - Introduction     │  │ EMAIL SIGNUP     ││
│  │ 06:00 - Technical Deep   │  │ [Form]           ││
│  │ 26:00 - Business Context │  │                  ││
│  │ 36:00 - Applications     │  │ SHARE            ││
│  │                          │  │ [Social Icons]   ││
│  │ RESOURCES MENTIONED      │  │                  ││
│  │ • Link to resource 1     │  │ RELATED EPISODES ││
│  │ • Link to resource 2     │  │ [Episode Card]   ││
│  │                          │  │ [Episode Card]   ││
│  │ FULL TRANSCRIPT          │  │ [Episode Card]   ││
│  │ (Expandable/collapsible) │  │                  ││
│  │                          │  │                  ││
│  └──────────────────────────┘  └──────────────────┘│
│                                                      │
├─────────────────────────────────────────────────────┤
│  [FOOTER]                                           │
└─────────────────────────────────────────────────────┘

Mobile Adaptation:
- Stack sidebar below main content
- Guest bio card first
- Then email signup
- Then related episodes
```

### 4.4 About Page Layout

```
┌─────────────────────────────────────────────────────┐
│  [NAVIGATION BAR]                                   │
├─────────────────────────────────────────────────────┤
│                                                      │
│  HERO SECTION (Centered)                            │
│  [Large Logo]                                       │
│  H1: About Security Cocktail Hour                   │
│  Tagline/Mission Statement                          │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  PODCAST STORY SECTION                              │
│  H2: Our Story                                      │
│  2-3 paragraphs about the podcast                   │
│  - How it started                                   │
│  - What makes it unique                             │
│  - Who it's for                                     │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  HOSTS SECTION (2-column on desktop)                │
│  H2: Meet Your Hosts                                │
│                                                      │
│  ┌────────────────────┐  ┌────────────────────┐    │
│  │ [Joe's Photo]      │  │ [Adam's Photo]     │    │
│  │ H3: Joe Patti      │  │ H3: Adam Roth      │    │
│  │ Title/Role         │  │ Title/Role         │    │
│  │ Biography (3-4     │  │ Biography (3-4     │    │
│  │ paragraphs)        │  │ paragraphs)        │    │
│  │ - Credentials      │  │ - Credentials      │    │
│  │ - Experience       │  │ - Experience       │    │
│  │ - Expertise areas  │  │ - Expertise areas  │    │
│  │ [LinkedIn] [Other] │  │ [LinkedIn] [Other] │    │
│  └────────────────────┘  └────────────────────┘    │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  WHAT YOU'LL GET SECTION                            │
│  H2: What You'll Get From This Podcast              │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │ [Icon]      │ │ [Icon]      │ │ [Icon]      │   │
│  │ Benefit 1   │ │ Benefit 2   │ │ Benefit 3   │   │
│  │ Description │ │ Description │ │ Description │   │
│  └─────────────┘ └─────────────┘ └─────────────┘   │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  STATS/ACHIEVEMENTS (Optional)                      │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐         │
│  │ [Number]  │ │ [Number]  │ │ [Number]  │         │
│  │ Episodes  │ │ Guests    │ │ Topics    │         │
│  └───────────┘ └───────────┘ └───────────┘         │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  EMAIL SIGNUP CTA                                   │
│  H2: Stay Connected                                 │
│  [Email Signup Form]                                │
│                                                      │
├─────────────────────────────────────────────────────┤
│  [FOOTER]                                           │
└─────────────────────────────────────────────────────┘
```

---

## 5. Responsive Design Guidelines

### 5.1 Breakpoints

```
Mobile (Portrait):        0px - 599px
Mobile (Landscape):       600px - 899px
Tablet (Portrait):        900px - 1199px
Desktop:                  1200px - 1535px
Large Desktop:            1536px+

Primary breakpoints to use:
- 600px  (mobile → tablet)
- 900px  (tablet → desktop)
- 1200px (desktop → large)
```

### 5.2 Layout Adaptations

**Grid Systems:**
```
Mobile:      1 column (full width with padding)
Tablet:      2 columns (for cards)
Desktop:     3-4 columns (for cards)
Large:       Up to 4 columns max

Container Max Width:
- Mobile: 100% (with 16px side padding)
- Tablet: 100% (with 24px side padding)
- Desktop: 1200px (centered)
- Large: 1400px (centered)
```

**Typography Scaling:**
```
Mobile:
- H1: 2rem (32px)
- H2: 1.75rem (28px)
- H3: 1.375rem (22px)
- Body: 1rem (16px)

Desktop:
- H1: 2.5rem (40px)
- H2: 2rem (32px)
- H3: 1.5rem (24px)
- Body: 1rem (16px)
```

**Touch Targets (Mobile):**
```
Minimum: 44px x 44px (iOS guideline)
Recommended: 48px x 48px (Material Design)

Apply to:
- Buttons
- Links in navigation
- Form inputs
- Interactive icons
```

### 5.3 Mobile-First Approach

**Start with mobile design, then enhance for larger screens:**

1. **Mobile:** Single column, stacked content
2. **Tablet:** 2-column grids, side-by-side content
3. **Desktop:** 3-4 column grids, more white space
4. **Large:** Maintain max-width, more generous spacing

**Progressive Enhancement:**
- Core functionality works on all devices
- Enhanced interactions on desktop (hover states)
- Optimized images based on screen size
- Conditional loading of non-essential features

---

## 6. Interaction Design

### 6.1 Micro-interactions

**Button Hover/Click:**
```
Hover:
- Transform: translateY(-2px)
- Box Shadow: Elevated
- Transition: 0.2s ease

Active (Click):
- Transform: translateY(0)
- Box Shadow: Reduced
- Transition: 0.1s ease

Focus (Keyboard):
- Outline: 2px solid Action Blue (#436098)
- Outline Offset: 2px
```

**Card Hover:**
```
Hover:
- Transform: translateY(-4px)
- Box Shadow: Medium → Strong
- Transition: 0.3s ease
```

**Link Hover:**
```
Default: Color + underline on hover
Header Navigation: Color change only
Footer: Opacity increase
```

### 6.2 Loading States

**Skeleton Screens:**
```
Use for:
- Episode cards while loading
- Content placeholders

Style:
- Light gray background
- Subtle pulse animation
- Match shape of final content
```

**Spinners:**
```
Use for:
- Form submissions
- Search queries
- Page transitions

Style:
- Circular spinner
- Action Blue (#436098) color
- Centered in container
```

### 6.3 Empty States

**No Search Results:**
```
- Icon (search with X)
- Heading: "No episodes found"
- Suggestion: Try different keywords
- Link to all episodes
```

**No Content:**
```
- Relevant icon
- Heading: Explain why empty
- Action: What user can do
```

### 6.4 Error States

**Form Errors:**
```
- Red border on input
- Error message below field (red text)
- Icon indicating error
- Clear, actionable message
```

**Page Errors (404, etc.):**
```
- Large, friendly heading
- Explanation of what happened
- Link back to homepage
- Search functionality
- Recent episodes as fallback
```

---

## 7. Accessibility Requirements

### 7.1 Color Contrast

**WCAG 2.1 AA Compliance:**
```
Normal Text (< 18px):
- Contrast ratio: 4.5:1 minimum
- Example: Primary (#192A56) on White (12.6:1) ✓

Large Text (≥ 18px or bold ≥ 14px):
- Contrast ratio: 3:1 minimum

UI Components:
- Contrast ratio: 3:1 minimum for interactive elements
```

**Testing:**
- Test all color combinations
- Verify with contrast checker tools
- Test with color blindness simulators

### 7.2 Keyboard Navigation

**Requirements:**
- All interactive elements keyboard accessible
- Logical tab order (top to bottom, left to right)
- Visible focus indicators (outline, highlight)
- Skip navigation links for main content
- Escape key closes modals/menus

**Focus Indicators:**
```
Style:
- Outline: 2px solid Action Blue (#436098)
- Outline Offset: 2px
- Border Radius: matches element
```

### 7.3 Screen Reader Support

**Semantic HTML:**
- Use proper heading hierarchy (H1 → H2 → H3)
- Use `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>`
- Use `<button>` for buttons, `<a>` for links
- Use `<label>` for form inputs

**ARIA Labels:**
- Add `aria-label` for icon-only buttons
- Use `aria-describedby` for form hints
- Use `aria-live` for dynamic content updates
- Add `alt` text for all images

**Example:**
```html
<button aria-label="Close menu">
  <svg>...</svg>
</button>

<img src="episode-cover.jpg" 
     alt="Episode 42: Security Automation with Jane Doe">
```

### 7.4 Content Accessibility

**Text:**
- Minimum font size: 16px body text
- Maximum line length: 70 characters
- Line height: 1.5-1.6 for body text
- No text in images (use HTML text)

**Media:**
- Transcripts for all episodes
- Captions for video content (when applicable)
- Audio descriptions (if relevant)

**Forms:**
- Clear labels for all inputs
- Error messages associated with fields
- Required field indicators
- Instructions before form, not just in placeholders

---

## 8. Performance Guidelines

### 8.1 Image Optimization

**Format Strategy:**
```
Photos/Complex Images:
- WebP (primary) with JPEG fallback
- Compress: 80-85% quality

Simple Graphics/Logos:
- SVG (preferred for scalability)
- PNG with transparency if needed

Icons:
- SVG sprites or inline SVG
- Font icons as fallback
```

**Responsive Images:**
```html
<picture>
  <source 
    srcset="episode-cover-800w.webp 800w,
            episode-cover-400w.webp 400w"
    type="image/webp">
  <source 
    srcset="episode-cover-800w.jpg 800w,
            episode-cover-400w.jpg 400w"
    type="image/jpeg">
  <img src="episode-cover-800w.jpg" 
       alt="Episode description"
       loading="lazy">
</picture>
```

**Guidelines:**
- Max file size: 200KB for hero images, 100KB for cards
- Use `loading="lazy"` for below-fold images
- Provide `width` and `height` attributes to prevent layout shift
- Generate multiple sizes for different viewports

### 8.2 Loading Strategy

**Critical CSS:**
- Inline critical CSS in `<head>`
- Defer non-critical CSS
- Use CSS containment where applicable

**JavaScript:**
- Defer non-critical scripts
- Use async for analytics
- Minimize third-party scripts
- Bundle and minify

**Fonts:**
- Use system fonts (no web font loading delay)
- If custom fonts needed: Use `font-display: swap`

**Third-Party Embeds:**
- Lazy load social media embeds
- Use facades for video embeds (load on click)
- Minimize tracking scripts

### 8.3 Performance Budgets

**Targets:**
```
Page Load Time (3G):
- First Contentful Paint: < 2s
- Largest Contentful Paint: < 3s
- Time to Interactive: < 4s

Total Page Weight:
- HTML: < 50KB (gzipped)
- CSS: < 50KB (gzipped)
- JavaScript: < 100KB (gzipped)
- Images: < 500KB (optimized, lazy loaded)
- Total: < 1MB

Lighthouse Scores:
- Performance: 90+
- Accessibility: 100
- Best Practices: 95+
- SEO: 100
```

---

## 9. SEO Implementation

### 9.1 Schema Markup

**Podcast Schema (Organization/Website level):**
```json
{
  "@context": "https://schema.org",
  "@type": "PodcastSeries",
  "name": "Security Cocktail Hour",
  "url": "https://securitycocktailhour.com",
  "description": "Your episode listing tagline",
  "author": {
    "@type": "Organization",
    "name": "Security Cocktail Hour",
    "url": "https://securitycocktailhour.com"
  },
  "image": "https://securitycocktailhour.com/logo.jpg"
}
```

**Episode Schema (Individual episode pages):**
```json
{
  "@context": "https://schema.org",
  "@type": "PodcastEpisode",
  "url": "https://securitycocktailhour.com/episodes/[episode-slug]",
  "name": "Episode Title",
  "datePublished": "2025-10-03",
  "timeRequired": "PT45M",
  "description": "Episode description",
  "associatedMedia": {
    "@type": "MediaObject",
    "contentUrl": "[audio file URL]"
  },
  "partOfSeries": {
    "@type": "PodcastSeries",
    "name": "Security Cocktail Hour",
    "url": "https://securitycocktailhour.com"
  }
}
```

### 9.2 Meta Tags Template

**Homepage:**
```html
<title>Security Cocktail Hour | Cybersecurity Podcast</title>
<meta name="description" content="[150-160 char description with keywords]">

<!-- Open Graph -->
<meta property="og:title" content="Security Cocktail Hour">
<meta property="og:description" content="[Same as meta description]">
<meta property="og:image" content="[social-share-image.jpg]">
<meta property="og:url" content="https://securitycocktailhour.com">
<meta property="og:type" content="website">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Security Cocktail Hour">
<meta name="twitter:description" content="[Same as meta description]">
<meta name="twitter:image" content="[social-share-image.jpg]">
```

**Episode Page:**
```html
<title>[Episode Title] | Security Cocktail Hour</title>
<meta name="description" content="[Episode description with keywords]">

<!-- Open Graph -->
<meta property="og:title" content="[Episode Title]">
<meta property="og:description" content="[Episode description]">
<meta property="og:image" content="[episode-cover.jpg]">
<meta property="og:url" content="[episode-url]">
<meta property="og:type" content="article">
<meta property="article:published_time" content="[ISO date]">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Episode Title]">
<meta name="twitter:description" content="[Episode description]">
<meta name="twitter:image" content="[episode-cover.jpg]">
```

### 9.3 URL Structure

```
Homepage:           /
Episodes:           /episodes/
Episode Detail:     /episodes/[slug]/
About:              /about/
Resources:          /resources/
Resource Detail:    /resources/[slug]/
Contact:            /contact/
Blog:               /blog/
Blog Post:          /blog/[slug]/

SEO-Friendly Slug Format:
- Use keywords from title
- Lowercase, hyphen-separated
- Remove stop words (a, an, the, etc.)
- Keep reasonably short

Example:
Title: "Dr. Nikki Robinson: Why Security Teams Fail at Human Factors"
Slug: /episodes/dr-nikki-robinson-security-teams-human-factors/
```

---

## 10. Content Guidelines

### 10.1 Episode Show Notes Template

**Structure:**
```markdown
# [Episode Number]: [Episode Title]

**Guest:** [Guest Name], [Title] at [Organization]
**Published:** [Date]
**Duration:** [MM:SS]
**Category:** [Primary Category]

## Episode Description
[2-3 paragraphs with target keywords in first 100 words]
- What the episode covers
- Why it matters to listeners
- Key takeaways

## In This Episode
- Timestamp - Topic/section 1
- Timestamp - Topic/section 2
- Timestamp - Topic/section 3
- Timestamp - Topic/section 4

## Guest Bio
[2-3 paragraphs about guest]
- Background and credentials
- Current role
- Areas of expertise

**Connect with [Guest Name]:**
- LinkedIn: [URL]
- Twitter: [URL]
- Website: [URL]

## Resources Mentioned
- [Resource 1 name and link]
- [Resource 2 name and link]
- [Resource 3 name and link]

## Listen Now
[Buttons/links to YouTube, Spotify, Apple Podcasts]

## Related Episodes
- [Episode title and link]
- [Episode title and link]
- [Episode title and link]

## Full Transcript
[Expandable/collapsible section with full episode transcript]
```

### 10.2 Image Requirements

**Episode Cover Images:**
- Dimensions: 3000x3000px (1:1 ratio) or 1920x1080px (16:9)
- Format: JPEG (80% quality) and WebP
- File size: < 100KB for web use
- Include episode number and title if visible
- Consistent branding/template

**Hero/Banner Images:**
- Dimensions: 1920x600px minimum
- Format: WebP with JPEG fallback
- File size: < 200KB
- Relevant to content

**Social Share Images:**
- Dimensions: 1200x630px (Facebook/LinkedIn)
- Dimensions: 1200x600px (Twitter)
- Include logo, episode title, guest name
- High contrast, readable text

### 10.3 Writing Style

**General Guidelines:**
- Professional but conversational tone
- Active voice preferred
- Short paragraphs (2-4 sentences)
- Use bullet points for scanability
- Bold key terms and takeaways
- Clear headings and subheadings

**SEO Writing:**
- Target keyword in first 100 words
- Use keyword variations naturally
- Include related keywords
- Write for humans first, search engines second
- Aim for 800-1200 words for episode pages

**Calls-to-Action:**
- Be specific and action-oriented
- Create urgency when appropriate
- Use contrasting buttons
- One primary CTA per section

---

## 11. Brand Voice & Messaging

### 11.1 Brand Voice

**Characteristics:**
- **Expert but Accessible:** Knowledgeable without jargon overload
- **Curious:** Always learning, exploring new areas
- **Inclusive:** Welcoming to all skill levels
- **Conversational:** Like talking with a colleague over drinks
- **Professional:** Credible and trustworthy

**What We Are:**
- Knowledgeable guides
- Curious explorers
- Friendly colleagues
- Industry insiders

**What We're Not:**
- Overly academic or theoretical
- Exclusive or elitist
- Too casual or unprofessional
- Dry or boring

### 11.2 Key Messages

**Primary Message:**
"Expanding cybersecurity knowledge beyond your specialty, one conversation at a time."

**Supporting Messages:**
- "Covering underserved areas of cybersecurity"
- "Learning from practitioners, not just theory"
- "Making security accessible to all"
- "Your career development companion"

**Value Propositions:**
- Discover security topics outside your specialty
- Learn from real-world practitioners
- Career insights and development guidance
- Accessible to technical and non-technical professionals

### 11.3 Content Tone Examples

**Homepage Hero:**
"Explore the breadth of cybersecurity with Security Cocktail Hour—where practitioners share their journeys, insights, and lessons learned beyond the headlines."

**Episode Description Opening:**
"In this episode, we dive into [topic] with [Guest Name], who brings [X] years of experience in [specialty]. We discuss [key topics] and explore practical approaches to [challenge]."

**Email Newsletter:**
"Hey there, security professionals! This week we're featuring an insightful conversation with [Guest] about [topic]. Here's what you'll learn..."

**About Page:**
"Security Cocktail Hour was born from a simple observation: cybersecurity is vast, but most professionals work in specialized corners of the field. We created this podcast to bridge those silos..."

---

## 12. Implementation Priorities

### Phase 1: MVP Launch (Days 1-14)

**Must Have:**
- Homepage with hero, latest episode, recent episodes
- Episode library with search and filter
- Individual episode pages with show notes
- About page with host bios
- Contact page with form
- Resources page (basic)
- Email signup forms (Mailchimp integrated)
- Navigation and footer
- Mobile responsive
- Basic SEO (meta tags, schema markup)
- Google Analytics

**Can Defer:**
- Blog/articles section
- Advanced search features
- User accounts
- Comments system
- Newsletter archive
- Advanced animations

### Phase 2: Enhancement (Post-Launch, Weeks 2-4)

**Add:**
- Blog functionality
- Enhanced episode search
- More resources and organization
- Social media feeds
- Video embeds
- Performance optimizations
- Additional SEO enhancements

### Phase 3: Growth Features (Months 2-3)

**Consider:**
- Personalized recommendations
- User accounts and saved episodes
- Community features
- Advanced analytics dashboard
- A/B testing implementation
- Premium content areas (if pursuing)

---

## 13. Design Deliverables Checklist

**Before Development:**
- [ ] Design system documented (colors, typography, spacing)
- [ ] Component library defined (buttons, cards, forms)
- [ ] Page layouts specified (all core pages)
- [ ] Responsive breakpoints defined
- [ ] Accessibility requirements documented
- [ ] Performance guidelines established

**During Development:**
- [ ] Visual design matches specifications
- [ ] Components reusable and consistent
- [ ] Responsive design tested on multiple devices
- [ ] Accessibility standards met (WCAG AA)
- [ ] Performance budgets maintained
- [ ] Browser compatibility verified

**After Development:**
- [ ] Style guide documentation for future reference
- [ ] Component library maintained
- [ ] Design patterns documented
- [ ] Brand guidelines updated if needed

---

## 14. Testing Checklist

### Visual Testing
- [ ] All pages render correctly on mobile, tablet, desktop
- [ ] Colors match design system
- [ ] Typography scales appropriately
- [ ] Images load and display correctly
- [ ] Spacing and alignment consistent
- [ ] Hover states work on desktop
- [ ] Touch targets appropriate size on mobile

### Functional Testing
- [ ] Navigation works on all devices
- [ ] Search functionality works
- [ ] Forms submit successfully
- [ ] Email signup integration works
- [ ] All internal links work
- [ ] All external links open correctly
- [ ] Contact form delivers messages

### Performance Testing
- [ ] Page load time < 3 seconds on 3G
- [ ] Lighthouse performance score 90+
- [ ] Images optimized and lazy loading
- [ ] No render-blocking resources
- [ ] Fonts load efficiently

### Accessibility Testing
- [ ] Keyboard navigation works
- [ ] Screen reader testing completed
- [ ] Color contrast ratios meet AA standards
- [ ] Focus indicators visible
- [ ] ARIA labels appropriate
- [ ] Alt text on all images
- [ ] Form labels and errors accessible

### Browser Testing
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)
- [ ] iOS Safari
- [ ] Chrome Mobile

### SEO Testing
- [ ] Meta tags on all pages
- [ ] Schema markup implemented
- [ ] XML sitemap generated
- [ ] Robots.txt configured
- [ ] URLs are SEO-friendly
- [ ] Redirects from old site work
- [ ] Google Search Console configured
- [ ] Google Analytics tracking

---

**Design Specification Complete**
*Ready for implementation with Claude Code*