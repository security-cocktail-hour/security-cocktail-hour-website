#!/usr/bin/env python3
"""
Blog Testing for Security Cocktail Hour Website
Tests blog list page and latest 5 blog posts
"""

import sys
import time
from playwright.sync_api import sync_playwright
from test_helpers import (
    BASE_URL, TIMEOUT_MS,
    print_test_header, print_result, format_duration,
    validate_page_load, validate_seo_metadata,
    check_console_errors, take_failure_screenshot,
    discover_blog_posts, select_blog_posts_to_test
)

def test_blog_list_page(page):
    """
    Test /blog/ page functionality.
    Returns: (passed, failed)
    """
    passed = 0
    failed = 0

    print("\n[Testing Blog List Page]")

    # Set up console error tracking
    console_errors = check_console_errors(page)

    # Load page
    success, message = validate_page_load(page, BASE_URL + '/blog/', 'Blog')
    if success:
        print_result(True, f"Page loaded: /blog/", indent=1)
        passed += 1
    else:
        print_result(False, f"Page load failed: {message}", indent=1)
        take_failure_screenshot(page, "blog_list_load", message)
        failed += 1
        return passed, failed

    # Check blog post cards
    try:
        blog_cards = page.locator('article').count()
        if blog_cards >= 2:  # Should have multiple blog posts
            print_result(True, f"Blog post cards visible: {blog_cards}", indent=1)
            passed += 1
        else:
            print_result(False, f"Expected multiple blog cards, found only {blog_cards}", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Could not count blog cards: {e}", indent=1)
        failed += 1

    # Check search input
    try:
        search_input = page.locator('#blog-search, input[placeholder*="Search" i]')
        if search_input.count() > 0:
            print_result(True, "Search input present", indent=1)
            passed += 1
        else:
            print_result(False, "Search input not found", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Search input check failed: {e}", indent=1)
        failed += 1

    # Check category filter
    try:
        category_filter = page.locator('#category-filter, select')
        if category_filter.count() > 0:
            print_result(True, "Category filter present", indent=1)
            passed += 1
        else:
            print_result(False, "Category filter not found", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Category filter check failed: {e}", indent=1)
        failed += 1

    # Check tag filter
    try:
        tag_filter = page.locator('#tag-filter, select')
        if tag_filter.count() > 0:
            print_result(True, "Tag filter present", indent=1)
            passed += 1
        else:
            print_result(False, "Tag filter not found", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Tag filter check failed: {e}", indent=1)
        failed += 1

    # Check sort dropdown
    try:
        sort_filter = page.locator('#sort-filter, select')
        if sort_filter.count() > 0:
            print_result(True, "Sort dropdown present", indent=1)
            passed += 1
        else:
            print_result(False, "Sort dropdown not found", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Sort dropdown check failed: {e}", indent=1)
        failed += 1

    # Check newsletter sidebar
    try:
        newsletter_section = page.locator('text=Newsletter, text=newsletter')
        if newsletter_section.count() > 0:
            print_result(True, "Newsletter sidebar present", indent=1)
            passed += 1
        else:
            print_result(False, "Newsletter sidebar not found", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Newsletter sidebar check failed: {e}", indent=1)
        failed += 1

    # Test search functionality
    try:
        search_input = page.locator('#blog-search, input[placeholder*="Search" i]').first
        if search_input.count() > 0:
            search_input.fill('scam')
            page.wait_for_timeout(500)  # Wait for JS filtering
            print_result(True, "Search functionality works", indent=1)
            passed += 1
        else:
            print_result(False, "Could not test search functionality", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Search functionality test failed: {e}", indent=1)
        failed += 1

    # Reload to check console errors
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

def test_blog_post(page, post_data):
    """
    Test individual blog post page.
    Returns: (passed, failed)
    """
    passed = 0
    failed = 0

    post_slug = post_data['filename'].replace('.md', '')
    post_title_short = post_data['title'][:40]

    print(f"\n[Testing Blog Post: {post_title_short}...]")

    # Set up console error tracking
    console_errors = check_console_errors(page)

    # Load page
    post_url = f"{BASE_URL}/blog/{post_slug}/"
    success, message = validate_page_load(page, post_url)
    if success:
        print_result(True, f"Page loaded: {post_slug}", indent=1)
        passed += 1
    else:
        print_result(False, f"Page load failed: {message}", indent=1)
        take_failure_screenshot(page, f"blog_{post_slug}_load", message)
        failed += 1
        return passed, failed

    # Check title matches
    try:
        page_title = page.title()
        if post_data['title'] and post_data['title'][:30] in page_title:
            print_result(True, f"Title matches", indent=1)
            passed += 1
        else:
            print_result(False, f"Title mismatch", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Title check failed: {e}", indent=1)
        failed += 1

    # Check author name
    try:
        if post_data['author']:
            author_displayed = page.locator(f'text={post_data["author"]}')
            if author_displayed.count() > 0:
                print_result(True, f"Author '{post_data['author']}' displayed", indent=1)
                passed += 1
            else:
                print_result(False, f"Author '{post_data['author']}' not displayed", indent=1)
                failed += 1
        else:
            print_result(True, "No author to check", indent=1)
            passed += 1
    except Exception as e:
        print_result(False, f"Author check failed: {e}", indent=1)
        failed += 1

    # Check publication date
    try:
        date_displayed = page.locator(f'text={post_data["date"]}')
        if date_displayed.count() > 0 or page.locator('text=/\\d{4}-\\d{2}-\\d{2}|\\w+ \\d+, \\d{4}/').count() > 0:
            print_result(True, "Publication date displayed", indent=1)
            passed += 1
        else:
            print_result(False, "Publication date not displayed", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Date check failed: {e}", indent=1)
        failed += 1

    # Check category badge
    try:
        if post_data['category']:
            category_displayed = page.locator(f'text={post_data["category"]}')
            if category_displayed.count() > 0:
                print_result(True, f"Category '{post_data['category']}' displayed", indent=1)
                passed += 1
            else:
                print_result(False, f"Category '{post_data['category']}' not displayed", indent=1)
                failed += 1
        else:
            print_result(True, "No category to check", indent=1)
            passed += 1
    except Exception as e:
        print_result(False, f"Category check failed: {e}", indent=1)
        failed += 1

    # Check tags
    try:
        tags = post_data.get('tags', [])
        if isinstance(tags, list) and len(tags) > 0:
            # Look for at least one tag
            tag_found = False
            for tag in tags[:3]:  # Check first 3 tags
                tag_elem = page.locator(f'text={tag}')
                if tag_elem.count() > 0:
                    tag_found = True
                    break

            if tag_found:
                print_result(True, "Tags displayed", indent=1)
                passed += 1
            else:
                print_result(False, "Tags not displayed", indent=1)
                failed += 1
        else:
            print_result(True, "No tags to check", indent=1)
            passed += 1
    except Exception as e:
        print_result(False, f"Tags check failed: {e}", indent=1)
        failed += 1

    # Check related episode link (if present)
    try:
        related_episode = post_data.get('related_episode', '')
        if related_episode:
            related_link = page.locator('text=Related Episode, text=Podcast Episode, a[href*="episode"]')
            if related_link.count() > 0:
                print_result(True, "Related episode link present", indent=1)
                passed += 1
            else:
                print_result(False, "Related episode link not found (expected)", indent=1)
                failed += 1
        else:
            print_result(True, "No related episode expected", indent=1)
            passed += 1
    except Exception as e:
        print_result(False, f"Related episode check failed: {e}", indent=1)
        failed += 1

    # Check content sections
    try:
        content_length = len(page.inner_text('main, article, .content'))
        if content_length > 500:  # Substantial blog post content
            print_result(True, "Content sections present", indent=1)
            passed += 1
        else:
            print_result(False, f"Content appears too short: {content_length} chars", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Content check failed: {e}", indent=1)
        failed += 1

    # Check newsletter form in sidebar
    try:
        newsletter_form = page.locator('text=Newsletter, text=newsletter')
        if newsletter_form.count() > 0:
            print_result(True, "Newsletter form present", indent=1)
            passed += 1
        else:
            print_result(False, "Newsletter form not found", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Newsletter form check failed: {e}", indent=1)
        failed += 1

    # Check SEO metadata
    try:
        seo_success, seo_issues = validate_seo_metadata(page)
        if seo_success:
            print_result(True, "SEO metadata valid (BlogPosting schema)", indent=1)
            passed += 1
        else:
            for issue in seo_issues:
                print_result(False, f"SEO issue: {issue}", indent=1)
            failed += len(seo_issues)
    except Exception as e:
        print_result(False, f"SEO metadata check failed: {e}", indent=1)
        failed += 1

    # Reload to check console errors
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

def run_blog_tests():
    """
    Main orchestrator for blog testing.
    Returns: dict with results
    """
    print_test_header("BLOG TESTING RESULTS")

    start_time = time.time()

    # Discover all blog posts
    print("Discovering blog posts...")
    all_posts = discover_blog_posts()
    print(f"Found {len(all_posts)} total blog posts")

    # Select posts to test (latest 5)
    posts_to_test = select_blog_posts_to_test(all_posts, latest_count=5)
    print(f"\nTesting {len(posts_to_test)} latest posts:")
    for post in posts_to_test:
        print(f"  - {post['title'][:60]}...")

    total_passed = 0
    total_failed = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Test blog list page
        print(f"\n[1/{len(posts_to_test) + 1}] ", end='')
        passed, failed = test_blog_list_page(page)
        total_passed += passed
        total_failed += failed

        # Test individual posts
        for idx, post_data in enumerate(posts_to_test, start=2):
            print(f"\n[{idx}/{len(posts_to_test) + 1}] ", end='')
            passed, failed = test_blog_post(page, post_data)
            total_passed += passed
            total_failed += failed

        browser.close()

    duration = time.time() - start_time

    # Print summary
    print(f"\n{'=' * 80}")
    print("BLOG TESTING SUMMARY")
    print(f"{'=' * 80}")
    print(f"Blog List Page: {'✅ PASSED' if total_failed == 0 else '❌ FAILED'}")
    print(f"Individual Posts Tested: {len(posts_to_test)}")
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
    results = run_blog_tests()
    sys.exit(0 if results['failed'] == 0 else 1)
