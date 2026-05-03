import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

with open("liber_primus/markdown/20.md", "r") as f:
    runes = rt.get_runes_only(f.read())
indices = [rt.RUNE_TO_INDEX[r] for r in runes]

# Block 1 starts at 23. Let's take index 23 to 60.
black = indices[23:61]

for g in range(29):
    # LIN
    dec_lin = [(black[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(black))]
    t_lin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec_lin])

    # BOU (first 21 runes reversed)
    l2 = black[:21]
    rem = black[21:]
    reading = l2[::-1] + rem
    dec_bou = [(reading[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(reading))]
    t_bou = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec_bou])

    print(f"G={g:2d} | LIN: {t_lin}")
    print(f"     | BOU: {t_bou}")
