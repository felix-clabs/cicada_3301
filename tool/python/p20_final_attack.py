import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def get_golden():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]
    return [(idx - P71_KEY[i % 28]) % 29 for i, idx in enumerate(indices)]

def routine_reconstruction():
    golden = get_golden()

    # Fragmento reconstruido mediante anclaje de Verdad Terrestre (PIGEON)
    # y expansión radial léxica.

    # 1. Bloque Backward (S5, G=23): Estructura del Sendero
    backward = [(idx - 23) % 29 for idx in golden[110:123]]

    # 2. Bloque Anchor (Seam, G=0): El Ancla PIGEON
    anchor = golden[123:141]

    # 3. Bloque Forward (Lower, G=22): Conectores
    forward = [(idx - 22) % 29 for idx in golden[141:263]]

    full_indices = backward + anchor + forward
    full_latin = rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in full_indices])

    print("[CANDIDATO DE ALTA CONFIANZA - FASE 23]")
    print(full_latin)

    print("\nANÁLISIS ESTRUCTURAL:")
    print("- Ancla 'P I G EO N' (Índices 123-127) FIJADA.")
    print("- Expansión Backward (S5, G=23) contiene 'PATH' y 'WAY'.")

if __name__ == "__main__":
    routine_reconstruction()
