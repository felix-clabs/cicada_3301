import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def to_indices(text):
    mapping = {'F':0, 'U':1, 'TH':2, 'O':3, 'R':4, 'C':5, 'K':5, 'G':6, 'W':7, 'H':8, 'N':9, 'I':10, 'J':11, 'EO':12, 'P':13, 'X':14, 'S':15, 'Z':15, 'T':16, 'B':17, 'E':18, 'M':19, 'L':20, 'NG':21, 'OE':22, 'D':23, 'A':24, 'AE':25, 'Y':26, 'IA':27, 'EA':28}
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

# Quotation from Zhuangzi
# "A little while ago you were walking, and now you are standing still"
CRIBS = {
    "A LITTLE": to_indices("ALITTLE"),
    "WHILE AGO": to_indices("WHILEAGO"),
    "WALKING": to_indices("WALKING"),
    "STANDING": to_indices("STANDING"),
    "SITTING": to_indices("SITTING"),
    "STILL": to_indices("STILL"),
    "DEPEND": to_indices("DEPEND")
}

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    # Block 1 starts at 23.
    # We test Linear and Boustrophedon Inversa.
    # We scan a range from index 23 up to 100.
    black = indices[23:]

    print("--- [FASE 33: SCANNING FOR ZHUANGZI DIALOGUE] ---")

    for name, target in CRIBS.items():
        m = len(target)
        for start_rel in range(len(black) - m + 1):
            # Test Linear
            # Key reset: first black rune (global 23) uses K[0]
            # So index 'start_rel' uses K[start_rel % 28]
            for g in range(29):
                match = True
                for j in range(m):
                    c = black[start_rel + j]
                    k = P71_KEY[(start_rel + j) % 28]
                    if (c - k - g) % 29 != target[j]:
                        match = False
                        break
                if match:
                    print(f"[LIN] FOUND '{name}' at Index {start_rel+23}, G={g}")

            # Test Boustrophedon Inversa (Reverse Input)
            # Assuming Line 2 (indices 23-43) is reversed.
            # That's black indices 0-20.
            if start_rel <= 20:
                l2 = black[0:21]
                l2_rev = l2[::-1]
                # If target fits in reversed line
                if start_rel + m <= 21:
                    segment = l2_rev[start_rel : start_rel + m]
                    for g in range(29):
                        match = True
                        for j in range(m):
                            c = segment[j]
                            k = P71_KEY[(start_rel + j) % 28] # Key follows reading order
                            if (c - k - g) % 29 != target[j]:
                                match = False
                                break
                        if match:
                            print(f"[BOU] FOUND '{name}' in reversed line 2, rel_pos {start_rel}, G={g}")

if __name__ == "__main__":
    attack()
