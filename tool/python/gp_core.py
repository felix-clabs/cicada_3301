"""
Gematria Primus Core Module
Contains the GP alphabet mappings and conversion functions.
Supports both GP 2014 (Phonemic) and GP 2013 (Forward/Standard).
Default is GP 2014 Index (0-28).
"""

# GP 2014 Alphabet (Phonemic Mapping) - Official Base 29
# Index 0-28
GP_2014 = [
    ('ᚠ', 'F', 0), ('ᚢ', 'U', 1), ('ᚦ', 'TH', 2), ('ᚩ', 'O', 3), ('ᚱ', 'R', 4),
    ('ᚳ', 'C/K', 5), ('ᚷ', 'G', 6), ('ᚹ', 'W', 7), ('ᚻ', 'H', 8), ('ᚾ', 'N', 9),
    ('ᛁ', 'I', 10), ('ᛄ', 'J', 11), ('ᛇ', 'EO', 12), ('ᛈ', 'P', 13), ('ᛉ', 'X', 14),
    ('ᛋ', 'S/Z', 15), ('ᛏ', 'T', 16), ('ᛒ', 'B', 17), ('ᛖ', 'E', 18), ('ᛗ', 'M', 19),
    ('ᛚ', 'L', 20), ('ᛝ', 'NG', 21), ('ᛟ', 'OE', 22), ('ᛞ', 'D', 23), ('ᚪ', 'A', 24),
    ('ᚫ', 'AE', 25), ('ᚣ', 'Y', 26), ('ᛡ', 'IA/IO', 27), ('ᛠ', 'EA', 28)
]

# GP 2013 Alphabet (Forward Mapping A-Z)
GP_2013_MAP = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
    'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

RUNES = [item[0] for item in GP_2014]
RUNE_TO_INDEX = {item[0]: item[2] for item in GP_2014}
INDEX_TO_RUNE = {item[2]: item[0] for item in GP_2014}

# Latin GP to Index (Phonemic 2014)
LATIN_TO_INDEX_2014 = {
    'F': 0, 'U': 1, 'TH': 2, 'O': 3, 'R': 4,
    'C': 5, 'K': 5, 'G': 6, 'W': 7, 'H': 8, 'N': 9, 'I': 10, 'J': 11, 'EO': 12, 'P': 13, 'X': 14,
    'S': 15, 'Z': 15, 'T': 16, 'B': 17, 'E': 18, 'M': 19, 'L': 20, 'NG': 21, 'OE': 22, 'D': 23,
    'A': 24, 'AE': 25, 'Y': 26, 'IA': 27, 'IO': 27, 'EA': 28
}

INDEX_TO_LATIN_2014 = {
    0: 'F', 1: 'U', 2: 'TH', 3: 'O', 4: 'R', 5: 'C', 6: 'G', 7: 'W', 8: 'H', 9: 'N',
    10: 'I', 11: 'J', 12: 'EO', 13: 'P', 14: 'X', 15: 'S', 16: 'T', 17: 'B', 18: 'E',
    19: 'M', 20: 'L', 21: 'NG', 22: 'OE', 23: 'D', 24: 'A', 25: 'AE', 26: 'Y', 27: 'IO', 28: 'EA'
}

def rune_to_index(rune):
    return RUNE_TO_INDEX.get(rune)

def index_to_rune(index):
    return INDEX_TO_RUNE.get(index % 29)

def runes_to_indices(text):
    return [RUNE_TO_INDEX[c] for c in text if c in RUNE_TO_INDEX]

def indices_to_runes(indices):
    return "".join([INDEX_TO_RUNE[i % 29] for i in indices])

def latin_to_indices(text, mode='2014'):
    res = []
    text = text.upper()
    if mode == '2013':
        for char in text:
            if char in GP_2013_MAP:
                res.append(GP_2013_MAP[char])
        return res
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i:i+2] in LATIN_TO_INDEX_2014:
            res.append(LATIN_TO_INDEX_2014[text[i:i+2]])
            i += 2
        elif text[i] in LATIN_TO_INDEX_2014:
            res.append(LATIN_TO_INDEX_2014[text[i]])
            i += 1
        else:
            i += 1
    return res

def indices_to_latin(indices, mode='2014'):
    if mode == '2013':
        REV_2013 = {v: k for k, v in GP_2013_MAP.items()}
        return "".join([REV_2013.get(i % 26, '?') for i in indices])
    return "".join([INDEX_TO_LATIN_2014.get(i % 29, '?') for i in indices])

def get_runes_from_text(text):
    return [c for c in text if c in RUNE_TO_INDEX]
