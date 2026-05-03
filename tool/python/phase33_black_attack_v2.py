import sys
sys.path.append("tool/python")
import rune_tools as rt

# Recalculated TRUE P71 Key based on Page 71 decryption
P71_KEY = [1, 2, 4, 6, 10, 12, 16, 18, 22, 28, 1, 7, 11, 13, 17, 23, 0, 2, 8, 12, 14, 20, 24, 1, 9, 13, 15, 19, 21, 4, 28, 25, 2, 5, 16, 27, 3, 23, 21, 27, 4, 6, 16, 18, 22, 24, 7, 19, 23]

def to_indices(text):
    mapping = {'F':0, 'U':1, 'TH':2, 'O':3, 'R':4, 'C':5, 'K':5, 'G':6, 'W':7, 'H':8, 'N':9, 'I':10, 'J':11, 'EO':12, 'P':13, 'X':14, 'S':15, 'Z':15, 'T':16, 'B':17, 'E':18, 'M':19, 'L':20, 'NG':21, 'OE':22, 'D':23, 'A':24, 'AE':25, 'Y':26, 'IA':27, 'EA':28}
    res = []
    i = 0
    text = text.upper().replace(" ", "")
    while i < len(text):
        if i+2 <= len(text) and text[i:i+2] in mapping: res.append(mapping[text[i:i+2]]); i+=2
        elif text[i] in mapping: res.append(mapping[text[i]]); i+=1
        else: i+=1
    return res

CRIBS = {
    "A LITTLE": to_indices("ALITTLE"),
    "WHILE AGO": to_indices("WHILEAGO"),
    "YOU WERE": to_indices("YOUWERE"),
    "WALKING": to_indices("WALKING"),
    "STANDING": to_indices("STANDING"),
    "SITTING": to_indices("SITTING"),
    "DEPEND": to_indices("DEPEND")
}

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    # Block 1 starts at 23.
    black = indices[23:]

    print("--- [FASE 33: DIALOGUE ATTACK V2 (TRUE P71 KEY)] ---")

    for g in range(29):
        # 1. Linear (L-to-R)
        dec_lin = [(black[i] - P71_KEY[i % len(P71_KEY)] - g) % 29 for i in range(len(black))]
        latin_lin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec_lin])

        # 2. Boustrophedon Inversa (Reverse Input)
        l2 = black[0:21]
        rem = black[21:]
        reading = l2[::-1] + rem
        dec_bou = [(reading[i] - P71_KEY[i % len(P71_KEY)] - g) % 29 for i in range(len(reading))]
        latin_bou = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec_bou])

        for name, target in CRIBS.items():
            t_str = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in target])
            if t_str in latin_lin:
                print(f"[MATCH LIN] G={g:2d} | Crib={name:10} | {latin_lin[:80]}...")
            if t_str in latin_bou:
                print(f"[MATCH BOU] G={g:2d} | Crib={name:10} | {latin_bou[:80]}...")

attack()
