#!/usr/bin/env python3
"""
Convert DaVinci Resolve transcript format to episode transcript format.

Input format:
[HH:MM:SS:FF - HH:MM:SS:FF]
Speaker Name
 Dialogue text...

Output format:
*Speaker Name (MM:SS)*
Dialogue text...
"""

import re
import sys

def convert_timecode(timecode_str):
    """Convert [HH:MM:SS:FF - HH:MM:SS:FF] to (MM:SS) using start time."""
    # Extract start time from bracket format
    match = re.match(r'\[(\d+):(\d+):(\d+):\d+ - \d+:\d+:\d+:\d+\]', timecode_str)
    if match:
        hours = int(match.group(1))
        minutes = int(match.group(2))
        seconds = int(match.group(3))

        # Convert to total minutes and seconds
        total_minutes = (hours * 60) + minutes

        return f"({total_minutes:02d}:{seconds:02d})"
    return "(00:00)"

def format_davinci_transcript(input_file, output_file):
    """Convert DaVinci transcript to episode format."""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    formatted = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Check if this line is a timecode
        if line.startswith('[') and ' - ' in line and line.endswith(']'):
            timecode = convert_timecode(line)

            # Next line should be speaker name
            if i + 1 < len(lines):
                speaker = lines[i + 1].strip()

                # Next line(s) should be dialogue (may be multiple lines until next timecode)
                i += 2  # Move past timecode and speaker
                dialogue_lines = []

                while i < len(lines):
                    next_line = lines[i].strip()

                    # If we hit another timecode or empty line followed by timecode, stop
                    if next_line.startswith('[') and ' - ' in next_line and next_line.endswith(']'):
                        break

                    # Skip empty lines between dialogue blocks
                    if next_line:
                        dialogue_lines.append(next_line)

                    i += 1

                # Format the entry
                if dialogue_lines:
                    dialogue = ' '.join(dialogue_lines)
                    formatted.append(f"\n*{speaker} {timecode}*")
                    formatted.append(dialogue)

                continue

        i += 1

    # Write formatted output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(formatted))

    print(f"✓ Transcript converted successfully")
    print(f"  Input:  {input_file}")
    print(f"  Output: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 format_davinci_transcript.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    format_davinci_transcript(input_file, output_file)
