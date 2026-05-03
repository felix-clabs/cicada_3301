import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    # Block 1 starts at index 23.
    # We take enough runes for the dialogue.
    black = indices[23:70]

    print("--- [FASE 33: DUMP BLOQUE 1 (23-69)] ---")
    for g in range(29):
        # Linear decryption with pointer reset at 23
        p_lin = [(black[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(black))]
        t_lin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in p_lin])

        # Boustrophedon Inversa (assuming Line 2 reversed)
        # Line 2: 23-43 (21 runes)
        l2 = black[:21]
        rem = black[21:]
        reading = l2[::-1] + rem
        p_bou = [(reading[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(reading))]
        t_bou = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in p_bou])

        # Scan for crib fragments: LITTLE, WHILE, AGO, WALK, STAND, STILL, DEPEND, SIT
        cribs = ["LITTLE", "WHILE", "AGO", "WALK", "STAND", "STILL", "DEPEND", "SITTING", "YOU", "ARE"]
        for c in cribs:
            if c in t_lin: print(f"[HIT LIN] G={g:2d} | Crib={c:8} | TEXT={t_lin[:60]}...")
            if c in t_bou: print(f"[HIT BOU] G={g:2d} | Crib={c:8} | TEXT={t_bou[:60]}...")

attack()
