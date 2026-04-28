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

def decrypt_prime(runes, primes, shift, mode='sub'):
    result = []
    for i, r in enumerate(runes):
        c_idx = rt.RUNE_TO_INDEX[r]
        p = primes[i]
        if mode == 'sub':
            p_idx = (c_idx - (p + shift)) % 29
        else:
            p_idx = (c_idx + (p + shift)) % 29
        result.append(rt.INDEX_TO_RUNE[p_idx])
    return "".join(result)

def decrypt_prime_v2(runes, primes, shift, mode='sub'):
    # In some versions, the prime used for the first rune might not be 2.
    # Let's try skipping first N primes.
    result = []
    # Actually, the PHP code uses GetNextPrime(1) which is 2.
    # But let's try starting at different primes.
    pass

if __name__ == "__main__":
    max_len = 500
    all_primes = get_primes(max_len + 100)

    for i in range(17, 72):
        fname = f"liber_primus/markdown/{i:02}_transcription.txt"
        try:
            with open(fname, "r") as f:
                content = f.read()
            runes = rt.get_runes_only(content)
            if not runes: continue

            for skip in range(10): # Try starting at different positions in the prime sequence
                primes = all_primes[skip:skip+len(runes)]
                for mode in ['sub', 'add']:
                    for s in range(29):
                        dec = decrypt_prime(runes, primes, s, mode)
                        ic = rt.calculate_ic(dec)
                        if ic > 1.4:
                            print(f"Page {i:02} | Skip: {skip} | Mode: {mode} | Shift: {s:2} | IC: {ic:.4f}")
                            if ic > 1.6:
                                print(f"  {rt.translate_to_latin(dec[:60])}")
        except FileNotFoundError:
            pass
