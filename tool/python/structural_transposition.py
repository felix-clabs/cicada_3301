import rune_tools as rt
from collections import Counter

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def get_golden_indices():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]
    golden = []
    # Best alignment offset found is 0
    for i, idx in enumerate(indices):
        golden.append((idx - P71_KEY[i % 28]) % 29)
    return golden

def check_anagrams(indices, block_name):
    print(f"\n--- Anagram Analysis for {block_name} ---")
    counts = Counter(indices)
    keywords = {
        "PILGRIM": ["P", "I", "L", "G", "R", "I", "M"],
        "DIVINITY": ["D", "I", "V", "I", "N", "I", "T", "Y"],
        "WISDOM": ["W", "I", "S/Z", "D", "O", "M"],
        "TRUTH": ["T", "R", "U", "T", "H"]
    }

    for word, chars in keywords.items():
        word_indices = []
        for char in chars:
            for rune, latin, prime in rt.GEMATRIA_PRIMUS:
                if char in latin.split('/'):
                    word_indices.append(rt.RUNE_TO_INDEX[rune])
                    break

        word_counts = Counter(word_indices)
        if all(counts[idx] >= count for idx, count in word_counts.items()):
            print(f"!!! '{word}' CAN be formed from the {block_name} block inventory.")

def execute():
    golden = get_golden_indices()
    # Segments delimited by dot pairs (indices of dots: 21,22, 42,43, 63,64, 87,88, 108,109, 123-140)
    segments = [
        golden[0:21],    # S0
        golden[23:42],   # S1
        golden[44:63],   # S2
        golden[65:87],   # S3
        golden[89:108],  # S4
        golden[110:123], # S5
        golden[141:263]  # S6 (Lower Block)
    ]

    print("--- Structural Transposition Analysis (Phase 20) ---")
    upper = [idx for s in segments[:6] for idx in s]
    lower = segments[6]

    check_anagrams(upper, "Upper")
    check_anagrams(lower, "Lower")

    # Boustrophedon / Route Routing
    print("\n--- Route Routing (Boustrophedon) ---")
    v1 = []
    for i, s in enumerate(segments):
        if i % 2 == 1:
            v1.extend(reversed(s))
            print(f"Segment {i} (len {len(s)}): REVERSED")
        else:
            v1.extend(s)
            print(f"Segment {i} (len {len(s)}): NORMAL")

    text = "".join([rt.INDEX_TO_RUNE[idx] for idx in v1])
    print(f"\nBoustrophedon (Odd Reversed) IC: {rt.calculate_ic(text):.4f}")
    print(f"Latin Result (First 200 runes):")
    print(rt.translate_to_latin(text[:200]))

if __name__ == "__main__":
    execute()
