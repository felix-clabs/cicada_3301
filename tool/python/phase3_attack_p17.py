
import rune_tools as rt
import itertools
import random
import re
from collections import Counter

# derived from solved pages 0-14 and 72
ENGLISH_RUNE_FREQ = [2.78, 4.33, 2.52, 3.58, 4.39, 4.27, 1.04, 5.58, 2.68, 2.82, 3.98, 2.08, 2.48, 6.36, 1.25, 5.30, 4.69, 1.91, 6.11, 3.32, 2.48, 2.58, 1.81, 3.66, 4.61, 2.48, 2.52, 3.84, 4.55]

def chi_square(observed, expected):
    """Calculates Chi-square statistic."""
    return sum((o - e)**2 / e for o, e in zip(observed, expected))

def get_observed_freq(runes_list):
    n = len(runes_list)
    counts = Counter(runes_list)
    return [(counts[rt.INDEX_TO_RUNE[i]] / n) * 100 for i in range(29)]

def check_success(decrypted_text, method_name):
    ic = rt.calculate_ic(decrypted_text)
    latin = rt.translate_to_latin(decrypted_text)

    # Strictly filter results
    if ic > 1.50:
        print(f"!!! [SUCCESS BY IC] !!! Method: {method_name} | IC: {ic:.4f}")
        print(f"  {latin[:300]}")
        return True

    # Check for legible words sequence
    # Heuristic: 3+ words from lexicon appearing
    hits = 0
    for w in [" THE ", " AND ", " WITH ", " FROM ", " YOUR ", " SHALL "]:
        if w in latin: hits += 1
    if hits >= 3:
        print(f"!!! [SUCCESS BY LEXICON] !!! Method: {method_name} | IC: {ic:.4f}")
        print(f"  {latin[:300]}")
        return True

    return False

def routine_1_columnar_analysis(ciphertext_runes):
    """Routine 1: Deconstruction by columns and frequency analysis."""
    n_cols = 18
    best_shifts = []

    for c in range(n_cols):
        column = ciphertext_runes[c::n_cols]
        best_col_shift = 0
        min_chi = float('inf')

        for s in range(29):
            # Apply shift s to column
            shifted_col = []
            for r in column:
                p_idx = (rt.RUNE_TO_INDEX[r] - s) % 29
                shifted_col.append(rt.INDEX_TO_RUNE[p_idx])

            obs = get_observed_freq(shifted_col)
            # Avoid division by zero in chi-square if expected freq was 0 (shouldn't be in our list)
            chi = chi_square(obs, ENGLISH_RUNE_FREQ)
            if chi < min_chi:
                min_chi = chi
                best_col_shift = s

        best_shifts.append(best_col_shift)

    # Apply Master Key
    dec_text = rt.vigenere_decrypt("".join(ciphertext_runes), best_shifts)
    ic = rt.calculate_ic(dec_text)
    print(f"Routine 1 (Columnar Chi-Sq) | Best Key IC: {ic:.4f}")
    check_success(dec_text, f"Routine 1 (Columnar Chi-Sq) | Key: {best_shifts}")
    return best_shifts

def routine_2_cyclic_prime(ciphertext_runes):
    """Routine 2: Prime-Shift Cyclic Modulo 18."""
    # First 18 primes
    primes_18 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]

    # Variant A: Direct prime shifts
    dec_a = rt.vigenere_decrypt("".join(ciphertext_runes), [p % 29 for p in primes_18])
    check_success(dec_a, "Routine 2A (Cyclic Prime)")

    # Variant B: Prime shifts with offset 28 (Page 71 style)
    dec_b = rt.vigenere_decrypt("".join(ciphertext_runes), [(p + 28) % 29 for p in primes_18])
    check_success(dec_b, "Routine 2B (Cyclic Prime + 28)")

def apply_external_key_18(ciphertext_runes, key_array):
    """Routine 3: External Key Hook."""
    if len(key_array) != 18:
        print("Error: External key must be exactly 18 integers.")
        return
    dec = rt.vigenere_decrypt("".join(ciphertext_runes), [k % 29 for k in key_array])
    ic = rt.calculate_ic(dec)
    print(f"External Key Test | IC: {ic:.4f}")
    check_success(dec, f"External Key {key_array}")

if __name__ == "__main__":
    import os
    target_path = "liber_primus/markdown/17.md"
    if not os.path.exists(target_path):
        print(f"File {target_path} not found.")
        sys.exit(1)

    with open(target_path, "r") as f:
        content = f.read()

    runes = rt.get_runes_only(content)
    atb_runes = rt.get_runes_only(rt.atbash("".join(runes)))

    targets = [("Normal", runes), ("Atbash", atb_runes)]

    for name, ct_runes in targets:
        print(f"--- FOCUSED ATTACK (LEN 18) ON {name} P17 ---")

        # Routine 1
        routine_1_columnar_analysis(ct_runes)

        # Routine 2
        routine_2_cyclic_prime(ct_runes)

    print("Attack cycle complete.")
