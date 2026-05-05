import sys
import os
from collections import Counter

# Import rune_tools
sys.path.append('tool/python')
import rune_tools as rt

VOWELS_GP = set(['U', 'O', 'I', 'EO', 'E', 'OE', 'A', 'AE', 'Y', 'IA', 'EA'])
NGRAM_WEIGHTS = {
    "TH": 5, "HE": 4, "IN": 4, "ER": 4, "AN": 3, "RE": 3, "ND": 3, "NG": 5, "EA": 4, "EO": 4,
    "TION": 10, "THE": 10, "ING": 8, "AND": 8, "THAT": 8, "FOR": 7, "ARE": 7
}

def balanced_fitness(text):
    score = 0
    # N-gram scoring
    for n in [2, 3, 4]:
        for i in range(len(text) - n + 1):
            gram = text[i:i+n]
            if gram in NGRAM_WEIGHTS:
                score += NGRAM_WEIGHTS[gram]

    # Consonant Penalty
    consonant_streak = 0
    penalty_active = False
    for char in text:
        if char in VOWELS_GP:
            consonant_streak = 0
        else:
            consonant_streak += 1

        if consonant_streak > 3:
            penalty_active = True
            # We don't break, just halve the final score if it ever happens

    if penalty_active:
        score /= 2

    return score

def atbash_transform(indices):
    # GP alphabet is 29 characters (0-28)
    # Atbash: Index i becomes (28 - i)
    return [(28 - idx) for idx in indices]

def run_p72_attack():
    p72_path = 'liber_primus/markdown/72.md'
    if not os.path.exists(p72_path):
        print(f"Error: {p72_path} not found.")
        return

    with open(p72_path, 'r') as f:
        runes = rt.get_runes_only(f.read())

    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    results = []

    # ROUTINE 1: Caesar Sweep (29 G-Shifts)
    for g in range(29):
        dec_indices = [(idx - g) % 29 for idx in indices]
        text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[i]].split('/')[0] for i in dec_indices])
        score = balanced_fitness(text)
        results.append({
            "method": f"Shift {g}",
            "score": score,
            "text": text
        })

    # ROUTINE 2: Atbash Attack
    atbash_indices = atbash_transform(indices)
    atbash_text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[i]].split('/')[0] for i in atbash_indices])
    atbash_score = balanced_fitness(atbash_text)
    results.append({
        "method": "Atbash",
        "score": atbash_score,
        "text": atbash_text
    })

    # Also test Atbash + Shift (sometimes possible)
    for g in range(29):
        dec_indices = [(idx - g) % 29 for idx in atbash_indices]
        text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[i]].split('/')[0] for i in dec_indices])
        score = balanced_fitness(text)
        results.append({
            "method": f"Atbash + Shift {g}",
            "score": score,
            "text": text
        })

    # ROUTINE 3: Heuristic Analysis (Sort by Score)
    results.sort(key=lambda x: x["score"], reverse=True)
    top_3 = results[:3]

    print("PHASE 44: TOP CANDIDATES FOR P72")
    for idx, res in enumerate(top_3):
        print(f"{idx+1}. Method: {res['method']} | Score: {res['score']}")
        print(f"   Snippet: {res['text'][:100]}...")

    # Update DECODING_PROGRESS.md
    with open('DECODING_PROGRESS.md', 'a') as f:
        f.write("\n## PHASE 44 REPORT: PAGE 72 MONOALPHABETIC CRACK\n\n")
        f.write("### TOP CANDIDATES\n")
        f.write("| Method | Score | Snippet |\n")
        f.write("|---|---|---|\n")
        for res in top_3:
            f.write(f"| {res['method']} | {res['score']} | `{res['text'][:100]}...` |\n")

        f.write(f"\n**Verdict:** The winning method for Page 72 is **{top_3[0]['method']}**.\n")

if __name__ == "__main__":
    run_p72_attack()
