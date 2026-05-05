import sys
import os
import math
from collections import Counter

# Import rune_tools
sys.path.append('tool/python')
import rune_tools as rt

# Master Key from Page 71
MASTER_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def calculate_fitness(text):
    score = 0
    # Check 2-grams, 3-grams, 4-grams
    for n in [2, 3, 4]:
        for i in range(len(text) - n + 1):
            gram = text[i:i+n]
            if gram in rt.NGRAM_WEIGHTS:
                score += rt.NGRAM_WEIGHTS[gram]

    # Penalize impossible clusters
    v_count = 0
    c_count = 0
    for char in text:
        if char in "UOIEA": # Simple check
            v_count += 1
            c_count = 0
        else:
            c_count += 1
            v_count = 0
        if v_count >= 5 or c_count >= 5:
            score -= 20

    return score

def run():
    # Load Page 20
    path = 'liber_primus/markdown/20.md'
    if not os.path.exists(path):
        print(f"Error: {path} not found.")
        return

    with open(path, 'r') as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    print("--- ROUTINE 1: THE GHOST TEST ---")
    ghost_block = []
    for i in range(min(115, len(indices)), min(150, len(indices))):
        p = (indices[i] - MASTER_KEY[i % len(MASTER_KEY)]) % 29
        lat = rt.translate_to_latin(rt.INDEX_TO_RUNE[p])
        ghost_block.append(lat)

    ghost_text = "".join(ghost_block)
    print(f"Context (115-150): {ghost_text}")

    print("\n--- ROUTINE 2: BLIND N-GRAM SCAN ---")
    targets = [
        ("Block 1", 23, 42),
        ("Lower Block", 141, min(263, len(indices)))
    ]

    best_results = []
    for name, start, end in targets:
        if start >= len(indices): continue
        print(f"Scanning {name}...")
        results = []
        for g in range(29):
            for mode in ["LINEAR", "REVERSED"]:
                if mode == "REVERSED":
                    rev_indices = list(range(start, end))[::-1]
                    decoded = []
                    for idx in rev_indices:
                        val_p = (indices[idx] - MASTER_KEY[idx % len(MASTER_KEY)] - g) % 29
                        decoded.append(val_p)
                else:
                    decoded = []
                    for i in range(start, end):
                        val_p = (indices[i] - MASTER_KEY[i % len(MASTER_KEY)] - g) % 29
                        decoded.append(val_p)

                text = rt.translate_to_latin("".join([rt.INDEX_TO_RUNE[idx] for idx in decoded]))
                score = calculate_fitness(text)
                results.append((score, g, mode, text))

        results.sort(key=lambda x: x[0], reverse=True)
        best_results.append((name, results[:3]))

    # Output report
    with open('DECODING_PROGRESS.md', 'w') as f:
        f.write("# DECODING PROGRESS - PAGE 20\n\n")
        for name, tops in best_results:
            f.write(f"#### Best candidates for {name}:\n")
            f.write("| Score | G | Mode | Text |\n|---|---|---|---|\n")
            for score, g, mode, text in tops:
                f.write(f"| {score} | {g} | {mode} | `{text}` |\n")
            f.write("\n")

    print("Execution Complete. Results in DECODING_PROGRESS.md")

if __name__ == "__main__":
    run()
