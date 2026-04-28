
import math
from collections import Counter

# Gematria Primus mapping
GEMATRIA_PRIMUS = [
    ('ᚠ', 'F', 2), ('ᚢ', 'U', 3), ('ᚦ', 'TH', 5), ('ᚩ', 'O', 7), ('ᚱ', 'R', 11),
    ('ᚳ', 'C/K', 13), ('ᚷ', 'G', 17), ('ᚹ', 'W', 19), ('ᚻ', 'H', 23), ('ᚾ', 'N', 29),
    ('ᛁ', 'I', 31), ('ᛄ', 'J', 37), ('ᛇ', 'EO', 41), ('ᛈ', 'P', 43), ('ᛉ', 'X', 47),
    ('ᛋ', 'S/Z', 53), ('ᛏ', 'T', 59), ('ᛒ', 'B', 61), ('ᛖ', 'E', 67), ('ᛗ', 'M', 71),
    ('ᛚ', 'L', 73), ('ᛝ', 'NG/ING', 79), ('ᛟ', 'OE', 83), ('ᛞ', 'D', 89), ('ᚪ', 'A', 97),
    ('ᚫ', 'AE', 101), ('ᚣ', 'Y', 103), ('ᛡ', 'IA/IO', 107), ('ᛠ', 'EA', 109)
]

RUNES = [r[0] for r in GEMATRIA_PRIMUS]
PRIMES = [r[2] for r in GEMATRIA_PRIMUS]
RUNE_TO_INDEX = {r[0]: i for i, r in enumerate(GEMATRIA_PRIMUS)}
INDEX_TO_RUNE = {i: r[0] for i, r in enumerate(GEMATRIA_PRIMUS)}
RUNE_TO_LATIN = {r[0]: r[1] for r in GEMATRIA_PRIMUS}

def clean_text(text):
    """Removes non-rune characters except whitespace/newlines."""
    return "".join([c for c in text if c in RUNES or c.isspace()])

def get_runes_only(text):
    """Returns only runes from the text, no spaces or newlines."""
    return [c for c in text if c in RUNES]

def calculate_ic(text):
    """Calculates the Index of Coincidence of the runic text."""
    runes = get_runes_only(text)
    n = len(runes)
    if n <= 1:
        return 0
    counts = Counter(runes)
    num = sum(f * (f - 1) for f in counts.values())
    den = n * (n - 1)
    # Normalized IC (multiplier 29 because there are 29 runes)
    return 29 * (num / den)

def vigenere_decrypt(ciphertext, key_indices):
    """Standard Vigenere decryption on rune indices."""
    runes = get_runes_only(ciphertext)
    plaintext_indices = []
    for i, r in enumerate(runes):
        c_idx = RUNE_TO_INDEX[r]
        k_idx = key_indices[i % len(key_indices)]
        p_idx = (c_idx - k_idx) % 29
        plaintext_indices.append(p_idx)
    return "".join([INDEX_TO_RUNE[i] for i in plaintext_indices])

def prime_vigenere_decrypt(ciphertext, key_primes):
    """Vigenere decryption using prime values instead of indices."""
    runes = get_runes_only(ciphertext)
    plaintext_runes = []
    # This assumes the shift is (C_prime - K_prime) then finding the rune with that prime?
    # No, usually it's (C_index - K_prime_index) % 29 or (C_index - some_prime) % 29.
    # Let's implement index shift based on a sequence of primes.
    # We need to find which prime corresponds to which index.
    # Since PRIMES[i] is the prime for index i.
    pass

def atbash(ciphertext):
    """Atbash cipher on runes."""
    runes = get_runes_only(ciphertext)
    result = []
    for r in runes:
        idx = RUNE_TO_INDEX[r]
        result.append(INDEX_TO_RUNE[28 - idx])
    return "".join(result)

def translate_to_latin(runic_text):
    return " ".join([RUNE_TO_LATIN.get(c, c) for c in runic_text])

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        with open(filepath, 'r') as f:
            content = f.read()

        runes = get_runes_only(content)
        print(f"File: {filepath}")
        print(f"Rune count: {len(runes)}")
        print(f"IC: {calculate_ic(content):.4f}")

        # Simple frequency analysis
        counts = Counter(runes)
        print("Top 5 runes:")
        for r, count in counts.most_common(5):
            print(f"  {r} ({RUNE_TO_LATIN[r]}): {count}")
