# Security Cocktail Hour Podcast Website
## Requirements Document v1.0

**Date:** October 3, 2025  
**Project Owner:** Joe Patti  
**Document Status:** Draft for Review

---

## 1. Executive Summary

This document defines requirements for redesigning the Security Cocktail Hour podcast website. The current GoDaddy Website Builder platform is template-based with limited functionality and high cost. The new site must support the marketing strategy outlined in the comprehensive marketing plan while being cost-effective and maintainable.

### Primary Goals
1. Drive traffic to podcast episodes across all platforms (YouTube, Spotify, Apple Podcasts)
2. Serve as an information security resource for target audiences
3. Convey competence in both information security and podcasting
4. Raise profile of co-hosts Joe Patti and Adam Roth
5. Support email list growth through newsletter signups
6. Enable SEO-driven organic discovery

### Critical Constraints
- **Timeline:** Must migrate before GoDaddy contract renewal deadline
- **Hosting:** Must work with GoDaddy CPanel and other standard hosting providers
- **Maintainability:** Must be manageable by someone with HTML/CSS/basic JavaScript skills
- **Budget:** Cost-effective solution (minimize ongoing hosting costs)
- **Build Tool:** Will be built using Claude Code

---

## 2. Audience Requirements

### Target Personas (From Marketing Plan Section 1)

**Persona 1: Early- to Mid-Career Cybersecurity Professional**
- Age 22-35, entry to 7 years experience
- Needs broad cybersecurity knowledge beyond specialty
- Values technical depth with business context
- Limited time, consumes during commute (mobile-first)

**Persona 2: CISO/Manager**
- Age 35-50, 10+ years experience
- Needs strategic-level understanding
- Values business impact and ROI
- Time-constrained, wants efficient navigation

**Persona 3: Adjacent Professional**
- Age 25-45, security-adjacent roles
- Often intimidated by technical content
- Needs practical, accessible explanations
- Values clear takeaways

### Website Experience Requirements
- **Accessibility:** Content must be accessible to non-technical audiences
- **Navigation:** Clear paths to find relevant content for each persona
- **Mobile-First:** Optimized for mobile consumption (commute listening context)
- **Efficiency:** Easy to find specific topics/episodes quickly
- **Professional:** Conveys competence and credibility

---

## 3. Functional Requirements

### 3.1 Core Pages

**IMPORTANT:** All pages and functionality from the current site (https://securitycocktailhour.com) must be preserved in the new design.

#### 3.1.1 Homepage
**Purpose:** Convert visitors to podcast listeners and email subscribers

**Must Have:**
- Clear, compelling value proposition above the fold
- Visual identity establishing professionalism
- Latest episode feature with prominent play/listen buttons
- Email signup form with newsletter lead magnet
- Navigation to all major sections
- Social proof (listener count, review highlights, or testimonials)
- Clear calls-to-action (CTA): Listen, Subscribe, Sign Up

**Should Have:**
- Featured episodes or series
- Host photos with brief credentials
- Recent blog posts or resources preview
- Social media feed integration

**Nice to Have:**
- Rotating banner showcasing different aspects of podcast
- Stats/metrics dashboard (total episodes, guest count)
- Listener testimonials carousel

#### 3.1.2 Episode Library
**Purpose:** Enable discovery and consumption of past episodes

**Must Have:**
- List/grid view of all episodes with cover art
- Episode title, guest name, date, duration
- Episode description/summary (SEO-optimized)
- Direct links to all listening platforms (YouTube, Spotify, Apple Podcasts)
- Search functionality (by title, guest, topic)
- Filter/sort capabilities (by date, topic, guest type)
- Pagination or infinite scroll
- Individual episode pages with full show notes

**Should Have:**
- Category/topic tags on episodes
- "Related episodes" suggestions
- Guest bio snippets
- Listen time estimates
- Download options (if applicable)

**Nice to Have:**
- Advanced search (by keyword in show notes)
- Saved/favorite episodes (requires user accounts)
- Playback progress tracking
- Series/playlist groupings

#### 3.1.3 Individual Episode Pages
**Purpose:** SEO-optimized detailed episode information

**CLARIFICATION (Oct 3, 2025):** Only a small number of episodes currently have transcripts on the site. This needs to be expanded to all episodes over time. The MVP must have the CAPABILITY to display transcripts, but not all episodes need transcripts at launch.

**Must Have (From Marketing Plan Section 3):**
- Target keyword in first 100 words
- Detailed episode highlights with timestamps
- Full episode description (800-1200 words)
- Guest bio with credentials and links
- Resources mentioned in episode with links
- Call-to-action for email signup
- Social sharing buttons
- Links to all listening platforms
- Episode metadata (date, duration, category)
- Proper schema markup for podcasts

**Should Have:**
- Embedded audio/video player
- Episode transcript (SEO value, accessibility)
  - **Note:** Transcript capability required in MVP, but only small number of episodes currently have transcripts
  - Template must support transcripts (expandable/collapsible section)
  - Easy to add transcripts to additional episodes post-launch
  - Display gracefully when transcript not available
- Chapter markers/timestamps for navigation
- Related episodes section
- Comments section or discussion area

**Nice to Have:**
- Key quotes pulled out as highlights
- Visual chapter navigation
- Downloadable resources mentioned in episode
- Guest social media links

#### 3.1.4 About Page
**Purpose:** Establish credibility and host profiles

**Must Have:**
- Mission statement and podcast value proposition
- Detailed host bios (Joe Patti and Adam Roth)
- Professional host photos
- Credentials and experience highlights
- What makes the podcast unique/different
- Contact information or link to contact page

**Should Have:**
- Podcast origin story
- Behind-the-scenes photos
- Awards/recognition
- Guest testimonials
- Stats/achievements

**Nice to Have:**
- Video introduction from hosts
- Timeline of podcast journey
- FAQ section
- Press mentions/media kit link

#### 3.1.5 Resources Page
**Purpose:** Provide additional value and establish expertise

**Must Have:**
- Curated tools for information security professionals
- Educational guides and recommended reading
- Links to communities and organizations (ISACA, ISC2)
- Organized by category or audience type
- Brief descriptions for each resource

**Should Have:**
- Cybersecurity career roadmap content
- Tool recommendations by role
- Regular updates/new resources highlighted
- Search/filter functionality

**Nice to Have:**
- User-submitted resources
- Ratings or reviews of resources
- Downloadable resource guides
- Video tutorials or demos

#### 3.1.6 Contact Page
**Purpose:** Enable guest submissions and partnerships

**Must Have:**
- Contact form with fields:
  - Name
  - Email
  - Subject/Purpose (dropdown: Guest Submission, Partnership, General Inquiry, Press)
  - Message
- Clear expectations (response time)
- Alternative contact methods (email address, social media)
- Spam protection (CAPTCHA or similar)

**Should Have:**
- Guest submission guidelines/criteria
- Partnership opportunities description
- FAQ section
- Direct email addresses for specific inquiries

**Nice to Have:**
- Calendar integration for booking
- File upload capability (for press kits, etc.)
- Social media direct message links

#### 3.1.7 Blog/Articles Section
**Purpose:** Content multiplication strategy and SEO

**Must Have:**
- Blog post listing page
- Individual blog post pages with SEO optimization
- Categories and tags
- Social sharing buttons
- Related posts suggestions
- Author attribution (Joe or Adam)

**Should Have:**
- Search functionality
- RSS feed
- Comments section
- Newsletter signup CTA in each post

**Nice to Have:**
- Multi-author support
- Content series/collections
- Reader analytics (reading time, popular sections)

### 3.1A Additional Pages from Current Site

**CRITICAL:** The following pages exist on the current site and must be included in the new design:

#### 3.1A.1 Afterparties Page
**Purpose:** Special bonus content episodes (unboxings, events, behind-the-scenes)

**Current Functionality:**
- Special episodes separate from main podcast feed
- Video content (e.g., unboxing episodes, boxing match event)
- Different format from regular episodes
- Listed as separate section in navigation

**Must Have:**
- Dedicated page for afterparty episodes
- Video embedding capability
- Episode cards similar to main episodes
- Clear differentiation from main episodes
- Links to video platforms (YouTube primarily)

#### 3.1A.2 Store Pages
**Purpose:** E-commerce for podcast merchandise

**Current Implementation:**
- Two separate store pages:
  - "Store | Clothing" - apparel and clothing items
  - "Store | Pens, Mugs & More" - accessories and other merchandise

**Must Have for MVP:**
- Links to external store platform (likely Printful, Teespring, or similar)
- Product showcase if hosting externally
- OR implement simple e-commerce if desired

**Decision Needed:** 
- Keep external store links (simplest)?
- Implement basic e-commerce on new site?
- Integrate with existing store platform?

**Recommendation:** For 14-day timeline, maintain external store links. Can enhance later.

#### 3.1A.3 Support Us / Donation Page
**Purpose:** Enable direct financial support from listeners

**Current Functionality:**
- Stripe payment integration
- Multiple donation tiers: $25, $50, $100, $500, $1000
- Sponsorship inquiry messaging
- Clear value proposition ("Love the podcast but don't need more clutter")
- Disclosure: "All donations are final"

**Must Have:**
- Stripe integration for payments
- Multiple donation amount options
- Clear messaging about support
- Sponsorship contact information
- Legal disclosure about donations

**Technical Requirements:**
- Stripe API integration or embedded payment buttons
- Secure payment processing (HTTPS required)
- Thank you confirmation page
- Email confirmation to donor (via Stripe)

#### 3.1A.4 Consulting Page
**Purpose:** Promote consulting services offered by hosts

**Current Functionality:**
- Information about security consulting services
- Contact method for inquiries

**Must Have:**
- Description of consulting services offered
- Host credentials and expertise
- Contact form or email for inquiries
- Testimonials or case studies (if available)

**Should Have:**
- Service packages or offerings
- Industries served
- Contact CTA

#### 3.1A.5 Co-Host Appearances Page
**Purpose:** Showcase hosts' appearances on other podcasts and media

**Current Functionality:**
- List of hosts' guest appearances on other shows
- Links to external content

**Must Have:**
- List/grid of appearances
- Links to external shows/episodes
- Date and show information
- Description of topics discussed

**Should Have:**
- Filterable by host (Joe or Adam)
- Chronological listing
- Embedded media players where possible

#### 3.1A.6 Bios Page
**Purpose:** Detailed host biographies

**Current Functionality:**
- Extended biographies for both hosts
- Professional backgrounds
- Credentials and expertise

**Must Have:**
- Professional photos of both hosts
- Detailed career histories
- Areas of expertise
- Professional credentials/certifications
- Contact information or social links

**Should Have:**
- Downloadable professional headshots
- Media kit information
- Speaking topics

**Note:** This is different from the About page - more detailed professional bios

#### 3.1A.7 Gallery Page
**Purpose:** Photo gallery of events, guests, behind-the-scenes

**Current Functionality:**
- Image gallery
- Photos from recordings, events, conferences

**Must Have:**
- Photo grid/gallery layout
- Image lightbox for viewing
- Captions/descriptions for photos
- Mobile-responsive image viewing

**Should Have:**
- Categories/albums (by event, guest, year)
- Social media integration
- Download capability for high-res images (for guests/press)

#### 3.1A.8 Episode Organization Structure
**Current Implementation:**
Episodes are organized into groups of 10:
- Episodes 61-70 (current)
- Episodes 51-60
- Episodes 41-50
- Episodes 31-40
- Episodes 21-30
- Episodes 11-20
- Episodes 1-10

**Must Have:**
- Maintain this grouping structure OR
- Implement pagination that displays episodes in groups
- Clear navigation between episode groups
- "All Episodes" page or library

**Recommendation:** 
- Implement standard episode library with pagination
- Use decade grouping as secondary navigation if desired
- Prioritize searchable, filterable episode library

#### 3.1A.9 Individual Episode Transcript Pages
**Current Implementation:**
- Separate pages for episode transcripts (e.g., /transcript-ep-59)
- Full text transcripts of episodes

**Must Have:**
- Full transcript for each episode
- Either integrated into episode page OR separate transcript pages
- Searchable text
- Timestamped if possible

**Recommendation:**
- Integrate transcripts into episode detail pages as expandable sections
- Improves SEO and user experience
- Maintains single URL per episode

#### 3.1A.10 Contact Page (Expanded Requirements)
**Current Functionality:**
- Contact email: feedback@securitycocktailhour.com
- Likely contact form
- Social media: @SecCocktailHour on Twitter/X

**Must Have:**
- Contact form with fields:
  - Name
  - Email  
  - Subject/Purpose (Guest Submission, Partnership, Consulting, Sponsorship, General)
  - Message
- Display contact email
- Social media links
- Response time expectations

**Should Have:**
- reCAPTCHA or spam protection
- Auto-responder confirmation
- Separate paths for different inquiry types

### 3.1B Platform Integration Requirements

**Podcast Platforms (from current site):**

**Must Have Links To:**
- YouTube: https://youtube.com/@SecCocktailHour
- Spotify: https://open.spotify.com/show/7gWweI6mL1oVRU5gKNzzTy
- Apple Podcasts: https://podcasts.apple.com/us/podcast/security-cocktail-hour/id1679376200
- Amazon Music: https://music.amazon.com/podcasts/d11e431a-f7b1-4bb0-8671-024afce9ade6/security-cocktail-hour
- RSS Feed: https://anchor.fm/s/ed0bcf14/podcast/rss

**Note:** Buzzsprout appears to be the podcast hosting platform (securitycocktailhour.buzzsprout.com)

**Social Media:**
- Twitter/X: @SecCocktailHour
- Contact email: feedback@securitycocktailhour.com

### 3.1C Cookie Policy & Privacy

**Current Implementation:**
- Cookie notice: "We use cookies to analyze website traffic and optimize your website experience"
- Privacy policy acceptance
- Data aggregation disclosure

**Must Have:**
- Cookie consent banner/notice
- Privacy policy page
- Terms of service page (if needed for donations/store)
- GDPR compliance (cookie consent)
- Link to privacy policy in footer

**Technical Requirements:**
- Cookie consent management
- Google Analytics opt-in/opt-out
- Data privacy compliance

### 3.2 Email Capture System (From Marketing Plan Section 3)

**Must Have:**
- Email signup forms on every page
- Prominent header or sidebar signup widget
- Lead magnet: Newsletter positioning with clear value proposition:
  - Early access to episode announcements
  - Exclusive guest insights
  - Curated security resources
  - Career tips and industry analysis
- Integration with email marketing platform (likely Mailchimp)
- GDPR-compliant consent checkbox
- Confirmation/double opt-in flow
- Thank you page after signup

**Should Have:**
- Exit-intent popup (desktop)
- Scroll-triggered inline forms
- A/B testing capability for form designs
- Multiple lead magnet options for different audiences

**Nice to Have:**
- Gamification (progress bars, achievement badges)
- Referral incentives
- Subscriber count display
- Preview of newsletter content

### 3.3 Navigation & User Experience

**Must Have:**
- Clear, consistent navigation menu across all pages
- Mobile-responsive hamburger menu
- Breadcrumb navigation on deep pages
- Footer with sitemap links
- Search functionality (site-wide)
- Prominent "Listen Now" or "Subscribe" buttons

**Should Have:**
- Sticky header navigation (stays visible while scrolling)
- Multi-level navigation for large content library
- Quick links to latest episode
- Skip navigation links (accessibility)

**Nice to Have:**
- Personalized navigation based on user behavior
- Recently viewed episodes
- Customizable user dashboard

### 3.4 Error Handling

**Must Have:**
- Custom 404 error page
- User-friendly error message
- Navigation options (links to homepage, episodes page)
- Automatic redirect to homepage after countdown
- Consistent site design (header, footer)
- Prevents showing server default error pages

**Should Have:**
- Search box on 404 page
- List of popular pages
- Sitemap link

### 3.5 Integration Requirements

**Must Have:**
- Google Analytics integration
- Google Search Console integration
- Email marketing platform integration (Mailchimp or selected platform)
- Social media sharing buttons
- RSS feed for podcast
- Podcast platform links (YouTube, Spotify, Apple Podcasts)

**Should Have:**
- Social media feeds (LinkedIn, Twitter/X)
- YouTube video embed capability
- Spotify episode embed
- Newsletter archive integration
- Calendar integration for events

**Nice to Have:**
- CRM integration (future)
- Marketing automation platform
- Podcast analytics platform (Chartable/Podtrac)
- Community forum integration

---

## 4. Technical Requirements

### 4.1 Hosting & Deployment (Critical Constraint)

**Must Have:**
- Compatible with GoDaddy CPanel hosting
- Compatible with other standard web hosts (shared hosting)
- Static site generation OR simple PHP/database setup
- No specialized hosting requirements (no Node.js servers, etc.)
- Deployable via FTP/SFTP or file manager
- Works with standard Apache/nginx web servers

**Should Have:**
- Automated deployment process
- Easy backup and restoration
- Development and production environment separation

**Nice to Have:**
- Git-based deployment
- CI/CD pipeline
- Staging environment

### 4.2 Technology Stack

**Constraints:**
- Must be maintainable by someone with HTML/CSS/basic JavaScript skills
- Should avoid complex build processes if possible
- Must run on standard shared hosting

**Recommended Approach:**
- Static site generator (Jekyll, Hugo, or 11ty) OR
- Simple PHP-based CMS (if database needed) OR
- Hand-coded HTML/CSS/JS with templating

**Must Have:**
- HTML5 semantic markup
- CSS3 (responsive design)
- Vanilla JavaScript (no heavy frameworks required)
- Optional: Simple build process (if using static site generator)

**Should Have:**
- Template system for consistent design
- Content management approach that doesn't require database
- Version control friendly (Git)

### 4.3 Performance Requirements (From Marketing Plan Section 3)

**Must Have:**
- Fast page load times (< 3 seconds on 3G)
- Optimized images (WebP with fallbacks, lazy loading)
- Minified CSS and JavaScript
- Mobile-responsive design (works on all screen sizes)
- Lighthouse score: 90+ performance, 100 accessibility
- No render-blocking resources

**Should Have:**
- Content Delivery Network (CDN) for static assets
- Browser caching configured
- Gzip/Brotli compression
- Preloading of critical resources

**Nice to Have:**
- Service worker for offline capability
- Progressive Web App (PWA) features
- Image optimization pipeline

### 4.4 SEO Requirements (From Marketing Plan Section 3)

**Must Have:**
- Proper podcast schema markup implementation (Schema.org)
- XML sitemap for episodes and pages
- Robots.txt file
- Clean URL structure (human-readable, keyword-rich)
- SSL certificate (HTTPS)
- Meta titles and descriptions (unique per page)
- Open Graph tags for social sharing
- Twitter Card tags
- Canonical URLs to prevent duplicate content
- 301 redirects from old GoDaddy site URLs

**Should Have:**
- Structured data for articles, authors, organization
- Internal linking strategy
- Alt text on all images
- Heading hierarchy (H1, H2, H3)
- Breadcrumb schema markup

**Nice to Have:**
- AMP versions of pages
- hreflang tags (if international)
- FAQ schema markup
- VideoObject schema for video content

### 4.5 Security Requirements

**Must Have:**
- SSL/TLS certificate (HTTPS)
- Form spam protection (CAPTCHA or honeypot)
- SQL injection prevention (if using database)
- XSS protection
- CSRF tokens on forms
- Secure headers (Content-Security-Policy, X-Frame-Options)
- Regular security updates

**Should Have:**
- Rate limiting on forms
- Email validation and sanitization
- File upload restrictions (if implemented)
- Security monitoring

### 4.6 Accessibility Requirements (WCAG 2.1 AA)

**Must Have:**
- Semantic HTML structure
- Keyboard navigation support
- Alt text for all images
- Color contrast ratios meeting AA standards
- Skip navigation links
- ARIA labels where appropriate
- Focus indicators on interactive elements
- Accessible forms (labels, error messages)

**Should Have:**
- Transcript availability for audio/video
- Resizable text without breaking layout
- Screen reader testing
- Captions for video content

### 4.7 Browser & Device Support

**Must Have:**
- Modern browsers (Chrome, Firefox, Safari, Edge) - last 2 versions
- Mobile browsers (iOS Safari, Chrome Mobile)
- Responsive design (320px to 2560px+ width)
- Touch-friendly interface elements

**Should Have:**
- Graceful degradation for older browsers
- Progressive enhancement approach
- Tablet-optimized layouts

---

## 5. Content Requirements

### 5.1 Existing Content Migration

**Must Have:**
- Migrate all existing episodes from current site
- Preserve existing URLs where possible, or implement redirects
- Transfer all images, audio/video embeds
- Maintain episode descriptions and show notes

**Should Have:**
- Improve SEO of existing content during migration
- Add missing metadata to older episodes
- Optimize images during transfer

### 5.2 Content Management

**Must Have:**
- Easy process to add new episodes (template-based)
- Image upload and management
- Edit existing content without technical knowledge
- Preview before publishing

**Should Have:**
- Draft/published status for episodes
- Scheduling future publications
- Bulk operations (tagging, categorization)
- Content versioning

**Nice to Have:**
- Multi-user support (Joe and Adam)
- Editorial workflow (draft → review → publish)
- Content analytics dashboard

### 5.3 Episode Template Requirements (From Marketing Plan)

Each episode page must support:
- Episode number and title
- Publication date
- Duration
- Guest information (name, bio, credentials, links)
- Episode description (with keywords)
- Segmented format with timestamps:
  - Minutes 0-5: Universal Value Hook
  - Minutes 6-25: Technical Deep Dive
  - Minutes 26-35: Strategic Business Context
  - Minutes 36-45: Practical Applications
- Resources mentioned with links
- Listening platform links
- Social sharing options
- Email signup CTA
- Related episodes
- Categories/tags

---

## 6. Design Requirements

### 6.1 Visual Identity

**Must Have:**
- Professional, modern design aesthetic
- Consistent with existing podcast branding (colors, logo)
- Conveys competence in security and podcasting
- Clear visual hierarchy
- Legible typography (accessibility)

**Should Have:**
- Custom graphics and iconography
- Professional photography of hosts
- Consistent cover art treatment
- Dark mode option (popular with tech audience)

### 6.2 Branding Elements

**Must Have:**
- Podcast logo prominently displayed
- Consistent color scheme
- Typography system (headings, body, code)
- Button and link styles
- Form design patterns

**Should Have:**
- Custom illustrations
- Icon set for categories/topics
- Graphic templates for episode images
- Style guide documentation

### 6.3 User Interface Patterns

**Must Have:**
- Clear CTAs (contrasting colors, good size)
- Consistent card designs for episodes
- Form designs with good UX
- Error and success states
- Loading indicators
- Pagination controls

**Should Have:**
- Smooth transitions and animations (subtle)
- Interactive elements (hover states, etc.)
- Micro-interactions for engagement
- Empty states (no results, etc.)

---

## 7. Analytics & Tracking Requirements

### 7.1 Google Analytics (From Marketing Plan Section 9)

**Must Have:**
- Google Analytics 4 (GA4) implementation
- Page view tracking
- Event tracking:
  - Email signups
  - Podcast platform clicks
  - Social media clicks
  - Resource downloads
  - Contact form submissions
- Traffic source tracking
- User behavior flow

**Should Have:**
- Custom dimensions (episode, guest, category)
- Goal conversion tracking
- E-commerce tracking (if applicable)
- Enhanced link attribution

### 7.2 Google Search Console

**Must Have:**
- Property verification
- Sitemap submission
- Search performance monitoring
- Index coverage tracking
- Mobile usability reports

### 7.3 Additional Tracking

**Should Have:**
- Heatmap tracking (Hotjar or similar)
- Form analytics
- Error logging
- Performance monitoring (Core Web Vitals)

**Nice to Have:**
- A/B testing platform integration
- User session recording
- Conversion funnel analysis

---

## 8. Content Marketing Support (From Marketing Plan Section 4)

### 8.1 Content Multiplication

**Must Have:**
- Blog post creation from episode transcripts
- Quote extraction capability
- Social media sharing functionality
- Embeddable audio/video players

**Should Have:**
- Automated content generation workflows
- Social media preview cards
- Downloadable quote graphics
- Press kit/media kit page

### 8.2 Social Media Integration

**Must Have:**
- Social sharing buttons on all content
- Open Graph and Twitter Card metadata
- Social media links in header/footer
- Share count display (optional)

**Should Have:**
- Click-to-tweet functionality for quotes
- LinkedIn article integration
- YouTube video embeds
- Social media feed displays

---

## 9. Future Scalability & Nice-to-Haves

### 9.1 Phase 2 Features (Post-Launch)

- User accounts and authentication
- Commenting system
- Community forum
- Personalized recommendations
- Saved episodes/playlists
- Advanced search with filters
- Multiple language support
- Premium content areas

### 9.2 Monetization Support (Future)

- Sponsorship banner placement
- Affiliate link management
- Premium membership tiers
- Digital product sales
- Course platform integration

### 9.3 Advanced Features

- Podcast player with playlist support
- Interactive transcripts with search
- Guest directory with profiles
- Event calendar for webinars/appearances
- Job board for cybersecurity roles
- Resource rating/review system

---

## 10. Success Criteria

### 10.1 Launch Requirements (Minimum Viable Product)

**CLARIFICATIONS FROM JOE (Oct 3, 2025):**
- All 60-70 episodes to be migrated at launch
- NO decade grouping needed (was platform limitation) - unified library only
- Store: Single page with external links (two stores was platform limitation)
- Support Us page: NOT critical for Day 1 - can launch in Phase 2

**Must Be Complete Before Day 1 Launch:**

**Core Functionality:**
- [ ] **Homepage** with featured/latest episodes
- [ ] **Unified Episode Library** (/episodes)
  - All 60-70 episodes migrated
  - Search functionality
  - Filter by category/topic
  - Sort options (newest, oldest, relevant)
  - NO decade grouping (platform limitation eliminated)
  - Pagination (20-30 episodes per page)
- [ ] **Individual Episode Pages** (/episodes/[slug])
  - Full show notes and descriptions
  - Guest information with bio
  - Transcript capability (expandable section that shows/hides)
    - **Clarification:** Only small number of episodes have transcripts currently
    - Migrate existing transcripts at launch
    - Template must support adding transcripts easily post-launch
    - Display gracefully when transcript not available
  - All 60-70 episodes migrated (even if some lack transcripts)
  - Links to all podcast platforms
  - Social sharing buttons
  - Chapter markers/timestamps
  - Resources mentioned with links
  - Email signup CTA
  - Related episodes
- [ ] **About/Bios Page**
  - Podcast mission and story
  - Detailed host bios (Joe and Adam)
  - Professional photos (high-res available)
  - Credentials and expertise
  - Contact information
- [ ] **Contact Page**
  - Contact form (Guest Submission, Partnership, Consulting, Sponsorship, General, Press)
  - feedback@securitycocktailhour.com displayed
  - Social media links
  - reCAPTCHA protection
- [ ] **Resources Page**
  - Curated tools and guides for infosec professionals
  - Educational resources
  - Professional organizations (ISACA, ISC2, etc.)
  - Organized by category
  - Email signup CTA
- [ ] **Store Page** (simplified)
  - Single page with links to both external stores
  - Clear CTAs to clothing and accessories stores
  - Simple implementation (no e-commerce)
- [ ] **Privacy Policy** and **Terms of Service**
- [ ] **Cookie Consent Banner**
- [ ] **Custom 404 Error Page**
  - User-friendly error message
  - Automatic redirect to homepage (5-second countdown)
  - Manual navigation buttons (Homepage, Episodes)
  - Consistent site design
  - Configured in hosting (cPanel Error Pages)

**New Functionality (From Marketing Plan):**
- [ ] **Email Capture Forms** (Mailchimp integration)
  - Homepage signup
  - Footer signup (every page)
  - Episode page sidebar signup
  - Resources page signup
  - Thank you/confirmation page
  - Double opt-in flow
  - GDPR-compliant consent
- [ ] **Enhanced SEO**
  - Schema.org podcast markup
  - Optimized episode pages (800-1200 words)
  - XML sitemap
  - Clean URL structure
  - Meta tags and Open Graph

**Technical Requirements:**
- [ ] Mobile-responsive design (all devices)
- [ ] Fast performance (< 3 second load)
- [ ] Google Analytics implemented
- [ ] All podcast platform links working
- [ ] All forms functional and tested
- [ ] Social sharing working
- [ ] Accessibility (WCAG AA)
- [ ] 301 redirects from old site URLs
- [ ] SSL certificate (HTTPS)

**Can Defer to Phase 2 (First Week Post-Launch):**
- Support Us page with Stripe donations
- Afterparties page
- Consulting page
- Co-Host Appearances page
- Gallery page
- Blog/articles section

### 10.2 Success Metrics (From Marketing Plan Section 9)

**Website Goals (Month 1-3):**
- 500-1,000 monthly visitors
- 2-3% email signup conversion rate
- < 3 second page load time
- 90+ Lighthouse performance score
- 100 Lighthouse accessibility score

**Website Goals (Month 4-12):**
- 1,000-2,000 monthly visitors
- 3-5% email signup conversion rate
- Organic search traffic growth
- Increased time on site
- Lower bounce rate

---

## 11. Migration Strategy

### 11.1 Pre-Migration

**Must Complete:**
- Audit current GoDaddy site content inventory
- Document all existing URLs
- Export all content (episodes, images, text)
- Test new hosting environment
- Set up development environment
- Create URL mapping for redirects

### 11.2 Migration Process

**Must Complete:**
- Build new site in development environment
- Import and optimize content
- Test all functionality
- Set up redirects from old URLs
- Configure DNS/hosting
- SSL certificate installation
- Test on new hosting
- Deploy to production

### 11.3 Post-Migration

**Must Complete:**
- Submit sitemap to search engines
- Monitor for broken links (404 errors)
- Verify redirects working
- Check analytics tracking
- Test forms and integrations
- Monitor performance metrics
- Cancel GoDaddy Website Builder service

---

## 12. Maintenance & Support Requirements

### 12.1 Ongoing Maintenance

**Regular Tasks:**
- Add new episodes weekly
- Update blog/resources as needed
- Monitor and respond to contact forms
- Review analytics monthly
- Security updates as needed
- Content optimization based on SEO data
- Backup site regularly

### 12.2 Documentation Needs

**Must Create:**
- Content management guide (how to add episodes)
- Troubleshooting guide
- Hosting setup instructions
- Backup and recovery procedures
- Style guide for consistent content
- SEO checklist for new content

---

## 13. Open Questions & Decisions Needed

### 13.1 Technology Stack Decision

**DECISION: Static Site Generator**
- Will use static site generator (Hugo or 11ty - to be selected by Claude Code based on requirements)
- Rationale: Fast, secure, version-controlled, no database required, works perfectly with cPanel hosting
- Deployment: Build locally, upload via FTP/SFTP to GoDaddy cPanel
- Content management: Markdown files for episodes and blog posts

### 13.2 Email Marketing Platform

**DECISION: Mailchimp Free Tier**
- Starting with free tier (up to 500 subscribers)
- Rationale: No cost to start, familiar interface, good integration options
- Will graduate to paid tier as list grows beyond 500 subscribers

### 13.3 Design Approach

**DECISION: Use Existing Podcast Branding**

**Brand Asset:**
- Logo: Circular badge design with martini glass, security keyhole, and spotlight effect
- Design aesthetic: Retro/vintage, professional but approachable
- Visual metaphor: Security meets cocktail hour

**Color Palette (from logo):**
- Primary Red: #C8534B (for headers, CTAs, accent elements)
- Dark Blue: #1E4D8B (for text, backgrounds, depth)
- Light Blue/Cyan: #3BA0D4 (for highlights, links, interactive elements)
- Lighter Cyan: #81C9E8 (for gradients, subtle backgrounds)
- Olive Green: #7BA956 (for accents, success states)
- Black: #000000 (for text, borders)
- White/Cream: #FFFFFF (for backgrounds, text on dark)

**Design Principles:**
- Maintain retro/vintage aesthetic from logo
- Clean, bold graphics
- Professional yet accessible
- Not overly corporate
- Tech-savvy but welcoming to non-technical audiences

### 13.4 Hosting Selection

**DECISION: GoDaddy cPanel Hosting**

**Rationale:**
- Simplifies domain management (no transfer needed)
- Familiar environment
- Avoids migration complexity
- Cost-effective

**Requirements:**
- Switch from GoDaddy Website Builder to cPanel hosting
- SSL certificate included or easy to add (Let's Encrypt)
- Support for static file hosting
- FTP/SFTP access for deployment
- .htaccess support for redirects and optimization

**Timeline Note:** 
- Current contract renewal in 14 days
- Will investigate month-to-month extension option if needed
- Target: Complete migration before renewal deadline

---

## 14. Project Timeline Estimate

**CRITICAL: 14-Day Deadline**
Current GoDaddy contract renewal is in 14 days. Target completion before renewal deadline. Investigating month-to-month extension option as contingency.

### Days 1-5: Planning & Setup
- ✅ Requirements finalized
- ✅ Technology stack selected (Static site generator)
- ✅ Hosting decision made (GoDaddy cPanel)
- ✅ Email platform selected (Mailchimp)
- ✅ Brand assets documented (logo and colors)
- Day 1-2: Set up development environment with Claude Code
- Day 2-3: Export content from current site
- Day 3-4: Create design system and wireframes
- Day 4-5: Choose specific static site generator and set up project structure

### Days 6-10: Development
- Day 6-7: Implement core page templates (Home, About, Contact, Resources)
- Day 7-8: Build episode library and episode detail pages
- Day 8-9: Implement navigation, search, and email capture
- Day 9-10: Responsive design implementation and content migration

### Days 11-14: SEO, Testing & Launch
- Day 11: Implement schema markup and SEO elements
- Day 11-12: Set up Google Analytics, Search Console, redirects
- Day 12-13: Performance optimization and cross-browser testing
- Day 13: Build and deploy to GoDaddy cPanel
- Day 14: Final testing, monitoring, and go-live

**Contingency:** 
- If timeline slips, pursue month-to-month extension of current contract
- Can defer nice-to-have features to post-launch
- MVP approach: Launch with essential features, enhance later

**Total Time:** 14 days (aggressive but achievable with focused effort)

---

## 15. Budget Estimate

### One-Time Costs
- Domain transfer/setup (if needed): $0-15
- SSL certificate (if not included): $0 (Let's Encrypt free)
- Design assets (if hiring designer): $0-500
- Development tools/licenses: $0-50
- Migration services (if needed): $0

**Estimated One-Time Total:** $0-565

### Recurring Costs (Monthly)
- Web hosting: $5-20/month
- Email marketing platform: $0-15/month (starting with free tier)
- Domain registration: $1-2/month ($12-24/year)
- Analytics tools: $0 (using free tiers)
- CDN (optional): $0-10/month

**Estimated Monthly Total:** $6-47/month

**Comparison:** Current GoDaddy Website Builder likely $20-40/month, so savings expected.

---

## 16. Risk Assessment

### High Priority Risks

**Risk 1: Timeline Pressure**
- Issue: Contract renewal deadline approaching
- Mitigation: Start immediately, use MVP approach, defer nice-to-haves
- Contingency: Extend current contract by 1 month if needed

**Risk 2: Technical Complexity**
- Issue: Joe unfamiliar with modern frameworks, first time using Claude Code
- Mitigation: Choose simple technology stack, thorough documentation, phased approach
- Contingency: Seek additional technical help if needed

**Risk 3: Content Migration**
- Issue: Large volume of episodes to migrate
- Mitigation: Create migration scripts/tools, prioritize recent episodes
- Contingency: Launch with subset of episodes, migrate remainder post-launch

**Risk 4: SEO Impact**
- Issue: URL changes could impact search rankings
- Mitigation: Implement comprehensive redirects, maintain URL structure where possible
- Contingency: Monitor search rankings closely, adjust redirects as needed

### Medium Priority Risks

**Risk 5: Hosting Compatibility**
- Issue: Chosen solution doesn't work well with selected hosting
- Mitigation: Test on hosting environment before full build
- Contingency: Switch hosting provider if necessary

**Risk 6: Email Platform Integration**
- Issue: Integration more complex than expected
- Mitigation: Start with simple form-to-email, enhance later
- Contingency: Use third-party form services (Typeform, etc.)

---

## 17. Next Steps

### Immediate Actions
1. **Review and approve** this requirements document
2. **Make key decisions** from Section 13 (technology stack, hosting, email platform)
3. **Set up** development environment with Claude Code
4. **Create** basic design mockups/wireframes
5. **Begin** technical implementation

### Before Starting Development
- [ ] Requirements document approved
- [ ] Technology stack selected
- [ ] Hosting provider chosen
- [ ] Email marketing platform selected
- [ ] Development environment ready
- [ ] Content export completed from current site
- [ ] Design direction established
- [ ] Claude Code setup and tested

---

## Appendix A: Reference Documents

- **Source:** Security Cocktail Hour Marketing Plan v1.0 (October 3, 2025)
- **Key Sections:**
  - Section 1: Target Audience Strategy
  - Section 3: Website & SEO Strategy
  - Section 11: 90-Day Implementation Roadmap
  - Section 16: Recommended Immediate Next Steps

## Appendix B: Current Site Inventory

**Site URL:** https://securitycocktailhour.com  
**Hosting Platform:** GoDaddy Website Builder (to be migrated)  
**Podcast Host:** Buzzsprout (securitycocktailhour.buzzsprout.com)

### Complete Page List

**Main Navigation Pages:**
1. Home (/)
2. Episodes 61-70 (/episodes-61-70) - Most recent
3. Episodes 51-60 (/episodes-51-60)
4. Episodes 41-50 (/episodes-41-50)
5. Episodes 31-40 (/episodes-31-40)
6. Episodes 21-30 (/episodes-21-30)
7. Episodes 11-20 (/episodes-11-20)
8. Episodes 1-10 (/episodes-1-10)
9. Afterparties (/afterparties)
10. Store | Clothing (/store or similar - external link?)
11. Store | Pens, Mugs & More (/store-2 or similar - external link?)
12. Support Us (/support-us)
13. Consulting (/consulting)
14. Co-Host Appearances (/guest-appearances or /co-host-appearances)
15. Bios (/bios)
16. Gallery (/gallery)
17. Contact (/contact)

**Additional Pages:**
18. Individual Episode Transcript pages (/transcript-ep-##)
19. Privacy Policy (assumed, for cookie compliance)
20. Terms of Service (assumed, for donations/store)

### Current Features Inventory

**Homepage Features:**
- Hero section with podcast description
- Featured/latest episodes (appears to show 3 episodes)
- Links to all major podcast platforms
- Call-to-action to visit store
- Navigation menu
- Footer with links
- Cookie consent notice

**Episode Features:**
- Episode cover images
- Episode titles and descriptions
- Guest information
- Links to listen on multiple platforms
- Full transcripts (separate pages)
- Organized in groups of 10 episodes

**Afterparties Features:**
- Special bonus content section
- Video content (YouTube embeds likely)
- Unboxing episodes
- Special events (e.g., boxing match)
- Different from regular episode format

**Store Features:**
- Two separate stores:
  - Clothing/apparel
  - Accessories (pens, mugs, etc.)
- External platform integration (likely Printful, Teespring, or similar)

**Support Us Features:**
- Stripe payment integration
- Multiple donation tiers: $25, $50, $100, $500, $1000
- Sponsorship inquiry information
- Clear value messaging
- Payment buttons for each tier
- Donation policy disclosure

**Consulting Features:**
- Service description
- Contact information
- Host expertise presentation

**Co-Host Appearances Features:**
- List of external podcast/media appearances
- Links to external content
- Show/episode information
- Topics discussed

**Bios Features:**
- Detailed host biographies
- Professional backgrounds
- Credentials and expertise
- Professional photos

**Gallery Features:**
- Photo gallery
- Event photos
- Guest photos
- Behind-the-scenes content

**Contact Features:**
- Contact form (likely)
- Email: feedback@securitycocktailhour.com
- Social media: @SecCocktailHour (Twitter/X)
- Multiple inquiry types supported

**Technical Integrations:**
- Buzzsprout (podcast hosting)
- Stripe (payment processing)
- Google Analytics (assumed for "analyze website traffic")
- Cookie consent system
- Social media embeds
- Video embeds (YouTube)

**Podcast Platform Links:**
- YouTube: https://youtube.com/@SecCocktailHour
- Spotify: https://open.spotify.com/show/7gWweI6mL1oVRU5gKNzzTy
- Apple Podcasts: https://podcasts.apple.com/us/podcast/security-cocktail-hour/id1679376200
- Amazon Music: https://music.amazon.com/podcasts/d11e431a-f7b1-4bb0-8671-024afce9ade6/security-cocktail-hour
- RSS: https://anchor.fm/s/ed0bcf14/podcast/rss

### Migration Priorities

**Phase 1 - Critical (Must have for launch):**
- ✅ Home page
- ✅ Episode library (all episodes searchable/browsable)
- ✅ Individual episode pages with show notes
- ✅ Episode transcripts (integrated into episode pages)
- ✅ About/Bios page
- ✅ Contact page
- ⚠️ Support Us page (with Stripe integration)
- ✅ Platform links (YouTube, Spotify, Apple, Amazon, RSS)

**Phase 2 - Important (Should have soon after launch):**
- Afterparties page
- Consulting page
- Co-Host Appearances page
- Gallery page
- Store links (maintain external links for now)

**Phase 3 - Nice to Have (Can be added post-launch):**
- Blog/articles section (new feature from marketing plan)
- Resources page (new feature from marketing plan)
- Enhanced search and filtering
- Newsletter archive (new feature)

### Content Export Requirements

**To Export from Current Site:**
- [ ] All episode information (titles, descriptions, dates, guests)
- [ ] Episode cover images
- [ ] All episode transcripts
- [ ] Host professional photos and bios
- [ ] Gallery photos with captions
- [ ] Co-host appearances list
- [ ] Consulting services description
- [ ] Afterparties episode information
- [ ] Store product images (if applicable)
- [ ] Any static content (privacy policy, terms)

**External Content (No Migration Needed):**
- Podcast audio files (hosted on Buzzsprout)
- Store products (hosted on external platform)
- Stripe payment integration (reconfigure on new site)
- Social media content (external platforms)

### Technical Debt to Address

**Issues with Current Site:**
1. Template-based system with limited customization
2. High cost relative to features
3. Limited SEO optimization capabilities
4. No email capture integration (per marketing plan)
5. Episodes grouped by decades instead of searchable library
6. No blog/article functionality for content marketing
7. No resources section for audience value
8. Limited analytics integration

**Improvements in New Site:**
1. Unified episode library with search/filter
2. SEO-optimized episode pages
3. Email capture throughout site
4. Blog functionality for content multiplication
5. Resources section for audience education
6. Better mobile experience
7. Faster load times
8. Enhanced analytics tracking
9. More flexible content management

## Appendix C: Glossary

- **CPanel:** Web hosting control panel
- **Schema Markup:** Structured data format for search engines
- **SEO:** Search Engine Optimization
- **SSL/TLS:** Secure connection protocol (HTTPS)
- **CTA:** Call-To-Action
- **CMS:** Content Management System
- **CDN:** Content Delivery Network
- **PWA:** Progressive Web App
- **WCAG:** Web Content Accessibility Guidelines

---

**Document End**

*This requirements document should be reviewed and approved before proceeding with design and implementation phases.*