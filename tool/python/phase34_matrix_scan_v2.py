import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

# Keywords with possible phonetic variations or fragments
KEYWORDS = ["LITTLE", "WHILE", "AGO", "WALK", "STAND", "STILL", "DEPEND", "SHADOW", "PENUMBRA", "SAID", "PIGEON", "PATH", "WAY"]

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    # Range of widths: up to the full page width
    for w in range(2, 50):
        rows = [indices[i:i+w] for i in range(0, len(indices), w)]

        # Pattern 1: Row 0 linear, Row 1 reversed...
        stream1 = []
        for i, row in enumerate(rows):
            if i % 2 == 1: stream1.extend(row[::-1])
            else: stream1.extend(row)

        # Pattern 2: Row 0 reversed, Row 1 linear...
        stream2 = []
        for i, row in enumerate(rows):
            if i % 2 == 0: stream2.extend(row[::-1])
            else: stream2.extend(row)

        for s_idx, stream in enumerate([stream1, stream2]):
            for g in range(29):
                dec = [(stream[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(stream))]
                text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])

                # Success Check
                found = [kw for kw in KEYWORDS if kw in text]
                if len(found) >= 3 or ("PIGEON" in found and len(found) >= 2):
                    print(f"!!! HIT !!! W={w} Pattern={s_idx} G={g:2d} | Found: {found}")
                    print(f"TEXT: {text[:120]}...")

attack()
