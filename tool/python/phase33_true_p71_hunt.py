import sys
sys.path.append("tool/python")
import rune_tools as rt

# Calculated from Page 71 decryption
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

KEYWORDS = ["LITTLE", "WHILE", "WALKING", "STANDING", "SITTING", "DEPEND", "SAID"]

def hunt():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    for kw in KEYWORDS:
        target = to_indices(kw)
        m = len(target)
        for start in range(len(indices) - m + 1):
            for k_off in range(len(P71_KEY)):
                # Linear
                for g in range(29):
                    match = True
                    for j in range(m):
                        c = indices[start + j]
                        k = P71_KEY[(k_off + j) % len(P71_KEY)]
                        if (c - k - g) % 29 != target[j]:
                            match = False
                            break
                    if match:
                        print(f"!!! MATCH LIN !!! Kw={kw:10} Index={start:3d} K_Off={k_off:2d} G={g:2d}")

                # Reverse Input
                segment_rev = indices[start : start + m][::-1]
                for g in range(29):
                    match = True
                    for j in range(m):
                        c = segment_rev[j]
                        k = P71_KEY[(k_off + j) % len(P71_KEY)]
                        if (c - k - g) % 29 != target[j]:
                            match = False
                            break
                    if match:
                        print(f"!!! MATCH REV !!! Kw={kw:10} Index={start:3d} K_Off={k_off:2d} G={g:2d}")

if __name__ == "__main__":
    hunt()
