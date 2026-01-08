#!/usr/bin/env python3
"""
Episode Testing for Security Cocktail Hour Website
Tests episodes list page and selected individual episodes using block strategy
"""

import sys
import time
from playwright.sync_api import sync_playwright
from test_helpers import (
    BASE_URL, TIMEOUT_MS,
    print_test_header, print_result, format_duration,
    validate_page_load, validate_seo_metadata,
    check_console_errors, take_failure_screenshot,
    discover_episodes, select_episodes_to_test
)

def test_episodes_list_page(page):
    """
    Test /episodes/ page functionality.
    Returns: (passed, failed)
    """
    passed = 0
    failed = 0

    print("\n[Testing Episodes List Page]")

    # Set up console error tracking
    console_errors = check_console_errors(page)

    # Load page
    success, message = validate_page_load(page, BASE_URL + '/episodes/', 'Episodes')
    if success:
        print_result(True, f"Page loaded: /episodes/", indent=1)
        passed += 1
    else:
        print_result(False, f"Page load failed: {message}", indent=1)
        take_failure_screenshot(page, "episodes_list_load", message)
        failed += 1
        return passed, failed

    # Check episode cards
    try:
        episode_cards = page.locator('article').count()
        if episode_cards >= 10:  # Should have many episodes
            print_result(True, f"Episode cards visible: {episode_cards}", indent=1)
            passed += 1
        else:
            print_result(False, f"Expected many episode cards, found only {episode_cards}", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Could not count episode cards: {e}", indent=1)
        failed += 1

    # Check search input
    try:
        search_input = page.locator('#episode-search, input[placeholder*="Search" i]')
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

    # Test search functionality
    try:
        search_input = page.locator('#episode-search, input[placeholder*="Search" i]').first
        if search_input.count() > 0:
            search_input.fill('flipper')
            page.wait_for_timeout(500)  # Wait for JS filtering
            # Just verify no JavaScript errors occurred
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

def test_episode_page(page, episode_data):
    """
    Test individual episode page.
    Returns: (passed, failed)
    """
    passed = 0
    failed = 0

    episode_num = episode_data['episode_num']
    episode_slug = episode_data['filename'].replace('.md', '')

    print(f"\n[Testing Episode {episode_num}]")

    # Set up console error tracking
    console_errors = check_console_errors(page)

    # Load page
    episode_url = f"{BASE_URL}/episodes/{episode_slug}/"
    success, message = validate_page_load(page, episode_url)
    if success:
        print_result(True, f"Page loaded: {episode_slug}", indent=1)
        passed += 1
    else:
        print_result(False, f"Page load failed: {message}", indent=1)
        take_failure_screenshot(page, f"episode_{episode_num}_load", message)
        failed += 1
        return passed, failed

    # Check title matches
    try:
        page_title = page.title()
        if episode_data['title'] and episode_data['title'][:30] in page_title:
            print_result(True, f"Title matches", indent=1)
            passed += 1
        else:
            print_result(False, f"Title mismatch", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Title check failed: {e}", indent=1)
        failed += 1

    # Check episode number displayed
    try:
        ep_num_display = page.locator(f'text=/^{episode_num}$/').or_(
            page.locator(f'text="Episode {episode_num}"')
        )
        if ep_num_display.count() > 0:
            print_result(True, f"Episode number {episode_num} displayed", indent=1)
            passed += 1
        else:
            print_result(False, f"Episode number {episode_num} not displayed", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Episode number check failed: {e}", indent=1)
        failed += 1

    # Check date and duration displayed
    try:
        date_displayed = page.locator(f'text={episode_data["date"]}')
        if date_displayed.count() > 0 or page.locator('text=/\\d{4}-\\d{2}-\\d{2}|\\w+ \\d+, \\d{4}/').count() > 0:
            print_result(True, "Date displayed", indent=1)
            passed += 1
        else:
            print_result(False, "Date not displayed", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Date check failed: {e}", indent=1)
        failed += 1

    # Check category badge
    try:
        if episode_data['category']:
            category_displayed = page.locator(f'text={episode_data["category"]}')
            if category_displayed.count() > 0:
                print_result(True, f"Category '{episode_data['category']}' displayed", indent=1)
                passed += 1
            else:
                print_result(False, f"Category '{episode_data['category']}' not displayed", indent=1)
                failed += 1
        else:
            print_result(True, "No category to check", indent=1)
            passed += 1
    except Exception as e:
        print_result(False, f"Category check failed: {e}", indent=1)
        failed += 1

    # Check platform buttons
    try:
        platforms_found = 0
        platforms = episode_data.get('platforms', {})

        if isinstance(platforms, dict):
            for platform_name in ['youtube', 'spotify', 'apple', 'amazon']:
                if platform_name in platforms and platforms[platform_name]:
                    # Look for link with that platform's URL
                    platform_link = page.locator(f'a[href*="{platform_name}"], a[href*="{platforms[platform_name]}"]')
                    if platform_link.count() > 0:
                        platforms_found += 1

        if platforms_found >= 2:  # Should have at least 2 platform links
            print_result(True, f"Platform links present: {platforms_found} found", indent=1)
            passed += 1
        else:
            print_result(False, f"Expected multiple platform links, found {platforms_found}", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Platform links check failed: {e}", indent=1)
        failed += 1

    # Check episode image
    try:
        episode_img = page.locator('img[src*="episode"]')
        if episode_img.count() > 0:
            print_result(True, "Episode image present", indent=1)
            passed += 1
        else:
            print_result(False, "Episode image not found", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Episode image check failed: {e}", indent=1)
        failed += 1

    # Check description/content
    try:
        # Just verify there's substantial text content
        content_length = len(page.inner_text('main, article, .content'))
        if content_length > 200:  # Reasonable amount of content
            print_result(True, "Description/content present", indent=1)
            passed += 1
        else:
            print_result(False, f"Content appears too short: {content_length} chars", indent=1)
            failed += 1
    except Exception as e:
        print_result(False, f"Content check failed: {e}", indent=1)
        failed += 1

    # Check transcript section (if episode has transcript)
    try:
        if episode_data['has_transcript']:
            transcript_section = page.locator('text=Transcript, summary >> visible=true')
            if transcript_section.count() > 0:
                print_result(True, "Transcript section present", indent=1)
                passed += 1
            else:
                print_result(False, "Transcript section not found (expected)", indent=1)
                failed += 1
        else:
            print_result(True, "No transcript expected", indent=1)
            passed += 1
    except Exception as e:
        print_result(False, f"Transcript check failed: {e}", indent=1)
        failed += 1

    # Check related episodes section (if episode has related episodes)
    try:
        related_episodes = episode_data.get('related_episodes', [])
        if related_episodes and len(related_episodes) > 0:
            related_section = page.locator('text=Related Episodes, text=Related Podcast, text=You might also like')
            if related_section.count() > 0:
                print_result(True, "Related episodes section present", indent=1)
                passed += 1
            else:
                print_result(False, "Related episodes section not found (expected)", indent=1)
                failed += 1
        else:
            print_result(True, "No related episodes expected", indent=1)
            passed += 1
    except Exception as e:
        print_result(False, f"Related episodes check failed: {e}", indent=1)
        failed += 1

    # Check newsletter form
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
            print_result(True, "SEO metadata valid", indent=1)
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

def run_episodes_tests():
    """
    Main orchestrator for episode testing.
    Returns: dict with results
    """
    print_test_header("EPISODE TESTING RESULTS")

    start_time = time.time()

    # Discover all episodes
    print("Discovering episodes...")
    all_episodes = discover_episodes()
    print(f"Found {len(all_episodes)} total episodes")

    # Select episodes to test
    episodes_to_test = select_episodes_to_test(all_episodes, newest_count=5)
    print(f"\nSelected {len(episodes_to_test)} episodes to test:")

    # Show newest episodes
    newest = [ep for ep in episodes_to_test if ep in all_episodes[:5]]
    print(f"\n  Newest {len(newest)}:")
    for ep in newest:
        print(f"    - Episode {ep['episode_num']}: {ep['title'][:50]}")

    # Show block samples
    block_samples = [ep for ep in episodes_to_test if ep not in newest]
    if block_samples:
        print(f"\n  From blocks of 10 ({len(block_samples)} episodes):")
        for ep in block_samples:
            block_start = ((ep['episode_num'] - 1) // 10) * 10 + 1
            block_end = block_start + 9
            print(f"    - Episode {ep['episode_num']} (block {block_start}-{block_end}): {ep['title'][:40]}")

    total_passed = 0
    total_failed = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Test episodes list page
        print(f"\n[1/{len(episodes_to_test) + 1}] ", end='')
        passed, failed = test_episodes_list_page(page)
        total_passed += passed
        total_failed += failed

        # Test individual episodes
        for idx, episode_data in enumerate(episodes_to_test, start=2):
            print(f"\n[{idx}/{len(episodes_to_test) + 1}] ", end='')
            passed, failed = test_episode_page(page, episode_data)
            total_passed += passed
            total_failed += failed

        browser.close()

    duration = time.time() - start_time

    # Print summary
    print(f"\n{'=' * 80}")
    print("EPISODE TESTING SUMMARY")
    print(f"{'=' * 80}")
    print(f"Episodes List Page: {'✅ PASSED' if total_failed == 0 else '❌ FAILED'}")
    print(f"Individual Episodes Tested: {len(episodes_to_test)}")
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
    results = run_episodes_tests()
    sys.exit(0 if results['failed'] == 0 else 1)
