# Rollback Procedures

Instructions for reverting to a previous deployment if something goes wrong.

## Quick Rollback (via Script)

The deployment script keeps backups named `public_html_YYYYMMDD_HHMMSS`.

### List Available Backups

```bash
python3 .claude/skills/cpanel-deploy/scripts/deploy_to_cpanel.py --list-backups
```

Output example:
```
[INFO] Existing backups on server:
  - public_html_20260118_143022
  - public_html_20260115_091534
  - public_html_20260110_162847
```

## Manual Rollback Steps

### Step 1: Connect to Server

```bash
ssh your_username@securitycocktailhour.com
```

### Step 2: Identify Backup to Restore

```bash
# List all backups with dates
ls -la public_html_*
```

### Step 3: Remove Current (Failed) Deployment

```bash
rm -rf public_html
```

### Step 4: Restore Backup

```bash
# Replace YYYYMMDD_HHMMSS with actual backup timestamp
mv public_html_20260118_143022 public_html
```

### Step 5: Verify Restoration

```bash
# Check files are present
ls public_html/

# Verify .htaccess exists
cat public_html/.htaccess | head -5
```

### Step 6: Test the Site

Visit https://securitycocktailhour.com/ and verify:
- Homepage loads
- Navigation works
- Content displays correctly

## Emergency Rollback (One-Liner)

If you know the exact backup name:

```bash
ssh your_username@securitycocktailhour.com 'rm -rf public_html && mv public_html_20260118_143022 public_html'
```

## Backup Retention

### Recommended Policy

Keep the last 3-5 backups to balance storage and safety.

### List Backup Sizes

```bash
ssh your_username@securitycocktailhour.com 'du -sh public_html_*'
```

### Clean Up Old Backups (Keep Last 5)

```bash
ssh your_username@securitycocktailhour.com '
  backups=$(ls -d public_html_* 2>/dev/null | sort -r)
  count=0
  for dir in $backups; do
    count=$((count + 1))
    if [ $count -gt 5 ]; then
      echo "Removing: $dir"
      rm -rf "$dir"
    fi
  done
'
```

## When to Rollback

### Immediate Rollback Triggers

- Homepage shows error page
- 500 Internal Server Error
- Blank pages across site
- SSL certificate errors (though unlikely from deployment)
- Major broken functionality

### Investigate First

- Minor styling issues
- Single page errors
- Form submission issues (may need server-side fix)
- Performance degradation

## Post-Rollback Actions

1. **Document the issue** - Note what went wrong
2. **Check build logs** - Review `./scripts/build_production.sh` output
3. **Verify local build** - Test with `hugo server -D` locally
4. **Fix the issue** - Address root cause
5. **Rebuild and redeploy** - Create new package and try again

## Preventing Future Issues

1. **Always run pre-deployment tests**:
   ```bash
   python3 scripts/tests/run_all_tests.py
   ```

2. **Verify package contents**:
   ```bash
   unzip -l production-deployment-*.zip | head -30
   ```

3. **Check .htaccess validation**:
   ```bash
   python3 scripts/validate_htaccess.py
   ```

4. **Test in dry-run mode**:
   ```bash
   python3 .claude/skills/cpanel-deploy/scripts/deploy_to_cpanel.py --dry-run
   ```
