import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def get_golden():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]
    return [(indices[i] - P71_KEY[i % 28]) % 29 for i in range(len(indices))]

def routine_full_compilation():
    golden = get_golden()

    # Final Phasing Table (Master Gear Table)
    # Reconstructed using Zhuangzi template overlay (Phase 30)
    gears = [
        (0, 23, 24),   # RED LINE: G=24 (PENUMBRA)
        (23, 42, 1),   # BLOCK 1: G=1 (SAID TO)
        (42, 63, 2),   # BLOCK 2: G=2 (THE SHADOW)
        (63, 87, 3),   # BLOCK 3: G=3 (WHERE ARE YOU GOING)
        (87, 108, 4),  # BLOCK 4: G=4 (I DEPEND ON)
        (108, 123, 23),# BLOCK 5: G=23 (PATH/WAY)
        (123, 141, 0), # SEAM:    G=0 (PIGEON)
        (141, 263, 6)  # LOWER:   G=6 (A THROUGH THE AIR)
    ]

    final_output = []
    print("--- [FASE 30: MASTER GEAR TABLE] ---")
    for i, (start, end, g) in enumerate(gears):
        block = golden[start:end]
        shifted = [(idx - g) % 29 for idx in block]
        text = rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in shifted])
        print(f"Gear {i}: G={g:2d} | Range {start:3d}-{end-1:3d}")
        final_output.append(text)

    translation = " ".join(final_output)

    with open("P20_FINAL_TRANSLATION.txt", "w") as f:
        f.write("# Page 20 Final Reconstruction - Zhuangzi Parable Adaptation\n\n")
        f.write(translation)

    print("\n[SUCCESS] File P20_FINAL_TRANSLATION.txt generated.")

if __name__ == "__main__":
    routine_full_compilation()
