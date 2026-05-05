#!/usr/bin/env python3
"""
Generate markdown files for pages 17-72 by extracting rune content from
liber_primus.md (primary) and pages_and_ciphers.md (secondary).

The mapping from liber_primus.md is:
- Pages 00-16: LP1 (already done, in master)
- Pages 25-31 = LP2 pages 8-14  
- Page 32 = LP2 page 15
- Pages 33-43 = LP2 pages 16-26 (covered by multi-page sections)
- Pages 44-49 = LP2 pages 27-32
- Page 50 = LP2 page 33
- Pages 50-56 = LP2 pages 33-39
- Page 56 = LP2 page 39
- Page 57 = LP2 page 40
- Pages 58-64 = LP2 pages 41-47
- Pages 65-74 = LP2 pages 48-57

pages_and_ciphers.md blocks (in order) map to sequential pages.
"""

import re
import os

def extract_liber_primus_sections(filepath):
    """Extract sections from liber_primus.md mapped to image filenames."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Split by ## headers
    sections = re.split(r'\n## ', '\n' + text)
    
    result = {}
    for sec in sections[1:]:
        header = sec.split('\n')[0]
        
        # Extract image numbers from header
        # Examples: "Runes - 01.jpg", "25.jpg, 26.jpg, ... - 8.jpg-14.jpg", "72.jpg - 55.jpg"
        img_nums = re.findall(r'(\d+)\.jpg', header.split(' - ')[0] if ' - ' in header else header)
        
        # Check if it has Runes: section
        runes_match = re.search(r'Runes:\s*\n(.*?)(?=\n(?:English|Using|Outguess|##|\Z))', sec, re.DOTALL)
        
        # Check for inline runes (some pages have runes directly without "Runes:" label)
        # Like page 57 which has runes inline
        
        # Extract the full section for reference
        rune_lines = []
        if runes_match:
            for line in runes_match.group(1).strip().split('\n'):
                line = line.strip()
                if line and any(c in line for c in 'ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛄᛇᛈᛉᛋᛏᛒᛖᛗᛚᛝᛟᛞᚪᚫᚣᛡᛠ'):
                    rune_lines.append(line)
        
        # Also check for runes in the section body (for pages without "Runes:" label)
        body_rune_lines = []
        for line in sec.split('\n'):
            line = line.strip()
            if line and any(c in line for c in 'ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛄᛇᛈᛉᛋᛏᛒᛖᛗᛚᛝᛟᛞᚪᚫᚣᛡᛠ'):
                # Skip lines that are English translations or contain mostly ASCII
                ascii_chars = sum(1 for c in line if c.isascii() and c.isalpha())
                rune_chars = sum(1 for c in line if c in 'ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛄᛇᛈᛉᛋᛏᛒᛖᛗᛚᛝᛟᛞᚪᚫᚣᛡᛠ')
                if rune_chars > ascii_chars:
                    body_rune_lines.append(line)
        
        for num in img_nums:
            n = int(num)
            info = {
                'header': header,
                'rune_lines': rune_lines if rune_lines else body_rune_lines,
                'has_runes': bool(rune_lines or body_rune_lines),
                'section': sec[:500]  # first 500 chars for reference
            }
            if n not in result:
                result[n] = info
            elif info['has_runes'] and not result[n]['has_runes']:
                result[n] = info
    
    return result


def extract_pages_and_ciphers_blocks(filepath):
    """Extract code blocks from pages_and_ciphers.md."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    blocks = re.findall(r'```\n(.*?)\n```', text, re.DOTALL)
    return blocks


def main():
    lp_sections = extract_liber_primus_sections('liber_primus.md')
    pc_blocks = extract_pages_and_ciphers_blocks('pages_and_ciphers.md')
    
    print(f"Found {len(lp_sections)} sections in liber_primus.md")
    print(f"Found {len(pc_blocks)} blocks in pages_and_ciphers.md")
    
    print("\n=== liber_primus.md sections ===")
    for num in sorted(lp_sections.keys()):
        info = lp_sections[num]
        has = "HAS RUNES" if info['has_runes'] else "no runes"
        rune_count = sum(len(l) for l in info['rune_lines'])
        print(f"  Page {num:02d}: {info['header'][:60]:60s} | {has} ({rune_count} chars)")
    
    print("\n=== pages_and_ciphers.md blocks ===")
    for i, block in enumerate(pc_blocks):
        # Count rune chars
        rune_chars = sum(1 for c in block if c in 'ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛄᛇᛈᛉᛋᛏᛒᛖᛗᛚᛝᛟᛞᚪᚫᚣᛡᛠ')
        first_30 = block[:30].replace('\n', ' ')
        print(f"  Block {i:2d}: {first_30:30s}... ({rune_chars} rune chars, {len(block)} total)")
    
    # Now identify which pages are missing (17-72)
    print("\n=== Pages 17-72 status ===")
    for p in range(17, 73):
        if p in lp_sections and lp_sections[p]['has_runes']:
            print(f"  Page {p:02d}: COVERED by liber_primus.md")
        elif p in lp_sections:
            print(f"  Page {p:02d}: In liber_primus.md but NO RUNES")
        else:
            print(f"  Page {p:02d}: NOT in liber_primus.md")


if __name__ == '__main__':
    main()
