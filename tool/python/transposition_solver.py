import rune_tools as rt
import re

def get_lexicon():
    with open("tool/python/cicada_lexicon.txt", "r") as f:
        return [line.strip() for line in f if len(line.strip()) >= 4]

LEXICON = get_lexicon()

def check_english(text):
    latin = rt.translate_to_latin(text)
    simple_latin = re.sub(r'\[([^|\]]+)\|[^\]]+\]', r'\1', latin)
    clean_latin = "".join([c if c.isalpha() else " " for c in simple_latin]).upper()
    words_found = clean_latin.split()
    hits = [w for w in words_found if w in LEXICON]
    return hits

def routine_1_keyed_transposition(text, key_indices):
    print("--- ROUTINE 1: KEYED COLUMNAR TRANSPOSITION (COL EXTRACTION) ---")
    n_cols = len(key_indices)
    indexed_key = list(enumerate(key_indices))
    sorted_key = sorted(indexed_key, key=lambda x: x[1])

    rows = (len(text) + n_cols - 1) // n_cols
    grid = [['' for _ in range(n_cols)] for _ in range(rows)]
    for i, char in enumerate(text):
        grid[i // n_cols][i % n_cols] = char

    # Read columns in order of sorted key
    dec_chars = []
    for original_idx, value in sorted_key:
        for r in range(rows):
            if grid[r][original_idx]:
                dec_chars.append(grid[r][original_idx])

    dec = "".join(dec_chars)
    hits = check_english(dec)
    if len(hits) >= 3:
        print(f"!!! Success !!! Hits: {hits}")
        print(rt.translate_to_latin(dec))
    else:
        print(f"No match. Sample hits: {hits[:5]}")

if __name__ == "__main__":
    with open("tool/python/p20_key_output.txt", "r") as f:
        lines = f.readlines()
    key = [int(x) for x in lines[0].strip().split(",")]
    text = lines[1].strip()
    routine_1_keyed_transposition(text, key)

def routine_2_intra_block(text):
    print("\n--- ROUTINE 2: INTRA-BLOCK ANAGRAMS (LEN 28) ---")
    # Divide into blocks of 28
    block_size = 28
    blocks = [text[i:i+block_size] for i in range(0, len(text), block_size)]

    for i, block in enumerate(blocks):
        # We can't brute force 28!
        # But we can check if it contains runes of common words
        latin = rt.translate_to_latin(block)
        # Count runes matching "PILGRIM", "DIVINITY", etc.
        hits = 0
        for word in ["THE", "AND", "WITH", "SHALL", "YOUR", "THIS", "WILL"]:
             # Simple heuristic: if enough letters of the word are present
             pass
        if i == 0:
             print(f"Block 0: {rt.translate_to_latin(block)}")

if __name__ == "__main__":
    with open("tool/python/p20_key_output.txt", "r") as f:
        lines = f.readlines()
    key = [int(x) for x in lines[0].strip().split(",")]
    text = lines[1].strip()
    routine_1_keyed_transposition(text, key)
    routine_2_intra_block(text)
