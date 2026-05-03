import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

# Dialogue super-cribs
SUPER_CRIBS = [
    "ALITTLEWHILEAGO", "YOUWEREWALKING", "STANDINGSTILL", "IDEPENDON", "DEPENDINGON",
    "AGO", "WHILE", "LITTLE", "WALKING", "STANDING", "STILL", "DEPEND", "SITTING"
]

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    # Block 1 starts at 23.
    # We take indices 23 to 100 to catch any start.
    black = indices[23:100]

    print("--- [FASE 33: DIALOGUE SCAN V3 (Indices 23-100)] ---")

    for g in range(29):
        # 1. Linear (L-to-R)
        dec_lin = [(black[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(black))]
        latin_lin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec_lin])

        # 2. Boustrophedon Inversa (Reverse whole black block)
        black_rev = black[::-1]
        dec_rev = [(black_rev[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(black_rev))]
        latin_rev = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec_rev])

        # 3. Line-by-line Boustrophedon (Assuming 21-22 runes per line)
        line_lens = [21, 20, 21, 22, 22] # approx
        reading_bou = []
        curr = 0
        for i, length in enumerate(line_lens):
            seg = black[curr : curr+length]
            if i % 2 == 0: reading_bou.extend(seg[::-1])
            else: reading_bou.extend(seg)
            curr += length

        dec_bou = [(reading_bou[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(reading_bou))]
        latin_bou = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec_bou])

        for crib in SUPER_CRIBS:
            if crib in latin_lin: print(f"[HIT LIN] G={g:2d} | Crib={crib:15} | TEXT={latin_lin[:60]}...")
            if crib in latin_rev: print(f"[HIT REV] G={g:2d} | Crib={crib:15} | TEXT={latin_rev[:60]}...")
            if crib in latin_bou: print(f"[HIT BOU] G={g:2d} | Crib={crib:15} | TEXT={latin_bou[:60]}...")

attack()
