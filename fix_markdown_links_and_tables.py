#!/usr/bin/env python3
"""
Fix markdown files by:
1. Converting broken wiki-style links to plain text
2. Cleaning up table formatting
3. Fixing footnote formatting
4. Removing tags line at the bottom
"""

import re
import sys
from pathlib import Path
import argparse

def fix_wiki_links(content):
    """Convert wiki-style links to plain text"""
    # Pattern to match wiki-style links with paths like [text](relative%20path.md)
    # Replace with just the link text
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    def replace_link(match):
        link_text = match.group(1)
        link_path = match.group(2)
        
        # If the path ends with .md, it's a wiki-style link
        if link_path.endswith('.md'):
            # If the path contains spaces encoded as %20 or has directory separators,
            # it's a wiki-style link that should be converted to plain text
            if '%20' in link_path or '/' in link_path or '\\' in link_path:
                return link_text
            else:
                return link_text
        else:
            # Keep non-markdown links as they are
            return match.group(0)
    
    content = re.sub(pattern, replace_link, content)
    
    # Fix nested wiki links like [[text
    content = re.sub(r'\[\[([^\[\]]+)', r'\1', content)
    
    return content

def fix_tables(content):
    """Clean up table formatting by removing excessive spacing"""
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Check if this is a table row (contains |)
        if '|' in line:
            # Split by | and strip whitespace from each cell
            cells = [cell.strip() for cell in line.split('|')]
            # Rebuild the line with consistent spacing
            cleaned_line = ' | '.join(cells)
            # Remove leading/trailing pipes if they have no content
            if cleaned_line.startswith(' |  | '):
                cleaned_line = cleaned_line[4:]
            if cleaned_line.endswith(' |  | '):
                cleaned_line = cleaned_line[:-4]
            cleaned_lines.append(cleaned_line)
        else:
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def fix_footnotes(content):
    """Fix footnote formatting"""
    # Fix footnote references [^1] to be properly formatted
    content = re.sub(r'\s*\^\s*(\d+)', r'[^\1]', content)
    
    # Fix footnote definitions
    # Look for lines that start with a number followed by . or : 
    lines = content.split('\n')
    cleaned_lines = []
    in_footnote_section = False
    
    for i, line in enumerate(lines):
        # Check if we're entering a footnote section
        if i > 0 and lines[i-1].strip() == '' and re.match(r'^\d+\s*[:.]', line.strip()):
            in_footnote_section = True
        
        # Check if this looks like a footnote definition
        match = re.match(r'^(\d+)\s*[:.]?\s*(.*)$', line.strip())
        if match and in_footnote_section:
            # This is likely a footnote definition
            footnote_num = match.group(1)
            footnote_text = match.group(2)
            cleaned_lines.append(f'[^{footnote_num}]: {footnote_text}')
        else:
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def remove_tags_section(content):
    """Remove tags section at the bottom of the file"""
    # Remove tags: line at the end
    content = re.sub(r'\n\s*tags:\s*\n$', '\n', content)
    content = re.sub(r'\n\s*tags:\s*$', '', content)
    
    # Remove trailing yaml sections
    if '\n---\n' in content:
        parts = content.split('\n---\n')
        # Keep only the main content, not trailing metadata
        if len(parts) > 2:
            content = '\n---\n'.join(parts[:-1])
    
    return content.rstrip() + '\n'

def process_file(file_path):
    """Process a single markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply all fixes
        content = fix_wiki_links(content)
        content = fix_tables(content)
        content = fix_footnotes(content)
        content = remove_tags_section(content)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Fix markdown files')
    parser.add_argument('path', help='Path to markdown file or directory')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without modifying files')
    
    args = parser.parse_args()
    
    path = Path(args.path)
    
    if path.is_file() and path.suffix == '.md':
        # Process single file
        if args.dry_run:
            print(f"Would process: {path}")
        else:
            if process_file(path):
                print(f"Fixed: {path}")
            else:
                print(f"No changes needed: {path}")
    
    elif path.is_dir():
        # Process all markdown files in directory recursively
        md_files = list(path.rglob('*.md'))
        fixed_count = 0
        
        for md_file in md_files:
            if args.dry_run:
                print(f"Would process: {md_file}")
            else:
                if process_file(md_file):
                    print(f"Fixed: {md_file}")
                    fixed_count += 1
        
        if not args.dry_run:
            print(f"\nFixed {fixed_count} out of {len(md_files)} files")
    
    else:
        print(f"Error: {path} is not a markdown file or directory")
        sys.exit(1)

if __name__ == '__main__':
    main()