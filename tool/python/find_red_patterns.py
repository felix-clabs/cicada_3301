import rune_tools as rt

def find_pattern_anywhere(text_runes, pattern_latin):
    pattern_indices = []
    for char in pattern_latin:
        if char == ' ': continue
        # Find rune for this char
        found = False
        for r, l, p in rt.GEMATRIA_PRIMUS:
            if l == char or (isinstance(l, list) and char in l) or (char == 'S' and l == 'S/Z') or (char == 'Z' and l == 'S/Z') or (char == 'C' and l == 'C/K') or (char == 'K' and l == 'C/K'):
                pattern_indices.append(rt.RUNE_TO_INDEX[r])
                found = True
                break
        if not found:
            print(f"Char {char} not found in Gematria")
            return

    # Try all shifts
    for shift in range(29):
        shifted_pattern = [(idx + shift) % 29 for idx in pattern_indices]
        pattern_str = "".join([rt.INDEX_TO_RUNE[idx] for idx in shifted_pattern])
        idx = text_runes.find(pattern_str)
        while idx != -1:
            print(f"Found '{pattern_latin}' with shift {shift} at index {idx}")
            idx = text_runes.find(pattern_str, idx + 1)

if __name__ == "__main__":
    with open("liber_primus/markdown/20.md", "r") as f:
        content = f.read()
    all_runes = "".join(rt.get_runes_only(content))

    print(f"Total runes: {len(all_runes)}")

    patterns = ["OSHADOWTHE", "HEHAS", "SHADOW", "THE", "HAS"]
    for p in patterns:
        print(f"--- Searching for {p} ---")
        find_pattern_anywhere(all_runes, p)

    # Check Atbash too
    atbash_runes = rt.atbash(all_runes)
    print("\n--- ATBASH SEARCH ---")
    for p in patterns:
        find_pattern_anywhere(atbash_runes, p)
