import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

# Keywords for Zhuangzi dialogue and Anchors
CRIBS = ["PENUMBRA", "SHADOW", "PIGEON", "LITTLE", "WHILE", "WALKING", "STANDING", "SAID"]

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    # 1. Broad Width Scan
    for w in range(10, 40):
        rows = [indices[i:i+w] for i in range(0, len(indices), w)]

        # Test standard Boustrophedon
        stream = []
        for i, row in enumerate(rows):
            if i % 2 == 1: stream.extend(row[::-1])
            else: stream.extend(row)

        # 2. Substitution Scan
        for g in range(29):
            dec = [(stream[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(stream))]
            text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])

            # Check for multiple anchors
            found = [c for c in CRIBS if c in text]
            if len(found) >= 2 or "PIGEON" in found:
                # Extra check: Does it start with O SHADOW?
                if text.startswith("OSHADOW"):
                     print(f"!!! START HIT !!! W={w} G={g:2d}")
                if "PIGEON" in found and len(found) >= 2:
                     print(f"!!! HIT !!! W={w} G={g:2d} | Found: {found}")
                     print(f"TEXT: {text[:100]}...")

attack()
