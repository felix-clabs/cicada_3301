import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

# Keywords from the Zhuangzi dialogue
# "A little while ago you were walking, and now you are standing still;
# a little while ago you were sitting, and now you are rising.
# Why this lack of stability?"
CRIBS = [
    "ALITTLEWHILEAGO", "YOUWEREWALKING", "STANDINGSTILL", "YOUARESITTING",
    "RISING", "STABILITY", "IDEPEND", "LACK", "PENUMBRA", "SHADOW", "PIGEON"
]

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    for w in range(16, 29):
        # 1. Row split
        rows = [indices[i:i+w] for i in range(0, len(indices), w)]

        # 2. Pattern: Row 0 linear, Row 1 reversed... (Standard Boustrophedon)
        stream = []
        for i, row in enumerate(rows):
            if i % 2 == 1: stream.extend(row[::-1])
            else: stream.extend(row)

        # 3.Substitution
        for g in range(29):
            dec = [(stream[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(stream))]
            text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])

            # 4. Search
            found = [c for c in CRIBS if c in text]
            if len(found) >= 2 or "PIGEON" in found:
                # Calculate a more complex score
                score = len(found) * 5
                if "PIGEON" in found: score += 10
                if "PENUMBRA" in found: score += 10

                if score >= 15:
                    print(f"!!! HIT !!! W={w} G={g:2d} | Found: {found}")
                    print(f"TEXT: {text[:150]}...")

attack()
