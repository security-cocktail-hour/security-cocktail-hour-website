#!/bin/bash
# Fix file permissions after deployment
# Run this script on the server after extracting the deployment package

echo "Fixing file permissions..."

# Set directories to 755
find . -type d -exec chmod 755 {} \;

# Set files to 644
find . -type f -exec chmod 644 {} \;

echo "Permissions fixed!"
echo "Directories: 755 (rwxr-xr-x)"
echo "Files: 644 (rw-r--r--)"
