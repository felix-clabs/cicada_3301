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

with open("liber_primus/markdown/71_transcription.txt", "r") as f:
    content = f.read()

runes = rt.get_runes_only(content)
primes = get_primes(len(runes))
dec = decrypt_prime(runes, primes, 28, 'sub')
print("Decrypted Page 71:")
print(rt.translate_to_latin(dec))
