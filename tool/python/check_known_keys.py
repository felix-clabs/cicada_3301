import rune_tools as rt

keys = ["DIVINITY", "FIRFUMFERENFE", "INSTAR", "PARABLE", "PILGRIM", "TRUTH", "WISDOM", "KOAN"]

def try_vigenere(ciphertext, key_word):
    # Map word to runes
    # Note: This is a simplification, mapping latin letters back to runes is ambiguous (C/K, S/Z)
    # But usually key is provided in runes or standard latin mapping
    # Let's try matching the key word characters to the closest rune latin mapping
    key_indices = []
    for char in key_word:
        found = False
        for r_char, latin, val in rt.GEMATRIA_PRIMUS:
            if char in latin.split('/'):
                key_indices.append(rt.RUNE_TO_INDEX[r_char])
                found = True
                break
        if not found:
            print(f"Could not find rune for {char}")

    if len(key_indices) == 0:
        return ""

    return rt.vigenere_decrypt(ciphertext, key_indices)

if __name__ == "__main__":
    with open("liber_primus/markdown/17_transcription.txt", "r") as f:
        content = f.read()

    print("Trying known keys on Page 17:")
    for k in keys:
        dec = try_vigenere(content, k)
        ic = rt.calculate_ic(dec)
        print(f"Key {k:15}: IC {ic:.4f} | {rt.translate_to_latin(dec[:40])}")
