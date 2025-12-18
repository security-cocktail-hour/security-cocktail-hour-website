#!/bin/bash
#
# Production Build Script for Security Cocktail Hour Website
# Validates .htaccess, builds production package, and creates deployment ZIP
#
# Usage: ./scripts/build_production.sh
#

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Project directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo -e "${BOLD}${BLUE}======================================================================${NC}"
echo -e "${BOLD}${BLUE}Security Cocktail Hour - Production Build Script${NC}"
echo -e "${BOLD}${BLUE}======================================================================${NC}\n"

# Change to project directory
cd "$PROJECT_DIR"
echo -e "${YELLOW}Working directory: ${PROJECT_DIR}${NC}\n"

# Step 1: Validate .htaccess before building
echo -e "${BOLD}Step 1: Validating .htaccess file integrity${NC}"
echo -e "${BLUE}Running: python3 scripts/validate_htaccess.py${NC}\n"

if python3 scripts/validate_htaccess.py; then
    echo -e "\n${GREEN}✓ .htaccess validation passed${NC}\n"
else
    echo -e "\n${RED}✗ .htaccess validation FAILED${NC}"
    echo -e "${RED}Fix errors before deploying to production${NC}\n"
    exit 1
fi

# Step 2: Build production site
echo -e "${BOLD}Step 2: Building production site${NC}"
echo -e "${BLUE}Running: hugo --minify${NC}\n"

hugo --minify

if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}✓ Hugo build completed successfully${NC}\n"
else
    echo -e "\n${RED}✗ Hugo build failed${NC}\n"
    exit 1
fi

# Step 3: Re-validate .htaccess in public/ directory
echo -e "${BOLD}Step 3: Re-validating built .htaccess file${NC}"
echo -e "${BLUE}Running: python3 scripts/validate_htaccess.py${NC}\n"

if python3 scripts/validate_htaccess.py; then
    echo -e "\n${GREEN}✓ Built .htaccess validation passed${NC}\n"
else
    echo -e "\n${RED}✗ Built .htaccess validation FAILED${NC}"
    echo -e "${RED}The static/.htaccess and public/.htaccess files don't match${NC}\n"
    exit 1
fi

# Step 4: Create production deployment ZIP
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
ZIP_NAME="production-deployment-${TIMESTAMP}.zip"

echo -e "${BOLD}Step 4: Creating deployment package${NC}"
echo -e "${BLUE}Creating: ${ZIP_NAME}${NC}\n"

cd public
zip -r "../${ZIP_NAME}" . > /dev/null 2>&1
cd ..

if [ -f "${ZIP_NAME}" ]; then
    FILE_SIZE=$(ls -lh "${ZIP_NAME}" | awk '{print $5}')
    FILE_COUNT=$(unzip -l "${ZIP_NAME}" | tail -1 | awk '{print $2}')

    echo -e "${GREEN}✓ Deployment package created${NC}"
    echo -e "  File: ${BOLD}${ZIP_NAME}${NC}"
    echo -e "  Size: ${BOLD}${FILE_SIZE}${NC}"
    echo -e "  Files: ${BOLD}${FILE_COUNT}${NC}\n"
else
    echo -e "${RED}✗ Failed to create deployment package${NC}\n"
    exit 1
fi

# Step 5: Summary
echo -e "${BOLD}${BLUE}======================================================================${NC}"
echo -e "${BOLD}${GREEN}Production Build Complete!${NC}"
echo -e "${BOLD}${BLUE}======================================================================${NC}\n"

echo -e "${BOLD}Deployment Package:${NC}"
echo -e "  ${GREEN}${ZIP_NAME}${NC}\n"

echo -e "${BOLD}Next Steps:${NC}"
echo -e "  1. Review the deployment checklist in GODADDY-DEPLOYMENT-INSTRUCTIONS.md"
echo -e "  2. Log into GoDaddy cPanel"
echo -e "  3. Upload ${ZIP_NAME} to public_html/"
echo -e "  4. Extract and deploy following the instructions\n"

echo -e "${BOLD}Validation Summary:${NC}"
echo -e "  ${GREEN}✓${NC} .htaccess file integrity verified"
echo -e "  ${GREEN}✓${NC} All 24 redirect rules present"
echo -e "  ${GREEN}✓${NC} ErrorDocument 404 configured"
echo -e "  ${GREEN}✓${NC} Security headers enabled"
echo -e "  ${GREEN}✓${NC} Performance optimizations enabled\n"

echo -e "${BOLD}${BLUE}======================================================================${NC}\n"

exit 0
