import collections
import gp_core

def calculate_ioc(indices):
    """
    Calculates the Index of Coincidence for a list of indices (Base 29).
    Normalized IoC = (29 * sum(f_i * (f_i - 1))) / (N * (N - 1))
    """
    N = len(indices)
    if N <= 1:
        return 0.0

    counts = collections.Counter(indices)
    sum_fi = sum(f * (f - 1) for f in counts.values())

    ioc = sum_fi / (N * (N - 1))
    normalized_ioc = ioc * 29
    return normalized_ioc

def find_repeats(indices, min_len=3, max_len=5):
    """
    Finds repeated n-grams and returns distances between them.
    """
    repeats = collections.defaultdict(list)
    for length in range(min_len, max_len + 1):
        for i in range(len(indices) - length + 1):
            ngram = tuple(indices[i:i+length])
            repeats[ngram].append(i)

    distances = []
    for ngram, positions in repeats.items():
        if len(positions) > 1:
            for i in range(len(positions) - 1):
                for j in range(i + 1, len(positions)):
                    distances.append(positions[j] - positions[i])
    return distances

def get_factors(n, max_val=29):
    factors = []
    for i in range(2, max_val + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def kasiski_examination(indices, min_ngram=3, max_ngram=5, max_key_len=29):
    """
    Performs Kasiski examination to find likely key lengths.
    """
    distances = find_repeats(indices, min_ngram, max_ngram)
    if not distances:
        return []
    factor_counts = collections.Counter()
    for d in distances:
        factors = get_factors(d, max_key_len)
        for f in factors:
            factor_counts[f] += 1

    return factor_counts.most_common(5)

if __name__ == "__main__":
    # Test with random-ish data
    import random
    random.seed(42)
    random_indices = [random.randint(0, 28) for _ in range(1000)]
    print(f"Random IoC (should be ~1.0): {calculate_ioc(random_indices):.4f}")

    # Test with biased data (simulating plaintext)
    biased_indices = [random.choices(range(29), weights=[10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], k=1000)[0] for _ in range(1000)]
    print(f"Biased IoC (should be > 1.0): {calculate_ioc(biased_indices):.4f}")

    # Test with periodic data
    key = [1, 5, 10]
    periodic_indices = [(biased_indices[i] + key[i % len(key)]) % 29 for i in range(len(biased_indices))]
    print(f"Periodic (biased) IoC (should be < Biased IoC but > 1.0): {calculate_ioc(periodic_indices):.4f}")
    print(f"Kasiski factors (should favor 3): {kasiski_examination(periodic_indices)}")
