#!/usr/bin/env python3
"""
cPanel Production Deployment Script

Deploys production packages to cPanel server via SFTP with SSH key authentication.
Handles backup of existing site and extraction of new content.

Usage:
    python3 deploy_to_cpanel.py [--dry-run] [--package PATH]

Options:
    --dry-run       Show what would be done without making changes
    --package PATH  Specify a specific package file (default: most recent)
"""

import argparse
import glob
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


# ANSI color codes
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  # No Color


def print_status(message: str, status: str = "info"):
    """Print colored status message."""
    colors = {
        "info": Colors.BLUE,
        "success": Colors.GREEN,
        "warning": Colors.YELLOW,
        "error": Colors.RED,
        "step": Colors.CYAN,
    }
    color = colors.get(status, Colors.NC)
    prefix = {
        "info": "[INFO]",
        "success": "[OK]",
        "warning": "[WARN]",
        "error": "[ERROR]",
        "step": "[STEP]",
    }.get(status, "[*]")
    print(f"{color}{prefix}{Colors.NC} {message}")


def load_credentials() -> dict:
    """Load cPanel credentials from ~/.cpanel_credentials."""
    creds_path = Path.home() / ".cpanel_credentials"

    if not creds_path.exists():
        print_status(f"Credentials file not found: {creds_path}", "error")
        print_status("Create it with:", "info")
        print(f"""
cat > ~/.cpanel_credentials << 'EOF'
CPANEL_HOST=securitycocktailhour.com
CPANEL_USER=your_username
CPANEL_PORT=22
EOF
chmod 600 ~/.cpanel_credentials
""")
        sys.exit(1)

    # Check permissions (should be 600 or more restrictive)
    mode = creds_path.stat().st_mode & 0o777
    if mode > 0o600:
        print_status(f"Credentials file has insecure permissions: {oct(mode)}", "warning")
        print_status("Consider running: chmod 600 ~/.cpanel_credentials", "info")

    credentials = {}
    with open(creds_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                credentials[key.strip()] = value.strip()

    required = ['CPANEL_HOST', 'CPANEL_USER']
    for key in required:
        if key not in credentials:
            print_status(f"Missing required credential: {key}", "error")
            sys.exit(1)

    # Set default port if not specified
    credentials.setdefault('CPANEL_PORT', '22')

    return credentials


def find_latest_package(project_root: Path) -> Path:
    """Find the most recent production deployment package."""
    pattern = str(project_root / "production-deployment-*.zip")
    packages = glob.glob(pattern)

    if not packages:
        print_status("No production deployment packages found!", "error")
        print_status("Run ./scripts/build_production.sh first", "info")
        sys.exit(1)

    # Sort by modification time, newest first
    packages.sort(key=os.path.getmtime, reverse=True)
    return Path(packages[0])


def test_ssh_connection(credentials: dict) -> bool:
    """Test SSH connection to server."""
    host = credentials['CPANEL_HOST']
    user = credentials['CPANEL_USER']
    port = credentials['CPANEL_PORT']

    print_status(f"Testing SSH connection to {user}@{host}:{port}...", "step")

    result = subprocess.run(
        ['ssh', '-p', port, '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=10',
         f'{user}@{host}', 'echo "Connection successful"'],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print_status("SSH connection successful", "success")
        return True
    else:
        print_status(f"SSH connection failed: {result.stderr}", "error")
        print_status("Ensure your SSH key is added to cPanel SSH Access", "info")
        return False


def get_backup_name() -> str:
    """Generate backup directory name with timestamp."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"public_html_{timestamp}"


def run_remote_command(credentials: dict, command: str, dry_run: bool = False) -> tuple:
    """Run a command on the remote server via SSH."""
    host = credentials['CPANEL_HOST']
    user = credentials['CPANEL_USER']
    port = credentials['CPANEL_PORT']

    if dry_run:
        print_status(f"[DRY RUN] Would execute: {command}", "info")
        return (0, "", "")

    result = subprocess.run(
        ['ssh', '-p', port, f'{user}@{host}', command],
        capture_output=True,
        text=True
    )

    return (result.returncode, result.stdout, result.stderr)


def upload_file(credentials: dict, local_path: Path, remote_path: str, dry_run: bool = False) -> bool:
    """Upload a file to the server via SFTP."""
    host = credentials['CPANEL_HOST']
    user = credentials['CPANEL_USER']
    port = credentials['CPANEL_PORT']

    if dry_run:
        print_status(f"[DRY RUN] Would upload: {local_path} -> {remote_path}", "info")
        return True

    # Use scp for simpler file transfer
    result = subprocess.run(
        ['scp', '-P', port, str(local_path), f'{user}@{host}:{remote_path}'],
        capture_output=True,
        text=True
    )

    return result.returncode == 0


def backup_existing_site(credentials: dict, backup_name: str, dry_run: bool = False) -> bool:
    """Rename public_html to backup directory."""
    print_status(f"Backing up existing site to {backup_name}...", "step")

    # Check if public_html exists
    returncode, stdout, stderr = run_remote_command(
        credentials,
        'test -d public_html && echo "exists" || echo "not_found"',
        dry_run
    )

    if dry_run:
        return True

    if 'not_found' in stdout:
        print_status("No existing public_html found, skipping backup", "warning")
        return True

    # Rename public_html to backup
    returncode, stdout, stderr = run_remote_command(
        credentials,
        f'mv public_html {backup_name}',
        dry_run
    )

    if returncode != 0:
        print_status(f"Failed to create backup: {stderr}", "error")
        return False

    print_status(f"Backup created: {backup_name}", "success")
    return True


def deploy_package(credentials: dict, package_path: Path, dry_run: bool = False) -> bool:
    """Upload and extract the production package."""
    package_name = package_path.name

    # Step 1: Upload the ZIP file
    print_status(f"Uploading {package_name}...", "step")
    if not upload_file(credentials, package_path, package_name, dry_run):
        print_status("Failed to upload package", "error")
        return False
    print_status("Package uploaded", "success")

    # Step 2: Create public_html directory
    print_status("Creating public_html directory...", "step")
    returncode, stdout, stderr = run_remote_command(
        credentials,
        'mkdir -p public_html',
        dry_run
    )
    if returncode != 0 and not dry_run:
        print_status(f"Failed to create public_html: {stderr}", "error")
        return False

    # Step 3: Extract ZIP file
    # The ZIP contains a 'public/' directory, so we extract and move contents
    print_status("Extracting package...", "step")
    extract_commands = f"""
cd ~ && \\
unzip -q {package_name} && \\
mv public/* public_html/ && \\
rmdir public && \\
rm {package_name}
"""
    returncode, stdout, stderr = run_remote_command(
        credentials,
        extract_commands,
        dry_run
    )

    if returncode != 0 and not dry_run:
        print_status(f"Failed to extract package: {stderr}", "error")
        return False

    print_status("Package extracted", "success")
    return True


def set_permissions(credentials: dict, dry_run: bool = False) -> bool:
    """Set correct file permissions on deployed files."""
    print_status("Setting file permissions...", "step")

    permission_commands = """
find public_html -type d -exec chmod 755 {} \\; && \\
find public_html -type f -exec chmod 644 {} \\;
"""
    returncode, stdout, stderr = run_remote_command(
        credentials,
        permission_commands,
        dry_run
    )

    if returncode != 0 and not dry_run:
        print_status(f"Failed to set permissions: {stderr}", "error")
        return False

    print_status("Permissions set (dirs: 755, files: 644)", "success")
    return True


def verify_deployment(credentials: dict, dry_run: bool = False) -> bool:
    """Verify key files exist after deployment."""
    print_status("Verifying deployment...", "step")

    # Check for key files
    files_to_check = ['public_html/index.html', 'public_html/.htaccess', 'public_html/404.html']

    for file in files_to_check:
        returncode, stdout, stderr = run_remote_command(
            credentials,
            f'test -f {file} && echo "exists" || echo "missing"',
            dry_run
        )

        if dry_run:
            continue

        if 'missing' in stdout:
            print_status(f"Missing file: {file}", "error")
            return False

    print_status("All key files verified", "success")
    return True


def list_backups(credentials: dict) -> list:
    """List existing backup directories."""
    returncode, stdout, stderr = run_remote_command(
        credentials,
        'ls -d public_html_* 2>/dev/null || echo "none"'
    )

    if 'none' in stdout or not stdout.strip():
        return []

    return sorted(stdout.strip().split('\n'), reverse=True)


def main():
    parser = argparse.ArgumentParser(
        description='Deploy production package to cPanel server'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )
    parser.add_argument(
        '--package',
        type=Path,
        help='Specific package file to deploy (default: most recent)'
    )
    parser.add_argument(
        '--skip-backup',
        action='store_true',
        help='Skip backing up existing site (use with caution!)'
    )
    parser.add_argument(
        '--list-backups',
        action='store_true',
        help='List existing backup directories on server'
    )

    args = parser.parse_args()

    # Determine project root (script is in .claude/skills/cpanel-deploy/scripts/)
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent.parent.parent.parent

    print(f"\n{Colors.CYAN}=== cPanel Production Deployment ==={Colors.NC}\n")

    if args.dry_run:
        print_status("DRY RUN MODE - No changes will be made", "warning")
        print()

    # Load credentials
    print_status("Loading credentials...", "step")
    credentials = load_credentials()
    print_status(f"Server: {credentials['CPANEL_USER']}@{credentials['CPANEL_HOST']}:{credentials['CPANEL_PORT']}", "info")

    # List backups mode
    if args.list_backups:
        backups = list_backups(credentials)
        if backups:
            print_status("Existing backups on server:", "info")
            for backup in backups:
                print(f"  - {backup}")
        else:
            print_status("No backups found on server", "info")
        return

    # Test SSH connection
    if not test_ssh_connection(credentials):
        sys.exit(1)

    # Find package to deploy
    if args.package:
        package_path = args.package.resolve()
        if not package_path.exists():
            print_status(f"Package not found: {package_path}", "error")
            sys.exit(1)
    else:
        package_path = find_latest_package(project_root)

    # Display package info
    package_size = package_path.stat().st_size / (1024 * 1024)  # MB
    package_mtime = datetime.fromtimestamp(package_path.stat().st_mtime)

    print()
    print_status("Package to deploy:", "info")
    print(f"  File: {package_path.name}")
    print(f"  Size: {package_size:.2f} MB")
    print(f"  Date: {package_mtime.strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Generate backup name
    backup_name = get_backup_name()

    if not args.skip_backup:
        print_status(f"Backup will be created as: {backup_name}", "info")
    else:
        print_status("SKIPPING BACKUP (--skip-backup flag)", "warning")

    print()

    # Confirmation
    if not args.dry_run:
        print(f"{Colors.YELLOW}This will deploy to PRODUCTION.{Colors.NC}")
        response = input("Continue? [y/N]: ").strip().lower()
        if response != 'y':
            print_status("Deployment cancelled", "info")
            sys.exit(0)
        print()

    # Execute deployment steps
    success = True

    # Step 1: Backup existing site
    if not args.skip_backup:
        if not backup_existing_site(credentials, backup_name, args.dry_run):
            print_status("Backup failed! Aborting deployment.", "error")
            sys.exit(1)

    # Step 2: Deploy new package
    if not deploy_package(credentials, package_path, args.dry_run):
        print_status("Deployment failed!", "error")
        if not args.skip_backup:
            print_status(f"To rollback: ssh {credentials['CPANEL_USER']}@{credentials['CPANEL_HOST']}", "info")
            print_status(f"Then run: rm -rf public_html && mv {backup_name} public_html", "info")
        sys.exit(1)

    # Step 3: Set permissions
    if not set_permissions(credentials, args.dry_run):
        print_status("Permission setting failed (non-critical)", "warning")

    # Step 4: Verify deployment
    if not verify_deployment(credentials, args.dry_run):
        print_status("Verification failed! Site may not be working correctly.", "error")
        success = False

    print()
    if success:
        print(f"{Colors.GREEN}=== Deployment Complete ==={Colors.NC}")
        print()
        print_status("Please verify the site at: https://securitycocktailhour.com/", "info")
        print()
        print("Verification checklist:")
        print("  [ ] Homepage loads correctly")
        print("  [ ] Navigation works")
        print("  [ ] Latest content visible")
        print("  [ ] Test 404 page: https://securitycocktailhour.com/nonexistent")
        print("  [ ] SSL certificate valid (green padlock)")
        print()
        if not args.skip_backup:
            print_status(f"Rollback available: {backup_name}", "info")
    else:
        print(f"{Colors.RED}=== Deployment had issues ==={Colors.NC}")
        print_status("Review the errors above and verify site manually", "warning")

    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
