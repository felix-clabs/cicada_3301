import rune_tools as rt
import os

def find_vigenere_key_len(ciphertext, max_len=30):
    runes = rt.get_runes_only(ciphertext)
    results = []
    for l in range(1, max_len + 1):
        ics = []
        for i in range(l):
            slice_str = "".join(runes[i::l])
            if len(slice_str) > 1:
                ics.append(rt.calculate_ic(slice_str))
        if ics:
            avg_ic = sum(ics) / len(ics)
            results.append((l, avg_ic))
    return results

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "liber_primus/markdown/17.md"
    if os.path.exists(path):
        with open(path, "r") as f:
            content = f.read()
        print(f"Analyzing {path}...")
        res = find_vigenere_key_len(content)
        for l, ic in sorted(res, key=lambda x: x[1], reverse=True)[:10]:
            print(f"Length {l:2}: Avg IC {ic:.4f}")
