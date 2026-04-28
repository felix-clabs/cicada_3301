import rune_tools as rt
import os

results = []
for i in range(73):
    fname = f"liber_primus/markdown/{i:02}_transcription.txt"
    if os.path.exists(fname):
        with open(fname, "r") as f:
            content = f.read()
        ic = rt.calculate_ic(content)
        runes = rt.get_runes_only(content)
        results.append((i, ic, len(runes)))

# Sort by IC descending
results.sort(key=lambda x: x[1], reverse=True)
for i, ic, length in results:
    print(f"Page {i:02}: IC {ic:.4f} | Length: {length}")
