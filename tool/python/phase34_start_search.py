import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

# O SHADOW THE PENUMBRA SAID
# O(3) S(15) H(8) A(24) D(23) O(3) W(7) TH(2) E(18) P(13) E(18) N(9) U(1) M(19) B(17) R(4) A(24) S(15) A(24) I(10) D(23)
TARGET = [3, 15, 8, 24, 23, 3, 7, 2, 18, 13, 18, 9, 1, 19, 17, 4, 24, 15, 24, 10, 23]

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    for w in range(15, 30):
        rows = [indices[i:i+w] for i in range(0, len(indices), w)]
        flat = []
        for i, row in enumerate(rows):
            if i % 2 == 1: flat.extend(row[::-1])
            else: flat.extend(row)

        for g in range(29):
            dec = [(flat[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(flat))]
            # Check how many of the first 21 characters match the target
            matches = 0
            for i in range(min(len(dec), len(TARGET))):
                if dec[i] == TARGET[i]:
                    matches += 1

            if matches >= 5:
                latin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])
                print(f"W={w} G={g:2d} Matches={matches:2d} | {latin[:40]}...")

attack()
