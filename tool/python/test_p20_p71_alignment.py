import rune_tools as rt

P71_KEY = [22,7,27,8,16,5,19,22,23,24,3,13,2,25,28,22,5,4,22,8,11,19,11,11,5,21,6,9]

def get_p20_runes():
    with open("liber_primus/markdown/20.md", "r") as f:
        return rt.get_runes_only(f.read())

all_runes = get_p20_runes()
black_runes = all_runes[23:]

print("Testing Page 20 decryption using Page 71 key with absolute alignment...")

for offset in range(28):
    decrypted = []
    for i, r in enumerate(black_runes):
        c_idx = rt.RUNE_TO_INDEX[r]
        # Absolute index of this rune is i + 23
        # We try all possible offsets for the key alignment
        k_idx = P71_KEY[(i + 23 + offset) % 28]
        decrypted.append((c_idx - k_idx) % 29)

    text = "".join([rt.INDEX_TO_RUNE[idx] for idx in decrypted])
    ic = rt.calculate_ic(text)
    if ic > 1.3:
        print(f"Offset {offset} IC: {ic:.4f}")
        print(f"Latin: {rt.translate_to_latin(text[:140])}")

# Also try Addition
print("\nTesting with Addition...")
for offset in range(28):
    decrypted = []
    for i, r in enumerate(black_runes):
        c_idx = rt.RUNE_TO_INDEX[r]
        k_idx = P71_KEY[(i + 23 + offset) % 28]
        decrypted.append((c_idx + k_idx) % 29)

    text = "".join([rt.INDEX_TO_RUNE[idx] for idx in decrypted])
    ic = rt.calculate_ic(text)
    if ic > 1.3:
        print(f"Offset {offset} IC: {ic:.4f}")
