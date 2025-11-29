#!/usr/bin/env python3
"""
Title Tag Audit Script
Analyzes all title tags across the Security Cocktail Hour website
Checks both regular titles and optional SEO titles for episodes
"""

import os
import re
from pathlib import Path

# Character limits for title tags (what appears in search results)
TARGET_LENGTH = 60  # Optimal for search results
WARNING_LENGTH = 70  # Warning zone
MAX_RECOMMENDED = 60  # Hard recommendation

def extract_title(file_path):
    """Extract title from markdown front matter"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    return match.group(1).strip() if match else None

def extract_seo_title(file_path):
    """Extract optional seo_title from markdown front matter"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'^seo_title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    return match.group(1).strip() if match else None

def suggest_shortened_title(title, target=TARGET_LENGTH):
    """Suggest a shortened version of the title"""
    if len(title) <= target:
        return title

    # Remove guest information in parentheses or after "with"
    shortened = re.sub(r'\s*\([^)]+\)\s*$', '', title)
    shortened = re.sub(r'\s+with\s+[^|]+$', '', shortened)

    if len(shortened) <= target:
        return shortened.strip()

    # Try to cut at a separator (| or :)
    parts = re.split(r'\s*[|:]\s*', title)
    if len(parts) > 1:
        # Keep the most important part (usually the first)
        result = parts[0].strip()
        if len(result) <= target and len(result) > 20:  # Make sure it's substantial
            return result

    # Cut at word boundary
    words = title.split()
    result = ""
    for word in words:
        if len(result) + len(word) + 1 <= target:
            result += word + " "
        else:
            break

    return result.strip()

def categorize_length(length):
    """Categorize title length for reporting"""
    if length <= TARGET_LENGTH:
        return "optimal"
    elif length <= WARNING_LENGTH:
        return "acceptable"
    else:
        return "too_long"

def main():
    base_dir = Path("/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website")

    results = {
        'optimal': [],          # ≤60 characters (effective title)
        'acceptable': [],       # 61-70 characters (effective title)
        'too_long': [],         # >70 characters (effective title)
        'has_seo_title': [],    # Episodes with seo_title field
        'identical_titles': [], # Episodes where title == seo_title (pointless)
    }

    # Check episodes
    episodes_dir = base_dir / "content" / "episodes"
    for episode_file in sorted(episodes_dir.glob("episode-*.md")):
        title = extract_title(episode_file)
        seo_title = extract_seo_title(episode_file)

        if not title:
            continue

        relative_path = str(episode_file.relative_to(base_dir))

        # Determine which title will be used in <title> tag
        effective_title = seo_title if seo_title else title
        effective_length = len(effective_title)
        category = categorize_length(effective_length)

        # Check if title and seo_title are identical (pointless duplication)
        titles_identical = seo_title and (title == seo_title)

        item = {
            'type': 'Episode',
            'file': relative_path,
            'title': title,
            'title_length': len(title),
            'seo_title': seo_title,
            'seo_title_length': len(seo_title) if seo_title else None,
            'effective_title': effective_title,
            'effective_length': effective_length,
            'titles_identical': titles_identical
        }

        results[category].append(item)

        if seo_title:
            results['has_seo_title'].append(item)

        if titles_identical:
            results['identical_titles'].append(item)

    # Check blog posts
    blog_dir = base_dir / "content" / "blog"
    if blog_dir.exists():
        for blog_file in sorted(blog_dir.glob("*.md")):
            if blog_file.name == "_index.md":
                continue

            title = extract_title(blog_file)
            seo_title = extract_seo_title(blog_file)

            if not title:
                continue

            relative_path = str(blog_file.relative_to(base_dir))

            # Determine which title will be used in <title> tag
            effective_title = seo_title if seo_title else title
            effective_length = len(effective_title)
            category = categorize_length(effective_length)

            # Check if title and seo_title are identical (pointless duplication)
            titles_identical = seo_title and (title == seo_title)

            item = {
                'type': 'Blog Post',
                'file': relative_path,
                'title': title,
                'title_length': len(title),
                'seo_title': seo_title,
                'seo_title_length': len(seo_title) if seo_title else None,
                'effective_title': effective_title,
                'effective_length': effective_length,
                'titles_identical': titles_identical
            }

            results[category].append(item)

            if seo_title:
                results['has_seo_title'].append(item)

            if titles_identical:
                results['identical_titles'].append(item)

    # Check other content pages
    content_dir = base_dir / "content"
    for content_file in content_dir.glob("*.md"):
        title = extract_title(content_file)
        seo_title = extract_seo_title(content_file)

        if not title:
            continue

        relative_path = str(content_file.relative_to(base_dir))

        # Determine which title will be used in <title> tag
        effective_title = seo_title if seo_title else title
        effective_length = len(effective_title)
        category = categorize_length(effective_length)

        # Check if title and seo_title are identical (pointless duplication)
        titles_identical = seo_title and (title == seo_title)

        item = {
            'type': 'Page',
            'file': relative_path,
            'title': title,
            'title_length': len(title),
            'seo_title': seo_title,
            'seo_title_length': len(seo_title) if seo_title else None,
            'effective_title': effective_title,
            'effective_length': effective_length,
            'titles_identical': titles_identical
        }

        results[category].append(item)

        if seo_title:
            results['has_seo_title'].append(item)

        if titles_identical:
            results['identical_titles'].append(item)

    # Generate report
    total_pages = len(results['optimal']) + len(results['acceptable']) + len(results['too_long'])

    print("=" * 80)
    print("TITLE TAG AUDIT REPORT")
    print("=" * 80)

    # Definitions section
    print("\nHOW TITLES WORK:")
    print("-" * 80)
    print("There are only TWO titles:")
    print()
    print("1. title (front matter field)")
    print("   - The full, real episode title")
    print("   - Used in: H1 heading, episode listings, Schema.org markup, RSS feeds")
    print("   - Schema.org title used by search engines for indexing")
    print("   - Schema.org: No hard limit, but ≤150 chars is optimal")
    print()
    print("2. seo_title (optional front matter field)")
    print("   - Shortened version for display to user in search engines")
    print("   - Used ONLY in: HTML <title> tag")
    print("   - The <title> tag IS what appears in search engine results")
    print("   - Target: 55-60 chars optimal, 60 chars MAX")
    print()
    print("If seo_title is present: <title> tag uses seo_title")
    print("If seo_title is absent:  <title> tag uses title")
    print()
    print("LENGTH TARGETS (for <title> tag / search results):")
    print(f"  Optimal:     ≤{TARGET_LENGTH} characters (fully displayed on all devices)")
    print(f"  Acceptable:  {TARGET_LENGTH+1}-{WARNING_LENGTH} characters (may truncate on mobile)")
    print(f"  Too Long:    >{WARNING_LENGTH} characters (will be truncated in search results)")
    print("-" * 80)

    print(f"\nTotal Pages Analyzed: {total_pages}")
    print(f"Optimal (≤{TARGET_LENGTH} chars): {len(results['optimal'])} ({len(results['optimal'])/total_pages*100:.1f}%)")
    print(f"Acceptable ({TARGET_LENGTH+1}-{WARNING_LENGTH} chars): {len(results['acceptable'])} ({len(results['acceptable'])/total_pages*100:.1f}%)")
    print(f"Too Long (>{WARNING_LENGTH} chars): {len(results['too_long'])} ({len(results['too_long'])/total_pages*100:.1f}%)")
    print(f"\nPages with SEO Title: {len(results['has_seo_title'])}")

    if results['identical_titles']:
        print(f"⚠️  Identical Titles (pointless duplication): {len(results['identical_titles'])}")

    # Identical Titles Warning
    if results['identical_titles']:
        print("\n" + "=" * 80)
        print("⚠️  IDENTICAL TITLES (Pointless Duplication)")
        print("=" * 80)
        print("These pages have seo_title identical to title - no benefit!")
        print("Either remove seo_title or create a shorter version.\n")

        for item in results['identical_titles']:
            print(f"  {item['type']}: {item['file']}")
            print(f"  Both title and seo_title are: \"{item['title']}\" ({item['title_length']} chars)")
            print(f"  ⚠️  Remove seo_title field or create a shorter version")
            print()

    # Too Long Titles
    if results['too_long']:
        print("\n" + "=" * 80)
        print(f"TITLES EXCEEDING {WARNING_LENGTH} CHARACTERS (Likely Truncated)")
        print("=" * 80)

        # Sort by effective length, longest first
        results['too_long'].sort(key=lambda x: x['effective_length'], reverse=True)

        for i, item in enumerate(results['too_long'], 1):
            print(f"\n{i}. {item['type']}: {item['file']}")
            print(f"   Effective Title Length: {item['effective_length']} characters (OVER target by {item['effective_length'] - TARGET_LENGTH})")

            if item['seo_title']:
                print(f"   Title ({item['title_length']} chars): \"{item['title']}\"")
                print(f"   SEO Title ({item['seo_title_length']} chars): \"{item['seo_title']}\"")
                print(f"   ⚠️  SEO title is being used but is still too long!")
            else:
                print(f"   Title: \"{item['title']}\"")
                print(f"   ⚠️  No seo_title field - consider adding one")

            # Generate suggestion
            suggestion = suggest_shortened_title(item['title'])
            if suggestion != item['title'] and len(suggestion) <= TARGET_LENGTH:
                print(f"\n   Suggested SEO Title ({len(suggestion)} chars):")
                print(f"   \"{suggestion}\"")
                print(f"   Add to front matter: seo_title: \"{suggestion}\"")

            print("-" * 80)

    # Acceptable Length Titles
    if results['acceptable']:
        print("\n" + "=" * 80)
        print(f"TITLES IN ACCEPTABLE RANGE ({TARGET_LENGTH+1}-{WARNING_LENGTH} characters)")
        print("=" * 80)
        print("These may be truncated on mobile devices but are generally OK\n")

        results['acceptable'].sort(key=lambda x: x['effective_length'], reverse=True)

        for item in results['acceptable']:
            if item['seo_title']:
                status = "✓ Has SEO title"
                if item['titles_identical']:
                    status = "⚠️  Identical!"
            else:
                status = "○ No SEO title"

            print(f"  {status} | {item['effective_length']} chars | {item['type']}: {item['effective_title'][:60]}...")

    # Optimal Titles
    print("\n" + "=" * 80)
    print(f"OPTIMAL TITLES (≤{TARGET_LENGTH} characters)")
    print("=" * 80)

    # Group by type
    for page_type in ['Page', 'Blog Post', 'Episode']:
        type_items = [x for x in results['optimal'] if x['type'] == page_type]
        if type_items:
            print(f"\n{page_type}s ({len(type_items)}):")
            for item in type_items:
                if item['seo_title']:
                    if item['titles_identical']:
                        status = "⚠️  Dup"
                    else:
                        status = "✓ SEO"
                else:
                    status = "○ Full"
                print(f"  {status} | {item['effective_length']:2d} chars | {item['effective_title'][:70]}")

    # SEO Title Implementation Summary
    if results['has_seo_title']:
        print("\n" + "=" * 80)
        print(f"SEO TITLE IMPLEMENTATION SUMMARY")
        print("=" * 80)
        print(f"Total pages with seo_title field: {len(results['has_seo_title'])}")
        print("\nPages using SEO titles:")

        for item in results['has_seo_title']:
            if item['titles_identical']:
                print(f"\n  ⚠️  {item['type']}: {item['file']}")
                print(f"  Full Title: \"{item['title']}\" ({item['title_length']} chars)")
                print(f"  SEO Title: \"{item['seo_title']}\" ({item['seo_title_length']} chars)")
                print(f"  ❌ IDENTICAL - No benefit, remove seo_title or make it shorter")
            else:
                improvement = item['title_length'] - item['seo_title_length']
                print(f"\n  {item['type']}: {item['file']}")
                print(f"  Full Title: \"{item['title']}\" ({item['title_length']} chars)")
                print(f"  SEO Title: \"{item['seo_title']}\" ({item['seo_title_length']} chars)")
                print(f"  Saved {improvement} chars")

                if item['seo_title_length'] <= TARGET_LENGTH:
                    print(f"  ✅ SEO title is optimal!")
                elif item['seo_title_length'] <= WARNING_LENGTH:
                    print(f"  ⚠️  SEO title is acceptable but could be shorter")
                else:
                    print(f"  ❌ SEO title is still too long (>{WARNING_LENGTH} chars)")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    needs_attention = len(results['too_long'])
    could_improve = len(results['acceptable'])
    has_duplicates = len(results['identical_titles'])

    if needs_attention == 0:
        print("✅ All effective titles are within acceptable length!")
    else:
        print(f"⚠️  {needs_attention} titles need attention (>{WARNING_LENGTH} chars)")

    if could_improve > 0:
        print(f"💡 {could_improve} titles could be improved ({TARGET_LENGTH+1}-{WARNING_LENGTH} chars)")

    if has_duplicates > 0:
        print(f"⚠️  {has_duplicates} pages have identical title and seo_title (remove duplication)")

    print(f"\nRecommendation: Add seo_title field to pages with titles >{TARGET_LENGTH} characters")
    print("See docs/SEO-TITLE-TAG-STANDARDS.md for guidelines")
    print("=" * 80)

if __name__ == "__main__":
    main()
