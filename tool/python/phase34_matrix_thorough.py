import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

KEYWORDS = ["LITTLE", "WHILE", "WALKING", "STANDING", "SITTING", "RISING", "DEPEND", "SHADOW", "PENUMBRA", "SAID", "PIGEON"]

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    for w in range(2, 40):
        # 1. Split into rows
        rows = [indices[i:i+w] for i in range(0, len(indices), w)]

        # 2. Try two boustrophedon patterns (starting row linear or reversed)
        for start_rev in [0, 1]:
            stream = []
            for i, row in enumerate(rows):
                if i % 2 == start_rev: stream.extend(row[::-1])
                else: stream.extend(row)

            # 3.Substitution
            for g in range(29):
                dec = [(stream[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(stream))]
                text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])

                # 4. Score
                found = [kw for kw in KEYWORDS if kw in text]
                if "PIGEON" in found and len(found) >= 2:
                    print(f"!!! HIT !!! W={w} StartRev={start_rev} G={g:2d} | Found: {found}")
                    print(f"TEXT: {text[:150]}...")
                elif len(found) >= 3:
                     print(f"!!! DIALOGUE HIT !!! W={w} StartRev={start_rev} G={g:2d} | Found: {found}")

if __name__ == "__main__":
    attack()
