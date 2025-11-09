#!/usr/bin/env python3
"""
Script to fix nested internal links in markdown files.
Converts patterns like [text](path/to/file.md) to just text.
"""

import os
import re
import shutil
from datetime import datetime

def fix_nested_links(content):
    """Fix nested links in the content."""
    # Pattern to match markdown links: [text](path)
    # This pattern looks for [text] followed by (path) where path can contain any characters
    pattern = r'\[([^\]]+)\]\([^)]+\)'
    
    # Replace all matches with just the link text
    fixed_content = re.sub(pattern, r'\1', content)
    
    return fixed_content

def process_file(file_path):
    """Process a single markdown file to fix nested links."""
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix the nested links
        fixed_content = fix_nested_links(content)
        
        # Only write if content changed
        if content != fixed_content:
            # Create backup
            backup_path = f"{file_path}.backup"
            shutil.copy2(file_path, backup_path)
            
            # Write the fixed content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            
            print(f"✓ Fixed: {file_path}")
            return True
        else:
            print(f"  No changes needed: {file_path}")
            return False
            
    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all markdown files in the project."""
    root_dir = "/Users/rogerlin/Reserve/VoyageLemma"
    processed = 0
    fixed = 0
    
    print(f"Starting to process markdown files in {root_dir}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)
    
    # Walk through all directories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden directories and specific directories we don't want to process
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d not in ['node_modules', 'venv', '__pycache__']]
        
        for filename in filenames:
            if filename.endswith('.md') and not filename.endswith('.backup'):
                file_path = os.path.join(dirpath, filename)
                processed += 1
                if process_file(file_path):
                    fixed += 1
    
    print("-" * 60)
    print(f"Processing complete!")
    print(f"Total files processed: {processed}")
    print(f"Files fixed: {fixed}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()