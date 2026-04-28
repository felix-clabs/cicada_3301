import rune_tools as rt

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def phi(n):
    result = n
    p = 2
    temp_n = n
    while p * p <= temp_n:
        if temp_n % p == 0:
            while temp_n % p == 0:
                temp_n //= p
            result -= result // p
        p += 1
    if temp_n > 1:
        result -= result // temp_n
    return result

if __name__ == "__main__":
    phis = [phi(i) for i in range(1, 500)]

    for i in range(17, 72):
        fname = f"liber_primus/markdown/{i:02}_transcription.txt"
        try:
            with open(fname, "r") as f:
                content = f.read()
            runes = rt.get_runes_only(content)
            if not runes: continue

            # Try phi(i) as shift
            res = []
            for j, r in enumerate(runes):
                c_idx = rt.RUNE_TO_INDEX[r]
                shift = phis[j]
                p_idx = (c_idx - shift) % 29
                res.append(rt.INDEX_TO_RUNE[p_idx])

            ic = rt.calculate_ic("".join(res))
            if ic > 1.3:
                print(f"Page {i} Phi Shift IC: {ic:.4f}")
                print(f"  {rt.translate_to_latin(''.join(res[:40]))}")
        except FileNotFoundError:
            pass
