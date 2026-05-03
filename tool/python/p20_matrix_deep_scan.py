import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

# Zhuangzi dialogue words
DIAL = ["LITTLE", "WHILE", "WALKING", "STANDING", "SITTING", "DEPEND", "AGO"]

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    for w in range(10, 30):
        rows = [indices[i : i + w] for i in range(0, len(indices), w)]

        # Try both: even rows reversed, or odd rows reversed
        for start_rev in [0, 1]:
            stream = []
            for i, row in enumerate(rows):
                if i % 2 == start_rev: stream.extend(row[::-1])
                else: stream.extend(row)

            for g in range(29):
                # P(i) = (C - K - G)
                p = [(stream[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(stream))]
                latin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in p])

                found = [w for w in DIAL if w in latin]
                if found or "PIGEON" in latin:
                    # If we find PIGEON or dialogue, check if we also find SHADOW/PENUMBRA
                    bonus = []
                    for b in ["PENUMBRA", "SHADOW", "SAID"]:
                        if b in latin: bonus.append(b)

                    if len(found) >= 1 or len(bonus) >= 1:
                        print(f"W={w} StartRev={start_rev} G={g:2d} | Found: {found + bonus}")
                        if "PIGEON" in latin:
                             print(f"TEXT: {latin}")

if __name__ == "__main__":
    attack()
