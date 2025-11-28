# Security Cocktail Hour Website - Documentation Index

**Last Updated**: November 28, 2025

---

## Quick Start

- **Adding New Episodes**: [NEW-EPISODE-DEPLOYMENT.md](NEW-EPISODE-DEPLOYMENT.md)
- **Creating Blog Posts**: [BLOG-DOCUMENTATION.md](BLOG-DOCUMENTATION.md)
- **SEO Standards**: [SEO-META-DESCRIPTION-STANDARDS.md](SEO-META-DESCRIPTION-STANDARDS.md) & [SEO-TITLE-TAG-STANDARDS.md](SEO-TITLE-TAG-STANDARDS.md)

---

## Project Documentation

### Working Context
- [SESSION_CONTEXT.md](../SESSION_CONTEXT.md) - Current project status and recent updates (in root)
- [ARCHIVE.md](../ARCHIVE.md) - Historical fixes and reference material (in root)

### Content Creation

#### Episodes
- **[NEW-EPISODE-DEPLOYMENT.md](NEW-EPISODE-DEPLOYMENT.md)** - Complete workflow for adding new podcast episodes
  - Episode content requirements
  - Deployment process
  - Meta description SEO standards
  - Format standards for timestamps and topics

#### Blog
- **[BLOG-DOCUMENTATION.md](BLOG-DOCUMENTATION.md)** - Complete guide for creating and managing blog posts
  - Front matter template
  - Meta description SEO requirements
  - Content structure guidelines
  - SEO optimization details
- **[BLOG-SEO-PLAN.md](BLOG-SEO-PLAN.md)** - SEO strategy and implementation plan for blog section

### SEO Standards
- **[SEO-META-DESCRIPTION-STANDARDS.md](SEO-META-DESCRIPTION-STANDARDS.md)** - MANDATORY standards for all meta descriptions
  - Character limits (120-155 chars)
  - Writing guidelines with examples
  - Common mistakes to avoid
  - Validation tools
- **[SEO-TITLE-TAG-STANDARDS.md](SEO-TITLE-TAG-STANDARDS.md)** - OPTIONAL standards for episode title tags
  - Character limits (50-60 chars)
  - Dual-title system implementation
  - When and how to use seo_title field
  - Examples from production

---

## Design Specifications

### Master Design System
- **[design_specs/sch_design_spec_v1_2.md](design_specs/sch_design_spec_v1_2.md)** - Complete design system specification
  - Color palette
  - Typography
  - Components library
  - Layout system
  - All page implementations

### Page-Specific Specs
- **[design_specs/blog_page_spec.md](design_specs/blog_page_spec.md)** - Blog section design specification
  - Blog archive page
  - Individual blog posts
  - Featured posts on homepage
  - SEO implementation

- **[design_specs/partnership_page_spec.md](design_specs/partnership_page_spec.md)** - Partnership/sponsorship page specification
  - Sponsorship tiers
  - Page structure
  - Component details

---

## Technical Documentation

### Project Planning
- **[sch_website_requirements.md](sch_website_requirements.md)** - Original project requirements
- **[immediate_action_plan.md](immediate_action_plan.md)** - Initial implementation plan
- **[Project Handoff Document.md](Project Handoff Document.md)** - Project handoff documentation

### Infrastructure
- **[hosting_requirements.md](hosting_requirements.md)** - Hosting setup and requirements
- **[web-project-launch-checklist.md](web-project-launch-checklist.md)** - Launch preparation checklist

### Content Strategy
- **[transcript_strategy.md](transcript_strategy.md)** - Strategy for episode transcripts

### Design Assets
- **[color palette 2025-10-08.md](color palette 2025-10-08.md)** - Current color palette specification
- **[color palette 2025-10-08.png](color palette 2025-10-08.png)** - Visual color palette reference

---

## Tools & Scripts

Located in `/scripts/` directory:

- **audit_meta_descriptions.py** - Scans all pages for meta description compliance
- **fix_all_meta_descriptions.py** - Batch updates meta descriptions

### Usage:
```bash
# Check all meta descriptions
python3 scripts/audit_meta_descriptions.py

# View audit results (latest in temp/, historical in docs/reports/)
cat docs/reports/meta-description-audit-report-2025-11-27.txt
```

---

## File Organization

```
docs/
├── README.md (this file)
├── NEW-EPISODE-DEPLOYMENT.md
├── BLOG-DOCUMENTATION.md
├── BLOG-SEO-PLAN.md
├── SEO-META-DESCRIPTION-STANDARDS.md
├── SEO-TITLE-TAG-STANDARDS.md
├── sch_website_requirements.md
├── hosting_requirements.md
├── immediate_action_plan.md
├── Project Handoff Document.md
├── transcript_strategy.md
├── web-project-launch-checklist.md
├── color palette 2025-10-08.md
├── color palette 2025-10-08.png
├── design_specs/
│   ├── sch_design_spec_v1_2.md
│   ├── blog_page_spec.md
│   └── partnership_page_spec.md
└── reports/
    ├── README.md
    ├── meta-description-audit-2025-11-27.md
    ├── meta-description-audit-report-2025-11-27.txt
    └── trailing-slash-seo-fix-2025-11-28.md

Root directory:
├── SESSION_CONTEXT.md (current working context)
└── ARCHIVE.md (historical reference)
```

---

## Documentation Standards

### When to Update Documentation

**SESSION_CONTEXT.md**:
- After completing major features
- When making significant updates
- Before/after deployments
- Update "Recent Updates" section

**ARCHIVE.md**:
- When issues are fully resolved
- For historical reference
- Technical troubleshooting details
- Keep out of SESSION_CONTEXT when resolved

**Design Specs**:
- When implementing new features
- After design changes
- Keep version history updated

**Content Guidelines**:
- When workflow changes
- After policy updates
- When new standards are established

---

## Quick Reference

### Most Frequently Referenced

1. **Adding Episodes**: docs/NEW-EPISODE-DEPLOYMENT.md
2. **Writing Blog Posts**: docs/BLOG-DOCUMENTATION.md
3. **SEO Standards**: docs/SEO-META-DESCRIPTION-STANDARDS.md & docs/SEO-TITLE-TAG-STANDARDS.md
4. **Current Status**: SESSION_CONTEXT.md (root)
5. **Design System**: docs/design_specs/sch_design_spec_v1_2.md

### For Developers

1. **Master Design Spec**: docs/design_specs/sch_design_spec_v1_2.md
2. **Blog Implementation**: docs/design_specs/blog_page_spec.md
3. **Partnership Page**: docs/design_specs/partnership_page_spec.md
4. **Requirements**: docs/sch_website_requirements.md

### For Content Creators

1. **Episode Workflow**: docs/NEW-EPISODE-DEPLOYMENT.md
2. **Blog Workflow**: docs/BLOG-DOCUMENTATION.md
3. **SEO Meta Descriptions**: docs/SEO-META-DESCRIPTION-STANDARDS.md (required)
4. **SEO Title Tags**: docs/SEO-TITLE-TAG-STANDARDS.md (optional)
5. **Writing Guidelines**: Built into workflow docs

---

## Documentation Maintenance

- Review documentation quarterly
- Update after major changes
- Keep examples current
- Remove outdated information
- Cross-reference related documents

---

**Need Help?**

- Check SESSION_CONTEXT.md for current project status
- Search this README for specific topics
- Review relevant design specs for implementation details
- Consult SEO standards before creating content

---

**End of Documentation Index**
