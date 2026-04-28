import rune_tools as rt
import random
import re
import itertools

# Numbers from Page 16
SEEDS = [434, 1311, 312, 278, 966, 204, 812, 934, 280, 1071, 626, 620, 809, 620, 626, 1071, 280, 934, 812, 204, 966, 278, 312, 1311, 434]

# High priority Cicada Lexicon for key generation
KEY_LEXICON = ["DIVINITY", "PILGRIM", "WISDOM", "TRUTH", "CHAPTER", "WELCOME", "BELIEVE", "NOTHING", "KNOWLEDGE", "SACRED", "DECEPTION", "PRESERVATION", "CONSUMPTION", "ADHERENCE", "INSTAR", "PARABLE"]

def latin_to_indices(word):
    indices = []
    for char in word:
        for r_char, latin, val in rt.GEMATRIA_PRIMUS:
            if char in latin.split('/'):
                indices.append(rt.RUNE_TO_INDEX[r_char])
                break
    return indices

def lcg(seed, n):
    a = 1103515245
    c = 12345
    m = 2**31
    res = []
    curr = seed
    for _ in range(n):
        curr = (a * curr + c) % m
        res.append(curr % 29)
    return res

def check_success(text):
    ic = rt.calculate_ic(text)
    if ic > 1.45: return True, f"IC: {ic:.4f}"
    return False, ""

def run_attacks(ciphertext, name_prefix):
    runes = rt.get_runes_only(ciphertext)
    n = len(runes)
    # PRNG Attack
    for seed in SEEDS:
        seq = lcg(seed, n)
        dec = "".join([rt.INDEX_TO_RUNE[(rt.RUNE_TO_INDEX[r] - s) % 29] for r, s in zip(runes, seq)])
        success, msg = check_success(dec)
        if success:
            print(f"MATCH: {name_prefix} PRNG LCG {seed} | {msg}")
            return True
    # Dictionary Attack
    for length in [16, 18, 20]:
        candidates = [w for w in KEY_LEXICON if len(w) == length]
        for w1, w2 in itertools.product(KEY_LEXICON, repeat=2):
            if len(w1) + len(w2) == length: candidates.append(w1 + w2)
        for k_latin in set(candidates):
            k_indices = latin_to_indices(k_latin)
            dec = rt.vigenere_decrypt(ciphertext, k_indices)
            success, msg = check_success(dec)
            if success:
                print(f"MATCH: {name_prefix} Dictionary {k_latin} | {msg}")
                return True
    return False

if __name__ == "__main__":
    with open("liber_primus/markdown/17.md", "r") as f:
        content = f.read()
    runes = "".join(rt.get_runes_only(content))
    for name, ct in [("Normal", runes), ("Atbash", rt.atbash(runes))]:
        print(f"Scanning {name}...")
        run_attacks(ct, name)
