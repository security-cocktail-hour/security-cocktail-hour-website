#!/usr/bin/env python3
"""
Meta Description Audit Script
Analyzes all meta descriptions across the Security Cocktail Hour website
"""

import os
import re
from pathlib import Path

# Character limits
TARGET_LENGTH = 120
MAX_LENGTH = 155

def extract_description(file_path):
    """Extract description from markdown front matter"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match YAML front matter description (handles both single line and multi-line)
    # Pattern for single line: description: "text"
    single_line = re.search(r'^description:\s*["\'](.+?)["\']', content, re.MULTILINE)
    if single_line:
        return single_line.group(1).strip()

    # Pattern for multi-line with >- or >
    multi_line = re.search(r'^description:\s*>-?\s*\n\s*(.+?)(?=\n\w+:|---|\n\n)', content, re.MULTILINE | re.DOTALL)
    if multi_line:
        # Clean up the description - remove extra whitespace and newlines
        desc = multi_line.group(1).strip()
        desc = ' '.join(desc.split())  # Normalize whitespace
        return desc

    return None

def extract_title(file_path):
    """Extract title from markdown front matter"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    return match.group(1).strip() if match else "Unknown"

def suggest_shortened_description(description, target=MAX_LENGTH):
    """Suggest a shortened version of the description"""
    if len(description) <= target:
        return description

    # Try to cut at a sentence boundary
    sentences = re.split(r'(?<=[.!?])\s+', description)
    result = ""
    for sentence in sentences:
        if len(result) + len(sentence) + 1 <= target:
            result += sentence + " "
        else:
            break

    if result.strip():
        return result.strip()

    # If no sentence fits, cut at word boundary
    words = description.split()
    result = ""
    for word in words:
        if len(result) + len(word) + 1 <= target - 3:  # Leave room for "..."
            result += word + " "
        else:
            break

    return result.strip()

def main():
    base_dir = Path("/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website")

    results = {
        'exceeding': [],
        'compliant': [],
        'missing': []
    }

    # Check episodes
    episodes_dir = base_dir / "content" / "episodes"
    for episode_file in sorted(episodes_dir.glob("episode-*.md")):
        title = extract_title(episode_file)
        description = extract_description(episode_file)

        if description:
            length = len(description)
            relative_path = str(episode_file.relative_to(base_dir))

            if length > MAX_LENGTH:
                results['exceeding'].append({
                    'type': 'Episode',
                    'file': relative_path,
                    'title': title,
                    'description': description,
                    'length': length,
                    'over_by': length - MAX_LENGTH
                })
            else:
                results['compliant'].append({
                    'type': 'Episode',
                    'file': relative_path,
                    'title': title,
                    'length': length
                })

    # Check blog posts
    blog_dir = base_dir / "content" / "blog"
    if blog_dir.exists():
        for blog_file in sorted(blog_dir.glob("*.md")):
            if blog_file.name == "_index.md":
                continue

            title = extract_title(blog_file)
            description = extract_description(blog_file)

            if description:
                length = len(description)
                relative_path = str(blog_file.relative_to(base_dir))

                if length > MAX_LENGTH:
                    results['exceeding'].append({
                        'type': 'Blog Post',
                        'file': relative_path,
                        'title': title,
                        'description': description,
                        'length': length,
                        'over_by': length - MAX_LENGTH
                    })
                else:
                    results['compliant'].append({
                        'type': 'Blog Post',
                        'file': relative_path,
                        'title': title,
                        'length': length
                    })

    # Check other content pages
    content_dir = base_dir / "content"
    for content_file in content_dir.glob("*.md"):
        title = extract_title(content_file)
        description = extract_description(content_file)

        if description:
            length = len(description)
            relative_path = str(content_file.relative_to(base_dir))

            if length > MAX_LENGTH:
                results['exceeding'].append({
                    'type': 'Page',
                    'file': relative_path,
                    'title': title,
                    'description': description,
                    'length': length,
                    'over_by': length - MAX_LENGTH
                })
            else:
                results['compliant'].append({
                    'type': 'Page',
                    'file': relative_path,
                    'title': title,
                    'length': length
                })

    # Check hardcoded descriptions in layouts
    blog_list_layout = base_dir / "layouts" / "blog" / "list.html"
    if blog_list_layout.exists():
        with open(blog_list_layout, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'<meta name="description" content="(.+?)">', content)
        if match:
            description = match.group(1)
            length = len(description)

            if length > MAX_LENGTH:
                results['exceeding'].append({
                    'type': 'Layout',
                    'file': 'layouts/blog/list.html',
                    'title': 'Blog Archive Page',
                    'description': description,
                    'length': length,
                    'over_by': length - MAX_LENGTH
                })

    # Generate report
    print("=" * 80)
    print("META DESCRIPTION AUDIT REPORT")
    print("=" * 80)
    print(f"\nTotal Pages Analyzed: {len(results['exceeding']) + len(results['compliant'])}")
    print(f"Pages EXCEEDING limit (>{MAX_LENGTH} chars): {len(results['exceeding'])}")
    print(f"Pages COMPLIANT (≤{MAX_LENGTH} chars): {len(results['compliant'])}")
    print("\n" + "=" * 80)
    print("PAGES EXCEEDING 155 CHARACTER LIMIT")
    print("=" * 80)

    # Sort by how much they exceed
    results['exceeding'].sort(key=lambda x: x['over_by'], reverse=True)

    for i, item in enumerate(results['exceeding'], 1):
        print(f"\n{i}. {item['type']}: {item['title']}")
        print(f"   File: {item['file']}")
        print(f"   Current Length: {item['length']} characters (OVER by {item['over_by']})")
        print(f"   Current Description:")
        print(f"   \"{item['description']}\"")

        # Generate suggestion
        suggestion = suggest_shortened_description(item['description'])
        print(f"\n   Suggested Description ({len(suggestion)} characters):")
        print(f"   \"{suggestion}\"")
        print("-" * 80)

    print("\n" + "=" * 80)
    print("COMPLIANT PAGES (≤155 characters)")
    print("=" * 80)

    # Group by type
    for page_type in ['Page', 'Blog Post', 'Episode']:
        type_items = [x for x in results['compliant'] if x['type'] == page_type]
        if type_items:
            print(f"\n{page_type}s ({len(type_items)}):")
            for item in type_items:
                print(f"  ✅ {item['title']} ({item['length']} chars)")

    print("\n" + "=" * 80)
    print(f"SUMMARY: {len(results['exceeding'])} pages need attention")
    print("=" * 80)

if __name__ == "__main__":
    main()
