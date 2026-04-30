import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def get_golden():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]
    return [(idx - P71_KEY[i % 28]) % 29 for i, idx in enumerate(indices)]

def routine_final_mantra():
    golden = get_golden()

    # 1. Fragmentación Estructural (Phase 20/21)
    segments = [
        golden[0:21],    # S0
        golden[23:42],   # S1
        golden[44:63],   # S2
        golden[65:87],   # S3
        golden[89:108],  # S4
        golden[110:123], # S5
        golden[123:141], # Costura (PIGEON Anchor)
        golden[141:263]  # Bloque Inferior
    ]

    # 2. Ensamblaje Boustrophedon (Variant IC 1.83)
    # Rev: S1, S3, S5
    u_proc = segments[0] + list(reversed(segments[1])) + segments[2] + list(reversed(segments[3])) + segments[4] + list(reversed(segments[5]))

    # Seam is linear (contains PIGEON)
    seam_proc = segments[6]

    # Lower is linear for now
    l_proc = segments[7]

    full_indices = u_proc + seam_proc + l_proc

    # Search for "PILGRIM" (13, 10, 20, 6, 4, 10, 19) with G-shifts
    target = [13, 10, 20, 6, 4, 10, 19]
    best_g = 0
    found_pilgrim = False

    for g in range(29):
        shifted = [(idx - g) % 29 for idx in full_indices]
        for i in range(len(shifted) - len(target)):
            if shifted[i : i+len(target)] == target:
                best_g = g
                found_pilgrim = True
                break
        if found_pilgrim: break

    # Final Reassembly
    final_shifted = [(idx - best_g) % 29 for idx in full_indices]
    final_runes = [rt.INDEX_TO_RUNE[idx] for idx in final_shifted]
    latin = rt.translate_to_latin(final_runes)

    # Output
    print("[RESULTADO DE ALTA CONFIANZA - MANTRA REASSEMBLY]")
    print(f"G-Shift: {best_g}")
    print(latin)

if __name__ == "__main__":
    routine_final_mantra()
