#!/usr/bin/env python3
"""Fix formatting issues in the markdown file."""

import re

def fix_formatting(filepath):
    """Fix formatting issues in the markdown file."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix extra spaces and spaces in LaTeX equations
    replacements = {
        # Fix spaces within LaTeX expressions
        r'\\\,\s+': '',  # Remove \, followed by spaces
        r'\s+\\\,': '',  # Remove spaces followed by \,
        # Fix common LaTeX patterns
        r'Z,\s+': 'Z_t ',
        r'A,\s+': 'A_t ',
        r'B,\s+': 'B_t ',
        r'V,\s+': 'V_t ',
        r'S,\s+': 'S_t ',
        r'H,\s+': 'H_t ',
        r'F,\s+': 'F_t ',
        r'U,\s+': 'U_t ',
        r'E,\s+': 'E_t ',
        r'p,\s+': 'p_t ',
        r'r,\s+': 'r_t ',
        r'T,\s+': 'T_t ',
        r'Z,': 'Z_t',
        r'A,': 'A_t',
        r'B,': 'B_t',
        r'V,': 'V_t',
        r'S,': 'S_t',
        r'H,': 'H_t',
        r'F,': 'F_t',
        r'U,': 'U_t',
        r'E,': 'E_t',
        r'p,': 'p_t',
        r'r,': 'r_t',
        r'T,': 'T_t',
        # Fix italics notation
        r'\*Z,\s+': '*$Z_t$ ',
        r'\*A,\s+': '*$A_t$ ',
        r'\*B,\s+': '*$B_t$ ',
        r'\*V,\s+': '*$V_t$ ',
        r'\*S,\s+': '*$S_t$ ',
        r'\*H,\s+': '*$H_t$ ',
        r'\*F,\s+': '*$F_t$ ',
        r' \*': ' *',
        r'\* ': '* ',
        # Fix LaTeX within text
        r'I\(': '$I($',
        r'\)': ')$',
        r'Zt,\s+Zt,\s+Zt,': '$Z_t$',
        r'Icz,\s+cBI': '$I_{\\{Z_t < B\\}}$',
        # Fix malformed LaTeX brackets
        r'\{Z,\s+>A\)': '{Z_t > A}',
        r'\{Z,\s+<B\),\s+\*': '{Z_t < B}',
        # Fix equation endings
        r'\$\$\$\$': '$$',
        r'\$\$\s*\(': '$$ (',
        r'\)\s*\$\$': ') $$',
        # Fix the weird mathfrak
        r'\$\$\(\{\\mathfrak\{I\}\}\{\\mathfrak\{I\}\}\)': '(3)',
        # Fix mu at the end
        r',\s+\$\$\$\\mu\$': '$$',
        # Fix comma spacing outside equations
        r'(?<![\\$]),\s+': ', ',
        # Fix double spaces
        r'  +': ' ',
        # Fix footnote notation
        r'sNote': '^5^Note',
        # Clean up equation formatting
        r'\\!\s*\\left': '\\left',
        r'\\right\s*\\!': '\\right',
    }
    
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)
    
    # Fix specific problematic lines
    lines = content.split('\n')
    fixed_lines = []
    for i, line in enumerate(lines):
        # Fix Bid and Ask Prices With Private Information
        line = line.replace('Bid and Ask Prices With Private Information|bid-ask spread]]', 
                          '[[Bid and Ask Prices With Private Information|bid-ask spread]]')
        # Fix **Also, **
        line = line.replace('**Also, **', 'Also, ')
        # Fix **Basic Model**
        line = line.replace('**Basic Model**', 'Basic Model')
        # Fix **An Example**
        line = line.replace('**An Example**', 'An Example')
        # Fix **A Model With Discounting**
        line = line.replace('**A Model With Discounting**', 'A Model With Discounting')
        # Fix subscripts in text
        line = re.sub(r'([A-Za-z]+)_([a-z]+)', r'$\\1_{\\2}$', line)
        fixed_lines.append(line)
    
    content = '\n'.join(fixed_lines)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed formatting in {filepath}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python fix_formatting.py <filepath>")
        sys.exit(1)
    
    fix_formatting(sys.argv[1])