import sys
import os

# Import rune_tools
sys.path.append('tool/python')
import rune_tools as rt

def to_indices(text):
    mapping = {'F':0, 'U':1, 'TH':2, 'O':3, 'R':4, 'C':5, 'K':5, 'G':6, 'W':7, 'H':8, 'N':9, 'I':10, 'J':11, 'EO':12, 'P':13, 'X':14, 'S':15, 'Z':15, 'T':16, 'B':17, 'E':18, 'M':19, 'L':20, 'NG':21, 'OE':22, 'D':23, 'A':24, 'AE':25, 'Y':26, 'IA':27, 'EA':28}
    res = []; i = 0; text = text.upper().replace(' ', '')
    while i < len(text):
        if i+2 <= len(text) and text[i:i+2] in mapping: res.append(mapping[text[i:i+2]]); i+=2
        elif text[i] in mapping: res.append(mapping[text[i]]); i+=1
        else: i+=1
    return res

def crib_drag_with_g(stream, crib_text, start_offset):
    target = to_indices(crib_text)
    results = []
    for j in range(len(stream) - len(target) + 1):
        g_shifts = [(stream[j+k] - target[k]) % 29 for k in range(len(target))]
        if len(set(g_shifts)) == 1:
            results.append((j + start_offset, g_shifts[0]))
    return results

def run_phase41():
    P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

    # Load Page 20
    with open('liber_primus/markdown/20.md', 'r') as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    # Lower Block starts at 141 (black runes)
    lower_ct = indices[141:263]

    # Process Linear: (C - K) % 29
    stream_lin = [(indices[i] - P71_KEY[i % 28]) % 29 for i in range(141, 263)]

    # Process Boustro: Entire Lower Block reversed
    # Reading runes 262, 261... 141
    # Key pointer still follows absolute page index?
    # Directive: "para la runa en el índice 141... aplica P71_KEY[141 % 28]"
    # Usually Boustro means reversing the ciphertext sequence THEN applying key.
    lower_rev_ct = indices[141:263][::-1]
    stream_bou = []
    for i, val_c in enumerate(lower_rev_ct):
        abs_idx = 141 + i # Absolute page index for the key
        stream_bou.append((val_c - P71_KEY[abs_idx % 28]) % 29)

    cribs = [
        "THE CICADA", "LITTLE DOVE", "LAUGHED AND SAID",
        "FLYING THROUGH", "NINETY THOUSAND", "THE GREAT PENG",
        "CICADA", "LAUGHED", "DOVE"
    ]

    all_matches = []
    for s_name, stream in [("LINEAR", stream_lin), ("BOUSTRO", stream_bou)]:
        for crib in cribs:
            found = crib_drag_with_g(stream, crib, 141)
            for pos, g in found:
                all_matches.append(f"- **[CRIB DRAG SUCCESS]** Mode={s_name}, Word=`{crib}`, Index={pos}, G-Shift={g}")

    # Update DECODING_PROGRESS.md
    with open('DECODING_PROGRESS.md', 'w') as f:
        f.write("# DECODING PROGRESS - LIBER PRIMUS\n\n")
        f.write("## PHASE 41 REPORT: LOWER BLOCK ATTACK\n\n")
        f.write("### [STRATEGY]\n")
        f.write("- **Target:** Lower Block (Indices 141-262).\n")
        f.write("- **Key:** Continuous P71 from index 0.\n")
        f.write("- **Anchors:** PIGEON (123-140, G=0), PATH (110, G=23).\n\n")

        if all_matches:
            f.write("### [CRIB DRAG SUCCESS]\n")
            for m in all_matches:
                f.write(m + "\n")
            f.write("\n")
        else:
            f.write("### [RESULTS]\n")
            f.write("- No constant G-shift matches found for Zhuangzi Chapter 1 keywords in the lower block.\n\n")

    if all_matches:
        for m in all_matches: print(m)
    else:
        print("Phase 41 Complete: No matches found.")

if __name__ == "__main__":
    run_phase41()
