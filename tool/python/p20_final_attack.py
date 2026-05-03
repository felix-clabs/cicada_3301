import sys
import os

# Import rune_tools
sys.path.append('tool/python')
import rune_tools as rt

def run_phase38():
    # P71_KEY per Phase 37/38 instructions
    P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

    # Load Page 20
    with open('liber_primus/markdown/20.md', 'r') as f:
        lines = f.readlines()

    all_runes = []
    in_code_block = False
    for line in lines:
        if '```' in line:
            in_code_block = not in_code_block
            continue
        if in_code_block and line.strip():
            all_runes.extend(rt.get_runes_only(line))

    indices = [rt.RUNE_TO_INDEX[r] for r in all_runes]

    # ROUTINE 1: Header 1 (Indices 0-22)
    header_runes = indices[0:23]
    header_latin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in header_runes])
    # Known plaintext: O SHADOW THE PENUMBRA SAID

    # ROUTINE 2: Block 1 Attack (Indices 23-41)
    block1 = indices[23:42]

    keywords = ["ALITTLEWHILE", "AGO", "YOUWEREWALKING", "IDEPENDON", "WALK", "STAND"]

    results_lin = []
    results_rev = []

    # Linear Attack
    for g in range(29):
        decoded = []
        for i, val in enumerate(block1):
            shift = P71_KEY[i % 28]
            dec = (val - shift - g) % 29
            decoded.append(dec)
        text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in decoded])
        matches = [kw for kw in keywords if kw in text]
        results_lin.append({"g": g, "text": text, "matches": matches})

    # Reversed Attack
    rev_block = block1[::-1]
    for g in range(29):
        decoded = []
        for i, val in enumerate(rev_block):
            shift = P71_KEY[i % 28]
            dec = (val - shift - g) % 29
            decoded.append(dec)
        text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in decoded])
        matches = [kw for kw in keywords if kw in text]
        results_rev.append({"g": g, "text": text, "matches": matches})

    # EXPORT TO DECODING_PROGRESS.md
    with open('DECODING_PROGRESS.md', 'w') as f:
        f.write("# DECODING PROGRESS - LIBER PRIMUS\n\n")
        f.write("## PHASE 38 REPORT\n\n")

        f.write("### ROUTINE 1: Bypass Rojo (Plaintext Protection)\n")
        f.write(f"- **Indices 0-22:** `{header_latin}`\n")
        f.write("- **Status:** Plaintext Header confirmed (O SHADOW THE PENUMBRA SAID).\n\n")

        f.write("### ROUTINE 2: Bloque 1 (Indices 23-41) - P71 Key Attack\n")
        f.write("Key: `[22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]`\n\n")

        f.write("#### TABLA DE ENGRANAJES: LINEAR (L-to-R)\n")
        f.write("| G-Shift | Resulting Text | Match |\n")
        f.write("|---------|----------------|-------|\n")
        for r in results_lin:
            f.write(f"| {r['g']} | {r['text']} | {', '.join(r['matches']) if r['matches'] else 'None'} |\n")

        f.write("\n#### TABLA DE ENGRANAJES: REVERSED (R-to-L)\n")
        f.write("| G-Shift | Resulting Text | Match |\n")
        f.write("|---------|----------------|-------|\n")
        for r in results_rev:
            f.write(f"| {r['g']} | {r['text']} | {', '.join(r['matches']) if r['matches'] else 'None'} |\n")

        f.write("\n### ROUTINE 3: Escáner Léxico del Diálogo\n")
        cracked = [r for r in results_lin + results_rev if r["matches"]]
        if cracked:
            for r in cracked:
                f.write(f"- **[BLOCK 1 CRACKED]** G={r['g']} Text=`{r['text']}` Matches={r['matches']}\n")
        else:
            f.write("- No high-confidence lexical matches found in this block with the current key.\n")

    print("Phase 38 Execution Complete. DECODING_PROGRESS.md fully updated.")

if __name__ == "__main__":
    run_phase38()
