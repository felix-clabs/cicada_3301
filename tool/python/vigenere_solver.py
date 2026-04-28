import rune_tools as rt
from collections import Counter

def solve_vigenere(ciphertext, key_len):
    runes = rt.get_runes_only(ciphertext)
    best_key = []

    # English rune frequencies (approximate based on solved pages)
    # We can use a simplified model or just look for the most frequent rune to be 'E' (ᛖ) or 'A' (ᚪ)
    # E is index 18, A is index 24.

    for i in range(key_len):
        slice = runes[i::key_len]
        counts = Counter(slice)
        most_common_rune, count = counts.most_common(1)[0]
        c_idx = rt.RUNE_TO_INDEX[most_common_rune]

        # Try assuming most common is 'E' (index 18)
        # c_idx - k_idx = 18 => k_idx = c_idx - 18
        k_idx = (c_idx - 18) % 29
        best_key.append(k_idx)

    return best_key

if __name__ == "__main__":
    with open("liber_primus/markdown/17_transcription.txt", "r") as f:
        content = f.read()

    for l in [16, 18, 20]:
        key = solve_vigenere(content, l)
        dec = rt.vigenere_decrypt(content, key)
        print(f"Key Len {l}: IC {rt.calculate_ic(dec):.4f}")
        print(f"  Key indices: {key}")
        print(f"  {rt.translate_to_latin(dec[:60])}")
