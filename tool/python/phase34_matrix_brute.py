import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

# Zhuangzi / Liber Primus Keywords
ANCHORS = ["PENUMBRA", "SHADOW", "PIGEON", "LITTLE", "WHILE", "SAID", "PATH", "WAY", "DEPEND"]

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    # Range of widths as requested
    for w in range(16, 29):
        # 1. Fill Matrix
        rows = [indices[i:i+w] for i in range(0, len(indices), w)]

        # 2. Boustrophedon Inversion (Every odd row reversed)
        flat = []
        for i, row in enumerate(rows):
            if i % 2 == 1: flat.extend(row[::-1])
            else: flat.extend(row)

        # 3.Substitution Scan
        for g in range(29):
            dec = [(flat[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(flat))]
            latin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])

            # Check for multiple anchors
            found = [a for a in ANCHORS if a in latin]
            if len(found) >= 2:
                print(f"!!! HIT !!! W={w} G={g:2d} | Found: {found}")
                print(f"TEXT: {latin[:120]}...")
            elif "PENUMBRA" in found or "PIGEON" in found:
                print(f"Part-Hit W={w} G={g:2d} | Found: {found}")

if __name__ == "__main__":
    attack()
