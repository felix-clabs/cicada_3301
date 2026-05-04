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

def run_phase40_exhaustive():
    P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

    with open('liber_primus/markdown/20.md', 'r') as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    # First 60 runes
    ct_60 = indices[:60]

    cribs = [
        ("PENUMBRA", "PENUMBRA"),
        ("SHADOW", "SHADOW"),
        ("LITTLE", "LITTLE"),
        ("WHILE AGO", "WHILEAGO"),
        ("WALKING", "WALKING"),
        ("O SHADOW THE PENUMBRA SAID", "OSHADOWTHEPENUMBRASAID"),
        ("THE PENUMBRA SAID", "THEPENUMBRASAID"),
        ("SAID TO THE SHADOW", "SAIDTOTHESHADOW"),
        ("A LITTLE WHILE AGO", "ALITTLEWHILEAGO")
    ]

    all_results = []

    # Test configurations
    # Config 1: Linear
    # Config 2: Boustro (indices 23-60 reversed)

    for s_name in ["LINEAR", "BOUSTRO"]:
        current_ct = list(ct_60)
        if s_name == "BOUSTRO":
            current_ct[23:60] = current_ct[23:60][::-1]

        # Test every possible start offset of the P71 key
        for k_off in range(len(P71_KEY)):
            # Base decrypted stream for this alignment
            base_stream = [(current_ct[i] - P71_KEY[(i + k_off) % 28]) % 29 for i in range(len(current_ct))]

            for c_name, c_text in cribs:
                target = to_indices(c_text)
                for j in range(len(base_stream) - len(target) + 1):
                    # Calculate shifts
                    g_shifts = [(base_stream[j+k] - target[k]) % 29 for k in range(len(target))]
                    if len(set(g_shifts)) == 1:
                        all_results.append({
                            "mode": s_name,
                            "word": c_name,
                            "index": j,
                            "g": g_shifts[0],
                            "k_off": k_off
                        })

    # Filter and format results
    unique_matches = []
    seen = set()
    for res in all_results:
        key = (res["mode"], res["word"], res["index"], res["g"], res["k_off"])
        if key not in seen:
            unique_matches.append(res)
            seen.add(key)

    # Output to DECODING_PROGRESS.md
    with open('DECODING_PROGRESS.md', 'w') as f:
        f.write("# DECODING PROGRESS - LIBER PRIMUS\n\n")
        f.write("## PHASE 40 REPORT: EXHAUSTIVE CRIB DRAGGING\n\n")

        if unique_matches:
            f.write("### [CRIB DRAG SUCCESS]\n")
            for m in unique_matches:
                f.write(f"- Mode={m['mode']}, Word=`{m['word']}`, Index={m['index']}, G-Shift={m['g']}, KeyOffset={m['k_off']}\n")
            f.write("\n")
        else:
            f.write("### [CRIB DRAG RESULTS]\n")
            f.write("- No constant G-shift matches found for any alignment or geometry.\n\n")

        f.write("### TECHNICAL AUDIT\n")
        f.write("- **Scan Range:** Indices 0-60.\n")
        f.write("- **Key Stream:** Continuous P71 (tested all 28 offsets).\n")
        f.write("- **Geometries:** Linear and Segmented Boustrophedon (23-60 rev).\n")
        f.write("- **Cribs:** Zhuangzi dialogue components.\n")

    if unique_matches:
        for m in unique_matches:
            print(f"SUCCESS: {m['word']} at {m['index']} (G={m['g']}, KOff={m['k_off']}, Mode={m['mode']})")
    else:
        print("Phase 40 Exhaustive Scan Complete: No matches found.")

if __name__ == "__main__":
    run_phase40_exhaustive()
