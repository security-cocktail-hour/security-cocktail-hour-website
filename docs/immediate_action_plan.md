# Security Cocktail Hour Website Redesign
## Immediate Action Plan - Next Steps

**Date:** October 3, 2025  
**Timeline:** 14 days to launch  
**Status:** Ready to begin development

---

## ✅ What's Complete

- [x] Requirements Document finalized
- [x] Design Specification complete
- [x] Current site analysis complete
- [x] Key decisions made:
  - Static site generator (Hugo or 11ty)
  - Mailchimp for email (free tier)
  - GoDaddy cPanel hosting
  - Logo and color palette established
  - All 60-70 episodes at launch
  - Unified episode library (no decade grouping)
  - Single store page (external links)
  - Support Us deferred to Phase 2

---

## 🎯 Today's Tasks (Day 1)

### Task 1: Content Export from Current Site ⏱️ 2-3 hours

**Priority:** Start this FIRST while we set up development environment

**Action Steps:**

1. **Login to GoDaddy Website Builder**
   - Access admin panel
   - Export all text content

2. **Episode Data Export**
   - [ ] All episode titles (60-70 episodes)
   - [ ] All episode descriptions
   - [ ] Episode dates and durations
   - [ ] Guest names and information
   - [ ] Episode cover images (download all)
   - [ ] Any episode metadata (categories, tags)

3. **Transcript Export**
   - [ ] Export existing transcripts (only small number currently available)
   - [ ] Identify which episodes have transcripts vs. which don't
   - [ ] Save as text files: transcript-ep-##.txt
   - [ ] Note: Not all episodes need transcripts at launch
   - [ ] Note: Template must support adding transcripts later

4. **Page Content Export**
   - [ ] Homepage copy
   - [ ] About/Bios page content (both Joe and Adam)
   - [ ] Consulting page content
   - [ ] Co-host appearances list
   - [ ] Gallery photo descriptions
   - [ ] Contact page information
   - [ ] Any other static content

5. **Image Export**
   - [ ] Logo (high-res version you have)
   - [ ] Host photos (high-res versions you have)
   - [ ] All episode cover images
   - [ ] Gallery photos
   - [ ] Any other images used

6. **Configuration Export**
   - [ ] List all podcast platform URLs
   - [ ] Social media handles
   - [ ] Contact email address
   - [ ] Store URLs (both external stores)
   - [ ] Buzzsprout RSS feed URL
   - [ ] Any other links

**Output:** 
- Create a folder: `content-export/`
- Organize by type: `episodes/`, `images/`, `transcripts/`, `pages/`
- Create a spreadsheet or CSV with all episode metadata

---

### Task 2: Set Up Claude Code Development Environment ⏱️ 1-2 hours

**Action Steps:**

1. **Install Claude Code** (if not already installed)
   ```bash
   # Follow instructions at https://docs.claude.com/en/docs/claude-code
   ```

2. **Create Project Directory**
   ```bash
   mkdir security-cocktail-hour-website
   cd security-cocktail-hour-website
   ```

3. **Initialize Git Repository**
   ```bash
   git init
   echo "# Security Cocktail Hour Website" > README.md
   git add README.md
   git commit -m "Initial commit"
   ```

4. **Copy Documentation**
   - Place requirements document in `/docs/requirements.md`
   - Place design spec in `/docs/design-spec.md`
   - Place current site analysis in `/docs/current-site-analysis.md`
   - Place this action plan in `/docs/action-plan.md`

5. **Create Content Directory**
   - Copy exported content into `/content/` directory
   - Organize as needed

---

### Task 3: Technology Stack Selection with Claude Code ⏱️ 1 hour

**Action Steps:**

1. **Start Claude Code Session**
   - Open terminal in project directory
   - Launch Claude Code

2. **Present Requirements to Claude Code**
   - Share requirements document
   - Share design specification
   - Request technology recommendation

3. **Key Criteria for Static Site Generator Selection:**
   - Works with GoDaddy cPanel (standard hosting)
   - Supports 60-70 episodes efficiently
   - Good search functionality (or can integrate search)
   - Easy to build and deploy
   - Markdown-based content
   - Good template system
   - Fast build times
   - Active community support

4. **Likely Options:**
   - **Hugo:** Fast, powerful, great for large sites
   - **11ty (Eleventy):** Flexible, JavaScript-based, modern
   - **Jekyll:** Ruby-based, mature, GitHub Pages compatible

5. **Let Claude Code Recommend and Set Up**
   - Claude Code will analyze requirements
   - Recommend best fit
   - Initialize project structure
   - Set up basic configuration

---

### Task 4: GoDaddy Hosting Setup Verification ⏱️ 30 min - 1 hour

**Action Steps:**

1. **Login to GoDaddy Account**
   - Access hosting control panel
   - Verify cPanel access

2. **Check Hosting Plan Details**
   - [ ] Verify cPanel hosting is available
   - [ ] Check disk space (need enough for 60-70 episode images)
   - [ ] Verify SSL/HTTPS availability (Let's Encrypt)
   - [ ] Check FTP/SFTP access credentials
   - [ ] Verify domain is pointed to hosting

3. **Test FTP/SFTP Connection**
   - Use FileZilla or similar
   - Connect to hosting
   - Verify write access
   - Create test folder to confirm permissions

4. **Check .htaccess Support**
   - Verify Apache server (not nginx)
   - Test .htaccess file creation
   - This is needed for redirects

5. **SSL Certificate**
   - Check if SSL is already installed
   - If not, plan to install Let's Encrypt (free)

**Output:** Document hosting credentials (securely) and confirm everything is ready

---

### Task 5: Mailchimp Setup ⏱️ 30 min - 1 hour

**Action Steps:**

1. **Create Mailchimp Account** (if you don't have one)
   - Go to mailchimp.com
   - Sign up for free tier (up to 500 subscribers)
   - Verify email

2. **Create Audience/List**
   - Name: "Security Cocktail Hour Newsletter"
   - From name: "Security Cocktail Hour" or "Joe & Adam"
   - From email: feedback@securitycocktailhour.com (or dedicated newsletter email)
   - Reminder: How people signed up

3. **Configure Signup Form**
   - Create embedded form or use API
   - Fields: Email (required), First Name (optional), Last Name (optional)
   - Double opt-in: Enabled (GDPR compliance)
   - Welcome email: Enable

4. **Get Integration Details**
   - [ ] Audience ID
   - [ ] API Key
   - [ ] Form embed code (if using embedded forms)

5. **Create Welcome Email** (can refine later)
   - Subject: "Welcome to Security Cocktail Hour!"
   - Thank subscriber
   - Set expectations (weekly newsletter)
   - Link to latest episode
   - Unsubscribe link (required)

**Output:** Mailchimp credentials and integration details documented

---

## 📋 End of Day 1 Checklist

By end of today, you should have:

- [ ] All content exported from current site
- [ ] Content organized in folders
- [ ] Episode metadata in spreadsheet/CSV
- [ ] Claude Code installed and project initialized
- [ ] Technology stack selected (Hugo or 11ty)
- [ ] Project structure set up
- [ ] GoDaddy hosting verified and accessible
- [ ] FTP/SFTP connection tested
- [ ] Mailchimp account created and configured
- [ ] Git repository initialized

---

## 🔜 Tomorrow's Preview (Day 2)

### Major Tasks for Day 2:

1. **Build Core Page Templates with Claude Code**
   - Homepage template
   - Episode library page template
   - Individual episode page template
   - About page template
   - Contact page template

2. **Begin Content Migration**
   - Set up episode content structure
   - Import first 10-20 episodes as test
   - Verify templates render correctly

3. **Implement Design System**
   - CSS for colors, typography, components
   - Logo integration
   - Responsive design foundation

4. **Set Up Search Functionality**
   - Evaluate search options (client-side JS search like Lunr.js or Fuse.js)
   - Begin implementation

---

## 💡 Tips for Working with Claude Code

### Best Practices:

1. **Be Specific**
   - Share the requirements and design docs
   - Reference specific sections when asking for implementation
   - Provide examples from current site

2. **Iterative Development**
   - Start with one page template
   - Get it working
   - Then move to next page
   - Don't try to do everything at once

3. **Test Frequently**
   - Build and preview often
   - Test on mobile and desktop
   - Check browser console for errors

4. **Version Control**
   - Commit after each working feature
   - Write clear commit messages
   - Allows easy rollback if needed

5. **Ask for Explanations**
   - If you don't understand something Claude Code generates
   - Ask for explanation
   - Ask for alternatives if needed

### Example Claude Code Conversations:

**Initial Setup:**
```
"I need to build a podcast website using a static site generator. 
I have detailed requirements and design specs. The site needs to:
- Host 60-70 episodes with full metadata
- Have search and filter functionality
- Work on standard cPanel hosting (GoDaddy)
- Be fast and SEO-optimized

Which static site generator do you recommend and why?
Please initialize the project structure."
```

**First Template:**
```
"Let's build the homepage template. Here's what it needs:
[paste homepage requirements from design spec]

Use these colors from our logo:
- Red: #C8534B
- Blue: #1E4D8B
- Cyan: #3BA0D4

Please create the homepage HTML template with proper semantic markup
and CSS using our color palette."
```

**Episode Content Structure:**
```
"I need to set up the content structure for 60+ podcast episodes.
Each episode needs:
- Title, guest name, date, duration
- Description (SEO-optimized)
- Full transcript
- Links to multiple podcast platforms
- Category/topic tags
- Cover image

What's the best way to structure this content in [Hugo/11ty]?
Please create the content template and example files."
```

---

## 🚨 Blockers to Watch For

### Potential Issues:

1. **Content Export Problems**
   - If GoDaddy Website Builder makes export difficult
   - May need to copy/paste manually
   - Can be time-consuming but necessary

2. **Hosting Compatibility**
   - If cPanel doesn't support something needed
   - Have backup hosting plan ready (Netlify, Vercel)

3. **Transcript Volume**
   - 60-70 transcripts is a lot of content
   - May need scripting to organize
   - Claude Code can help with batch processing

4. **Image Optimization**
   - 60-70 episode cover images need optimization
   - Don't want to slow down site
   - Plan to compress before upload

---

## 📞 Help & Resources

### If You Get Stuck:

1. **Claude Code Documentation**
   - https://docs.claude.com/en/docs/claude-code
   - Has guides and examples

2. **Static Site Generator Docs**
   - Hugo: https://gohugo.io/documentation/
   - 11ty: https://www.11ty.dev/docs/

3. **Web Development Help**
   - MDN Web Docs: https://developer.mozilla.org/
   - CSS Tricks: https://css-tricks.com/

4. **This Chat**
   - Continue asking questions here
   - I can help troubleshoot
   - Can provide code examples

---

## ✨ Motivation

You've got this! Here's what you're accomplishing:

- ✅ Moving off expensive, limited platform
- ✅ Getting modern, fast, SEO-optimized site
- ✅ Adding email capture for marketing
- ✅ Better user experience for listeners
- ✅ Full control over your content
- ✅ Foundation for future growth

**Day 1 Goal:** Get everything set up and ready to build.

**By Day 14:** Live, beautiful, functional website!

Let's do this! 🚀

---

## Next: Start with Task 1

Begin exporting content from your current site. While you're doing that, I can help with any questions about Tasks 2-5.

Once you have content exported and Claude Code set up, we'll dive into development together!