#!/usr/bin/env python3
"""
Convert episode CSV files to Hugo markdown format
"""

import csv
import os
from datetime import datetime
import re

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def process_csv(csv_file):
    """Process a single CSV file and create markdown files"""
    print(f"Processing {csv_file}...")

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            # Skip empty rows
            if not row.get('Episode Number') or not row['Episode Number'].strip():
                continue

            ep_num = row['Episode Number'].strip()
            title = row['Title'].strip() if row['Title'] else f"Episode {ep_num}"
            guest = row['Guest Name'].strip() if row['Guest Name'] else ""
            guest_title = row['Guest Title/Organization'].strip() if row['Guest Title/Organization'] else ""
            date_str = row['Date Published'].strip()
            duration = row['Duration'].strip() if row['Duration'] else ""
            description = row['Description'].strip() if row['Description'] else ""
            category = row['Category/Topic'].strip() if row['Category/Topic'] else "General"
            has_transcript = row['Has Transcript'].strip().upper() == 'Y'
            image_file = row['Cover Image Filename'].strip() if row['Cover Image Filename'] else ""
            youtube = row['YouTube URL'].strip() if row['YouTube URL'] else ""
            spotify = row['Spotify URL'].strip() if row['Spotify URL'] else ""
            apple = row['Apple Podcasts URL'].strip() if row['Apple Podcasts URL'] else ""

            # Parse date
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                hugo_date = date_obj.strftime('%Y-%m-%d')
            except:
                print(f"Warning: Could not parse date for episode {ep_num}: {date_str}")
                hugo_date = "2023-01-01"

            # Create slug from episode number and title (truncate to avoid long filenames)
            title_slug = slugify(title)[:80]  # Limit to 80 chars
            slug = f"episode-{ep_num.zfill(2)}-{title_slug}" if title != f"Episode {ep_num}" else f"episode-{ep_num.zfill(2)}"

            # Build guest bio if we have guest info
            guest_bio = ""
            if guest:
                guest_bio = f"{guest}"
                if guest_title:
                    guest_bio += f", {guest_title}"

            # Build full title with guest if available
            full_title = title
            if guest and title != f"Episode {ep_num}":
                full_title = f"{title}"
            elif guest and title == f"Episode {ep_num}":
                full_title = f"Episode {ep_num}: {guest}"

            # Image path (relative to static folder)
            image_path = f"/images/episodes/{image_file}" if image_file else ""

            # Create markdown content using block scalar for description to handle quotes
            markdown = f"""---
title: "{full_title}"
date: {hugo_date}
draft: false
guest: "{guest}"
category: "{category}"
duration: "{duration}"
image: "{image_path}"
description: >-
  {description}
platforms:
  youtube: "{youtube}"
  spotify: "{spotify}"
  apple: "{apple}"
  amazon: "https://music.amazon.com/podcasts/d11e431a-f7b1-4bb0-8671-024afce9ade6/security-cocktail-hour"
guest_bio: "{guest_bio}"
---

{description}

## Episode Highlights

### Listen Now

Tune in to hear our discussion on {title.lower() if title != f"Episode {ep_num}" else "this topic"}.

## Key Takeaways

[Episode highlights and key takeaways will be added here]

## Resources Mentioned

[Resources mentioned in this episode will be listed here]

{"## Full Transcript" if has_transcript else ""}
{"" if has_transcript else ""}
{"[Transcript will be added soon]" if has_transcript else ""}
"""

            # Write markdown file
            output_file = f"content/episodes/{slug}.md"
            with open(output_file, 'w', encoding='utf-8') as out:
                out.write(markdown)

            print(f"  Created: {output_file}")

def main():
    """Process all CSV files"""
    csv_files = [
        'content/episodes/metadata_eps_01-10.csv',
        'content/episodes/metadata_eps_11-20.csv',
        'content/episodes/metadata_eps_21-30.csv',
        'content/episodes/metadata_eps_31-40.csv',
        'content/episodes/metadata_eps_41-50.csv',
        'content/episodes/metadata_eps_51-60.csv',
        'content/episodes/metadata_eps_61-70.csv',
    ]

    total = 0
    for csv_file in csv_files:
        if os.path.exists(csv_file):
            process_csv(csv_file)
            total += 1
        else:
            print(f"Warning: {csv_file} not found")

    print(f"\nDone! Processed {total} CSV files.")

if __name__ == '__main__':
    main()
