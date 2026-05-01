import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def get_golden():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]
    return [(indices[i] - P71_KEY[i % 28]) % 29 for i in range(len(indices))]

golden = get_golden()

# Search for any string of 4+ letters from the lexicon in ANY G-shift
LEXICON = ["PENUMBRA", "SHADOW", "CICADA", "PIGEON", "PENG", "LAUGHED", "SAID", "ASKED"]

for g in range(29):
    shifted = [(idx - g) % 29 for idx in golden]
    latin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in shifted])
    for w in LEXICON:
        if w in latin:
            print(f"G={g:2d}: Found {w} at index {latin.find(w)}")

# Test reversed
for g in range(29):
    shifted = [(idx - g) % 29 for idx in golden[::-1]]
    latin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in shifted])
    for w in LEXICON:
        if w in latin:
            print(f"G={g:2d} (REV): Found {w} at index {latin.find(w)}")
