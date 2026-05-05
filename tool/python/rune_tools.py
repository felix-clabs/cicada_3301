GEMATRIA_PRIMUS = [
    ('ᚠ', 'F', 2), ('ᚢ', 'U', 3), ('ᚦ', 'TH', 5), ('ᚩ', 'O', 7), ('ᚱ', 'R', 11),
    ('ᚳ', 'C/K', 13), ('ᚷ', 'G', 17), ('ᚹ', 'W', 19), ('ᚻ', 'H', 23), ('ᚾ', 'N', 29),
    ('ᛁ', 'I', 31), ('ᛄ', 'J', 37), ('ᛇ', 'EO', 41), ('ᛈ', 'P', 43), ('ᛉ', 'X', 47),
    ('ᛋ', 'S/Z', 53), ('ᛏ', 'T', 59), ('ᛒ', 'B', 61), ('ᛖ', 'E', 67), ('ᛗ', 'M', 71),
    ('ᛚ', 'L', 73), ('ᛝ', 'NG/ING', 79), ('ᛟ', 'OE', 83), ('ᛞ', 'D', 89), ('ᚪ', 'A', 97),
    ('ᚫ', 'AE', 101), ('ᚣ', 'Y', 103), ('ᛡ', 'IA/IO', 107), ('ᛠ', 'EA', 109)
]
RUNES = [r[0] for r in GEMATRIA_PRIMUS]
RUNE_TO_INDEX = {r[0]: i for i, r in enumerate(GEMATRIA_PRIMUS)}
INDEX_TO_RUNE = {i: r[0] for i, r in enumerate(GEMATRIA_PRIMUS)}
RUNE_TO_LATIN = {r[0]: r[1] for r in GEMATRIA_PRIMUS}

LATIN_TO_INDEX = {
    'F':0, 'U':1, 'TH':2, 'O':3, 'R':4, 'C':5, 'K':5, 'G':6, 'W':7, 'H':8, 'N':9, 'I':10, 'J':11, 'EO':12, 'P':13, 'X':14, 'S':15, 'Z':15, 'T':16, 'B':17, 'E':18, 'M':19, 'L':20, 'NG':21, 'OE':22, 'D':23, 'A':24, 'AE':25, 'Y':26, 'IA':27, 'EA':28
}

NGRAM_WEIGHTS = {
    "TH": 5, "HE": 4, "IN": 4, "ER": 4, "AN": 3, "RE": 3, "ND": 3, "NG": 5, "EA": 4, "EO": 4,
    "TION": 10, "THE": 10, "ING": 8, "AND": 8, "FOR": 7, "WAS": 7, "THAT": 8, "ARE": 7
}

VOWELS_GP = set(['U', 'O', 'I', 'EO', 'E', 'OE', 'A', 'AE', 'Y', 'IA', 'EA'])

def get_runes_only(text):
    return [c for c in text if c in RUNES]

def translate_to_latin(runic_text):
    return "".join([RUNE_TO_LATIN.get(c, c).split('/')[0] for c in runic_text])

def to_indices(text):
    res = []
    i = 0
    text = text.upper().replace(" ", "").replace("/", "")
    while i < len(text):
        if i+2 <= len(text) and text[i:i+2] in LATIN_TO_INDEX:
            res.append(LATIN_TO_INDEX[text[i:i+2]])
            i += 2
        elif text[i] in LATIN_TO_INDEX:
            res.append(LATIN_TO_INDEX[text[i]])
            i += 1
        else:
            i += 1
    return res
