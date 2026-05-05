import sys
import os
from collections import Counter

# Import rune_tools
sys.path.append('tool/python')
import rune_tools as rt

def balanced_fitness(text):
    score = 0
    # N-gram scoring
    for n in [2, 3, 4]:
        for i in range(len(text) - n + 1):
            gram = text[i:i+n]
            if gram in rt.NGRAM_WEIGHTS:
                score += rt.NGRAM_WEIGHTS[gram]

    # Consonant Penalty
    consonant_streak = 0
    penalty_active = False
    for char in text:
        if char in rt.VOWELS_GP:
            consonant_streak = 0
        else:
            consonant_streak += 1
        if consonant_streak > 3:
            penalty_active = True

    if penalty_active:
        score /= 2

    return score

def atbash_transform(indices):
    return [(28 - idx) for idx in indices]

def run():
    path = 'liber_primus/markdown/72.md'
    if not os.path.exists(path):
        print(f"Error: {path} not found.")
        return

    with open(path, 'r') as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    results = []
    # Routine 1: Shifts
    for g in range(29):
        dec_indices = [(idx - g) % 29 for idx in indices]
        text = rt.translate_to_latin("".join([rt.INDEX_TO_RUNE[i] for i in dec_indices]))
        score = balanced_fitness(text)
        results.append({"method": f"Shift {g}", "score": score, "text": text})

    # Routine 2: Atbash
    atbash_indices = atbash_transform(indices)
    for g in range(29):
        dec_indices = [(idx - g) % 29 for idx in atbash_indices]
        text = rt.translate_to_latin("".join([rt.INDEX_TO_RUNE[i] for i in dec_indices]))
        score = balanced_fitness(text)
        results.append({"method": f"Atbash + Shift {g}" if g > 0 else "Atbash", "score": score, "text": text})

    results.sort(key=lambda x: x["score"], reverse=True)
    top_3 = results[:3]

    print("TOP CANDIDATES FOR P72")
    for idx, res in enumerate(top_3):
        print(f"{idx+1}. Method: {res['method']} | Score: {res['score']}")

    with open('DECODING_PROGRESS.md', 'a') as f:
        f.write("\n## PAGE 72 REPORT\n\n")
        f.write("| Method | Score | Snippet |\n|---|---|---|\n")
        for res in top_3:
            f.write(f"| {res['method']} | {res['score']} | `{res['text'][:100]}...` |\n")

if __name__ == "__main__":
    run()
