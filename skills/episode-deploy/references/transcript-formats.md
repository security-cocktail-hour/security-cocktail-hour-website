# Transcript Format Reference

This document describes all supported transcript formats and how to handle them during episode deployment.

---

## Supported Formats

### Format 1: Standard Episode Format (Output Format)

**Description:** The target format for all episodes. All other formats are converted to this.

**Format:**
```
*Speaker Name (MM:SS)*
Dialogue text here...

*Another Speaker (MM:SS)*
More dialogue text...
```

**Example:**
```
*Joe (00:00)*
Welcome to Security Cocktail Hour. Today we're talking about the Flipper Zero firmware update.

*Adam (00:15)*
This is going to be an interesting demonstration.
```

**Characteristics:**
- Speaker name in bold/italics: `*Speaker Name (MM:SS)*`
- Timecode in parentheses: `(MM:SS)` format
- Blank line between entries
- Dialogue text immediately follows speaker line

**Handler Script:** None (this is the target format)

---

### Format 2: DaVinci Resolve Export Format

**Description:** Transcript format exported from DaVinci Resolve video editing software.

**Format:**
```
[HH:MM:SS:FF - HH:MM:SS:FF]
Speaker Name
 Dialogue text...
```

**Example:**
```
[00:00:03:18 - 00:00:08:08]
Joe
 Welcome to Security Cocktail Hour. Today we're talking about the Flipper Zero firmware update.

[00:00:08:10 - 00:00:15:22]
Adam
 This is going to be an interesting demonstration.
```

**Characteristics:**
- Timecode in brackets: `[HH:MM:SS:FF - HH:MM:SS:FF]`
- FF = Frame number (typically 24 or 30 fps)
- Speaker name on separate line after timecode
- Dialogue text on third line (may be indented)
- May span multiple lines until next timecode

**Handler Script:** `scripts/format_davinci_transcript.py`

**Usage:**
```bash
python3 scripts/format_davinci_transcript.py input.txt output.txt
```

**Conversion Details:**
- Extracts start timecode only (ignores end time)
- Converts `[HH:MM:SS:FF]` to `(MM:SS)` format
- Calculates total minutes: `(hours * 60) + minutes`
- Formats as `(MM:SS)` with leading zeros
- Combines multiline dialogue into single paragraph
- Preserves speaker names exactly as provided

---

### Format 3: Generic Transcript Format (Original)

**Description:** Original simple transcript format with timecodes.

**Format:**
```
Speaker Name [MM:SS]
Dialogue text here...

Another Speaker [MM:SS]
More dialogue text...
```

**Example:**
```
Joe [00:00]
Welcome to Security Cocktail Hour. Today we're talking about the Flipper Zero firmware update.

Adam [00:15]
This is going to be an interesting demonstration.
```

**Characteristics:**
- Speaker name followed by timecode in brackets: `[MM:SS]`
- Dialogue text on same or next line
- Blank line between entries

**Handler Script:** `scripts/format_transcript.py`

**Usage:**
```bash
python3 scripts/format_transcript.py input.txt output.txt
```

**Conversion Details:**
- Moves timecode from end to speaker line
- Reformats to `*Speaker Name (MM:SS)*` format
- Preserves dialogue text
- Maintains blank lines between entries

---

## Format Detection

When a transcript is provided, detect the format automatically by examining the file content:

### Detection Logic

1. **Check for DaVinci format:**
   - Look for lines matching: `[HH:MM:SS:FF - HH:MM:SS:FF]`
   - Pattern: `\[\d+:\d+:\d+:\d+ - \d+:\d+:\d+:\d+\]`
   - If found → Use `format_davinci_transcript.py`

2. **Check for generic format:**
   - Look for lines with speaker name followed by timecode: `Speaker [MM:SS]`
   - Pattern: `.+\[\d+:\d+\]`
   - If found → Use `format_transcript.py`

3. **Check if already in standard format:**
   - Look for lines matching: `*Speaker (MM:SS)*`
   - Pattern: `\*.*\(\d+:\d+\)\*`
   - If found → No conversion needed

### Sample Detection Code

```python
import re

def detect_transcript_format(file_path):
    """
    Detect transcript format from file content.

    Returns:
        'davinci': DaVinci Resolve format
        'generic': Generic transcript format
        'standard': Already in standard format
        'unknown': Unable to detect format
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for DaVinci format
    if re.search(r'\[\d+:\d+:\d+:\d+ - \d+:\d+:\d+:\d+\]', content):
        return 'davinci'

    # Check for standard format
    if re.search(r'\*.*\(\d+:\d+\)\*', content):
        return 'standard'

    # Check for generic format
    if re.search(r'.+\[\d+:\d+\]', content):
        return 'generic'

    return 'unknown'
```

---

## Adding New Transcript Formats

When encountering a new transcript format:

1. **Document the Format:**
   - Add a new section to this file describing the format
   - Include example input
   - Note all characteristics and special cases

2. **Create New Handler Script:**
   - Create `scripts/format_[format-name]_transcript.py`
   - Follow the same structure as existing handlers
   - Input: raw transcript file path
   - Output: formatted transcript file path
   - Test thoroughly with sample data

3. **Update Detection Logic:**
   - Add detection pattern for the new format
   - Update detection code/script
   - Ensure it doesn't conflict with existing patterns

4. **Copy Handler to Skill:**
   - Copy new handler script to `skills/episode-deploy/scripts/`
   - Update this reference document
   - Test in skill context

5. **Update Documentation:**
   - Add format to this document
   - Update NEW-EPISODE-DEPLOYMENT.md if needed
   - Note the change in CLAUDE.md

---

## Episode Markdown Transcript Formatting

Once converted to standard format, transcripts are embedded in episode markdown with:

### Collapsible Accordion Format

```markdown
## Full Episode Transcript

*Speaker Name (MM:SS)*
Dialogue text here...

*Another Speaker (MM:SS)*
More dialogue text...
```

### Features

- Automatically converted to collapsible `<details>` element
- Collapsed by default, expands on click
- All content in HTML DOM for SEO indexing
- No "hidden content" penalty from Google
- Improves user experience (page not overwhelmingly long)
- Mobile responsive with scrollable content area

### Implementation

The Hugo template `layouts/episodes/single.html` automatically detects `## Full Episode Transcript` heading and wraps content in a collapsible accordion.

---

## Best Practices

### For Format Detection
- Always detect format before conversion
- Provide clear error messages for unknown formats
- Fall back gracefully if detection fails

### For Handler Scripts
- Accept input and output file paths as arguments
- Print clear success/error messages
- Include usage instructions in script comments
- Handle encoding properly (UTF-8)
- Validate input before processing
- Don't modify files in place (use separate output file)

### For Transcript Quality
- Verify speaker names are consistent
- Check timecodes are sequential
- Ensure dialogue text is complete
- Remove any editing artifacts
- Preserve paragraph breaks appropriately

---

**Last Updated**: December 22, 2025
