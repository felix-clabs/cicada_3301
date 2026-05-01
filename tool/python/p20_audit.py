import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def get_p20_runes():
    with open("liber_primus/markdown/20.md", "r") as f:
        return rt.get_runes_only(f.read())

def routine_audit_block0():
    runes = get_p20_runes()
    # Indices 23-32 (first 10 black runes)
    black10 = runes[23:33]
    c_vals = [rt.RUNE_TO_INDEX[r] for r in black10]
    k_vals = [P71_KEY[i % 28] for i in range(23, 33)]

    print("--- [RUTINA 2: LISTA CRUDA DE 29 DESPLAZAMIENTOS (Indices 23-32)] ---")
    for g in range(29):
        p_vals = [(c - k - g) % 29 for c, k in zip(c_vals, k_vals)]
        latin = rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in p_vals])
        print(f"G={g:2d}: {latin}")

def routine_truth_isolation():
    runes = get_p20_runes()
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    print("\n--- [RUTINA 3: AISLAMIENTO DE VERDAD TERRESTRE] ---")
    # Logic validated in Phase 23/26
    s5_c = indices[110:123]
    s5_k = [P71_KEY[i % 28] for i in range(110, 123)]
    s5_p = [(c - k - 23) % 29 for c, k in zip(s5_c, s5_k)]
    print(f"SEG 5 (G=23): {rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in s5_p])}")

    seam_c = indices[123:141]
    seam_k = [P71_KEY[i % 28] for i in range(123, 141)]
    seam_p = [(c - k - 0) % 29 for c, k in zip(seam_c, seam_k)]
    print(f"SEAM (G=0):  {rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in seam_p])}")

if __name__ == "__main__":
    routine_audit_block0()
    routine_truth_isolation()
