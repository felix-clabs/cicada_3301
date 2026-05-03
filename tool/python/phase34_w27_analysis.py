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

    for g in range(29):
        dec = [(flat[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(flat))]
        text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])

        if "PIGEON" in text:
             print(f"--- [W=27, G={g}] ---")
             print(text)
             # Search for fragments
             for word in ["LITTLE", "WHILE", "AGO", "WALK", "STAND", "SIT", "DEPEND", "SHADOW", "PENUMBRA", "SAID"]:
                 if word in text:
                     print(f"FOUND: {word}")

attack()
