import sys
sys.path.append("tool/python")
import rune_tools as rt

# P71 Key derived from Page 71 decryption (Length 28)
P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def get_p20_data():
    with open("liber_primus/markdown/20.md", "r") as f:
        # Get all lines and their runes
        lines = [rt.get_runes_only(line) for line in f.readlines() if rt.get_runes_only(line)]

    all_runes = []
    red_indices = set()

    current_idx = 0
    for i, line in enumerate(lines):
        # Line 1 (i=0) and Line 7 (i=6) are red headers
        if i == 0 or i == 6:
            for _ in range(len(line)):
                red_indices.add(current_idx)
                current_idx += 1
        else:
            current_idx += len(line)
        all_runes.extend(line)

    return all_runes, red_indices

def execute_attack(w, mode="sub"):
    runes, red_indices = get_p20_data()
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    # Routine 1: Load Matrix (W columns)
    rows = []
    orig_pos_rows = []
    for i in range(0, len(indices), w):
        rows.append(indices[i:i+w])
        orig_pos_rows.append(list(range(i, min(i+w, len(indices)))))

    # Routine 2: Structural Boustrophedon
    # Even rows (0, 2, ...) L2R, Odd rows (1, 3, ...) R2L
    flat_indices = []
    flat_orig_pos = []
    for i, row in enumerate(rows):
        if i % 2 == 1:
            flat_indices.extend(row[::-1])
            flat_orig_pos.extend(orig_pos_rows[i][::-1])
        else:
            flat_indices.extend(row)
            flat_orig_pos.extend(orig_pos_rows[i])

    # Routine 3: Strict Pointer Substitution
    k = 0
    decoded_indices = []
    for i in range(len(flat_indices)):
        orig_idx = flat_orig_pos[i]
        val = flat_indices[i]

        if orig_idx in red_indices:
            # Red rune: Intact, bypass key
            decoded_indices.append(val)
        else:
            # Black rune: Decrypt
            if mode == "sub":
                dec = (val - P71_KEY[k % 28]) % 29
            else: # add
                dec = (val + P71_KEY[k % 28]) % 29
            decoded_indices.append(dec)
            k += 1

    text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in decoded_indices])
    return text

if __name__ == "__main__":
    print("--- [PHASE 36: BOUSTROPHEDON EXECUTION] ---")
    for w in [27]:
        for mode in ["sub", "add"]:
            res = execute_attack(w, mode)
            print(f"W={w} MODE={mode}")
            print(f"FIRST 50: {res[:50]}")
            # Check for keywords in full text
            keywords = ["SHADOW", "PENUMBRA", "LITTLE", "AGO", "WHILE", "PIGEON", "WALK", "STAND"]
            found = [kw for kw in keywords if kw in res]
            if found:
                print(f"KEYWORDS FOUND: {found}")
            print("-" * 20)
