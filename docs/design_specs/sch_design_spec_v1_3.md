# Security Cocktail Hour Website
## Design Specification v1.3

**Date:** December 9, 2025
**Status:** Implemented & Deployed
**Based On:** Requirements Document v1.0
**Previous Version:** v1.2 (November 8, 2025)

**Updated:**
- Art Deco design system implemented (December 2025) - complete visual redesign
- Typography updated to Google Fonts: Oswald, PT Serif, Bebas Neue (December 2025)
- Color palette updated to Art Deco scheme: Red, Navy, Teal, Cream (December 2025)
- Homepage hero section redesigned with art deco patterns and ornaments (December 2025)
- Episode page fixes: newsletter box, episode cards, cache-busting (December 8, 2025)
- Gradient options expanded to include all production gradients (November 8, 2025)
- Collapsible transcript accordion and manual related episodes implemented (December 2, 2025)

---

## 1. Design Philosophy

### Core Principles

**Art Deco Modern Fusion**
- Premium vintage aesthetic inspired by 1920s-1940s art deco movement
- Geometric patterns, bold typography, and elegant ornamental details
- Modern web design principles for usability and performance
- Balance between sophisticated design and contemporary functionality

**Professional but Approachable**
- Convey cybersecurity expertise with confidence and style
- Welcome both technical and non-technical audiences
- Maintain professionalism while being engaging
- Premium feel without being intimidating

**Content-First Design**
- Prioritize episode discovery and consumption
- Clear information hierarchy
- Minimal friction to podcast platforms
- Visual design enhances rather than distracts from content

**Performance-Oriented**
- Clean, efficient design that loads fast
- Mobile-first responsive approach
- Progressive enhancement
- Optimized assets and minimal dependencies

---

## 2. Visual Design System

### 2.1 Color Palette

**Updated: December 9, 2025 - Art Deco Redesign**

The website uses a sophisticated Art Deco-inspired color palette that conveys premium quality, professionalism, and vintage elegance.

**Primary Colors**

```
Red (Art Deco Accent)
- Hex: #D74444
- RGB: 215, 68, 68
- Use: Primary CTAs, "Listen Now" buttons, important highlights, category badges
- Psychology: Energy, importance, action
- Accessibility: Use with white text (AAA compliant)
- CSS Variable: --red

Navy (Primary Dark)
- Hex: #2B4D7D
- RGB: 43, 77, 125
- Use: Header/footer backgrounds, primary text, headings, navigation
- Psychology: Trust, professionalism, authority
- Accessibility: Excellent contrast with light backgrounds (AAA compliant)
- CSS Variable: --navy

Teal (Accent/Interactive)
- Hex: #4A9B9B
- RGB: 74, 155, 155
- Use: Links, interactive elements, secondary accents, tag colors
- Psychology: Calm, modern, tech-forward
- Accessibility: Good contrast (AA compliant)
- CSS Variable: --teal

Cream (Base/Background)
- Hex: #F5F1E8
- RGB: 245, 241, 232
- Use: Main page background, card backgrounds, subtle contrast
- Psychology: Warmth, sophistication, vintage elegance
- Accessibility: Excellent base for dark text
- CSS Variable: --cream

White (Pure)
- Hex: #FFFFFF
- RGB: 255, 255, 255
- Use: Card backgrounds, text on dark backgrounds, high contrast elements
- Psychology: Cleanliness, clarity, space
- Accessibility: Maximum contrast
- CSS Variable: --white

Black (Deep Text)
- Hex: #1A1A1A
- RGB: 26, 26, 26
- Use: Body text (rarely - Navy preferred), maximum contrast situations
- Psychology: Authority, sophistication
- Accessibility: Maximum contrast (AAA+ compliant)
- CSS Variable: --black
```

**Extended Palette (Variations)**

```
Red Dark
- Hex: #A63333
- RGB: 166, 51, 51
- Use: Red hover states, darker red accents
- CSS Variable: --red-dark

Navy Light
- Hex: #3A5F99
- RGB: 58, 95, 153
- Use: Lighter navy accents, gradient endpoints
- CSS Variable: --navy-light

Navy Dark
- Hex: #1F3859
- RGB: 31, 56, 89
- Use: Darker navy accents, gradient starting points
- CSS Variable: --navy-dark

Teal Light
- Hex: #6BB8B8
- RGB: 107, 184, 184
- Use: Lighter teal accents, hover states
- CSS Variable: --teal-light

Silver
- Hex: #C0C0C0
- RGB: 192, 192, 192
- Use: Art deco ornamental details, subtle borders
- CSS Variable: --silver

Cream Dark
- Hex: #E8E0D0
- RGB: 232, 224, 208
- Use: Darker cream accents, subtle backgrounds
- CSS Variable: --cream-dark
```

**CSS Variable Mapping**

```css
:root {
  /* Art Deco Color Palette */
  --red: #D74444;
  --red-dark: #A63333;
  --navy: #2B4D7D;
  --navy-light: #3A5F99;
  --navy-dark: #1F3859;
  --teal: #4A9B9B;
  --teal-light: #6BB8B8;
  --silver: #C0C0C0;
  --cream: #F5F1E8;
  --cream-dark: #E8E0D0;
  --black: #1A1A1A;
  --white: #FFFFFF;

  /* Legacy mappings for backward compatibility */
  --color-primary: #2B4D7D;           /* Navy */
  --color-secondary: #8D99AE;         /* Cool Grey (legacy) */
  --color-background: #F5F1E8;        /* Cream */
  --color-action: #436098;            /* Professional Blue (legacy) */
  --color-accent: #D74444;            /* Red */
}
```

**Gradient Options**

All gradients use 135deg diagonal direction for consistent art deco aesthetic.

```
Navy Gradient (primary - hero sections, headers)
- Linear gradient: Navy Dark (#1F3859) → Navy (#2B4D7D) → Navy Light (#3A5F99)
- Direction: 135deg diagonal
- Use: Hero sections, major headers, emphasis backgrounds
- Currently in use: Homepage hero, About page hero, Episode page headers

Red Gradient (accent - premium/CTA)
- Linear gradient: Red Dark (#A63333) → Red (#D74444)
- Direction: 135deg diagonal
- Use: Premium CTAs, "Listen Now" buttons, newsletter signup boxes, high-priority elements
- Currently in use: Listen Now buttons, Newsletter sections, Episode sponsor cards

Teal Gradient (supporting - secondary emphasis)
- Linear gradient: Teal (#4A9B9B) → Teal Light (#6BB8B8)
- Direction: 135deg diagonal
- Use: Secondary emphasis, alternative CTAs, supporting sections
- Currently in use: Secondary buttons, alternate section backgrounds

Cream Gradient (subtle - background depth)
- Linear gradient: White (#FFFFFF) → Cream (#F5F1E8)
- Direction: 135deg diagonal (or 180deg vertical)
- Use: Page backgrounds, subtle depth, card backgrounds
- Currently in use: Page transitions, section backgrounds
```

**Color Usage Guidelines**

**Red (#D74444):**
- Primary CTA buttons: "Listen Now", "Subscribe"
- Category badges and important labels
- Newsletter signup sections
- Hover states for critical actions
- Use sparingly for maximum impact
- Always pair with sufficient whitespace

**Navy (#2B4D7D):**
- Header and footer backgrounds
- Primary navigation text
- Body text and headings
- Section backgrounds when contrast needed
- Professional, authoritative contexts

**Teal (#4A9B9B):**
- Links in body text
- Tag badges and metadata
- Interactive element accents
- Secondary navigation elements
- Provides friendly contrast to navy/red

**Cream (#F5F1E8):**
- Main page background throughout site
- Card backgrounds (often white, but cream for variety)
- Provides warmth and vintage feel
- Reduces harsh white contrast

**Color Contrast Requirements:**
- All text must meet WCAG AA standards (4.5:1 for normal text, 3:1 for large text)
- Red on white: 4.86:1 (AA compliant)
- Navy on cream: 8.54:1 (AAA compliant)
- Teal on white: 3.12:1 (AA compliant for large text)
- White on navy: 9.63:1 (AAA compliant)

### 2.2 Typography

**Updated: December 9, 2025 - Google Fonts Implementation**

The website uses a carefully selected combination of Google Fonts that reinforce the Art Deco aesthetic while maintaining excellent readability.

**Font Strategy**
Three complementary Google Fonts provide hierarchical visual interest and period-appropriate styling:

**1. Oswald (Headings)**
```css
font-family: 'Oswald', sans-serif;
font-weight: 600 (Semi-bold) for H3-H6, UI elements
font-weight: 700 (Bold) for H1-H2, major headlines
```

**Character:**
- Condensed sans-serif with strong geometric structure
- Art Deco-inspired letterforms
- Excellent for display headings and impact
- Clean, modern interpretation of 1920s type design

**Usage:**
- H1 page titles
- H2 section headings
- Major hero text
- Navigation elements
- Card titles

**2. PT Serif (Body Text)**
```css
font-family: 'PT Serif', serif;
font-weight: 400 (Regular) for body text
font-weight: 700 (Bold) for emphasis within body text
```

**Character:**
- Transitional serif with humanist qualities
- Excellent readability at all sizes
- Slightly condensed for efficient text display
- Elegant without being overly decorative

**Usage:**
- All body text and paragraphs
- Episode descriptions
- Blog post content
- Metadata and captions
- Long-form reading content

**3. Bebas Neue (UI Elements)**
```css
font-family: 'Bebas Neue', cursive;
font-weight: 400 (Regular - only weight available)
```

**Character:**
- Tall, narrow, all-caps display face
- Strong geometric construction
- Quintessential Art Deco style
- Best used at larger sizes for impact

**Usage:**
- Episode badges and numbers
- Decorative labels
- Call-out text
- Special emphasis elements
- Art deco ornamental text

**Font Loading**
```html
<!-- In <head> -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Oswald:wght@600;700&family=PT+Serif:wght@400;700&display=swap" rel="stylesheet">
```

**Typography Scale**

```
H1 (Page Titles, Hero Headlines)
- Font: Oswald Bold (700)
- Size: clamp(2.5rem, 5vw, 4rem) - fluid sizing
  - Mobile: 2.5rem (40px)
  - Desktop: 3-4rem (48-64px)
- Line Height: 1.1
- Letter Spacing: -0.02em (tighter for impact)
- Color: Red (#D74444) or White (on dark backgrounds)
- Usage: Homepage hero, page heroes, major statements

H2 (Section Headings)
- Font: Oswald Bold (700)
- Size: clamp(2rem, 4vw, 3rem)
  - Mobile: 2rem (32px)
  - Desktop: 2.5-3rem (40-48px)
- Line Height: 1.2
- Letter Spacing: -0.01em
- Color: Navy (#2B4D7D) or White (on dark backgrounds)
- Usage: Major section headings, category titles

H3 (Subsection Headings, Card Titles)
- Font: Oswald Semi-bold (600)
- Size: clamp(1.5rem, 3vw, 2rem)
  - Mobile: 1.5rem (24px)
  - Desktop: 1.75-2rem (28-32px)
- Line Height: 1.3
- Letter Spacing: -0.005em
- Color: Navy (#2B4D7D)
- Usage: Episode titles, card headings, subsections

H4 (Minor Headings, Widget Titles)
- Font: Oswald Semi-bold (600)
- Size: 1.25rem (20px)
- Line Height: 1.4
- Letter Spacing: normal
- Color: Navy (#2B4D7D)
- Usage: Sidebar headings, metadata labels, form labels

Body Text (Paragraphs, Descriptions)
- Font: PT Serif Regular (400)
- Size: 1rem (16px)
- Line Height: 1.7 (increased for readability with serif)
- Color: Navy (#2B4D7D) - darker than typical body text for premium feel
- Max Width: 70ch for optimal readability
- Usage: All paragraph text, descriptions, reading content

Small Text (Metadata, Captions, Notes)
- Font: PT Serif Regular (400)
- Size: 0.875rem (14px)
- Line Height: 1.5
- Color: Navy (#2B4D7D) at 80% opacity or Teal (#4A9B9B)
- Usage: Dates, durations, categories, footnotes, metadata

UI Labels (Badges, Numbers, Decorative Elements)
- Font: Bebas Neue Regular (400)
- Size: Varies by context (typically 1.25rem-2rem)
- Letter Spacing: 0.05em (slightly opened up)
- Text Transform: uppercase
- Color: Red (#D74444), White, or Navy (#2B4D7D)
- Usage: Episode numbers, category badges, decorative labels

Links (Inline Text Links)
- Font: Inherits from parent (typically PT Serif)
- Size: Inherits from parent
- Color: Teal (#4A9B9B)
- Hover: Red (#D74444)
- Text Decoration: Underline on hover
- Transition: color 0.2s ease
```

**Typographic Hierarchy Rules**

1. **Only one H1 per page** - improves SEO and accessibility
2. **Logical heading order** - don't skip heading levels (H2 → H3, not H2 → H4)
3. **Consistent font pairing** - Oswald for headings, PT Serif for body, Bebas Neue for UI
4. **Adequate line height** - 1.7 for body text (serif), 1.1-1.4 for headings
5. **Limited max-width** - 70ch for body text prevents overly long lines
6. **Responsive scaling** - use clamp() for fluid typography on headings
7. **Sufficient color contrast** - all text meets WCAG AA standards

### 2.3 Spacing System

**Base Unit: 8px**

Consistent spacing creates rhythm and visual harmony. All spacing values use multiples of 8px.

```
xs: 4px   (0.25rem)  - Tight spacing, icon gaps
sm: 8px   (0.5rem)   - Compact elements, minimal padding
md: 16px  (1rem)     - Default spacing, standard padding
lg: 24px  (1.5rem)   - Section spacing, comfortable padding
xl: 32px  (2rem)     - Major component spacing
2xl: 48px (3rem)     - Section spacing, vertical rhythm
3xl: 64px (4rem)     - Hero sections, major page divisions
```

**CSS Variables:**
```css
:root {
  --space-xs: 0.25rem;   /* 4px */
  --space-sm: 0.5rem;    /* 8px */
  --space-md: 1rem;      /* 16px */
  --space-lg: 1.5rem;    /* 24px */
  --space-xl: 2rem;      /* 32px */
  --space-2xl: 3rem;     /* 48px */
  --space-3xl: 4rem;     /* 64px */
}
```

**Application:**
- **Padding**: Use multiples of 8px for all component padding
- **Margins**: Use multiples of 8px for all component margins
- **Grid gaps**:
  - Mobile: 16px (1rem)
  - Tablet: 24px (1.5rem)
  - Desktop: 32px (2rem)
- **Vertical rhythm**: Use 2xl (48px) between major page sections
- **Component spacing**: Use md (16px) as default between related elements

### 2.4 Border Radius

Rounded corners soften the geometric art deco style while maintaining clean lines.

```
sm: 4px   - Small elements (tags, badges, small buttons)
md: 8px   - Standard elements (cards, buttons, inputs, most UI)
lg: 12px  - Large cards, prominent containers
full: 50% - Circular elements (avatars, icon buttons)
```

**CSS Variables:**
```css
:root {
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
}
```

**Usage Guidelines:**
- Cards: 8px (md) for standard cards, 12px (lg) for hero/featured cards
- Buttons: 8px (md) for consistency
- Inputs: 8px (md) for form fields
- Images: 8px (md) when displayed in cards
- Badges/Tags: 4px (sm) or 20px (pill shape for some tags)

### 2.5 Shadows

Subtle shadows create depth and hierarchy in the interface.

```
Light (Standard UI, Gentle Elevation)
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
Use: Cards, buttons (resting state), dropdowns

Medium (Elevated Components, Hover States)
box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
Use: Cards on hover, elevated cards, prominent components

Strong (Modals, Critical Elements)
box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
Use: Modals, overlays, maximum emphasis

Art Deco Accent (Colored Shadows for Special Elements)
box-shadow: 0 4px 12px rgba(215, 68, 68, 0.3);  /* Red shadow */
box-shadow: 0 4px 12px rgba(43, 77, 125, 0.3);  /* Navy shadow */
Use: Buttons on hover, special emphasis, adds color depth
```

**CSS Variables:**
```css
:root {
  --shadow-light: 0 2px 8px rgba(0, 0, 0, 0.1);
  --shadow-medium: 0 4px 16px rgba(0, 0, 0, 0.12);
  --shadow-strong: 0 8px 24px rgba(0, 0, 0, 0.15);
}
```

**Shadow Animation:**
```css
transition: all 0.3s ease;  /* Smooth shadow transitions on hover/interaction */
```

---

## 3. Component Design

### 3.1 Buttons

Buttons are a critical part of the interface. The Art Deco design uses bold, confident button styling.

**Primary Button (Main CTAs - Red)**
```
Background: Red (#D74444)
Text: White
Padding: 12px 24px (0.75rem 1.5rem)
Border Radius: 8px (var(--radius-md))
Font: Oswald Semi-bold (600)
Font Size: 1rem (16px)
Text Transform: Uppercase
Letter Spacing: 0.05em
Border: None

Hover State:
- Background: Red Dark (#A63333)
- Box Shadow: 0 4px 12px rgba(215, 68, 68, 0.3) [colored shadow]
- Transform: translateY(-2px)
- Transition: all 0.2s ease

Active State:
- Transform: translateY(0)
- Box Shadow: 0 2px 8px rgba(215, 68, 68, 0.3)

Focus State:
- Outline: 2px solid Red (#D74444)
- Outline Offset: 2px

Examples: "Listen Now", "Subscribe", "Contact Us"
```

**Secondary Button (Alternative Actions - Navy)**
```
Background: Navy (#2B4D7D)
Text: White
Padding: 12px 24px (0.75rem 1.5rem)
Border Radius: 8px
Font: Oswald Semi-bold (600)
Font Size: 1rem (16px)
Text Transform: Uppercase
Letter Spacing: 0.05em
Border: None

Hover State:
- Background: Navy Light (#3A5F99)
- Box Shadow: 0 4px 12px rgba(43, 77, 125, 0.3)
- Transform: translateY(-2px)
- Transition: all 0.2s ease

Active State:
- Transform: translateY(0)
- Box Shadow: 0 2px 8px rgba(43, 77, 125, 0.3)

Examples: "Browse Episodes", "View All", "Learn More"
```

**Tertiary Button (Outline Style)**
```
Background: Transparent
Border: 2px solid Navy (#2B4D7D)
Text: Navy (#2B4D7D)
Padding: 10px 24px (adjusted for border)
Border Radius: 8px
Font: Oswald Semi-bold (600)
Font Size: 1rem (16px)
Text Transform: Uppercase
Letter Spacing: 0.05em

Hover State:
- Background: Navy (#2B4D7D)
- Text: White
- Border: 2px solid Navy (#2B4D7D)
- Transition: all 0.2s ease

Active State:
- Background: Navy Dark (#1F3859)
- Border: 2px solid Navy Dark (#1F3859)

Examples: "Learn More", "Read Details", "Explore Resources"
```

**Text Button (Minimal, Inline Links)**
```
Background: Transparent
Text: Teal (#4A9B9B)
Font: PT Serif Regular (400) or Oswald Semi-bold (600)
Font Size: 1rem (16px)
Text Decoration: None (underline on hover)
Border: None
Padding: Minimal or none

Hover State:
- Text: Red (#D74444)
- Text Decoration: Underline
- Transition: all 0.2s ease

Examples: "Read More →", "See Details", "View All Episodes →"
```

### 3.2 Cards

Cards are the primary container component for episodes, blog posts, and other content.

**Episode Card (Primary Content)**
```
Structure:
┌──────────────────────────────────────┐
│  [Episode Cover Image - 16:9]        │
├──────────────────────────────────────┤
│  Episode Badge (EP 65) - top right   │
│  Category Tag                         │
│  H3: Episode Title                    │
│  Guest Name | Duration                │
│  Brief description (2-3 lines)        │
│  [Listen Now Button]                  │
└──────────────────────────────────────┘

Style:
- Background: White
- Border: None
- Border Radius: 8px (var(--radius-md))
- Padding: 0 (image full bleed at top), 20px bottom content padding
- Box Shadow: 0 2px 8px rgba(0, 0, 0, 0.1) [light shadow]
- Overflow: visible (allows badge to extend beyond card)
- Transition: all 0.3s ease

Hover State:
- Box Shadow: 0 4px 16px rgba(0, 0, 0, 0.12) [medium shadow]
- Transform: translateY(-4px) [lift effect]

Cover Image:
- Aspect Ratio: 16:9 (preferred) or 1:1
- Object Fit: cover
- Border Radius: 8px 8px 0 0 (top corners only)
- Width: 100%
- Height: auto

Episode Badge (NEW - Art Deco Feature):
- Position: Absolute, top: -1rem, right: -1rem (floats outside card)
- Background: Red (#D74444) to Red Dark gradient
- Color: White
- Font: Bebas Neue (400)
- Padding: 0.5rem 1rem
- Border Radius: 8px
- Box Shadow: 0 2px 8px rgba(215, 68, 68, 0.3)
- Text: "EP 65" format
- Line 1: Episode number (larger)
- Line 2: "EP" label (smaller)

Category Tag:
- Background: Navy (#2B4D7D) or category-specific color
- Text: White
- Padding: 4px 12px
- Border Radius: 4px (var(--radius-sm))
- Font: Oswald Semi-bold (600)
- Font Size: 0.75rem (12px)
- Text Transform: Uppercase
- Letter Spacing: 0.05em
```

**Blog Card (Text-Focused)**
```
Structure:
┌──────────────────────────────────────┐
│  Category Tag                         │
│  H3: Blog Post Title                  │
│  Author | Date                        │
│  Tag Pills (first 3)                  │
│  Description (120 chars truncated)    │
│  [Read More Button]                   │
└──────────────────────────────────────┘

Style:
- Background: White
- Border: None
- Border Radius: 8px
- Padding: 2rem (32px)
- Box Shadow: 0 2px 8px rgba(0, 0, 0, 0.1)
- Transition: all 0.3s ease

Hover State:
- Box Shadow: 0 4px 16px rgba(0, 0, 0, 0.12)
- Transform: translateY(-2px) [subtle lift]

Category Tag:
- Same as episode cards

Tag Pills:
- Background: rgba(74, 155, 155, 0.1) [teal with transparency]
- Text: Teal (#4A9B9B)
- Padding: 4px 12px
- Border Radius: 12px (pill shape)
- Font Size: 0.75rem (12px)
```

### 3.3 Forms

Forms maintain the art deco aesthetic while prioritizing usability.

**Input Fields**
```
Style:
- Background: White
- Border: 2px solid Cream Dark (#E8E0D0)
- Border Radius: 8px (var(--radius-md))
- Padding: 12px 16px (0.75rem 1rem)
- Font: PT Serif Regular (400)
- Font Size: 1rem (16px)
- Color: Navy (#2B4D7D)
- Width: 100% (in form context)

Focus State:
- Border: 2px solid Teal (#4A9B9B)
- Box Shadow: 0 0 0 3px rgba(74, 155, 155, 0.1)
- Outline: None
- Transition: all 0.2s ease

Error State:
- Border: 2px solid Red (#D74444)
- Box Shadow: 0 0 0 3px rgba(215, 68, 68, 0.1)

Placeholder:
- Color: Navy (#2B4D7D) at 50% opacity
- Font Style: Italic (optional for PT Serif)

Labels:
- Font: Oswald Semi-bold (600)
- Font Size: 0.875rem (14px)
- Color: Navy (#2B4D7D)
- Text Transform: Uppercase
- Letter Spacing: 0.05em
- Margin Bottom: 8px (var(--space-sm))
```

**Email Signup Form (Newsletter)**
```
Layout Options:

Inline (for sections):
[Email Input Field] [Subscribe Button]

Stacked (for sidebar):
[Email Input Field]
[Subscribe Button (full width)]

Container Style:
- Background: Red gradient (#A63333 → #D74444, 135deg)
- Color: White
- Padding: 2rem
- Border Radius: 12px (var(--radius-lg))
- Box Shadow: 0 4px 16px rgba(0, 0, 0, 0.12)

Input Field (within newsletter form):
- Background: White
- Color: Navy (#2B4D7D)
- Placeholder: Navy at 50% opacity
- All other standard input styles

Submit Button:
- Background: White
- Color: Red (#D74444)
- Hover Background: Cream (#F5F1E8)
- All other primary button styles

Privacy Note (below form):
- Font Size: 0.875rem (14px)
- Opacity: 0.9
- Margin Top: 1rem
```

### 3.4 Navigation

**Desktop Navigation**
```
Structure:
[Logo] [Episodes] [Blog] [About] [Resources] [Partnership] [Contact] [Listen Now Button]

Style:
- Background: White with subtle bottom border or shadow
- Height: 80px
- Position: Sticky (stays at top on scroll)
- Z-index: 1000
- Padding: 0 2rem

Logo:
- Height: 60px
- Width: auto

Navigation Links:
- Font: Oswald Semi-bold (600)
- Font Size: 1rem (16px)
- Color: Navy (#2B4D7D)
- Text Transform: Uppercase
- Letter Spacing: 0.05em
- Padding: 0.5rem 1rem
- Transition: color 0.2s ease

Hover State:
- Color: Red (#D74444)

Active/Current Page:
- Color: Red (#D74444)
- Border Bottom: 2px solid Red (#D74444)

Listen Now Button:
- Primary button style (Red)
- Positioned at far right
```

**Mobile Navigation (< 900px)**
```
Structure:
[Logo] [Hamburger Menu Icon ☰]

Hamburger Icon:
- Size: 30px × 24px (three 4px lines)
- Color: Navy (#2B4D7D)
- Hover: Red (#D74444)
- Transition: all 0.3s ease
- Animates to X when menu open

Expanded State (Full Overlay):
- Background: Navy (#2B4D7D) gradient overlay
- Position: Fixed, full screen
- Z-index: 2000
- Animation: Slide in from right or fade in
- Close button (X) top right

Menu Links:
- Font: Oswald Bold (700)
- Font Size: 1.5rem (24px)
- Color: White
- Text Transform: Uppercase
- Letter Spacing: 0.05em
- Padding: 1.5rem 2rem
- Display: Block, stacked vertically
- Text Align: Center or left

Link Hover:
- Color: Red (#D74444)
- Transform: translateX(10px) [slide right slightly]
- Transition: all 0.2s ease

Social Icons (at bottom of mobile menu):
- Color: White
- Size: 32px
- Hover: Red (#D74444)
```

### 3.5 Footer

The footer uses a dark navy background with cream/white text, maintaining the art deco theme.

```
Structure (Desktop):
┌──────────────────────────────────────────────────────────┐
│  [Logo Column]    [Browse Column]    [About Column]      │
│  Tagline          - All Episodes    - About the Show     │
│                   - Blog             - Newsletter         │
│                   - Resources        - Contact            │
│                                      - Partnership        │
│                                                           │
│  [Listen On Column]                                       │
│  - YouTube                                                │
│  - Spotify                                                │
│  - Apple Podcasts                                         │
│  - Amazon Music                                           │
│                                                           │
│  ──────────────────────────────────────────────────────  │
│  © 2025 Security Mixologists LLC | Privacy | Terms       │
│  @SecCocktailHour | feedback@securitycocktailhour.com    │
└──────────────────────────────────────────────────────────┘

Style:
- Background: Navy (#2B4D7D)
- Color: White at 90% opacity (links)
- Color: White at 100% opacity (headings, current text)
- Padding: 3rem 0 2rem
- Font: PT Serif Regular (400) for links, Oswald Semi-bold (600) for headings

Column Headings:
- Font: Oswald Semi-bold (600)
- Font Size: 1rem (16px)
- Color: White
- Text Transform: Uppercase
- Letter Spacing: 0.05em
- Margin Bottom: 1rem

Links:
- Font: PT Serif Regular (400)
- Font Size: 0.9375rem (15px)
- Color: White at 90% opacity
- Text Decoration: None
- Transition: all 0.2s ease

Link Hover:
- Color: White at 100% opacity (full brightness)
- Transform: translateX(4px) [subtle slide right]

Logo:
- Height: 50px
- Margin Bottom: 1rem
- Opacity: 90%

Tagline:
- Font Style: Italic
- Opacity: 80%
- Margin Bottom: 2rem

Divider Line:
- Border Top: 1px solid White at 20% opacity
- Margin: 2rem 0

Copyright/Legal Links:
- Font Size: 0.875rem (14px)
- Opacity: 70%
- Margin Bottom: 0.5rem

Mobile Adaptation (< 900px):
- Stack all columns vertically
- Center align text
- Logo centered at top
- Reduce padding to 2rem 0
```

---

## 4. Page Layouts

### 4.1 Homepage Layout - Art Deco Hero Design

**Updated: December 9, 2025 - Complete Art Deco Redesign**

The homepage features a sophisticated art deco hero section with geometric patterns, ornamental details, and premium typography. This is the signature design element that sets the tone for the entire site.

```
┌────────────────────────────────────────────────────────────┐
│  [NAVIGATION BAR - Sticky, White background]               │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  HERO SECTION - Art Deco Design                            │
│  ┌────────────────────────────────────────────────────────┐│
│  │ [Art Deco Pattern Overlay - geometric crosshatch]      ││
│  │ [Corner Ornaments - top-left and bottom-right]         ││
│  │                                                         ││
│  │  ┌──────────────────────┐  ┌─────────────────────────┐││
│  │  │ LEFT: Hero Content   │  │ RIGHT: Latest Episode   │││
│  │  │                      │  │                         │││
│  │  │ H1: "Security        │  │ "Latest Episode" label  │││
│  │  │     Cocktail Hour"   │  │                         │││
│  │  │ (Oswald, huge)       │  │ ┌─────────────────────┐│││
│  │  │                      │  │ │ [Episode Badge]     ││││
│  │  │ [Decorative Divider] │  │ │ EP 65               ││││
│  │  │                      │  │ │                     ││││
│  │  │ Tagline: "Cybersec-  │  │ │ [Episode Image]     ││││
│  │  │ urity pros talking   │  │ │                     ││││
│  │  │ shop at the virtual  │  │ │ Category            ││││
│  │  │ bar."                │  │ │ Episode Title       ││││
│  │  │                      │  │ │ Guest | Duration    ││││
│  │  │ [Listen Now] [Browse]│  │ │ [Listen Now]        ││││
│  │  │                      │  │ └─────────────────────┘│││
│  │  │ Platform Links:      │  │                         │││
│  │  │ YouTube | Spotify    │  │                         │││
│  │  │ Apple | Amazon       │  │                         │││
│  │  └──────────────────────┘  └─────────────────────────┘││
│  │                                                         ││
│  └────────────────────────────────────────────────────────┘│
│                                                             │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  RECENT EPISODES SECTION (Cream background)                │
│  H2: "Recent Episodes"              [View All →]           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐     │
│  │Episode   │ │Episode   │ │Episode   │ │Episode   │     │
│  │Card      │ │Card      │ │Card      │ │Card      │     │
│  │Small     │ │Small     │ │Small     │ │Small     │     │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘     │
│  (Shows 4 episodes - after skipping latest)                │
│                                                             │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  FEATURED BLOG POSTS SECTION (White background)            │
│  (Conditional - only if featured posts exist)              │
│  H2: "Featured Blog Posts"          [View All →]           │
│  ┌──────────────────────────┐ ┌──────────────────────────┐│
│  │Blog Card                 │ │Blog Card                 ││
│  │Category, Title, Meta     │ │Category, Title, Meta     ││
│  │Tags, Description         │ │Tags, Description         ││
│  │[Read More]               │ │[Read More]               ││
│  └──────────────────────────┘ └──────────────────────────┘│
│  (Shows up to 2 featured posts)                            │
│                                                             │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  ABOUT SECTION (Navy gradient background, white text)      │
│  [Art Deco Pattern Overlay]                                │
│  ┌──────────────────────────┐ ┌──────────────────────────┐│
│  │H2: About the Show        │ │Hosted by                 ││
│  │                          │ │Joe Patti & Adam Roth     ││
│  │Description paragraphs    │ │                          ││
│  │about podcast mission     │ │Host bio paragraph        ││
│  │and value proposition     │ │                          ││
│  └──────────────────────────┘ └──────────────────────────┘│
│                                                             │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  NEWSLETTER SECTION (Red gradient background, white text)  │
│  H2: "Join Our Newsletter"                                 │
│  Description text                                           │
│  [Email Input] [Subscribe Button]                          │
│  Privacy note                                               │
│                                                             │
├────────────────────────────────────────────────────────────┤
│  [FOOTER - Navy background, white text]                    │
└────────────────────────────────────────────────────────────┘
```

**Hero Section - Detailed Specifications**

**Container:**
- Background: Navy gradient (135deg, #1F3859 → #2B4D7D → #3A5F99)
- Padding: 6rem 2rem (desktop), 4rem 1.5rem (mobile)
- Min Height: 600px (desktop), auto (mobile)
- Position: Relative (for absolute positioned children)
- Overflow: Hidden (for pattern effects)

**Art Deco Pattern Overlay:**
```css
.art-deco-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image:
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 35px,
      rgba(255, 255, 255, 0.03) 35px,
      rgba(255, 255, 255, 0.03) 70px
    ),
    repeating-linear-gradient(
      -45deg,
      transparent,
      transparent 35px,
      rgba(255, 255, 255, 0.03) 35px,
      rgba(255, 255, 255, 0.03) 70px
    );
  pointer-events: none;
  z-index: 1;
}
```

**Corner Ornaments:**
```css
.corner-ornament {
  position: absolute;
  width: 100px;
  height: 100px;
  border: 2px solid rgba(255, 255, 255, 0.1);
  pointer-events: none;
  z-index: 2;
}

.corner-tl {
  top: 2rem;
  left: 2rem;
  border-right: none;
  border-bottom: none;
}

.corner-br {
  bottom: 2rem;
  right: 2rem;
  border-left: none;
  border-top: none;
}
```

**Hero Grid:**
```css
.hero-grid {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;  /* Critical: fractional units account for gap */
  gap: 80px;
  align-items: center;
  position: relative;
  z-index: 3;
}

@media (max-width: 899px) {
  .hero-grid {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
}
```

**Hero Content (Left Column):**
```css
.hero-content {
  color: white;
}

.hero-title {
  font-family: 'Oswald', sans-serif;
  font-weight: 700;
  font-size: clamp(3rem, 6vw, 5rem);
  line-height: 1;
  letter-spacing: -0.02em;
  margin-bottom: 2rem;
  text-transform: uppercase;
}

.hero-title .highlight {
  color: var(--red);  /* "Cocktail Hour" in red */
  display: block;
}

.divider {
  width: 100%;
  height: 2px;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(255, 255, 255, 0.3) 20%,
    rgba(255, 255, 255, 0.3) 80%,
    transparent 100%
  );
  margin: 2rem 0;
  position: relative;
}

.divider-center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 40px;
  height: 40px;
  background: var(--navy);
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
}

.hero-tagline {
  font-family: 'PT Serif', serif;
  font-size: 1.25rem;
  font-style: italic;
  line-height: 1.6;
  margin-bottom: 2rem;
  opacity: 0.95;
}

.cta-container {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.platform-links {
  display: flex;
  gap: 1.5rem;
  align-items: center;
  flex-wrap: wrap;
}

.platform-label {
  font-family: 'Oswald', sans-serif;
  font-weight: 600;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  opacity: 0.8;
}

.platform-link {
  font-family: 'PT Serif', serif;
  font-size: 0.9375rem;
  color: white;
  text-decoration: none;
  opacity: 0.9;
  transition: all 0.2s ease;
}

.platform-link:hover {
  color: var(--red);
  opacity: 1;
  text-decoration: underline;
}
```

**Latest Episode Card (Right Column):**
```css
.episode-wrapper {
  position: relative;
  overflow: visible;  /* Critical: allows badge to extend beyond bounds */
}

.latest-label {
  font-family: 'Bebas Neue', cursive;
  font-size: 1.25rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: white;
  margin-bottom: 1rem;
  opacity: 0.9;
}

.episode-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
  overflow: visible;  /* Critical: allows badge to extend beyond card */
  position: relative;
  transition: all 0.3s ease;
}

.episode-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.25);
}

.episode-badge {
  position: absolute;
  top: -1rem;
  right: -1rem;
  background: linear-gradient(135deg, var(--red) 0%, var(--red-dark) 100%);
  color: white;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(215, 68, 68, 0.4);
  text-align: center;
  z-index: 10;
}

.episode-number {
  font-family: 'Bebas Neue', cursive;
  font-size: 2rem;
  line-height: 1;
  font-weight: 400;
}

.episode-label {
  font-family: 'Oswald', sans-serif;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-top: 0.25rem;
}

.episode-image {
  width: 100%;
  height: auto;
  max-width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  border-radius: 12px 12px 0 0;
  display: block;
}

.episode-content {
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.episode-category {
  display: inline-block;
  background: var(--navy);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-family: 'Oswald', sans-serif;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  align-self: flex-start;
}

.episode-title {
  font-family: 'Oswald', sans-serif;
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--navy);
  line-height: 1.3;
  margin: 0;
}

.episode-meta {
  font-family: 'PT Serif', serif;
  font-size: 0.875rem;
  color: var(--teal);
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.episode-guest {
  font-weight: 700;
}

.episode-cta {
  /* Uses primary button styling */
  background: var(--red);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-family: 'Oswald', sans-serif;
  font-weight: 600;
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  text-decoration: none;
  text-align: center;
  transition: all 0.2s ease;
  display: inline-block;
}

.episode-cta:hover {
  background: var(--red-dark);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(215, 68, 68, 0.3);
}
```

**Mobile Adaptation:**
```css
@media (max-width: 899px) {
  /* Hero section stacks vertically */
  .hero {
    padding: 4rem 1.5rem;
    min-height: auto;
  }

  .hero-title {
    font-size: clamp(2.5rem, 8vw, 3.5rem);
  }

  .cta-container {
    flex-direction: column;
  }

  .cta-container .btn {
    width: 100%;
    text-align: center;
  }

  .platform-links {
    flex-direction: column;
    align-items: flex-start;
  }

  /* Episode card adjustments */
  .episode-badge {
    top: -0.5rem;
    right: -0.5rem;
    padding: 0.5rem 0.75rem;
  }

  .episode-number {
    font-size: 1.5rem;
  }

  /* Corner ornaments hidden on mobile */
  .corner-ornament {
    display: none;
  }
}
```

### 4.2 Episode Library Layout

*[This section remains largely unchanged from v1.2 - include original content]*

### 4.3 Individual Episode Page Layout

*[This section remains largely unchanged from v1.2 - include original content]*

### 4.4 About Page Layout

*[This section remains largely unchanged from v1.2 - include original content]*

---

## 5. Recent Implementation Fixes

**Added: December 9, 2025**

### 5.1 Newsletter Signup Box Fix (Episode Single Pages)

**Problem**: Newsletter signup box on individual episode pages had white text on white background, making it invisible.

**Root Cause**: Both `.card` and `.card-content` classes in CSS had white/cream background gradients that needed to be overridden on the episode single template.

**Solution**: Added inline styles with `!important` to force red gradient background.

**Implementation** (`layouts/episodes/single.html`, lines 214-236):
```html
<div class="card" style="margin-bottom: 2rem; background: linear-gradient(135deg, #B33333 0%, #D74444 100%) !important; color: white;">
  <div class="card-content" style="background: linear-gradient(135deg, #B33333 0%, #D74444 100%) !important;">
    <h4 style="color: white; margin-bottom: 0.75rem;">Join Our Newsletter</h4>
    <p style="font-size: 0.875rem; margin-bottom: 1.5rem; opacity: 0.95;">
      Get exclusive insights, show news and more delivered to your inbox.
    </p>
    <form ...>
      <input type="email"
        style="width: 100%; padding: 0.875rem 1.25rem; border: 2px solid rgba(255, 255, 255, 0.3);
               border-radius: 4px; font-family: 'PT Serif', serif; font-size: 1rem;
               background: white; color: #2D2D2D; margin-bottom: 1rem; transition: all 0.3s ease;">
      <button type="submit"
        style="width: 100%; background: white; color: #D74444; padding: 0.875rem 1.5rem;
               font-weight: 600; border: 2px solid white; transition: all 0.3s ease;">
        Subscribe
      </button>
    </form>
  </div>
</div>
```

### 5.2 About Section Text Visibility Fix

**Problem**: About section on homepage had unreadable text (light text on light background).

**Root Cause**: Duplicate `.about-section` definition at line 2964 in CSS was overriding the correct navy gradient background (line 1111) with white background.

**Solution**: Removed `background: var(--white)` from duplicate definition at line 2966.

**File Modified**: `static/css/main.css`

**Before**:
```css
.about-section {
  padding: 4rem 2rem;
  background: var(--white);  /* ← This was the problem */
}
```

**After**:
```css
.about-section {
  padding: 4rem 2rem;
  /* background removed - inherits navy gradient from earlier definition */
}
```

### 5.3 Episode Card Images Fix (Homepage Recent Episodes)

**Problem**: Episode card images in "Recent Episodes" section didn't fill full width, leaving white space on right side and making cards unbalanced. Images were cropping top/bottom.

**Root Cause**: `.episode-card-small .episode-image` only had `height: 180px`, causing images to crop and not fill width.

**Solution**: Changed to `width: 100%; height: auto; display: block;` to show full images at natural aspect ratio.

**File Modified**: `static/css/main.css` (lines 1020-1022)

**Before**:
```css
.episode-card-small .episode-image {
  height: 180px;
}
```

**After**:
```css
.episode-card-small .episode-image {
  width: 100%;
  height: auto;
  display: block;
}
```

**Result**: Images now display at full aspect ratio without cropping, cards adjust height to accommodate images.

### 5.4 CSS Cache-Busting Implementation

**Problem**: Production site showed old design in regular browsers but worked in incognito mode - browsers were caching old CSS files.

**Solution**: Added `?v={{ now.Unix }}` timestamp parameter to CSS file links in both baseof.html and index.html templates.

**Files Modified**:
- `layouts/_default/baseof.html` (line 33)
- `layouts/index.html` (line 33)

**Implementation**:
```html
<!-- Before -->
<link rel="stylesheet" href="{{ "css/main.css" | relURL }}">

<!-- After -->
<link rel="stylesheet" href="{{ "css/main.css" | relURL }}?v={{ now.Unix }}">
```

**Result**: Each build generates unique CSS URL, forcing browsers to fetch updated files instead of using cache. This prevents users from seeing outdated styles after deployments.

### 5.5 Homepage Recent Episodes Count Reduction

**Change**: Reduced from 5 to 4 episodes in "Recent Episodes" section for better layout balance.

**File Modified**: `layouts/index.html` (line 164)

**Before**:
```go
{{ $recent := where .Site.RegularPages "Type" "episodes" | first 6 }}
```

**After**:
```go
{{ $recent := where .Site.RegularPages "Type" "episodes" | first 5 }}
```

**Note**: The query gets 5 episodes total, then `after 1` skips the latest episode (which appears in the hero), displaying the next 4 episodes.

---

*[Continue with remaining sections from original v1.2 spec, maintaining all existing content for sections 6-15]*

---

## 16. Implementation Timeline

**Phase 1: October-November 2025 - Initial Launch**
- Core website structure with Hugo
- Basic color palette (blues/grays)
- Episode library and individual pages
- Blog functionality
- Partnership page

**Phase 2: December 2-9, 2025 - Art Deco Redesign**
- Complete visual redesign with Art Deco theme
- New color palette (Red, Navy, Teal, Cream)
- Google Fonts implementation (Oswald, PT Serif, Bebas Neue)
- Homepage hero section redesign with patterns and ornaments
- Episode card enhancements with floating badges
- Newsletter box styling fixes
- Cache-busting implementation

**Phase 3: Ongoing - Enhancements**
- Additional episode features
- Blog post optimizations
- Performance improvements
- SEO enhancements

---

**End of Design Specification v1.3**

## 6. Responsive Design Guidelines

### 6.1 Breakpoints

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

### 6.2 Layout Adaptations

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
- H1: 2.5-3rem using clamp()
- H2: 2rem using clamp()
- H3: 1.5rem using clamp()
- Body: 1rem (16px)

Desktop:
- H1: 3-5rem using clamp()
- H2: 2.5-3rem using clamp()
- H3: 1.75-2rem using clamp()
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

### 6.3 Mobile-First Approach

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

## 7. Interaction Design

### 7.1 Micro-interactions

**Button Hover/Click:**
```
Hover:
- Transform: translateY(-2px)
- Box Shadow: Elevated with colored shadow
- Transition: 0.2s ease

Active (Click):
- Transform: translateY(0)
- Box Shadow: Reduced
- Transition: 0.1s ease

Focus (Keyboard):
- Outline: 2px solid Teal (#4A9B9B)
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
Default: Color change (Teal → Red) + underline on hover
Header Navigation: Color change only (Navy → Red)
Footer: Opacity increase (90% → 100%)
```

### 7.2 Loading States

**Skeleton Screens:**
```
Use for:
- Episode cards while loading
- Content placeholders

Style:
- Light gray background (#F5F5F5)
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
- Navy (#2B4D7D) or Red (#D74444) color
- Centered in container
```

### 7.3 Empty States

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

### 7.4 Error States

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

## 8. Accessibility Requirements

### 8.1 Color Contrast

**WCAG 2.1 AA Compliance:**
```
Normal Text (< 18px):
- Contrast ratio: 4.5:1 minimum
- Red (#D74444) on White: 4.86:1 ✓
- Navy (#2B4D7D) on Cream: 8.54:1 ✓
- Teal (#4A9B9B) on White: 3.12:1 (use for large text or links only)

Large Text (≥ 18px or bold ≥ 14px):
- Contrast ratio: 3:1 minimum

UI Components:
- Contrast ratio: 3:1 minimum for interactive elements
```

**Testing:**
- Test all color combinations
- Verify with contrast checker tools
- Test with color blindness simulators

### 8.2 Keyboard Navigation

**Requirements:**
- All interactive elements keyboard accessible
- Logical tab order (top to bottom, left to right)
- Visible focus indicators (outline, highlight)
- Skip navigation links for main content
- Escape key closes modals/menus

**Focus Indicators:**
```
Style:
- Outline: 2px solid Teal (#4A9B9B) or Navy (#2B4D7D)
- Outline Offset: 2px
- Border Radius: matches element
```

### 8.3 Screen Reader Support

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

### 8.4 Content Accessibility

**Text:**
- Minimum font size: 16px body text
- Maximum line length: 70 characters
- Line height: 1.7 for body text (serif requires more)
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

## 9. Performance Guidelines

### 9.1 Image Optimization

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

### 9.2 Loading Strategy

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
- Google Fonts with `display=swap` parameter
- Preconnect to fonts.googleapis.com and fonts.gstatic.com
- Load only required weights (Oswald 600/700, PT Serif 400/700, Bebas Neue 400)

**Third-Party Embeds:**
- Lazy load social media embeds
- Use facades for video embeds (load on click)
- Minimize tracking scripts

### 9.3 Performance Budgets

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
- Fonts: < 100KB (3 font families)
- Images: < 500KB (optimized, lazy loaded)
- Total: < 1MB

Lighthouse Scores:
- Performance: 90+
- Accessibility: 100
- Best Practices: 95+
- SEO: 100
```

---

## 10. SEO Implementation

### 10.1 Schema Markup

**Podcast Schema (Organization/Website level):**
```json
{
  "@context": "https://schema.org",
  "@type": "PodcastSeries",
  "name": "Security Cocktail Hour",
  "url": "https://securitycocktailhour.com",
  "description": "Cybersecurity pros talking shop at the virtual bar",
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

### 10.2 Meta Tags Template

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

### 10.3 URL Structure

```
Homepage:           /
Episodes:           /episodes/
Episode Detail:     /episodes/[slug]/
Blog:               /blog/
Blog Post:          /blog/[slug]/
About:              /about/
Resources:          /resources/
Partnership:        /partnership/
Contact:            /contact/
Newsletter:         /newsletter/

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

## 11. Content Guidelines

### 11.1 Episode Show Notes Template

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

### 11.2 Image Requirements

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

### 11.3 Writing Style

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

## 12. Brand Voice & Messaging

### 12.1 Brand Voice

**Characteristics:**
- **Expert but Accessible:** Knowledgeable without jargon overload
- **Curious:** Always learning, exploring new areas
- **Inclusive:** Welcoming to all skill levels
- **Conversational:** Like talking with a colleague over drinks
- **Professional:** Credible and trustworthy
- **Sophisticated:** Premium art deco aesthetic reflects quality content

**What We Are:**
- Knowledgeable guides
- Curious explorers
- Friendly colleagues
- Industry insiders
- Stylish professionals

**What We're Not:**
- Overly academic or theoretical
- Exclusive or elitist
- Too casual or unprofessional
- Dry or boring
- Flashy or gimmicky

### 12.2 Key Messages

**Primary Message:**
"Cybersecurity pros talking shop at the virtual bar."

**Supporting Messages:**
- "Expanding cybersecurity knowledge beyond your specialty"
- "Learning from practitioners, not just theory"
- "Making security accessible to all"
- "Your career development companion"

**Value Propositions:**
- Discover security topics outside your specialty
- Learn from real-world practitioners
- Career insights and development guidance
- Accessible to technical and non-technical professionals

### 12.3 Content Tone Examples

**Homepage Hero:**
"Cybersecurity pros talking shop at the virtual bar."

**Episode Description Opening:**
"In this episode, we dive into [topic] with [Guest Name], who brings [X] years of experience in [specialty]. We discuss [key topics] and explore practical approaches to [challenge]."

**Email Newsletter:**
"Hey there, security professionals! This week we're featuring an insightful conversation with [Guest] about [topic]. Here's what you'll learn..."

**About Page:**
"Cybersecurity is a diverse and fast-changing field. Reading and training are good, but there's nothing like hearing what's really happening from the people who are doing it."

---

## 13. Implementation Priorities

### Phase 1: MVP Launch (October 2025)

**Completed:**
- Homepage with hero, latest episode, recent episodes
- Episode library with search and filter
- Individual episode pages with show notes
- About page with host bios
- Contact page with form
- Resources page
- Partnership page
- Email signup forms (Mailchimp integrated)
- Navigation and footer
- Mobile responsive
- Basic SEO (meta tags, schema markup)
- Google Analytics

### Phase 2: Enhancement (November 2025)

**Completed:**
- Blog functionality
- Enhanced episode search
- Newsletter dedicated page
- Social media integration
- Performance optimizations
- Additional SEO enhancements

### Phase 3: Art Deco Redesign (December 2025)

**Completed:**
- Complete visual redesign with Art Deco aesthetic
- New color palette (Red, Navy, Teal, Cream)
- Google Fonts implementation
- Homepage hero section with patterns and ornaments
- Episode card enhancements with floating badges
- Newsletter box styling fixes
- Cache-busting implementation

### Phase 4: Growth Features (Future)

**Planned:**
- Advanced analytics dashboard
- Premium content areas (if needed)
- Community features (if desired)
- Additional integrations

---

## 14. Design Deliverables Checklist

**Before Development:**
- [✓] Design system documented (colors, typography, spacing)
- [✓] Component library defined (buttons, cards, forms)
- [✓] Page layouts specified (all core pages)
- [✓] Responsive breakpoints defined
- [✓] Accessibility requirements documented
- [✓] Performance guidelines established

**During Development:**
- [✓] Visual design matches specifications
- [✓] Components reusable and consistent
- [✓] Responsive design tested on multiple devices
- [✓] Accessibility standards met (WCAG AA)
- [✓] Performance budgets maintained
- [✓] Browser compatibility verified

**After Development:**
- [✓] Style guide documentation for future reference
- [✓] Component library maintained
- [✓] Design patterns documented
- [✓] Brand guidelines updated (v1.3 Art Deco redesign)

---

## 15. Testing Checklist

### Visual Testing
- [✓] All pages render correctly on mobile, tablet, desktop
- [✓] Colors match design system
- [✓] Typography scales appropriately
- [✓] Images load and display correctly
- [✓] Spacing and alignment consistent
- [✓] Hover states work on desktop
- [✓] Touch targets appropriate size on mobile

### Functional Testing
- [✓] Navigation works on all devices
- [✓] Search functionality works
- [✓] Forms submit successfully
- [✓] Email signup integration works
- [✓] All internal links work
- [✓] All external links open correctly
- [✓] Contact form delivers messages

### Performance Testing
- [✓] Page load time < 3 seconds on 3G
- [✓] Lighthouse performance score 90+
- [✓] Images optimized and lazy loading
- [✓] No render-blocking resources
- [✓] Fonts load efficiently
- [✓] Cache-busting implemented

### Accessibility Testing
- [✓] Keyboard navigation works
- [✓] Screen reader testing completed
- [✓] Color contrast ratios meet AA standards
- [✓] Focus indicators visible
- [✓] ARIA labels appropriate
- [✓] Alt text on all images
- [✓] Form labels and errors accessible

### Browser Testing
- [✓] Chrome (latest)
- [✓] Firefox (latest)
- [✓] Safari (latest)
- [✓] Edge (latest)
- [✓] iOS Safari
- [✓] Chrome Mobile

### SEO Testing
- [✓] Meta tags on all pages
- [✓] Schema markup implemented
- [✓] XML sitemap generated
- [✓] Robots.txt configured
- [✓] URLs are SEO-friendly
- [✓] Redirects from old site work
- [✓] Google Search Console configured
- [✓] Google Analytics tracking

---

## 16. Page-Specific Design Specifications

As the site grows, detailed specifications for individual pages are maintained as separate documents to keep documentation manageable and focused.

**Existing Page Specifications:**
- **Blog Pages**: `blog_page_spec.md` (v1.1, November 27, 2025) - Updated to v1.2 with Art Deco colors (December 9, 2025)
- **Partnership Page**: `partnership_page_spec.md` (November 8, 2025) - Color references updated (December 9, 2025)

**Note:** Additional page specifications will be created as needed when new pages are designed and implemented. Each page spec references this design system (v1.3) for colors, typography, components, and layout patterns.

---

**Design Specification v1.3 Complete**
**Security Cocktail Hour Website - Art Deco Edition**
