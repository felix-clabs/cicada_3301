import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def get_golden():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]
    return [(idx - P71_KEY[i % 28]) % 29 for i, idx in enumerate(indices)]

def routine_p26_final():
    golden = get_golden()

    # 1. Anchors
    red_anchor = "O SHADOW THE"
    pigeon_anchor = "P I G EO N"

    # 2. Lower Block Expansion
    # G-Shift 6 on index 141-262 (Lower block)
    lower_indices = [(idx - 6) % 29 for idx in golden[141:263]]
    lower_text = rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in lower_indices])

    # 3. Upper Block Bridge
    # Segment S5 (110-122) G-Shift 23 (PATH/WAY)
    s5_indices = [(idx - 23) % 29 for idx in golden[110:123]]
    s5_text = rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in s5_indices])

    # Seam (123-140) G-Shift 0
    seam_indices = [(idx - 0) % 29 for idx in golden[123:141]]
    seam_text = rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in seam_indices])

    print("--- [FASE 26: PIGEON EXPANSION & MACRO-GEOMETRY] ---")
    print(f"BYPASS RED: {red_anchor}")
    print(f"RECONSTRUCTED BRIDGE: {s5_text} {seam_text}")
    print(f"\n[ORACIÓN DETECTADA - BLOQUE INFERIOR (G=6)]")
    print(f"P I G EO N ... {lower_text[:200]}")

    print("\nTABLA DE ENGRANAJES (DYNAMIC G-SHIFT):")
    print("- SEG 5 (110-122): G=23")
    print("- SEAM  (123-140): G=0")
    print("- LOWER (141-262): G=6")

if __name__ == "__main__":
    routine_p26_final()
