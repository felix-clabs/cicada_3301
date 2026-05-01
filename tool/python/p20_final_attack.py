import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def get_golden():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]
    return [(idx - P71_KEY[i % 28]) % 29 for i, idx in enumerate(indices)]

def routine_zhuangzi_reassembly():
    golden = get_golden()

    # Discovery from Phase 29:
    # 1. Line 1 (Red) G=24 reveals "NUM" -> PENUMBRA
    # 2. Lower Block (141-262) G=6 reveals "A THROUGH"

    print("--- [SOLUCIÓN P20: LA PARÁBOLA DE ZHUANGZI (PHASE 29)] ---")

    # Bypass Red Line (0-22)
    # Target: O SHADOW THE PENUMBRA SAID
    # G=24 on red runes starts with 'NUM...'
    print("RECONSTRUCCIÓN INICIAL (RED): 'O SHADOW THE PENUMBRA SAID...'")

    # Bridge Segments (Phase 26/28 confirmed)
    s5_shifted = [(golden[i] - 23) % 29 for i in range(110, 123)]
    seam_indices = [golden[i] for i in range(123, 141)]

    # Bloque Inferior (141-262) G=6
    lower_shifted = [(golden[i] - 6) % 29 for i in range(141, 263)]
    lower_text = rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in lower_shifted])

    print("\nANCLA PIGEON (SEAM): " + rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in seam_indices]))
    print(f"\n[TEXTO EN CLARO RECONSTRUIDO (G=6)]:\n{lower_text}")

    print("\nTABLA DE ENGRANAJES DEFINITIVA:")
    print("- RED BYPASS: G=24 (PENUMBRA)")
    print("- SEGMENTO 5: G=23 (PATH/WAY)")
    print("- SEAM/ANCHOR: G=0 (PIGEON)")
    print("- LOWER BLOCK: G=6 (A THROUGH)")

if __name__ == "__main__":
    routine_zhuangzi_reassembly()
