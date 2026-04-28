import rune_tools as rt
import re
from collections import Counter

# Core Lexicon for skeleton attack
MAIN_WORDS = ["PILGRIM", "DIVINITY", "CONSUMPTION", "PRESERVATION", "INSTRUCTION", "ILLUSION"]

def get_word_chars(latin_word):
    # Map latin letters to rune indices (approximate)
    chars = []
    for char in latin_word:
        for r, l, v in rt.GEMATRIA_PRIMUS:
            if char in l.split('/'):
                chars.append(rt.RUNE_TO_INDEX[r])
                break
    return chars

def routine_1_word_skeleton(text_block):
    print("--- ROUTINE 1: WORD SKELETON ATTACK (BLOCK 0) ---")
    runes = rt.get_runes_only(text_block)
    block_indices = [rt.RUNE_TO_INDEX[r] for r in runes]
    b_counts = Counter(block_indices)

    print(f"Block chars: {rt.translate_to_latin(text_block)}")

    for word in MAIN_WORDS:
        w_indices = get_word_chars(word)
        w_counts = Counter(w_indices)
        possible = True
        for idx, count in w_counts.items():
            if b_counts[idx] < count:
                possible = False
                break
        if possible:
            print(f"Word '{word}' can be formed with characters from this block.")

    # Check for THE, AND
    for word in ["THE", "AND", "YOUR", "FOR"]:
        w_indices = get_word_chars(word)
        if all(b_counts[idx] >= count for idx, count in Counter(w_indices).items()):
             print(f"Word '{word}' can also be formed.")

def dynamic_block_permutation(text_block, index_array):
    if len(text_block) != len(index_array):
        return None
    runes = list(text_block)
    permuted = [''] * len(runes)
    for i, idx in enumerate(index_array):
        permuted[idx] = runes[i]
    return "".join(permuted)

if __name__ == "__main__":
    with open("tool/python/best_p20_runes.txt", "r") as f:
        text = f.read().strip()

    # Block 0 (first 28 chars)
    block0 = text[:28]
    routine_1_word_skeleton(block0)
