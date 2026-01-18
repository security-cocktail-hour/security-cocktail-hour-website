---
name: cpanel-deploy
description: "NOT CURRENTLY FUNCTIONAL - GoDaddy SSH authentication issues prevent automated deployment. Use manual deployment via cPanel File Manager instead. See GODADDY-DEPLOYMENT-INSTRUCTIONS.md for manual steps."
---

# cPanel Production Deployment Skill

## STATUS: NOT FUNCTIONAL

**Last tested**: January 18, 2026

This skill is **not currently working** due to SSH authentication issues with GoDaddy's cPanel hosting. Despite following all setup steps correctly, SSH key and password authentication both fail.

### Issue Summary

- SSH is enabled in GoDaddy account settings
- SSH key properly added to `~/.ssh/authorized_keys` on server with correct permissions (600)
- `.ssh` directory has correct permissions (700)
- Key is authorized in cPanel SSH Access
- Connection reaches server but authentication is rejected for both key and password auth
- GoDaddy support may be needed to resolve

### Server Details (for future troubleshooting)

- **IP Address**: 208.109.73.117
- **Port**: 22
- **cPanel Username**: nfgitkw863go
- **Home Directory**: /home/nfgitkw863go

### Current Workaround

Use **manual deployment** via cPanel File Manager. See `GODADDY-DEPLOYMENT-INSTRUCTIONS.md` for complete steps.

---

## Original Design (for when SSH is fixed)

Automates secure deployment of production packages to the Security Cocktail Hour cPanel server via SFTP with SSH key authentication.

### Overview

This skill handles the final deployment step: transferring a validated production ZIP to the live cPanel server. It:
- Backs up the existing `public_html` to `public_html_YYYYMMDD_HHMMSS`
- Uploads and extracts the new production package
- Verifies deployment success
- Provides rollback instructions if needed

### Prerequisites

Before using this skill, ensure:
1. **Production package exists**: Run `./scripts/build_production.sh` first
2. **SSH key configured**: Your SSH key must be added to cPanel
3. **Credentials file exists**: `~/.cpanel_credentials` with connection details

### Credentials File Setup

Create `~/.cpanel_credentials` with restricted permissions:

```bash
# Create the file
cat > ~/.cpanel_credentials << 'EOF'
CPANEL_HOST=securitycocktailhour.com
CPANEL_USER=your_cpanel_username
CPANEL_PORT=22
EOF

# Secure the file (owner read-only)
chmod 600 ~/.cpanel_credentials
```

### SSH Key Setup

1. Generate key if needed: `ssh-keygen -t ed25519 -C "cpanel-deploy"`
2. Add public key to cPanel: cPanel → Security → SSH Access → Manage SSH Keys → Import Key
3. Authorize the key in cPanel
4. Test connection: `ssh -p 22 your_username@securitycocktailhour.com`

## Workflow

### Phase 1: Pre-Deployment Validation

**Step 1: Verify Production Package**
- Locate the most recent `production-deployment-*.zip` file
- Verify file exists and has reasonable size (> 1MB)
- Display package details (filename, size, date)

**Step 2: Verify Credentials**
- Check `~/.cpanel_credentials` exists and is readable
- Verify SSH key authentication works
- Test SFTP connection to server

**Step 3: User Confirmation**
- Display what will be deployed
- Show backup naming convention
- **APPROVAL CHECKPOINT**: Wait for user to confirm deployment

### Phase 2: Backup & Deploy

**Step 4: Backup Existing Site**
- Connect to server via SFTP
- Rename `public_html` to `public_html_YYYYMMDD_HHMMSS`
- Verify backup was created successfully

**Step 5: Upload Production Package**
- Create new `public_html` directory
- Upload the production ZIP file
- Extract contents to `public_html`
- Remove the uploaded ZIP file (cleanup)

**Step 6: Set Permissions**
- Set directory permissions to 755
- Set file permissions to 644
- Verify `.htaccess` has correct permissions

### Phase 3: Post-Deployment Verification

**Step 7: Verify Deployment**
- Check key files exist on server
- Verify `.htaccess` is in place
- Test that the site responds

**Step 8: Production Site Check**
- **APPROVAL CHECKPOINT**: Ask user to verify site at https://securitycocktailhour.com/
- Provide checklist of items to verify:
  - Homepage loads correctly
  - Navigation works
  - Latest episode/blog post visible
  - 404 page works (test with /nonexistent-page)
  - SSL certificate valid (green padlock)

**Step 9: Completion**
- Display deployment summary
- Provide rollback instructions if needed
- Optionally update CLAUDE.md with deployment date

## Approval Checkpoints

1. **Pre-deployment confirmation** - Before any changes to production
2. **Post-deployment verification** - User confirms site works correctly

## Rollback Procedure

If something goes wrong, rollback is simple:

```bash
# Connect to server
ssh your_username@securitycocktailhour.com

# Remove failed deployment
rm -rf public_html

# Restore backup (use the most recent backup directory name)
mv public_html_YYYYMMDD_HHMMSS public_html
```

## Error Handling

| Error | Resolution |
|-------|------------|
| Credentials file not found | Create `~/.cpanel_credentials` per setup instructions |
| SSH connection failed | Verify SSH key is added and authorized in cPanel |
| Permission denied | Check file permissions on credentials file (should be 600) |
| Backup failed | Check disk space on server; may need to clean old backups |
| Upload failed | Check network connection; retry deployment |
| Extraction failed | Verify ZIP file integrity; rebuild if needed |

## Security Notes

- Never commit credentials to git
- SSH key authentication is more secure than passwords
- Credentials file should have 600 permissions (owner read-only)
- The skill never stores or logs passwords
- All transfers use encrypted SFTP

## Integration with Other Skills

This skill is typically the final step after:
1. **episode-deploy** or **blog-deploy** - Creates content and builds package
2. **build_production.sh** - Creates validated production ZIP

Typical workflow:
```
/episode-deploy → builds package → /cpanel-deploy → site live
```

## Manual Deployment Alternative

If automated deployment fails, see `GODADDY-DEPLOYMENT-INSTRUCTIONS.md` for manual cPanel deployment steps.
