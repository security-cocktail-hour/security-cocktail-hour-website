#!/usr/bin/env python3
"""
Capture screenshots of hero sections from the Security Cocktail Hour website.
Uses Playwright to take automated screenshots for design review.
"""

import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
import sys

# Configuration
BASE_URL = "http://localhost:1313"
OUTPUT_DIR = Path("temp/hero-screenshots")
VIEWPORT_WIDTH = 1920
VIEWPORT_HEIGHT = 1080

# Pages to capture
PAGES = [
    {"path": "/", "name": "home", "description": "Home page hero"},
    {"path": "/episodes/", "name": "episodes", "description": "Episodes page hero"},
    {"path": "/blog/", "name": "blog", "description": "Blog page hero"},
    {"path": "/about/", "name": "about", "description": "About page hero"},
    {"path": "/partnership/", "name": "partnership", "description": "Partnership page hero"},
    {"path": "/contact/", "name": "contact", "description": "Contact page hero"},
]


async def capture_hero_section(page, url, output_path):
    """Capture a screenshot of the top portion of a page (hero section)."""
    try:
        print(f"  Navigating to {url}...")
        await page.goto(url, wait_until="networkidle")

        # Wait a moment for any animations/fonts to load
        await page.wait_for_timeout(500)

        # Capture the viewport (top 1080px which includes hero)
        await page.screenshot(path=str(output_path))
        print(f"  ✓ Saved screenshot: {output_path.name}")
        return True

    except Exception as e:
        print(f"  ✗ Error capturing {url}: {e}")
        return False


async def main():
    """Main function to capture all hero sections."""

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\n📸 Hero Section Screenshot Capture")
    print(f"=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Output: {OUTPUT_DIR}")
    print(f"Viewport: {VIEWPORT_WIDTH}x{VIEWPORT_HEIGHT}")
    print(f"=" * 60)

    # Check if server is running
    try:
        import urllib.request
        urllib.request.urlopen(BASE_URL, timeout=2)
    except Exception:
        print(f"\n❌ Error: Hugo dev server not running at {BASE_URL}")
        print(f"Please start the server with: hugo server -D")
        sys.exit(1)

    async with async_playwright() as p:
        # Launch browser
        print(f"\n🚀 Launching browser...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": VIEWPORT_WIDTH, "height": VIEWPORT_HEIGHT}
        )
        page = await context.new_page()

        # Capture each page
        print(f"\n📷 Capturing screenshots...\n")
        successful = 0

        for page_config in PAGES:
            url = f"{BASE_URL}{page_config['path']}"
            output_file = OUTPUT_DIR / f"{page_config['name']}-hero.png"

            print(f"[{page_config['description']}]")
            if await capture_hero_section(page, url, output_file):
                successful += 1
            print()

        # Close browser
        await browser.close()

        # Summary
        print(f"=" * 60)
        print(f"✅ Completed: {successful}/{len(PAGES)} screenshots captured")
        print(f"📁 Location: {OUTPUT_DIR.absolute()}")
        print(f"=" * 60)

        if successful > 0:
            print(f"\nScreenshots ready for review!")
        else:
            print(f"\n⚠ No screenshots captured. Check errors above.")


if __name__ == "__main__":
    # Check for Playwright
    try:
        import playwright
    except ImportError:
        print("❌ Playwright not installed.")
        print("\nInstall with:")
        print("  pip install playwright")
        print("  playwright install chromium")
        sys.exit(1)

    asyncio.run(main())
