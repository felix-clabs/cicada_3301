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

def decrypt_prime_shift(ciphertext, prime_sequence):
    runes = rt.get_runes_only(ciphertext)
    result = []
    for i, r in enumerate(runes):
        c_idx = rt.RUNE_TO_INDEX[r]
        shift = prime_sequence[i]
        p_idx = (c_idx - shift) % 29
        result.append(rt.INDEX_TO_RUNE[p_idx])
    return "".join(result)

if __name__ == "__main__":
    with open("liber_primus/markdown/17_transcription.txt", "r") as f:
        content = f.read()

    n = len(rt.get_runes_only(content))
    primes = get_primes(n)

    # Try direct prime shift
    decrypted = decrypt_prime_shift(content, primes)
    print("Direct Prime Shift (First 50 runes):")
    print(decrypted[:50])
    print(rt.translate_to_latin(decrypted[:50]))
    print(f"IC: {rt.calculate_ic(decrypted):.4f}")

    # Try Atbash then Prime shift
    atbash_text = rt.atbash(content)
    decrypted_atbash_prime = decrypt_prime_shift(atbash_text, primes)
    print("\nAtbash + Prime Shift (First 50 runes):")
    print(decrypted_atbash_prime[:50])
    print(rt.translate_to_latin(decrypted_atbash_prime[:50]))
    print(f"IC: {rt.calculate_ic(decrypted_atbash_prime):.4f}")
