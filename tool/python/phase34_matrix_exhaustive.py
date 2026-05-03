import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

KEYWORDS = ["LITTLE", "WHILE", "AGO", "WALK", "STAND", "SITTING", "DEPEND", "OSHADOW", "PENUMBRA", "SAID", "PIGEON"]

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    for w in range(16, 30):
        # Generate rows
        rows = [indices[i:i+w] for i in range(0, len(indices), w)]

        # Test every possible starting line for reversal (all permutations of L/R reading)
        # That is 2^num_rows, too many.
        # But maybe just shift where the reversal starts?

        # Test standard Boustrophedon variants:
        patterns = [
            lambda r, i: r[::-1] if i % 2 == 1 else r, # Normal
            lambda r, i: r[::-1] if i % 2 == 0 else r, # Inverted
            lambda r, i: r, # Linear
        ]

        for p_idx, p_func in enumerate(patterns):
            flat = []
            for i, row in enumerate(rows):
                flat.extend(p_func(row, i))

            for g in range(29):
                dec = [(flat[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(flat))]
                text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])

                found = [kw for kw in KEYWORDS if kw in text]
                if len(found) >= 2 or "PIGEON" in found:
                    print(f"W={w} Pat={p_idx} G={g:2d} | {found}")
                    if "LITTLE" in found or "PENUMBRA" in found:
                         print(f"HIT!!! {text[:150]}")

attack()
