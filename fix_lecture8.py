import re

# Read the file
with open('/Users/rogerlin/Reserve/VoyageLemma/Advanced Investments/Lecture 8- Inflation & Sovereign Default Risk.md', 'r') as f:
    content = f.read()

# Remove Git merge conflict markers and keep the cleaner version
# Pattern to match merge conflicts
merge_pattern = r'<<<<<<< HEAD\n(.*?)\n=======\n(.*?)\n>>>>>>> [^\n]+\n'
def handle_merge(match):
    # Prefer the second version as it seems cleaner in most cases
    return match.group(2)

content = re.sub(merge_pattern, handle_merge, content, flags=re.DOTALL)

# Convert headers from ### to ##
content = re.sub(r'^### ', '## ', content, flags=re.MULTILINE)

# Fix wiki links with display text [[Something|display text]] -> display text
content = re.sub(r'\[\[(?:[^|]*?)\|([^\]]+?)\]\]', r'\1', content)

# Fix simple wiki links [[Something]] -> Something
content = re.sub(r'\[\[([^\]|]+?)\]\]', r'\1', content)

# Fix broken markdown links [text](file.md) -> text
content = re.sub(r'\[([^\]]+?)\]\([^)]+?\)', r'\1', content)

# Fix remaining broken references
content = re.sub(r'\[[^\]]+?\]\([^)]*?\)', lambda m: m.group(0).split(']')[0][1:], content)

# Fix spacing around headers (ensure blank line before headers)
content = re.sub(r'([^\n])(\n## )', r'\1\n\2', content)

# Fix spacing around figures
content = re.sub(r'(\!\[[^\]]*\]\([^)]*\))\n([^\n])', r'\1\n\n\2', content)
content = re.sub(r'([^\n])\n(\!\[[^\]]*\]\([^)]*\))', r'\1\n\n\2', content)

# Fix LaTeX equations spacing
content = re.sub(r'\n\s*\$\$\n', r'\n\n$$\n', content)
content = re.sub(r'\n\$\$\s*\n', r'\n$$\n\n', content)

# Fix multiple consecutive blank lines
content = re.sub(r'\n{3,}', '\n\n', content)

# Fix spaces in CPI variables
content = re.sub(r'C P I', r'CPI', content)

# Write the fixed content
with open('/Users/rogerlin/Reserve/VoyageLemma/Advanced Investments/Lecture 8- Inflation & Sovereign Default Risk.md', 'w') as f:
    f.write(content)

print("File has been fixed\!")
