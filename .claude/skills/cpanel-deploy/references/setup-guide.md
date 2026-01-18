# cPanel Deployment Setup Guide

Complete setup instructions for automated cPanel deployment via SFTP/SSH.

## Prerequisites

- macOS or Linux system
- SSH client installed (default on macOS)
- cPanel hosting account with SSH access enabled

## Step 1: Create Credentials File

Create a credentials file at `~/.cpanel_credentials`:

```bash
cat > ~/.cpanel_credentials << 'EOF'
CPANEL_HOST=securitycocktailhour.com
CPANEL_USER=your_cpanel_username
CPANEL_PORT=22
EOF
```

**Important**: Replace `your_cpanel_username` with your actual cPanel username.

Set secure permissions:

```bash
chmod 600 ~/.cpanel_credentials
```

## Step 2: Generate SSH Key (if needed)

If you don't already have an SSH key:

```bash
# Generate a new Ed25519 key (recommended)
ssh-keygen -t ed25519 -C "cpanel-deploy" -f ~/.ssh/cpanel_deploy

# Or use RSA if Ed25519 is not supported
ssh-keygen -t rsa -b 4096 -C "cpanel-deploy" -f ~/.ssh/cpanel_deploy
```

When prompted for a passphrase, you can either:
- Press Enter for no passphrase (less secure but convenient)
- Enter a passphrase (more secure, will be prompted each time)

## Step 3: Add SSH Key to cPanel

1. **Login to cPanel** at your hosting provider

2. **Navigate to SSH Access**:
   - Security section → SSH Access
   - Or search for "SSH" in cPanel

3. **Import your public key**:
   - Click "Manage SSH Keys"
   - Click "Import Key"
   - Name: `cpanel_deploy` (or any memorable name)
   - Paste the contents of your public key:
     ```bash
     cat ~/.ssh/cpanel_deploy.pub
     ```
   - Leave private key field empty
   - Click "Import"

4. **Authorize the key**:
   - Back on Manage SSH Keys page
   - Find your imported key in "Public Keys" section
   - Click "Manage" → "Authorize"

## Step 4: Configure SSH Client

Add to `~/.ssh/config`:

```
Host securitycocktailhour.com
    HostName securitycocktailhour.com
    User your_cpanel_username
    Port 22
    IdentityFile ~/.ssh/cpanel_deploy
    IdentitiesOnly yes
```

## Step 5: Test Connection

Test that everything works:

```bash
# Test SSH connection
ssh securitycocktailhour.com 'echo "Connection successful!"'

# Test with full credentials
ssh -p 22 your_username@securitycocktailhour.com 'pwd'
```

You should see your home directory path (usually `/home/username`).

## Step 6: Test Deployment Script

Run a dry-run to verify everything is configured:

```bash
python3 .claude/skills/cpanel-deploy/scripts/deploy_to_cpanel.py --dry-run
```

This will:
- Verify credentials file exists
- Test SSH connection
- Show what would be deployed
- NOT make any actual changes

## Troubleshooting

### "Permission denied (publickey)"

- Verify key is authorized in cPanel
- Check key permissions: `chmod 600 ~/.ssh/cpanel_deploy`
- Try verbose mode: `ssh -v securitycocktailhour.com`

### "Connection refused"

- SSH may not be enabled on your cPanel account
- Contact hosting provider to enable SSH access
- Some shared hosts restrict SSH to certain IP addresses

### "Host key verification failed"

- Accept the host key:
  ```bash
  ssh-keyscan -p 22 securitycocktailhour.com >> ~/.ssh/known_hosts
  ```

### Credentials file permission warning

- Run: `chmod 600 ~/.cpanel_credentials`

### "No production deployment packages found"

- Build a package first: `./scripts/build_production.sh`

## Security Best Practices

1. **Never commit credentials** - The credentials file is in your home directory, not the project
2. **Use SSH keys** - More secure than passwords
3. **Restrict key permissions** - `chmod 600` on all key files
4. **Use a dedicated key** - Create a key specifically for cPanel deployment
5. **Regular key rotation** - Consider rotating keys annually

## Backup Management

List existing backups on server:

```bash
python3 .claude/skills/cpanel-deploy/scripts/deploy_to_cpanel.py --list-backups
```

Clean up old backups (keep last 3):

```bash
ssh your_username@securitycocktailhour.com 'ls -d public_html_* | head -n -3 | xargs rm -rf'
```

## Manual Rollback

If deployment fails and you need to restore:

```bash
# Connect to server
ssh your_username@securitycocktailhour.com

# List backups to find the right one
ls -la public_html_*

# Remove failed deployment
rm -rf public_html

# Restore from backup
mv public_html_YYYYMMDD_HHMMSS public_html

# Verify
ls public_html/
```
