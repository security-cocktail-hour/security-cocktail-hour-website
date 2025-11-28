#!/usr/bin/env python3
"""
Batch fix all remaining meta descriptions that exceed 155 characters
Based on the audit report findings
"""

import os
import re

# Define all remaining updates based on audit report
# Format: (filename, new_description_within_155_chars)
updates = [
    ('episode-50-from-the-battlefield-to-the-boardroom-high-stakes-cyber-security.md',
     'Former IDF officer Keren de Via shares her journey from military leadership to CISO. High-stakes cybersecurity from battlefield to boardroom.'),

    ('episode-09.md',
     'Joe and Adam cover internet privacy basics: who wants your data, how they get it, and how to protect yourself from Big Tech.'),

    ('episode-22-zero-trust-and-80-proof-bourbon-with-adam-kohler.md',
     'What is Zero Trust security? Adam Kohler helps demystify the buzzword over bourbon. Security concepts explained practically.'),

    ('episode-03.md',
     'Should you keep using a company after they get hacked? Joe and Adam discuss the less obvious realities about data breaches.'),

    ('episode-54-dont-get-hacked-on-vacation-travel-cybersecurity-tips.md',
     'Travel cybersecurity tips: protect yourself from hotel Wi-Fi, airport chargers, and public networks while traveling this summer.'),

    ('episode-31-the-future-of-security-leadership-with-sivan-tehila.md',
     'Former CISO Sivan Tehila on the evolving role of security leadership and why she founded security startup Onyxia.'),

    ('episode-12-security-culture-club.md',
     'Joe and Adam discuss culture, human elements, and security with infrastructure expert Leticia Espinosa.'),

    ('episode-25-seven-trillion-reasons-to-drink-from-eric-oneill.md',
     'Spy hunter Eric O\'Neill on cybercrime costing $7 trillion, the Dark Web, ransomware, and infrastructure vulnerability.'),

    ('episode-26-ai-and-the-future-of-security-with-john-dwyer.md',
     'John Dwyer on how AI will bend reality and what that means for attackers and defenders. The future of security incidents.'),

    ('episode-19-tequila-with-rebecca-cahak.md',
     'Rebecca Cahak discusses women\'s leadership, her organization FIERCE, and work-life balance in business and IT.'),

    ('episode-53-the-new-rules-of-cyber-incident-response-new-attacks-new-response.md',
     'ThreatLight experts Lisa Landau and Tim Shipp on how incident response has evolved and why the old playbook no longer works.'),

    ('episode-51-agentic-ai-security-full-speed-into-the-unknown.md',
     'Is agentic AI a security nightmare? Kevin O\'Connor discusses autonomous AI security with Joe and Adam.'),

    ('episode-13-so-you-want-to-be-a-security-entrepreneur.md',
     'Idan Wiener, CEO of Illustria, shares startup experiences and lessons from building a software supply chain security company.'),

    ('episode-57-dr-nikki-robinson-why-security-teams-fail-at-human-factors.md',
     'Dr. Nikki Robinson explains the psychology behind why users hate security controls and how to fix failed implementations.'),

    ('episode-24-what-keeps-monte-fabiani-up-at-night.md',
     'Security veteran Monte Fabiani on building and running SOCs, and why being in security operations makes it hard to sleep.'),

    ('episode-14-security-campfire-stories.md',
     'Joe and Adam recount chilling legends: the Stuxnet and Target hacks, and why these classic tales still matter today.'),

    ('episode-23-holiday-security-tips-and-negronis-with-reut-weitzman.md',
     'Security consultant Reut Weitzman shares tips to keep cyber thieves and scammers from spoiling your holidays.'),

    ('episode-17-scotch-and-tea-with-chris-roberts.md',
     'Security legend Chris Roberts discusses dolphins, Porsches, and security in a wide-ranging conversation.'),

    ('episode-06.md',
     'Joe and Adam decode the Flipper Zero hype: what it does, how it fits in security, and the ethics of hacker tools.'),

    ('episode-27-purple-teaming-with-reut-weitzman.md',
     'Security consultant Reut Weitzman returns to discuss purple team exercises and testing security team capabilities.'),

    ('episode-21-medical-devices-halloween-and-whiskey-with-gabrielle-hempel.md',
     'Halloween episode covering medical device security with Gabrielle Hempel and her unconventional path into infosec.'),

    ('episode-61-ai-attacks-need-ai-defense-ransomwares-new-danger-and-how-a-top-cyber-expert-is-.md',
     'Karin Lagziel on ransomware gangs using AI and defense strategies: fighting back with AI and fundamentals.'),

    ('episode-58-travel-router-unboxing-dont-get-hacked-on-vacation.md',
     'Unboxing the travel router that protects you from hotel WiFi dangers and public network threats while traveling.'),

    ('episode-20-mai-tais-with-tom-cross.md',
     'Tom Cross brings news from Black Hat including the headline-grabbing satellite hacking challenge.'),

    ('episode-59-wifi-pineapple-unboxing-the-hacker-device-from-tv-shows.md',
     'Unboxing the Hak5 WiFi Pineapple Mark 7: the real penetration testing tool from TV hacker shows.'),

    ('episode-10.md',
     'Internet privacy part 2: How dissidents, journalists, and whistleblowers protect themselves with Tor and Tails.'),

    ('episode-16-french-75-with-jennifer-granick.md',
     'Internet civil liberties pioneer Jennifer Granick discusses protecting our rights in an age of government surveillance.'),

    ('episode-15-cyber-warrior.md',
     'Top security incident responder David Warshavski shares insights on attacker trends, cyber defense, and AI security issues.'),

    ('episode-08.md',
     'Small business owner Sal Toner discusses security challenges and solutions without the big corporate price tag.'),

    ('episode-29-mad-ais-and-poisoned-llms-fighting-digital-insanity-with-michael-silva.md',
     'CEO Michael Silva explains how large language models can steer you wrong and how to stay on track.'),

    ('episode-11-how-to-hire-a-security-team.md',
     'Joe and Adam share their tricks for hiring hard-to-find talent to build a top-notch security team.'),

    ('episode-28-threat-intelligence-with-ryan-westman.md',
     'Ryan Westman of eSentire explains threat intelligence and shows a neat Mac trick for laptop buyers.'),

    ('episode-60-crypto-kidnappings-lost-keys-and-million-dollar-bug-bounties.md',
     'Yevheniia Broshevan discusses crypto security, bug bounties, and the reality that 11-18% of Bitcoin is lost forever.'),

    ('episode-05.md',
     'Security can stress you out, but it leaves you with good stories. Hear how a security team really works.'),

    ('episode-02.md',
     'Joe and Adam discuss protecting yourself online while avoiding paranoia. Practical security for everyday life.'),

    ('episode-04.md',
     'Why VPN marketing is misleading. Joe and Adam explain what VPNs actually do and when you really need one.'),

    ('episode-07.md',
     'Generative AI is everywhere. Joe and Adam discuss security implications, risks, and opportunities of this technology.'),

    ('episode-37-cybersecurity-and-ai-what-the-experts-are-worried-about-and-what-theyre-doing.md',
     'Security experts discuss AI, deepfakes, and privacy. What everyone should worry about most will surprise you.'),

    ('episode-45-holiday-scams-unwrapped-tips-to-stay-safe-this-season.md',
     'Joe and Adam break down holiday scams from classics to new AI-driven schemes. Stay ahead of scammers this season.'),

    ('episode-56-from-zero-day-hunter-to-cyber-defender-cody-pierces-journey.md',
     'Why would a top hacker switch to defense? Cody Pierce shares his journey from Zero Day Initiative to founding Neon Cyber.'),

    ('episode-18-free-choice-with-jason-mar-tang.md',
     'Jason Mar-Tang discusses BlackHat, when to shut down security incidents, and attacking your own systems.'),

    ('_index.md',
     'Browse all episodes of the Security Cocktail Hour cybersecurity podcast featuring expert interviews and insights.'),

    ('ai-innovation-outpaces-security-governance.md',
     'Employees deploy AI tools in minutes, bypassing security. Build governance frameworks that enable productivity while maintaining compliance.')
]

def main():
    base_dir = "/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website"

    updated_count = 0
    error_count = 0

    for filename, new_desc in updates:
        # Determine correct path
        if filename == '_index.md':
            file_path = os.path.join(base_dir, 'content', 'episodes', filename)
        elif filename.endswith('-ai-innovation-outpaces-security-governance.md'):
            file_path = os.path.join(base_dir, 'content', 'blog', filename)
        else:
            file_path = os.path.join(base_dir, 'content', 'episodes', filename)

        if not os.path.exists(file_path):
            print(f"✗ Not found: {filename}")
            error_count += 1
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find and replace the description using regex
            # Pattern matches both >- block scalar and quoted formats
            pattern = r'description: >-\s*\n\s+.+?(?=\nplatforms:|\nguest_bio:|\n---|\ntitle:)'

            # Check if pattern exists
            if not re.search(pattern, content, re.DOTALL):
                # Try simpler quote pattern
                pattern = r'description: ".+?"'
                if not re.search(pattern, content):
                    print(f"✗ No description pattern found: {filename}")
                    error_count += 1
                    continue

            # Replace with new description
            new_description_line = f'description: "{new_desc}"'
            new_content = re.sub(pattern, new_description_line, content, flags=re.DOTALL)

            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"✓ Updated: {filename} ({len(new_desc)} chars)")
            updated_count += 1

        except Exception as e:
            print(f"✗ Error updating {filename}: {e}")
            error_count += 1

    print(f"\n{'='*60}")
    print(f"Batch update complete!")
    print(f"Updated: {updated_count}")
    print(f"Errors: {error_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
