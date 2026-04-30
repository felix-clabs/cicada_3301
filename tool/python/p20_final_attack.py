import rune_tools as rt

P71_KEY = [22,7,27,8,16,5,19,22,23,24,3,13,2,25,28,22,5,4,22,8,11,19,11,11,5,21,6,9]

def get_p20_runes():
    with open("liber_primus/markdown/20.md", "r") as f:
        return rt.get_runes_only(f.read())

def execute_final_attack():
    all_runes = get_p20_runes()
    black_runes = all_runes[23:]

    # Discovery from Phase 19:
    # Applying the Page 71 key with an absolute offset of 23 (start of black runes)
    # results in an IC of 1.70.

    print("--- Page 20 Final Attack Strategy (Phase 19) ---")
    decrypted = []
    for i, r in enumerate(black_runes):
        c_idx = rt.RUNE_TO_INDEX[r]
        # Alignment: (i + 23) is the absolute index in the page.
        # We use (i + 23) % 28 to index the 28-length Vigenere key.
        k_idx = P71_KEY[(i + 23) % 28]
        decrypted.append((c_idx - k_idx) % 29)

    dec_runes = [rt.INDEX_TO_RUNE[idx] for idx in decrypted]
    text = "".join(dec_runes)
    ic = rt.calculate_ic(text)
    latin = rt.translate_to_latin(text)

    print(f"Alignment: P71_KEY[(i + 23) % 28]")
    print(f"Resulting IC: {ic:.4f}")
    print("\nDecrypted Text (Latin):")
    print(latin)

    # Check for G-shifts
    print("\n--- Testing G-Shifts on the High-IC Result ---")
    for g in range(29):
        shifted_indices = [(idx - g) % 29 for idx in decrypted]
        shifted_text = "".join([rt.INDEX_TO_RUNE[idx] for idx in shifted_indices])
        s_latin = rt.translate_to_latin(shifted_text)
        if " THE " in s_latin or " AND " in s_latin:
            print(f"G-Shift {g}: {s_latin[:150]}")

if __name__ == "__main__":
    execute_final_attack()
