import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def to_indices(text):
    mapping = {'F':0, 'U':1, 'TH':2, 'O':3, 'R':4, 'C':5, 'K':5, 'G':6, 'W':7, 'H':8, 'N':9, 'I':10, 'J':11, 'EO':12, 'P':13, 'X':14, '':15, 'S':15, 'Z':15, 'T':16, 'B':17, 'E':18, 'M':19, 'L':20, 'NG':21, 'OE':22, 'D':23, 'A':24, 'AE':25, 'Y':26, 'IA':27, 'EA':28}
    res = []
    i = 0
    text = text.upper().replace(" ", "")
    while i < len(text):
        if i+2 <= len(text) and text[i:i+2] in mapping:
            res.append(mapping[text[i:i+2]])
            i += 2
        elif text[i] in mapping:
            res.append(mapping[text[i]])
            i += 1
        else:
            i += 1
    return res

KEYWORDS = [
    "LITTLE", "WHILE", "WALKING", "STANDING", "SITTING", "RISING",
    "DEPEND", "STABILITY", "SHADOW", "PENUMBRA", "SAID"
]

def hunt():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    for kw in KEYWORDS:
        target = to_indices(kw)
        m = len(target)
        for start in range(len(indices) - m + 1):
            # Test Linear with Key reset at 23
            # If start < 23, it might not use the key or use it differently.
            # But the user said "P71_KEY en el índice 23".
            # This implies for i >= 23, k_idx = (i-23) % 28.

            # Let's test all possible key offsets to be safe.
            for k_off in range(28):
                # Test Linear
                for g in range(29):
                    match = True
                    for j in range(m):
                        c = indices[start + j]
                        k = P71_KEY[(k_off + j) % 28]
                        if (c - k - g) % 29 != target[j]:
                            match = False
                            break
                    if match:
                        print(f"!!! HIT LIN !!! Kw={kw:10} Index={start:3d} K_Off={k_off:2d} G={g:2d}")

                # Test Reversed Segment
                segment_rev = indices[start : start + m][::-1]
                for g in range(29):
                    match = True
                    for j in range(m):
                        c = segment_rev[j]
                        k = P71_KEY[(k_off + j) % 28]
                        if (c - k - g) % 29 != target[j]:
                            match = False
                            break
                    if match:
                        print(f"!!! HIT REV !!! Kw={kw:10} Index={start:3d} K_Off={k_off:2d} G={g:2d}")

            # Also test Bypass (No Key)
            for g in range(29):
                match = True
                for j in range(m):
                    if (indices[start+j] - g) % 29 != target[j]:
                        match = False
                        break
                if match:
                    print(f"!!! HIT BYP !!! Kw={kw:10} Index={start:3d} G={g:2d}")

hunt()
