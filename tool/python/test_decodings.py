import rune_tools as rt

def get_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def decrypt_prime_vigenere(ciphertext, primes, shift=0):
    runes = rt.get_runes_only(ciphertext)
    result = []
    for i, r in enumerate(runes):
        c_idx = rt.RUNE_TO_INDEX[r]
        # Cicada usually uses the sequence of primes 2, 3, 5...
        # Shifted by some constant
        prime = primes[i]
        p_idx = (c_idx - (prime + shift)) % 29
        result.append(rt.INDEX_TO_RUNE[p_idx])
    return "".join(result)

def decrypt_vigenere_key(ciphertext, key):
    key_indices = [rt.RUNE_TO_INDEX[c] for c in key if c in rt.RUNES]
    if not key_indices:
        return ""
    return rt.vigenere_decrypt(ciphertext, key_indices)

if __name__ == "__main__":
    with open("liber_primus/markdown/17_transcription.txt", "r") as f:
        content = f.read()

    runes_only = rt.get_runes_only(content)
    n = len(runes_only)
    primes = get_primes(n)

    print("Testing variations of Prime Shift on Page 17:")
    for s in range(29):
        dec = decrypt_prime_vigenere(content, primes, shift=s)
        ic = rt.calculate_ic(dec)
        if ic > 1.3:
            print(f"Shift {s}: IC {ic:.4f}")
            print(f"  {dec[:60]}")
            print(f"  {rt.translate_to_latin(dec[:60])}")

    print("\nTesting Atbash + Prime Shift variations:")
    atbash_text = rt.atbash(content)
    for s in range(29):
        dec = decrypt_prime_vigenere(atbash_text, primes, shift=s)
        ic = rt.calculate_ic(dec)
        if ic > 1.3:
            print(f"Shift {s}: IC {ic:.4f}")
            print(f"  {dec[:60]}")
