import sys
sys.path.append("tool/python")
import rune_tools as rt

def to_indices(text):
    mapping = {'F':0, 'U':1, 'TH':2, 'O':3, 'R':4, 'C':5, 'K':5, 'G':6, 'W':7, 'H':8, 'N':9, 'I':10, 'J':11, 'EO':12, 'P':13, 'X':14, 'S':15, 'Z':15, 'T':16, 'B':17, 'E':18, 'M':19, 'L':20, 'NG':21, 'OE':22, 'D':23, 'A':24, 'AE':25, 'Y':26, 'IA':27, 'EA':28}
    res = []
    i = 0
    text = text.upper().replace(" ", "").replace("/", "")
    while i < len(text):
        if i+2 <= len(text) and text[i:i+2] in mapping: res.append(mapping[text[i:i+2]]); i+=2
        elif text[i] in mapping: res.append(mapping[text[i]]); i+=1
        else: i+=1
    return res

with open("liber_primus/markdown/71.md", "r") as f:
    runes = rt.get_runes_only(f.read())
c_indices = [rt.RUNE_TO_INDEX[r] for r in runes]

p_indices = to_indices("ANENDWITHINTHEDEEPWEBTHEREEXISTSTAPAGETHATHASHESTOITIS")

# K = (C - P) % 29
key = [(c_indices[i] - p_indices[i]) % 29 for i in range(len(p_indices))]
print(f"P71_KEY = {key}")
