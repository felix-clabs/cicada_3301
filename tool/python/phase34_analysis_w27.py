import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    w = 27
    rows = [indices[i:i+w] for i in range(0, len(indices), w)]
    flat = []
    for i, row in enumerate(rows):
        if i % 2 == 1: flat.extend(row[::-1])
        else: flat.extend(row)

    # Decrypt with P71 (G=0 base)
    base_dec = [(flat[i] - P71_KEY[i % 28]) % 29 for i in range(len(flat))]

    print("--- [W=27 ANALYSIS: RED LINE (0-22)] ---")
    for g in range(29):
        dec = [(base_dec[i] - g) % 29 for i in range(23)]
        latin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])
        if "SHADOW" in latin or "PENUMBRA" in latin or "SAID" in latin:
            print(f"G={g:2d}: {latin}")

    print("\n--- [W=27 ANALYSIS: FULL STREAM CRIB SEARCH] ---")
    # Dialogue keywords
    CRIBS = ["ALITTLE", "WHILE", "AGO", "WALKING", "STANDING", "SITTING", "STILL", "DEPEND", "SAIDTO", "PENUMBRA", "SHADOW"]
    for g in range(29):
        dec = [(base_dec[i] - g) % 29 for i in range(len(base_dec))]
        text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])
        found = [c for c in CRIBS if c in text]
        if found:
            print(f"G={g:2d} | Found: {found} | {text[:100]}...")

attack()
