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
def get_runes_only(text):
    return [c for c in text if c in RUNES]
def translate_to_latin(runic_text):
    return "".join([RUNE_TO_LATIN.get(c, c) for c in runic_text])
