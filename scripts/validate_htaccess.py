#!/usr/bin/env python3
"""
.htaccess Validation Script for Security Cocktail Hour Website
Validates .htaccess file integrity before production deployment

Usage:
    python3 scripts/validate_htaccess.py

Exit Codes:
    0 - All checks passed
    1 - Validation failed
"""

import sys
import os
from pathlib import Path

# ANSI color codes for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Expected redirects (source paths only - we'll verify these exist)
EXPECTED_REDIRECTS = [
    '/transcript-ep-59',
    '/transcript-ep-60',
    '/transcript-ep-61',
    '/transcript-ep-21',
    '/transcript-ep-53',
    '/transcript-hak5-unboxing',
    '/episodes-1-10',
    '/episodes-11-20',
    '/episodes-21-30',
    '/episodes-31-40',
    '/episodes-41-50-1',
    '/episodes-51-60',
    '/episodes-51-60-1',
    '/episodes-61-70',
    '/consulting',
    '/bios',
    '/guest-appearances',
    '/support-us',
    '/store',
    '/store-2',
    '/store-|-pens%2C-mugs-%26-more',
    '/store-|-clothing',
    '/merchandise',
    '/merchandise1',
]

class HtaccessValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.checks_passed = 0
        self.checks_total = 0

    def print_header(self):
        print(f"\n{BOLD}{BLUE}{'='*70}{RESET}")
        print(f"{BOLD}{BLUE}.htaccess Validation Script{RESET}")
        print(f"{BOLD}{BLUE}{'='*70}{RESET}\n")

    def print_summary(self):
        print(f"\n{BOLD}{BLUE}{'='*70}{RESET}")
        print(f"{BOLD}Validation Summary:{RESET}")
        print(f"  Checks Passed: {GREEN}{self.checks_passed}/{self.checks_total}{RESET}")

        if self.warnings:
            print(f"\n{YELLOW}⚠ Warnings ({len(self.warnings)}):{RESET}")
            for warning in self.warnings:
                print(f"  {YELLOW}• {warning}{RESET}")

        if self.errors:
            print(f"\n{RED}✗ Errors ({len(self.errors)}):{RESET}")
            for error in self.errors:
                print(f"  {RED}• {error}{RESET}")
            print(f"\n{RED}{BOLD}VALIDATION FAILED - DO NOT DEPLOY{RESET}")
            print(f"{BOLD}{BLUE}{'='*70}{RESET}\n")
            return False
        else:
            print(f"\n{GREEN}{BOLD}✓ ALL CHECKS PASSED - SAFE TO DEPLOY{RESET}")
            print(f"{BOLD}{BLUE}{'='*70}{RESET}\n")
            return True

    def check(self, name, condition, error_msg):
        """Run a validation check"""
        self.checks_total += 1
        if condition:
            print(f"{GREEN}✓{RESET} {name}")
            self.checks_passed += 1
            return True
        else:
            print(f"{RED}✗{RESET} {name}")
            self.errors.append(error_msg)
            return False

    def warn(self, message):
        """Add a warning"""
        self.warnings.append(message)

    def validate_file_exists(self, file_path):
        """Check if .htaccess file exists"""
        print(f"\n{BOLD}Checking file existence:{RESET}")
        exists = file_path.exists()
        self.check(
            f"File exists: {file_path}",
            exists,
            f"File not found: {file_path}"
        )
        return exists

    def validate_file_not_empty(self, file_path):
        """Check if file is not empty"""
        print(f"\n{BOLD}Checking file content:{RESET}")
        size = file_path.stat().st_size
        self.check(
            "File is not empty",
            size > 0,
            f"File is empty: {file_path}"
        )
        return size > 0

    def validate_error_document(self, content):
        """Check if ErrorDocument 404 directive exists"""
        print(f"\n{BOLD}Checking 404 error handling:{RESET}")
        has_error_doc = 'ErrorDocument 404 /404.html' in content
        self.check(
            "ErrorDocument 404 directive present",
            has_error_doc,
            "Missing 'ErrorDocument 404 /404.html' directive"
        )
        return has_error_doc

    def validate_redirects(self, content):
        """Check if all expected redirects are present"""
        print(f"\n{BOLD}Checking 301 redirects:{RESET}")

        # Find all redirect lines
        lines = content.split('\n')
        redirect_lines = [line for line in lines if line.strip().startswith('Redirect 301')]

        # Check total count
        found_count = len(redirect_lines)
        expected_count = len(EXPECTED_REDIRECTS)
        self.check(
            f"Total redirects ({expected_count} expected)",
            found_count >= expected_count,
            f"Expected {expected_count} redirects, found {found_count}"
        )

        # Check each expected redirect
        missing_redirects = []
        for expected_path in EXPECTED_REDIRECTS:
            found = any(expected_path in line for line in redirect_lines)
            if not found:
                missing_redirects.append(expected_path)

        all_found = len(missing_redirects) == 0
        self.check(
            f"All {expected_count} required redirects present",
            all_found,
            f"Missing redirects: {', '.join(missing_redirects)}" if missing_redirects else ""
        )

        # Check for duplicates
        redirect_sources = []
        duplicates = []
        for line in redirect_lines:
            parts = line.split()
            if len(parts) >= 3:
                source = parts[2]
                if source in redirect_sources:
                    duplicates.append(source)
                redirect_sources.append(source)

        no_duplicates = len(duplicates) == 0
        self.check(
            "No duplicate redirects",
            no_duplicates,
            f"Duplicate redirects found: {', '.join(set(duplicates))}" if duplicates else ""
        )

        return all_found and no_duplicates

    def validate_rewrite_rules(self, content):
        """Check if mod_rewrite rules are present"""
        print(f"\n{BOLD}Checking mod_rewrite configuration:{RESET}")

        has_rewrite_engine = 'RewriteEngine On' in content
        self.check(
            "RewriteEngine On directive present",
            has_rewrite_engine,
            "Missing 'RewriteEngine On' directive"
        )

        has_https = 'RewriteCond %{HTTPS} off' in content
        self.check(
            "HTTPS redirect rule present",
            has_https,
            "Missing HTTPS redirect rule"
        )

        has_trailing_slash = any('trailing slash' in line.lower() for line in content.split('\n'))
        self.check(
            "Trailing slash rule present",
            has_trailing_slash,
            "Missing trailing slash redirect rule"
        )

        return has_rewrite_engine and has_https

    def validate_security_headers(self, content):
        """Check if security headers are present"""
        print(f"\n{BOLD}Checking security headers:{RESET}")

        has_xframe = 'X-Frame-Options' in content
        self.check(
            "X-Frame-Options header present",
            has_xframe,
            "Missing X-Frame-Options security header"
        )

        has_xss = 'X-XSS-Protection' in content
        self.check(
            "X-XSS-Protection header present",
            has_xss,
            "Missing X-XSS-Protection security header"
        )

        has_content_type = 'X-Content-Type-Options' in content
        self.check(
            "X-Content-Type-Options header present",
            has_content_type,
            "Missing X-Content-Type-Options security header"
        )

        return has_xframe and has_xss and has_content_type

    def validate_performance(self, content):
        """Check if performance optimizations are present"""
        print(f"\n{BOLD}Checking performance optimizations:{RESET}")

        has_caching = 'mod_expires' in content
        self.check(
            "Cache control (mod_expires) configured",
            has_caching,
            "Missing cache control configuration"
        )

        has_compression = 'mod_deflate' in content
        self.check(
            "Gzip compression (mod_deflate) configured",
            has_compression,
            "Missing Gzip compression configuration"
        )

        return has_caching and has_compression

def main():
    validator = HtaccessValidator()
    validator.print_header()

    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Check both static and public directories
    static_htaccess = project_root / 'static' / '.htaccess'
    public_htaccess = project_root / 'public' / '.htaccess'

    print(f"Project root: {project_root}")
    print(f"Validating .htaccess files...\n")

    # Validate static/.htaccess (source)
    print(f"{BOLD}{YELLOW}=== VALIDATING: static/.htaccess ==={RESET}")
    if not validator.validate_file_exists(static_htaccess):
        validator.print_summary()
        sys.exit(1)

    if not validator.validate_file_not_empty(static_htaccess):
        validator.print_summary()
        sys.exit(1)

    # Read content
    with open(static_htaccess, 'r') as f:
        content = f.read()

    # Run all validations
    validator.validate_error_document(content)
    validator.validate_redirects(content)
    validator.validate_rewrite_rules(content)
    validator.validate_security_headers(content)
    validator.validate_performance(content)

    # Validate public/.htaccess if it exists (after hugo build)
    if public_htaccess.exists():
        print(f"\n{BOLD}{YELLOW}=== VALIDATING: public/.htaccess ==={RESET}")

        with open(public_htaccess, 'r') as f:
            public_content = f.read()

        # Check if static and public are in sync
        files_match = content == public_content
        validator.check(
            "static/.htaccess matches public/.htaccess",
            files_match,
            "static/.htaccess and public/.htaccess differ - rebuild required"
        )
    else:
        validator.warn("public/.htaccess not found - run 'hugo --minify' before deployment")

    # Print summary and exit
    if validator.print_summary():
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
