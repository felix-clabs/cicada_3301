import rune_tools as rt

P71_KEY = [22,7,27,8,16,5,19,22,23,24,3,13,2,25,28,22,5,4,22,8,11,19,11,11,5,21,6,9]
DOT_ABSOLUTE = [21, 22, 42, 43, 63, 64, 87, 88, 108, 109, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]

def get_p20_runes():
    with open("liber_primus/markdown/20.md", "r") as f:
        return rt.get_runes_only(f.read())

all_runes = get_p20_runes()
all_indices = [rt.RUNE_TO_INDEX[r] for r in all_runes]

decrypted_indices = []
for i, c_idx in enumerate(all_indices):
    k_idx = P71_KEY[i % 28]
    decrypted_indices.append((c_idx - k_idx) % 29)

dot_decrypted = [decrypted_indices[idx] for idx in DOT_ABSOLUTE]
dot_latin = [rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]] for idx in dot_decrypted]

print(f"Decrypted runes at dot positions: {' '.join(dot_latin)}")

# Crib provided by user
CRIB_LATIN = "S/Z D EA M C/K W L I Y TH D EA F S/Z O J AE U G T M NG/ING T TH NG/ING R G G"
print(f"Crib provided by user:          {CRIB_LATIN}")
