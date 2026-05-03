import sys
sys.path.append("tool/python")
import rune_tools as rt

# TRUE P71 KEY (from Page 71)
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

target = to_indices("OSHADOWTHEPENUMBRASAID")

with open("liber_primus/markdown/20.md", "r") as f:
    runes = rt.get_runes_only(f.read())
red = [rt.RUNE_TO_INDEX[r] for r in runes[:23]]

for k_off in range(len(P71_KEY)):
    for g in range(29):
        dec = [(red[i] - P71_KEY[(k_off + i) % len(P71_KEY)] - g) % 29 for i in range(len(red))]
        matches = 0
        for i in range(min(len(dec), len(target))):
            if dec[i] == target[i]: matches += 1
        if matches >= 15:
            latin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])
            print(f"!!! RED HIT !!! K_Off={k_off} G={g} Matches={matches} | {latin}")

# Also try without P71 (Bypass) again but for "O SHADOW THE PENUMBRA SAID"
for g in range(29):
    dec = [(red[i] - g) % 29 for i in range(len(red))]
    matches = 0
    for i in range(min(len(dec), len(target))):
        if dec[i] == target[i]: matches += 1
    if matches >= 15:
        latin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])
        print(f"!!! BYPASS HIT !!! G={g} Matches={matches} | {latin}")
