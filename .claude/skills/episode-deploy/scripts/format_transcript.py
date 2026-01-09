import re

# Read the original transcript
with open('/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website/temp/transcript-ep-051.txt', 'r') as f:
    lines = f.readlines()

formatted = []
for line in lines:
    line = line.rstrip('\n')
    
    # Check if line is a timestamp
    if re.match(r'^\d+:\d+$', line):
        formatted.append(f'\n**{line}**  ')
    # Check if line looks like a section header (short, starts with capital, no common sentence starters)
    elif (len(line) < 60 and 
          line and 
          not line.startswith(('I ', 'He ', 'She ', 'It ', 'We ', 'They ', 'You ', 'So ', 'And ', 'But ', 'The ', 'This ', 'What ', 'How ', 'Why ', 'When ', 'Where ', 'Who ', 'Yeah', 'No', 'Well')) and
          len(line.split()) <= 8 and
          line[0].isupper()):
        formatted.append(f'\n### {line}\n')
    else:
        formatted.append(line + '  ')

# Write formatted output
with open('/Users/joe/Library/CloudStorage/Dropbox/Security Cocktail Hour/website/redesign 2025-10/security-cocktail-hour-website/temp/transcript-formatted-final.txt', 'w') as f:
    f.write('\n'.join(formatted))

print("Transcript formatted successfully")
