import collections

def calculate_ioc(indices):
    N = len(indices)
    if N <= 1:
        return 0.0
    counts = collections.Counter(indices)
    sum_fi = sum(f * (f - 1) for f in counts.values())
    ioc = sum_fi / (N * (N - 1))
    return ioc * 29

def get_factors(n, max_val=40):
    factors = []
    for i in range(2, max_val + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def kasiski_examination(indices, min_ngram=3, max_ngram=5, max_key_len=40):
    ngram_positions = collections.defaultdict(list)
    for length in range(min_ngram, max_ngram + 1):
        for i in range(len(indices) - length + 1):
            ngram = tuple(indices[i:i+length])
            ngram_positions[ngram].append(i)
    distances = []
    for positions in ngram_positions.values():
        if len(positions) > 1:
            for i in range(len(positions) - 1):
                for j in range(i + 1, len(positions)):
                    distances.append(positions[j] - positions[i])
    if not distances:
        return []
    factor_counts = collections.Counter()
    for d in distances:
        for f in get_factors(d, max_key_len):
            factor_counts[f] += 1
    return [f[0] for f in factor_counts.most_common(5)]
