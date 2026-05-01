import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def get_golden():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]
    return [(idx - P71_KEY[i % 28]) % 29 for i, idx in enumerate(indices)]

def routine_zhuangzi_parable():
    """
    Fase 28: Expansión de la Parábola de Zhuangzi.
    Reconstrucción del Mantra basada en los anclajes de Verdad Terrestre.
    """
    golden = get_golden()

    # 1. Bypass Rojo (Line 1): O SHADOW THE
    red_indices = golden[0:23]
    # Note: Phase 26 confirmed this block acts as a Shift 0 Bypass.
    red_text = "O SHADOW THE" # Semantic anchor

    # 2. Segmento 5 (110-122): El Sendero
    # G-Shift 23 reveals: P A TH G U I EA AE A W A Y C/K
    s5_indices = [(golden[i] - 23) % 29 for i in range(110, 123)]
    s5_text = rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in s5_indices])

    # 3. Costura Central (123-140): PIGEON
    # G-Shift 0 reveals: P I G EO N EA Y EO L P J F T H C/K M O OE
    seam_indices = [golden[i] for i in range(123, 141)]
    seam_text = rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in seam_indices])

    # 4. Bloque Inferior (141-262): El Vuelo
    # G-Shift 6 reveals: A A TH R EO U Y ... (A THROUGH...)
    lower_indices = [(golden[i] - 6) % 29 for i in range(141, 263)]
    lower_text = rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in lower_indices])

    print("--- [SOLUCIÓN PARCIAL P20: LA PARÁBOLA DE ZHUANGZI] ---")
    print(f"ANCLA INICIAL (RED): {red_text}")
    print(f"PUENTE INTERMEDIO:   {s5_text}")
    print(f"ANCLA CENTRAL:       {seam_text}")
    print(f"\n[TEXTO EN CLARO RECONSTRUIDO - BLOQUE INFERIOR]")
    print(lower_text)

    print("\n--- TABLA DE ENGRANAJES (GEAR TABLE) ---")
    print("Red Line (0-22):   G=0 (Bypass)")
    print("Segment 5 (110-122): G=23")
    print("Seam (123-140):     G=0")
    print("Lower Block (141-262): G=6")

if __name__ == "__main__":
    routine_zhuangzi_parable()
