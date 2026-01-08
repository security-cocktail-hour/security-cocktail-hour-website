#!/usr/bin/env python3
"""
Test Helpers for Security Cocktail Hour Website Testing Suite
Shared utilities, validation functions, and content discovery
"""

import os
import re
import glob
import time
import random
from datetime import datetime
from pathlib import Path

# Configuration
BASE_URL = "http://localhost:1313"
SCREENSHOT_DIR = "test_screenshots"
TIMEOUT_MS = 30000

# Get the project root directory (parent of scripts/ directory)
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent  # Go up from scripts/tests/ to project root
CONTENT_DIR = PROJECT_ROOT / "content"

def ensure_screenshot_dir():
    """Create screenshot directory if it doesn't exist."""
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def print_test_header(test_name):
    """Print formatted test section header."""
    print(f"\n{'=' * 80}")
    print(f"{test_name}")
    print(f"{'=' * 80}\n")

def print_result(success, message, indent=0):
    """Print formatted result with ✅ or ❌."""
    prefix = "  " * indent
    symbol = "✅" if success else "❌"
    print(f"{prefix}{symbol} {message}")

def format_duration(seconds):
    """Format elapsed time."""
    if seconds < 60:
        return f"{seconds:.1f}s"
    else:
        minutes = int(seconds // 60)
        secs = seconds % 60
        return f"{minutes}m {secs:.1f}s"

def validate_page_load(page, url, expected_title_substring=None, timeout=TIMEOUT_MS):
    """
    Load page and verify basic success criteria.
    Returns: (success, error_message)
    """
    try:
        page.goto(url, timeout=timeout)
        page.wait_for_load_state('networkidle', timeout=timeout)

        # Check if page loaded
        title = page.title()

        if expected_title_substring and expected_title_substring not in title:
            return False, f"Title mismatch. Expected substring '{expected_title_substring}', got '{title}'"

        return True, title
    except Exception as e:
        return False, f"Page load failed: {str(e)}"

def validate_seo_metadata(page):
    """
    Check presence of title, description, og tags.
    Returns: (success, issues)
    """
    issues = []

    # Check title
    title = page.locator('title').first
    if title.count() == 0:
        issues.append("Missing <title> tag")

    # Check meta description
    meta_desc = page.locator('meta[name="description"]').first
    if meta_desc.count() == 0:
        issues.append("Missing meta description")

    # Check og:title
    og_title = page.locator('meta[property="og:title"]').first
    if og_title.count() == 0:
        issues.append("Missing og:title")

    # Check og:description
    og_desc = page.locator('meta[property="og:description"]').first
    if og_desc.count() == 0:
        issues.append("Missing og:description")

    return len(issues) == 0, issues

def validate_navigation_links(page, expected_links):
    """
    Verify navigation menu contains expected links.
    expected_links: dict of {"Link Text": "/url/"}
    Returns: (success, issues)
    """
    issues = []

    for link_text, expected_url in expected_links.items():
        link = page.locator(f'nav a:has-text("{link_text}")').first
        if link.count() == 0:
            issues.append(f"Navigation link '{link_text}' not found")
        else:
            href = link.get_attribute('href')
            if expected_url not in href:
                issues.append(f"Link '{link_text}' has wrong URL: {href} (expected {expected_url})")

    return len(issues) == 0, issues

def check_console_errors(page):
    """
    Capture and return console errors.
    Note: This requires setting up the listener before page navigation.
    Returns: list of error messages
    """
    console_errors = []

    def handle_console(msg):
        if msg.type == 'error':
            # Filter out favicon errors (known minor issue)
            if 'favicon' not in msg.text.lower():
                console_errors.append(msg.text)

    page.on('console', handle_console)
    return console_errors

def take_failure_screenshot(page, test_name, error_description):
    """
    Save screenshot only on failure for debugging.
    Filename: {test_name}_{timestamp}_FAILED.png
    Returns: screenshot path
    """
    ensure_screenshot_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Sanitize test name for filename
    safe_test_name = re.sub(r'[^a-zA-Z0-9_-]', '_', test_name)
    filename = f"{safe_test_name}_{timestamp}_FAILED.png"
    filepath = os.path.join(SCREENSHOT_DIR, filename)

    try:
        page.screenshot(path=filepath, full_page=True)
        return filepath
    except Exception as e:
        print(f"  ⚠️  Could not capture screenshot: {e}")
        return None

def validate_form_elements(page, required_fields):
    """
    Check form has expected input fields.
    required_fields: list of field descriptions
    Returns: (success, issues)
    """
    issues = []

    for field_desc in required_fields:
        # Try multiple selectors for flexibility
        field = page.locator(f'input:near(:text("{field_desc}"))').or_(
            page.locator(f'input[placeholder*="{field_desc}" i]')
        ).or_(
            page.locator(f'input[name*="{field_desc.lower()}"]')
        ).or_(
            page.locator(f'textarea[placeholder*="{field_desc}" i]')
        ).or_(
            page.locator(f'textarea[name*="{field_desc.lower()}"]')
        )

        if field.count() == 0:
            issues.append(f"Form field '{field_desc}' not found")

    return len(issues) == 0, issues

def parse_frontmatter(content):
    """
    Extract YAML frontmatter from markdown content.
    Returns: dict of frontmatter data
    """
    # Match content between --- delimiters
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return {}

    frontmatter_text = match.group(1)
    data = {}

    # Simple YAML parsing (basic key: value pairs)
    current_key = None
    current_list = None

    for line in frontmatter_text.split('\n'):
        line = line.rstrip()

        # List item
        if line.startswith('  -') or line.startswith('    -'):
            if current_list is not None:
                item = line.strip()[1:].strip().strip('"')
                current_list.append(item)
            continue

        # Key-value pair
        if ':' in line and not line.startswith(' '):
            parts = line.split(':', 1)
            key = parts[0].strip()
            value = parts[1].strip() if len(parts) > 1 else ''

            # Remove quotes
            value = value.strip('"').strip("'")

            if not value:  # Empty value might start a nested structure or list
                current_key = key
                current_list = []
                data[key] = current_list
            else:
                data[key] = value
                current_key = key
                current_list = None
        # Nested key: value (like platforms)
        elif line.startswith('  ') and ':' in line and current_key:
            nested_parts = line.strip().split(':', 1)
            nested_key = nested_parts[0].strip()
            nested_value = nested_parts[1].strip() if len(nested_parts) > 1 else ''
            nested_value = nested_value.strip('"').strip("'")

            if isinstance(data.get(current_key), list):
                # Convert to dict if we encounter nested structure
                data[current_key] = {}

            if isinstance(data.get(current_key), dict):
                data[current_key][nested_key] = nested_value

    return data

def discover_episodes(content_dir=None):
    """
    Find all episode files and parse metadata.
    Returns sorted list by date (newest first).
    """
    if content_dir is None:
        content_dir = CONTENT_DIR

    episodes = []
    episode_dir = Path(content_dir) / "episodes"

    for filepath in episode_dir.glob("episode-*.md"):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                frontmatter = parse_frontmatter(content)

                # Extract episode number from filename
                filename = filepath.name
                ep_match = re.match(r'episode-(\d+)', filename)
                episode_num = int(ep_match.group(1)) if ep_match else 0

                episodes.append({
                    'filename': filename,
                    'filepath': str(filepath),
                    'episode_num': episode_num,
                    'title': frontmatter.get('title', ''),
                    'date': frontmatter.get('date', ''),
                    'category': frontmatter.get('category', ''),
                    'duration': frontmatter.get('duration', ''),
                    'platforms': frontmatter.get('platforms', {}),
                    'has_transcript': '## Full Episode Transcript' in content or '## Transcript' in content,
                    'related_episodes': frontmatter.get('related_episodes', [])
                })
        except Exception as e:
            print(f"  ⚠️  Error parsing {filepath}: {e}")
            continue

    # Sort by episode number (descending)
    episodes.sort(key=lambda x: x['episode_num'], reverse=True)
    return episodes

def discover_blog_posts(content_dir=None):
    """
    Find all blog post files and parse metadata.
    Returns sorted list by date (newest first).
    """
    if content_dir is None:
        content_dir = CONTENT_DIR

    posts = []
    blog_dir = Path(content_dir) / "blog"

    for filepath in blog_dir.glob("*.md"):
        # Skip _index.md
        if filepath.name == '_index.md':
            continue

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                frontmatter = parse_frontmatter(content)

                posts.append({
                    'filename': filepath.name,
                    'filepath': str(filepath),
                    'title': frontmatter.get('title', ''),
                    'date': frontmatter.get('date', ''),
                    'author': frontmatter.get('author', ''),
                    'category': frontmatter.get('category', ''),
                    'tags': frontmatter.get('tags', []),
                    'related_episode': frontmatter.get('related_episode', '')
                })
        except Exception as e:
            print(f"  ⚠️  Error parsing {filepath}: {e}")
            continue

    # Sort by date (descending)
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts

def select_episodes_to_test(all_episodes, newest_count=5):
    """
    Smart episode selection:
    - Newest N episodes
    - One from each block of 10 older episodes (middle episode from each block)
    Returns: list of episodes to test
    """
    if not all_episodes:
        return []

    # Get newest episodes
    newest = all_episodes[:newest_count]

    # Get older episodes (everything after newest)
    older = all_episodes[newest_count:]

    # Group older episodes into blocks of 10
    block_samples = []
    if older:
        # Determine how many blocks we have
        max_episode_num = max(ep['episode_num'] for ep in older)
        min_episode_num = min(ep['episode_num'] for ep in older)

        # Create blocks: 1-10, 11-20, 21-30, etc.
        for block_start in range(1, max_episode_num + 1, 10):
            block_end = block_start + 9
            block_episodes = [ep for ep in older if block_start <= ep['episode_num'] <= block_end]

            if block_episodes:
                # Pick the middle episode from this block
                mid_index = len(block_episodes) // 2
                block_samples.append(block_episodes[mid_index])

    return newest + block_samples

def select_blog_posts_to_test(all_posts, latest_count=5):
    """
    Select latest N blog posts.
    Returns: list of posts to test
    """
    return all_posts[:latest_count]
