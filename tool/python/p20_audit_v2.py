import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [1, 2, 4, 6, 10, 12, 16, 18, 22, 28, 1, 7, 11, 13, 17, 23, 0, 2, 8, 12, 14, 20, 24, 1, 9, 13, 15, 19, 21, 4, 28, 25, 2, 5, 16, 27, 3, 23, 21, 27, 4, 6, 16, 18, 22, 24, 7, 19, 23]

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    # Red line 0-22
    # Black block 23-
    black = indices[23:70]

    print("--- [FASE 33: DUMP BLOQUE 1 CON CLAVE P71 REAL] ---")
    for g in range(29):
        # LIN
        p_lin = [(black[i] - P71_KEY[i % len(P71_KEY)] - g) % 29 for i in range(len(black))]
        t_lin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in p_lin])

        # BOU
        l2 = black[:21]
        rem = black[21:]
        reading = l2[::-1] + rem
        p_bou = [(reading[i] - P71_KEY[i % len(P71_KEY)] - g) % 29 for i in range(len(reading))]
        t_bou = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in p_bou])

        print(f"G={g:2d} | LIN: {t_lin[:50]}")
        print(f"     | BOU: {t_bou[:50]}")

attack()
