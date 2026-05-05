#!/usr/bin/env python3
"""Generate missing markdown files for Liber Primus pages 17-72.
Uses liber_primus.md and pages_and_ciphers.md as source data."""

import os
import re

MD_DIR = "liber_primus/markdown"
IMG_BASE = "https://github.com/iBotPeaches/cicada_3301/raw/master/liber_primus"

# LP2 page number = image_number - 17
# So image 17 = LP2 page 0, image 73 = LP2 page 56

# Per-page rune data extracted from liber_primus.md
# For single-page sections where we have exact per-page runes
PAGE_RUNES = {}

# Page 32 - magic square
PAGE_RUNES[32] = {
    "section_title": "ᚠᚢᛚᛗ•ᚪᛠᚣᛟᚪ",
    "runes": """ᚠᚢᛚᛗ•ᚪᛠᚣᛟᚪ

3258\t3222\t3152\t3038
3278\t3299\t3298\t2838
3288\t3294\t3296\t2472
4516\t1206\t708\t\t1820""",
    "lp2_page": 15,
    "key": "?"
}

# Page 50 - section header
PAGE_RUNES[50] = {
    "section_title": "ᛞᛇ•ᛉᚳᚠᛁᚪᚹᚻᚷ",
    "runes": """ᛞᛇ•ᛉᚳᚠᛁᚪᚹᚻᚷ

ᛇᛟ•ᚠᛏᛖᛟᛠᚪᛡᛋᚷ•ᚣᛠᚾᚦᚫᚱ•ᚩᛡᛗ•ᚹᛉᛗ•ᚣᛞᛒᛏᚱ•ᚢᛄᚻ•ᚫᛟ•ᛡᛝᚹᚻᛋᚠᛡ•ᛚᚦᛏ•ᛁᚹᛏ•ᚩᚢᚾᚹᛗᛚ•ᛋᚦᛠᚹᛄ•ᚪᛄᚫᚷᚣᛗᚹᛞ•ᛈᛡ•ᛖᛄᚹ•ᛖᚢ•ᚻᚹ•ᛝᛁ•ᛋᚫᚷ•ᛄᛚ""",
    "lp2_page": 33,
    "key": "?"
}

# Base60 pages
PAGE_RUNES[66] = {
    "section_title": "Base60 Data",
    "runes": """3N 3p 2l 36 1b 3v 26 33
1W 49 2a 3g 47 04 33 3W
21 3M 0F 0X 1g 2H 0x 1R
1n 3I 2r 0P 2U 16 2L 2D
1t 1s 3H 0d 0s 1K 2D 05
1K 1O 0S 1D 3o 1l 3J 1G
4D 0G 0l 0x 1Q 2p 2a 1K
4E 1w 2Q 19 1k 3G 24 0p
22 4F 0P 3C 3J 1D 2n 1m
2i 1J 3P 2v 1s 2O 0k 1M""",
    "lp2_page": 49,
    "key": "?",
    "decimal": """203 231 167 186 97 237 126 183
92 249 156 222 247 4 183 212
121 202 15 33 102 137 59 87
109 224 173 25 150 66 141 133
115 114 197 39 54 80 133 5
80 84 28 73 230 81 199 76
253 16 21 59 86 171 156 80
254 118 146 69 106 196 124 51
122 255 25 192 199 73 169 108
164 79 205 177 114 144 46 82"""
}

PAGE_RUNES[67] = {
    "section_title": "Base60 Data",
    "runes": """2M 0w 3L 3D 2r 0S 1p 15
3V 3e 3I 0n 3u 1O 0u 0Z
3g 2U 1C 0Y 1N 3n 0W 3Q
22 13 0V 3c 0E 34 0W 1t
1D 2N 3H 47 0s 2p 0Z 34
0g 3v 1Q 0s 0D 0K 2h 3D
3L 2x 1Q 20 2n 2L 1C 2p
0A 29 3r 0D 45 0k 2e 2W
25 3U 1W 2r 46 2s 2X 39
3p 0X 0E 1q 0q 4B 49 48
3r 3b 3C 1M 1j 0I 4A 48
40 3m 4E 0s 2S 1v 3T 0I
3t 2B 2k 2t 2O 0e 2l 1L""",
    "lp2_page": 50,
    "key": "?",
    "decimal": """142 58 201 193 173 28 111 65
211 220 198 49 236 84 56 35
222 150 72 34 83 229 32 206
122 63 31 218 14 184 32 115
73 143 197 247 54 171 35 184
42 237 86 54 13 20 163 193
201 179 86 120 169 141 72 171
10 129 233 13 245 46 160 152
125 210 92 173 246 174 153 189
231 33 14 112 52 251 249 248
233 217 192 82 105 18 250 248
240 228 254 54 148 117 209 44
235 131 166 175 144 40 141 81"""
}

PAGE_RUNES[68] = {
    "section_title": "Base60 Data",
    "runes": """28 2a 0J 1L 0c 3C 2o 0X
00 2Z 2d 1T 2u 1t 1j 0l
1o 1E 3T 18 3E 1G 27 0L
0v 2t 06 11 1A 2U 4B 1O
2M 3d 2S 0x 0w 0q 0p 2V
18 0q 1D 49 2O 00 1v 2t
1k 3s 3G 21 3w 0W 29 2r
2O 2L 0g 3Y 0M 0u 3I 3C
1r 2c 2q 3o 30 0a 39 1K""",
    "lp2_page": 51,
    "key": "?",
    "decimal": """128 156 19 81 38 192 170 33
0 155 159 89 176 115 105 21
110 74 209 68 194 76 127 21
57 175 6 61 70 150 251 5
142 219 148 59 58 52 51 151
68 52 73 249 144 0 117 175
106 234 196 121 238 58 129 173
144 141 42 214 22 56 224 192
113 158 172 230 180 36 189 80"""
}

# Page 71 - has runes
PAGE_RUNES[71] = {
    "section_title": "ᚪ•ᛗᛝᛞᛡᚦᛉᛁᛗ",
    "runes": """ᚪ•ᛗᛝᛞᛡᚦᛉᛁᛗ

ᛡᛞᛈᛝᚢᚹᚪᛗ•ᛏᚪᛝ•ᛝᚦᛡᚹᛋᚻ•ᛁᚳ•ᚫᛈᚫᚷᚩ•ᛗᛁᚪ•ᛖᚩ•ᛏᚹᚩ•ᚠᚣᚢᛏᛄ•ᚦᛄᛠᛖᚳᚾᛠ•ᚳᛠᛖ•ᚱᚩᚢᛉ
ᛞᚹᚻᛒᛝᚠᚪᚳᛄᚢ•ᚩᛄᛡᛠᛁᛚᚷᚻ•ᛒᚢᛄ•ᛉᚪᚳᚹᛡ•ᛗᚩᛈᚣᛞᛡᛚᛈ•ᛇᛁᚦᚱ•ᚣᚷᛗ•ᛉᛟᚷᛋ•ᛗᛈᛄᛟᛞ
ᛟᛏᛡᛟ•ᛏᛝᛁ•ᛗᛝᚣᚪᚫ•ᛝ•ᚱᚣᛄ•ᚾᛚᚢᛉᛒ•ᚻᛈᛄᚩᛠ•ᚷᚫᚹ•ᛉᛋᛞᚳ•ᚢᛏ•ᛟᚻᛇᚾᛈᛏ•ᛠᚣᛒᚢᚷ
ᚷᚪᛇ•ᚾᚷᚩᛖᛚᛗᛒᚦ•ᚣᛡᛟᛇᚣ•ᛗᚳᛟᚦ•ᛖᛚᚱᛇᛈᚱᛞᚣ•ᛉᛞ•ᛝᚣᛈ•ᛋᛖᛉᚹ•ᚳᚷᚠᛞᚱᛖ
ᛞᛖᚹᚩᛇᛟ•ᚻᚩᛟ•ᛒᛋ•ᚻᛠᚪᚳᛁᛗᛉᛄᛗᛖ•ᛗᛚ•ᚷᚩᛏᚦᛉᛖᛠᚱᚷᚣᛝ•ᚫᛗᛁᚹ•ᛋᛒ•ᛉᛗ
ᛋᛇᚷᛞᚦᚫ•ᚠᛡᚪᛒᚳᚢ•ᚹᚱ•ᛒᛠᚠᛉᛁᛗᚢᚳᛈᚻᛝᛚᛇ•ᛗᛋᛞᛡᛈᚠ•ᛒᚻᛇᚳ•ᛇᛖ•ᛠᛖᛁᚷᛉᚷᛋ
ᛖᛋᛇᚦᚦᛖᛋ•ᚦᛟ•ᚳᛠᛁᛗᚳᛉ•ᛞᛄᚢ•ᛒᛖᛁ""",
    "lp2_page": 54,
    "key": "? (71.jpg - 72.jpg)"
}

# Section mapping: which section each page belongs to
# Format: page_num -> (section_name, page_range, has_runes_in_lp)
SECTION_MAP = {
    # Pages 17-19: Block "ᛋᚻᛖᚩᚷᛗᛡᚠ•ᛋᚣᛖᛝᚳ" (not in liber_primus.md individually)
    17: ("Chapter 2 (LP2)", "17-19", False),
    18: ("Chapter 2 (LP2)", "17-19", False),
    19: ("Chapter 2 (LP2)", "17-19", False),
    # Pages 20-22: Two blocks on page 20
    20: ("LP2 pages 3-5", "20-22", False),
    21: ("LP2 pages 3-5", "20-22", False),
    22: ("LP2 pages 3-5", "20-22", False),
    # Pages 23-24: Start of long block
    23: ("LP2 pages 6-7", "23-24", False),
    24: ("LP2 pages 6-7", "23-24", False),
    # Pages 25-31: In liber_primus.md
    25: ("LP2 pages 8-14", "25-31", True),
    26: ("LP2 pages 8-14", "25-31", True),
    27: ("LP2 pages 8-14", "25-31", True),
    28: ("LP2 pages 8-14", "25-31", True),
    29: ("LP2 pages 8-14", "25-31", True),
    30: ("LP2 pages 8-14", "25-31", True),
    31: ("LP2 pages 8-14", "25-31", True),
    # Page 32: Individual
    32: ("LP2 page 15", "32", True),
    # Pages 33-39: In liber_primus.md
    33: ("LP2 pages 16-22", "33-39", True),
    34: ("LP2 pages 16-22", "33-39", True),
    35: ("LP2 pages 16-22", "33-39", True),
    36: ("LP2 pages 16-22", "33-39", True),
    37: ("LP2 pages 16-22", "33-39", True),
    38: ("LP2 pages 16-22", "33-39", True),
    39: ("LP2 pages 16-22", "33-39", True),
    # Pages 40-43: In liber_primus.md
    40: ("LP2 pages 23-26", "40-43", True),
    41: ("LP2 pages 23-26", "40-43", True),
    42: ("LP2 pages 23-26", "40-43", True),
    43: ("LP2 pages 23-26", "40-43", True),
    # Pages 44-49: In liber_primus.md
    44: ("LP2 pages 27-32", "44-49", True),
    45: ("LP2 pages 27-32", "44-49", True),
    46: ("LP2 pages 27-32", "44-49", True),
    47: ("LP2 pages 27-32", "44-49", True),
    48: ("LP2 pages 27-32", "44-49", True),
    49: ("LP2 pages 27-32", "44-49", True),
    # Page 50: Individual + part of 50-56
    50: ("LP2 page 33", "50", True),
    # Pages 51-56: In liber_primus.md
    51: ("LP2 pages 33-39", "50-56", True),
    52: ("LP2 pages 33-39", "50-56", True),
    53: ("LP2 pages 33-39", "50-56", True),
    54: ("LP2 pages 33-39", "50-56", True),
    55: ("LP2 pages 33-39", "50-56", True),
    56: ("LP2 page 39", "56", True),
    # Page 57: Individual
    57: ("LP2 page 40", "57", True),
    # Pages 58-64: In liber_primus.md (no rune transcription)
    58: ("LP2 pages 41-47", "58-64", False),
    59: ("LP2 pages 41-47", "58-64", False),
    60: ("LP2 pages 41-47", "58-64", False),
    61: ("LP2 pages 41-47", "58-64", False),
    62: ("LP2 pages 41-47", "58-64", False),
    63: ("LP2 pages 41-47", "58-64", False),
    64: ("LP2 pages 41-47", "58-64", False),
    # Page 65: Individual
    65: ("LP2 page 48", "65", False),
    # Pages 66-68: Individual with base60
    66: ("LP2 page 49", "66", True),
    67: ("LP2 page 50", "67", True),
    68: ("LP2 page 51", "68", True),
    # Pages 69-70: Individual (no runes)
    69: ("LP2 page 52", "69", False),
    70: ("LP2 page 53", "70", False),
    # Page 71: Individual with runes
    71: ("LP2 page 54", "71", True),
    # Page 72: Individual (no runes)
    72: ("LP2 page 55", "72", False),
}

# Outguess info from liber_primus.md
OUTGUESS_PAGES = {
    43: "Outguessing the image yields 58,2kB garbage output.",
    65: "Outguessing the image yields 58,2kB garbage output.",
    66: "none",
    67: "none",
    68: "Outguessing the image yields 58,2kB garbage output.",
    69: "Outguessing the image yields 58,2kB garbage output.",
    70: "Outguessing the image yields 58,2kB garbage output.",
    71: "Outguessing the image yields 58,2kB garbage output.",
    72: "none",
}

def generate_md(page_num):
    lp2_page = page_num - 17
    section_name, page_range, has_runes = SECTION_MAP[page_num]
    
    lines = []
    # Image tag
    lines.append(f'<img src="{IMG_BASE}/{page_num:02d}.jpg" width="256" alt="{page_num:02d}">')
    lines.append("")
    
    # LP2 page note
    lines.append(f"_Commonly known as Page {lp2_page} of the LP2 dump._")
    lines.append("")
    
    # Section info
    if page_range != str(page_num):
        lines.append(f"_Part of section covering pages {page_range} ({section_name})._")
        lines.append("")
    
    # Per-page rune data if available
    if page_num in PAGE_RUNES:
        data = PAGE_RUNES[page_num]
        lines.append("```")
        lines.append(data["runes"])
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append(f"**Key:** {data.get('key', '?')}")
        lines.append("")
        if "decimal" in data:
            lines.append("### Decimal")
            lines.append("")
            lines.append("```")
            lines.append(data["decimal"])
            lines.append("```")
            lines.append("")
    else:
        lines.append("```")
        lines.append(f"[Rune transcription pending - verify against {page_num:02d}.jpg]")
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("**Key:** ?")
        lines.append("")
    
    # Status
    lines.append("**Status:** Not yet decrypted")
    lines.append("")
    
    # Outguess
    if page_num in OUTGUESS_PAGES:
        lines.append("### Outguess")
        lines.append("")
        lines.append("```")
        lines.append(OUTGUESS_PAGES[page_num])
        lines.append("```")
        lines.append("")
    
    return "\n".join(lines) + "\n"


def main():
    os.makedirs(MD_DIR, exist_ok=True)
    
    created = []
    skipped = []
    
    for page_num in range(17, 73):
        filepath = os.path.join(MD_DIR, f"{page_num:02d}.md")
        
        # Don't overwrite existing files
        if os.path.exists(filepath):
            skipped.append(page_num)
            continue
        
        content = generate_md(page_num)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        created.append(page_num)
    
    print(f"Created {len(created)} files: {created}")
    print(f"Skipped {len(skipped)} existing files: {skipped}")


if __name__ == "__main__":
    main()
