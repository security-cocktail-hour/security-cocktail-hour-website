#!/usr/bin/env python3
"""
Static Pages Testing for Security Cocktail Hour Website
Tests all 8 static pages: homepage, about, contact, partnership, resources, newsletter, privacy, terms
"""

import sys
import time
from playwright.sync_api import sync_playwright
from test_helpers import (
    BASE_URL, TIMEOUT_MS,
    print_test_header, print_result, format_duration,
    validate_page_load, validate_seo_metadata, validate_navigation_links,
    check_console_errors, take_failure_screenshot, validate_form_elements
)

# Expected navigation links present on all pages
NAV_LINKS = {
    'Episodes': '/episodes/',
    'Blog': '/blog/',
    'About': '/about/',
    'Resources': '/resources/',
    'Partnership': '/partnership/',
    'Contact': '/contact/'
}

def test_page(page, url, page_name, expected_title_substring, checks):
    """
    Generic page testing function.
    checks: dict of check names and check functions
    Returns: (passed_count, failed_count)
    """
    passed = 0
    failed = 0

    print(f"\n[Testing {page_name}]")

    # Set up console error tracking
    console_errors = check_console_errors(page)

    # Load page
    success, message = validate_page_load(page, url, expected_title_substring)
    if success:
        print_result(True, f"Page loaded: {url}", indent=1)
        print_result(True, f"Title: {message}", indent=1)
        passed += 2
    else:
        print_result(False, f"Page load failed: {message}", indent=1)
        take_failure_screenshot(page, f"{page_name}_load", message)
        failed += 2
        return passed, failed

    # Run custom checks
    for check_name, check_func in checks.items():
        try:
            check_success, check_message = check_func(page)
            if check_success:
                print_result(True, check_name, indent=1)
                passed += 1
            else:
                print_result(False, f"{check_name}: {check_message}", indent=1)
                take_failure_screenshot(page, f"{page_name}_{check_name}", check_message)
                failed += 1
        except Exception as e:
            print_result(False, f"{check_name}: {str(e)}", indent=1)
            take_failure_screenshot(page, f"{page_name}_{check_name}", str(e))
            failed += 1

    # Check navigation links
    nav_success, nav_issues = validate_navigation_links(page, NAV_LINKS)
    if nav_success:
        print_result(True, "Navigation links present", indent=1)
        passed += 1
    else:
        for issue in nav_issues:
            print_result(False, issue, indent=1)
        failed += len(nav_issues)

    # Check SEO metadata
    seo_success, seo_issues = validate_seo_metadata(page)
    if seo_success:
        print_result(True, "SEO metadata present", indent=1)
        passed += 1
    else:
        for issue in seo_issues:
            print_result(False, issue, indent=1)
        failed += len(seo_issues)

    # Reload to capture console errors
    page.reload()
    page.wait_for_load_state('networkidle')

    if len(console_errors) == 0:
        print_result(True, "No console errors", indent=1)
        passed += 1
    else:
        for error in console_errors:
            print_result(False, f"Console error: {error}", indent=1)
        failed += len(console_errors)

    return passed, failed

def test_homepage(page):
    """Test homepage (/)"""
    def check_hero_section(page):
        heading = page.locator('h1:has-text("Security Cocktail Hour")')
        if heading.count() == 0:
            return False, "Hero heading not found"
        tagline = page.locator('text=Cybersecurity pros talking shop')
        if tagline.count() == 0:
            return False, "Hero tagline not found"
        return True, "Hero section present"

    def check_latest_episode(page):
        latest = page.locator('text=Latest Episode')
        if latest.count() == 0:
            return False, "Latest Episode section not found"
        return True, "Latest Episode section present"

    def check_recent_episodes(page):
        heading = page.locator('h2:has-text("Recent Episodes")')
        if heading.count() == 0:
            return False, "Recent Episodes heading not found"
        return True, "Recent Episodes section present"

    def check_featured_blog(page):
        heading = page.locator('h2:has-text("Featured Blog Posts")')
        if heading.count() == 0:
            return False, "Featured Blog Posts heading not found"
        return True, "Featured Blog Posts section present"

    def check_newsletter_form(page):
        heading = page.locator('h2:has-text("Join Our Newsletter")')
        if heading.count() == 0:
            return False, "Newsletter heading not found"
        subscribe_btn = page.locator('button:has-text("Subscribe")')
        if subscribe_btn.count() == 0:
            return False, "Subscribe button not found"
        return True, "Newsletter form present"

    checks = {
        'Hero section': check_hero_section,
        'Latest Episode section': check_latest_episode,
        'Recent Episodes section': check_recent_episodes,
        'Featured Blog Posts section': check_featured_blog,
        'Newsletter form': check_newsletter_form
    }

    return test_page(page, BASE_URL + '/', 'Homepage', 'Security Cocktail Hour', checks)

def test_about(page):
    """Test about page (/about/)"""
    def check_about_content(page):
        heading = page.locator('h1:has-text("About"), h2:has-text("About")')
        if heading.count() == 0:
            return False, "About heading not found"
        return True, "About content present"

    def check_hosts_section(page):
        hosts = page.locator('text=Hosted by')
        if hosts.count() == 0:
            return False, "Hosts section not found"
        return True, "Hosts section present"

    checks = {
        'About content': check_about_content,
        'Hosts section': check_hosts_section
    }

    return test_page(page, BASE_URL + '/about/', 'About Page', 'About', checks)

def test_contact(page):
    """Test contact page (/contact/)"""
    def check_contact_form(page):
        required_fields = ['name', 'email', 'message']
        success, issues = validate_form_elements(page, required_fields)
        if not success:
            return False, ', '.join(issues)

        submit_btn = page.locator('button[type="submit"], input[type="submit"]')
        if submit_btn.count() == 0:
            return False, "Submit button not found"

        return True, "Contact form present with all fields"

    def check_formspree_action(page):
        form = page.locator('form[action*="formspree"]')
        if form.count() == 0:
            return False, "Formspree form action not found"
        return True, "Formspree integration present"

    checks = {
        'Contact form': check_contact_form,
        'Formspree integration': check_formspree_action
    }

    return test_page(page, BASE_URL + '/contact/', 'Contact Page', 'Contact', checks)

def test_partnership(page):
    """Test partnership page (/partnership/)"""
    def check_partnership_content(page):
        heading = page.locator('h1:has-text("Partnership"), h2:has-text("Partnership")')
        if heading.count() == 0:
            return False, "Partnership heading not found"
        return True, "Partnership content present"

    def check_sponsorship_tiers(page):
        # Look for sponsorship-related content
        sponsor_text = page.locator('text=Sponsor, text=sponsorship')
        if sponsor_text.count() == 0:
            return False, "Sponsorship information not found"
        return True, "Sponsorship tiers present"

    checks = {
        'Partnership content': check_partnership_content,
        'Sponsorship information': check_sponsorship_tiers
    }

    return test_page(page, BASE_URL + '/partnership/', 'Partnership Page', 'Partnership', checks)

def test_resources(page):
    """Test resources page (/resources/)"""
    def check_resources_content(page):
        heading = page.locator('h1:has-text("Resources"), h2:has-text("Resources")')
        if heading.count() == 0:
            return False, "Resources heading not found"
        return True, "Resources content present"

    def check_resource_categories(page):
        # Check for some expected resource categories
        links = page.locator('a[href^="http"]')
        if links.count() < 5:  # Should have multiple external resource links
            return False, f"Expected multiple resource links, found {links.count()}"
        return True, "Resource links present"

    checks = {
        'Resources content': check_resources_content,
        'Resource categories': check_resource_categories
    }

    return test_page(page, BASE_URL + '/resources/', 'Resources Page', 'Resources', checks)

def test_newsletter(page):
    """Test newsletter page (/newsletter/)"""
    def check_newsletter_form(page):
        heading = page.locator('text=Newsletter, text=newsletter')
        if heading.count() == 0:
            return False, "Newsletter heading not found"

        subscribe_btn = page.locator('button:has-text("Subscribe"), input[value*="Subscribe"]')
        if subscribe_btn.count() == 0:
            return False, "Subscribe button not found"

        return True, "Newsletter form present"

    def check_mailchimp_integration(page):
        form = page.locator('form[action*="list-manage"], form[action*="mailchimp"]')
        if form.count() == 0:
            return False, "Mailchimp form action not found"
        return True, "Mailchimp integration present"

    checks = {
        'Newsletter form': check_newsletter_form,
        'Mailchimp integration': check_mailchimp_integration
    }

    return test_page(page, BASE_URL + '/newsletter/', 'Newsletter Page', 'Newsletter', checks)

def test_privacy(page):
    """Test privacy policy page (/privacy/)"""
    def check_privacy_content(page):
        heading = page.locator('text=Privacy, text=privacy')
        if heading.count() == 0:
            return False, "Privacy heading not found"

        # Look for legal text indicators
        legal_text = page.locator('text=policy, text=data, text=information')
        if legal_text.count() < 3:
            return False, "Privacy policy content appears incomplete"

        return True, "Privacy policy content present"

    checks = {
        'Privacy policy content': check_privacy_content
    }

    return test_page(page, BASE_URL + '/privacy/', 'Privacy Page', 'Privacy', checks)

def test_terms(page):
    """Test terms of service page (/terms/)"""
    def check_terms_content(page):
        heading = page.locator('text=Terms, text=terms')
        if heading.count() == 0:
            return False, "Terms heading not found"

        # Look for legal text indicators
        legal_text = page.locator('text=service, text=agreement, text=use')
        if legal_text.count() < 2:
            return False, "Terms content appears incomplete"

        return True, "Terms of service content present"

    checks = {
        'Terms content': check_terms_content
    }

    return test_page(page, BASE_URL + '/terms/', 'Terms Page', 'Terms', checks)

def run_all_static_tests():
    """
    Main test orchestrator for static pages.
    Returns: dict with results
    """
    print_test_header("STATIC PAGES TEST RESULTS")

    start_time = time.time()
    total_passed = 0
    total_failed = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Test each page
        tests = [
            ('1/8', test_homepage),
            ('2/8', test_about),
            ('3/8', test_contact),
            ('4/8', test_partnership),
            ('5/8', test_resources),
            ('6/8', test_newsletter),
            ('7/8', test_privacy),
            ('8/8', test_terms)
        ]

        for label, test_func in tests:
            print(f"\n[{label}] ", end='')
            passed, failed = test_func(page)
            total_passed += passed
            total_failed += failed

        browser.close()

    duration = time.time() - start_time

    # Print summary
    print(f"\n{'=' * 80}")
    print("STATIC PAGES TEST SUMMARY")
    print(f"{'=' * 80}")
    print(f"Pages Tested: 8")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")
    print(f"Duration: {format_duration(duration)}")
    print(f"{'=' * 80}\n")

    return {
        'passed': total_passed,
        'failed': total_failed,
        'duration': duration
    }

if __name__ == '__main__':
    results = run_all_static_tests()
    sys.exit(0 if results['failed'] == 0 else 1)
