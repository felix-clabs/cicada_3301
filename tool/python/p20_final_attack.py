import rune_tools as rt

# Key extracted from P20 dots and decrypted with P71 (Crib)
P = [15, 23, 28, 19, 5, 7, 20, 10, 26, 2, 23, 28, 0, 15, 3, 11, 25, 1, 6, 16, 19, 21, 16, 2, 21, 4, 6, 6]

def get_p20_black():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
        return [rt.RUNE_TO_INDEX[r] for r in runes[23:]]

def routine_kpa():
    """Routine 1: Known-Plaintext Attack (KPA)"""
    print("\n--- Routine 1: Known-Plaintext Attack (KPA) ---")
    black = get_p20_black()
    c_block0 = black[:28]

    # K_i = (C_i - P_i) mod 29
    k_sub = [(c - p) % 29 for c, p in zip(c_block0, P)]
    # K_i = (C_i + P_i) mod 29
    k_add = [(c + p) % 29 for c, p in zip(c_block0, P)]

    print(f"Derived Key (C-P): {k_sub}")
    print(f"Derived Key (C+P): {k_add}")

    for k_name, k_val in [("C-P", k_sub), ("C+P", k_add)]:
        # Apply k_val as Vigenere to the whole page
        res = [(c - k_val[i % 28]) % 29 for i, c in enumerate(black)]
        text = "".join([rt.INDEX_TO_RUNE[idx] for idx in res])
        ic = rt.calculate_ic(text)
        print(f"Applied Key {k_name} IC: {ic:.4f}")
        if ic > 1.4:
            print(f"Result: {rt.translate_to_latin(text[:140])}")

def routine_autokey():
    """Routine 2: Autokey (Plaintext & Ciphertext Feedback)"""
    print("\n--- Routine 2: Autokey (Feedback) ---")
    black = get_p20_black()

    # 1. Plaintext Autokey
    # P[i] = (C[i] - K[i]) % 29
    # For i < 28: K[i] = P_crib[i]
    # For i >= 28: K[i] = P[i-28]
    p_autokey = []
    for i, c in enumerate(black):
        if i < 28:
            k = P[i]
        else:
            k = p_autokey[i-28]
        p_autokey.append((c - k) % 29)

    text_p = "".join([rt.INDEX_TO_RUNE[idx] for idx in p_autokey])
    print(f"Plaintext Autokey IC: {rt.calculate_ic(text_p):.4f}")
    print(f"First 56: {rt.translate_to_latin(text_p[:56])}")

    # 2. Ciphertext Autokey
    # P[i] = (C[i] - K[i]) % 29
    # For i < 28: K[i] = P_crib[i]
    # For i >= 28: K[i] = C[i-28]
    c_autokey = []
    for i, c in enumerate(black):
        if i < 28:
            k = P[i]
        else:
            k = black[i-28]
        c_autokey.append((c - k) % 29)

    text_c = "".join([rt.INDEX_TO_RUNE[idx] for idx in c_autokey])
    print(f"Ciphertext Autokey IC: {rt.calculate_ic(text_c):.4f}")
    print(f"First 56: {rt.translate_to_latin(text_c[:56])}")

def routine_prime_gshift():
    """Routine 3: Prime G-Shift"""
    print("\n--- Routine 3: Prime G-Shift ---")
    black = get_p20_black()
    # Convert P sequence to primes
    p_primes = [rt.PRIMES[i] for i in P]

    # Use primes as Vigenere key
    res = [(c - (p % 29)) % 29 for i, (c, p) in enumerate(zip(black, p_primes * 10))]
    text = "".join([rt.INDEX_TO_RUNE[idx] for idx in res])
    print(f"Prime G-Shift IC: {rt.calculate_ic(text):.4f}")
    print(f"First 56: {rt.translate_to_latin(text[:56])}")

if __name__ == "__main__":
    routine_kpa()
    routine_autokey()
    routine_prime_gshift()
