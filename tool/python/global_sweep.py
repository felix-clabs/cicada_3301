import sys
import os
import math
from collections import Counter

# Import rune_tools
sys.path.append('tool/python')
import rune_tools as rt

def calculate_ioc(runes):
    n = len(runes)
    if n <= 1:
        return 0.0
    counts = Counter(runes)
    sum_fi = sum(f * (f - 1) for f in counts.values())
    # Normalizing to alphabet size 29
    # IoC = (sum(fi(fi-1)) / (N(N-1))) * alphabet_size
    ioc = (sum_fi / (n * (n - 1))) * 29
    return ioc

def kasiski_examination(runes, seq_len=3):
    seqs = {}
    for i in range(len(runes) - seq_len + 1):
        seq = tuple(runes[i:i+seq_len])
        if seq not in seqs:
            seqs[seq] = []
        seqs[seq].append(i)

    distances = []
    for seq, positions in seqs.items():
        if len(positions) > 1:
            for i in range(len(positions) - 1):
                distances.append(positions[i+1] - positions[i])

    if not distances:
        return []

    def get_gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # Count frequencies of divisors of distances
    factors = []
    for d in distances:
        for i in range(2, 31): # Check key lengths 2-30
            if d % i == 0:
                factors.append(i)

    common_factors = Counter(factors).most_common(5)
    return common_factors

# Balanced Fitness Function (Routine 3)
VOWELS_GP = set(['U', 'O', 'I', 'EO', 'E', 'OE', 'A', 'AE', 'Y', 'IA', 'EA'])
NGRAM_WEIGHTS = {
    "TH": 5, "HE": 4, "IN": 4, "ER": 4, "AN": 3, "RE": 3, "ND": 3, "NG": 5, "EA": 4, "EO": 4,
    "TION": 10, "THE": 10, "ING": 8, "AND": 8
}

def balanced_fitness(text):
    score = 0
    # N-gram scoring
    for n in [2, 3, 4]:
        for i in range(len(text) - n + 1):
            gram = text[i:i+n]
            if gram in NGRAM_WEIGHTS:
                score += NGRAM_WEIGHTS[gram]

    # Consonant Penalty (Routine 3)
    consonant_streak = 0
    penalty_active = False
    for char in text:
        if char in VOWELS_GP:
            consonant_streak = 0
        else:
            consonant_streak += 1

        if consonant_streak > 3:
            penalty_active = True
            break

    if penalty_active:
        score /= 2

    return score

def run_sweep():
    results = []
    pages_dir = 'liber_primus/markdown/'

    print("Executing Routine 1: Global IoC Scanner...")
    for i in range(17, 73):
        filepath = os.path.join(pages_dir, f"{i:02d}.md")
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r') as f:
            content = f.read()
            runes = rt.get_runes_only(content)
            if not runes:
                continue

            indices = [rt.RUNE_TO_INDEX[r] for r in runes]
            ioc = calculate_ioc(indices)
            results.append({
                "page": i,
                "ioc": ioc,
                "indices": indices
            })

    # Sort by IoC descending (closest to English/1.7)
    results.sort(key=lambda x: x["ioc"], reverse=True)
    top_5 = results[:5]

    print("\nExecuting Routine 2: Kasiski Analysis on Top 5...")
    final_report_data = []
    for entry in top_5:
        p_num = entry["page"]
        ioc_val = entry["ioc"]
        kasiski = kasiski_examination(entry["indices"])
        final_report_data.append({
            "page": p_num,
            "ioc": ioc_val,
            "kasiski": kasiski
        })

    # Generate Report
    with open('GLOBAL_SWEEP_REPORT.md', 'w') as f:
        f.write("# GLOBAL VULNERABILITY SWEEP REPORT (P17-P72)\n\n")
        f.write("## 1. Top 5 Vulnerable Pages (Highest IoC)\n")
        f.write("IoC values normalized to alphabet size 29. Values closer to 1.7-2.0 indicate lower entropy.\n\n")
        f.write("| Rank | Page | IoC | Probable Key Lengths (Kasiski) |\n")
        f.write("|---|---|---|---|\n")
        for idx, item in enumerate(final_report_data):
            k_str = ", ".join([str(k[0]) for k in item["kasiski"]])
            f.write(f"| {idx+1} | {item['page']} | {item['ioc']:.4f} | {k_str} |\n")

        f.write("\n## 2. Technical Observations\n")
        f.write("- **Routine 1:** Identified potential weak links based on character distribution.\n")
        f.write("- **Routine 2:** Kasiski estimation reveals periodicity patterns in high-IoC candidates.\n")
        f.write("- **Routine 3:** Balanced N-Gram Fitness Function with Consonant Penalty has been registered for future decryption attempts.\n")

    print("\nGlobal Sweep Complete. Report generated in GLOBAL_SWEEP_REPORT.md")

if __name__ == "__main__":
    run_sweep()
