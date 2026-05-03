import sys
sys.path.append("tool/python")
import rune_tools as rt

OSHADOW = [3, 15, 8, 24, 23, 3, 7]
PENUMBRA = [13, 18, 9, 1, 19, 17, 4, 24]
PIGEON = [13, 10, 6, 12, 9]

def hunt():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    for w in range(16, 31):
        rows = [indices[i:i+w] for i in range(0, len(indices), w)]
        stream = []
        for i, row in enumerate(rows):
            if i % 2 == 1: stream.extend(row[::-1])
            else: stream.extend(row)

        # Bypass (No Key)
        for g in range(29):
            dec = [(idx - g) % 29 for idx in stream]
            text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])

            if "OSHADOW" in text or "PENUMBRA" in text:
                print(f"!!! BYPASS HIT !!! W={w} G={g} | Found at start: {text[:25]}")
                if "PIGEON" in text: print("    PIGEON FOUND TOO!")

hunt()
