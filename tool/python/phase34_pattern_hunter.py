import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

# O(3) S(15) H(8) A(24) D(23) O(3) W(7)
OSHADOW = [3, 15, 8, 24, 23, 3, 7]
# P(13) E(18) N(9) U(1) M(19) B(17) R(4) A(24)
PENUMBRA = [13, 18, 9, 1, 19, 17, 4, 24]
# P(13) I(10) G(6) EO(12) N(9)
PIGEON = [13, 10, 6, 12, 9]

def hunt():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    print("--- [HUNTING FOR OSHADOW AND PIGEON] ---")

    for w in range(16, 31):
        rows = [indices[i:i+w] for i in range(0, len(indices), w)]

        # Boustrophedon stream
        stream = []
        for i, row in enumerate(rows):
            if i % 2 == 1: stream.extend(row[::-1])
            else: stream.extend(row)

        # Test all key offsets and G-shifts
        for k_off in range(28):
            # We check the start for OSHADOW
            # (C[i] - K[i+k_off] - G) % 29 = P[i]
            # G = (C[i] - K[i+k_off] - P[i]) % 29

            # Use the first letter of OSHADOW to find G
            g = (stream[0] - P71_KEY[k_off] - OSHADOW[0]) % 29

            match_o = True
            for j in range(1, len(OSHADOW)):
                if (stream[j] - P71_KEY[(k_off + j) % 28] - g) % 29 != OSHADOW[j]:
                    match_o = False
                    break

            if match_o:
                print(f"!!! OSHADOW MATCH !!! W={w} K_Off={k_off} G={g}")
                # Now check if PIGEON exists in this stream
                dec = [(stream[i] - P71_KEY[(k_off + i) % 28] - g) % 29 for i in range(len(stream))]
                text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])
                if "PIGEON" in text:
                    print(f"    AND PIGEON FOUND! Text: {text}")
                else:
                    print(f"    (PIGEON not found)")

            # Also check for PENUMBRA at start
            g_p = (stream[0] - P71_KEY[k_off] - PENUMBRA[0]) % 29
            match_p = True
            for j in range(1, len(PENUMBRA)):
                if (stream[j] - P71_KEY[(k_off + j) % 28] - g_p) % 29 != PENUMBRA[j]:
                    match_p = False
                    break
            if match_p:
                 print(f"!!! PENUMBRA MATCH AT START !!! W={w} K_Off={k_off} G={g_p}")

if __name__ == "__main__":
    hunt()
