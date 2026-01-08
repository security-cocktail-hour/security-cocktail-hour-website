#!/usr/bin/env python3
"""
Master Test Runner for Security Cocktail Hour Website
Runs all pre-deployment tests and provides comprehensive summary.

Usage:
    python run_all_tests.py              # Run all tests
    python run_all_tests.py --static     # Run only static page tests
    python run_all_tests.py --episodes   # Run only episode tests
    python run_all_tests.py --blog       # Run only blog tests
"""

import sys
import time
import argparse
from test_helpers import format_duration, SCREENSHOT_DIR
from test_static_pages import run_all_static_tests
from test_episodes import run_episodes_tests
from test_blog import run_blog_tests

def print_banner():
    """Print startup banner."""
    print("=" * 80)
    print("SECURITY COCKTAIL HOUR - PRE-DEPLOYMENT TEST SUITE")
    print("=" * 80)
    print()

def print_final_summary(results):
    """
    Print comprehensive summary of all tests.

    results = {
        'static': {'passed': 8, 'failed': 0, 'duration': 45.3},
        'episodes': {'passed': 15, 'failed': 1, 'duration': 222.5},
        'blog': {'passed': 4, 'failed': 0, 'duration': 78.2}
    }
    """
    print()
    print("=" * 80)
    print("FINAL TEST SUMMARY")
    print("=" * 80)

    total_passed = 0
    total_failed = 0
    total_duration = 0.0

    # Static pages summary
    if 'static' in results:
        total_passed += results['static']['passed']
        total_failed += results['static']['failed']
        total_duration += results['static']['duration']

        status = '✅ PASSED' if results['static']['failed'] == 0 else '❌ FAILED'
        print(f"\nStatic Pages:  {status}")
        print(f"  Passed: {results['static']['passed']}")
        print(f"  Failed: {results['static']['failed']}")
        print(f"  Duration: {format_duration(results['static']['duration'])}")

    # Episodes summary
    if 'episodes' in results:
        total_passed += results['episodes']['passed']
        total_failed += results['episodes']['failed']
        total_duration += results['episodes']['duration']

        status = '✅ PASSED' if results['episodes']['failed'] == 0 else '❌ FAILED'
        print(f"\nEpisodes:      {status}")
        print(f"  Passed: {results['episodes']['passed']}")
        print(f"  Failed: {results['episodes']['failed']}")
        print(f"  Duration: {format_duration(results['episodes']['duration'])}")

    # Blog summary
    if 'blog' in results:
        total_passed += results['blog']['passed']
        total_failed += results['blog']['failed']
        total_duration += results['blog']['duration']

        status = '✅ PASSED' if results['blog']['failed'] == 0 else '❌ FAILED'
        print(f"\nBlog:          {status}")
        print(f"  Passed: {results['blog']['passed']}")
        print(f"  Failed: {results['blog']['failed']}")
        print(f"  Duration: {format_duration(results['blog']['duration'])}")

    print(f"\n{'=' * 80}")
    print(f"TOTAL: {total_passed} passed, {total_failed} failed")
    print(f"Duration: {format_duration(total_duration)}")
    print(f"{'=' * 80}")

    if total_failed == 0:
        print("\n✅ ALL TESTS PASSED - Ready for deployment!")
    else:
        print(f"\n❌ {total_failed} TEST(S) FAILED - Review errors before deployment")
        print(f"\nFailed test screenshots saved in: {SCREENSHOT_DIR}/")

def main():
    """Main test orchestrator."""
    parser = argparse.ArgumentParser(
        description='Run pre-deployment tests for Security Cocktail Hour website',
        epilog='Run all tests before deploying to production to catch issues early.'
    )
    parser.add_argument('--static', action='store_true',
                        help='Run only static page tests (homepage, about, contact, etc.)')
    parser.add_argument('--episodes', action='store_true',
                        help='Run only episode tests (episodes list + selected episodes)')
    parser.add_argument('--blog', action='store_true',
                        help='Run only blog tests (blog list + latest posts)')
    args = parser.parse_args()

    # If no specific test specified, run all
    run_all = not (args.static or args.episodes or args.blog)

    print_banner()

    start_time = time.time()
    results = {}

    # Determine which suites to run
    suites_to_run = []
    if run_all or args.static:
        suites_to_run.append(('static', 'Static Pages Tests', run_all_static_tests))
    if run_all or args.episodes:
        suites_to_run.append(('episodes', 'Episodes Tests', run_episodes_tests))
    if run_all or args.blog:
        suites_to_run.append(('blog', 'Blog Tests', run_blog_tests))

    # Run selected test suites
    for idx, (key, name, test_func) in enumerate(suites_to_run, start=1):
        print(f"\n[SUITE {idx}/{len(suites_to_run)}] Running {name}...")
        try:
            results[key] = test_func()
        except Exception as e:
            print(f"\n❌ ERROR: Test suite '{name}' failed with exception: {e}")
            results[key] = {'passed': 0, 'failed': 1, 'duration': 0}

    # Print final summary
    print_final_summary(results)

    # Exit code
    total_failed = sum(r.get('failed', 0) for r in results.values())
    sys.exit(0 if total_failed == 0 else 1)

if __name__ == '__main__':
    main()
