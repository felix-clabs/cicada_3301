import rune_tools as rt

P71_KEY = [22,7,27,8,16,5,19,22,23,24,3,13,2,25,28,22,5,4,22,8,11,19,11,11,5,21,6,9]

def get_p20_runes():
    with open("liber_primus/markdown/20.md", "r") as f:
        return rt.get_runes_only(f.read())

all_runes = get_p20_runes()
black_runes = all_runes[23:]

# Use the best alignment found: offset 0 (which corresponds to KEY[(i+23)%28])
base_decrypted = []
for i, r in enumerate(black_runes):
    c_idx = rt.RUNE_TO_INDEX[r]
    k_idx = P71_KEY[(i + 23) % 28]
    base_decrypted.append((c_idx - k_idx) % 29)

print("Testing G-Shifts on decrypted text...")
for g in range(29):
    shifted = [(idx - g) % 29 for idx in base_decrypted]
    text = "".join([rt.INDEX_TO_RUNE[idx] for idx in shifted])
    # IC remains the same, so we look for words
    latin = rt.translate_to_latin(text)
    if " THE " in latin or " AND " in latin or " OF " in latin:
        print(f"G-Shift {g}: {latin[:150]}")
