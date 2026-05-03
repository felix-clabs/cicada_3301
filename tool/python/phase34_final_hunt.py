import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

# Keywords to find
DIAL = ["LITTLE", "WHILE", "AGO", "WALK", "STAND", "SIT", "DEPEND", "SAID"]
ANCHORS = ["PIGEON", "PENUMBRA", "SHADOW", "OSHADOW"]

def hunt():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    print("--- [PHASE 34: THE GRAND MATRIX HUNT] ---")

    for w in range(2, 40):
        rows = [indices[i:i+w] for i in range(0, len(indices), w)]

        # Boustrophedon Pattern
        flat = []
        for i, row in enumerate(rows):
            if i % 2 == 1: flat.extend(row[::-1])
            else: flat.extend(row)

        for g in range(29):
            dec = [(flat[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(flat))]
            text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])

            # Check for PIGEON first
            if "PIGEON" in text:
                found_dial = [w for w in DIAL if w in text]
                found_anch = [w for w in ANCHORS if w in text]

                if len(found_dial) >= 1:
                    print(f"!!! HIT !!! W={w} G={g:2d} | Found: {found_anch} + {found_dial}")
                    print(f"TEXT: {text[:150]}...")
                    # If we found AGO and PIGEON, it might be the one
                    if "AGO" in found_dial:
                         print(f"FULL TEXT: {text}")

if __name__ == "__main__":
    hunt()
