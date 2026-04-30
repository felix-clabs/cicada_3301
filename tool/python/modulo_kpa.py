import rune_tools as rt

P_CRIB = [15, 23, 28, 19, 5, 7, 20, 10, 26, 2, 23, 28, 0, 15, 3, 11, 25, 1, 6, 16, 19, 21, 16, 2, 21, 4, 6, 6]
DOT_ABSOLUTE = [21, 22, 42, 43, 63, 64, 87, 88, 108, 109, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]

def get_p20_runes():
    with open("liber_primus/markdown/20.md", "r") as f:
        return rt.get_runes_only(f.read())

all_runes = get_p20_runes()
all_indices = [rt.RUNE_TO_INDEX[r] for r in all_runes]

# Rutina 2: Reconstrucción Modular
print("--- Rutina 2: Reconstrucción Modular de la Clave ---")

key = [None] * 28

for j, dot_idx in enumerate(DOT_ABSOLUTE):
    pos_clave = dot_idx % 28
    c_i = all_indices[dot_idx]
    p_j = P_CRIB[j]

    # K = (C - P) mod 29
    k_val = (c_i - p_j) % 29

    if key[pos_clave] is not None and key[pos_clave] != k_val:
        print(f"COLLISION at {pos_clave}: Existing {key[pos_clave]}, New {k_val}")
    key[pos_clave] = k_val

print(f"Reconstructed Key: {key}")

# Map to Latin
key_latin = []
for k in key:
    if k is None:
        key_latin.append("?")
    else:
        key_latin.append(rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[k]])

print(f"Latin Key: {' '.join(key_latin)}")

# Fill missing positions with common runes or based on patterns
# Missing: [1, 2, 5, 6, 9, 10]
# Key snippet: G ? ? O R ? ? Y H ? ? EO EA F S/Z O J AE U G T M NG/ING T TH NG/ING R G
# Wait, look at the key: ... F S/Z O J AE U G T M NG/ING T TH NG/ING R G ...
# This looks like alphabetical or sequential GP!
# F=0, U=1, TH=2, O=3, R=4...
# Let's check the indices of the key from index 12 onwards.
indices_part = key[12:]
print(f"Indices from 12 onwards: {indices_part}")
# Index 13: 15 (S)
# Index 14: 3 (O)
# Index 15: 11 (R) -- wait, no.
# Let's re-examine the Latin: G ? ? O R ? ? Y H ? ? EO EA F S/Z O J AE U G T M NG/ING T TH NG/ING R G
# Indices:
# 12: 0 (F)
# 13: 15 (S)
# 14: 3 (O)
# 15: 11 (R) -- NO.

# Let's look at the GP indices:
# F=0, U=1, TH=2, O=3, R=4, C=5, G=6, W=7, H=8, N=9, I=10, J=11, EO=12, P=13, X=14, S=15, T=16...
# Reconstructed Key Indices:
# 12: 0 (F)
# 13: 15 (S)
# 14: 3 (O)
# 15: 11 (R)
# 16: 25 (AE)
# 17: 1 (U)
# 18: 6 (G)
# 19: 16 (T)
# 20: 19 (W)
# 21: 21 (NG)
# 22: 16 (T)
# 23: 2 (TH)
# 24: 21 (NG)
# 25: 4 (R)
# 26: 6 (G)
# 27: 6 (G)

# Wait, the crib itself is: 15, 23, 28, 19, 5, 7, 20...
# Let's check the result of Applying the key.
full_key = []
for k in key:
    if k is None: full_key.append(0) # Temporary
    else: full_key.append(k)

# Decrypt
black_runes = all_runes[23:]
res = []
for i, r in enumerate(black_runes):
    c_idx = rt.RUNE_TO_INDEX[r]
    k_idx = full_key[i % 28]
    res.append((c_idx - k_idx) % 29)

text = "".join([rt.INDEX_TO_RUNE[idx] for idx in res])
print(f"IC: {rt.calculate_ic(text):.4f}")
print(f"Latin: {rt.translate_to_latin(text[:100])}")
