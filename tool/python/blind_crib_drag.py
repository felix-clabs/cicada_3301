import rune_tools as rt

P_CRIB = [15, 23, 28, 19, 5, 7, 20, 10, 26, 2, 23, 28, 0, 15, 3, 11, 25, 1, 6, 16, 19, 21, 16, 2, 21, 4, 6, 6]

def get_p20_runes():
    with open("liber_primus/markdown/20.md", "r") as f:
        return rt.get_runes_only(f.read())

def blind_crib_drag():
    all_runes = get_p20_runes()
    black_indices = [rt.RUNE_TO_INDEX[r] for r in all_runes[23:]]

    # Drag a 5-rune fragment of the crib
    crib_frag = P_CRIB[:5]
    print(f"Dragging Crib Fragment: {rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in crib_frag])}")

    for i in range(len(black_indices) - len(crib_frag)):
        k_frag = [(black_indices[i+j] - crib_frag[j]) % 29 for j in range(len(crib_frag))]
        # Check if k_frag matches the P71 key at any position
        # P71_KEY = [22,7,27,8,16,5,19,22,23,24,3,13,2,25,28,22,5,4,22,8,11,19,11,11,5,21,6,9]
        pass

blind_crib_drag()
