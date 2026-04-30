import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def get_golden():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]
    return [(idx - P71_KEY[i % 28]) % 29 for i, idx in enumerate(indices)]

def solve_full_mantra():
    golden = get_golden()

    # Gear Table derived from poly-shift lexical analysis
    gears = [
        (0, 21, 8),   # Block 0: 'O I H NG T EO NG M...'
        (23, 42, 22), # Block 1: 'TH AE OE AE T F G U EA...'
        (44, 63, 8),  # Block 2: 'EA J J C OE D EA N...'
        (65, 87, 6),  # Block 3: 'EO D L EO T A P X X...'
        (89, 108, 2), # Block 4: 'IA N TH O EO J L U Y...'
        (110, 123, 23),# Block 5: 'P A TH G U I EA AE A W A Y C'
        (123, 141, 0), # Seam:    'P I G EO N EA Y EO L P J F T H C M O OE'
        (141, 263, 22) # Lower:   'H H S B AE X I P L W T A AE U AE H R EO O...'
    ]

    print("--- [FASE 24: FINAL POLY-SHIFT UNLOCK] ---")
    print(f"{'BLOCK':<6} | {'G-SHIFT':<7} | {'TEXTO EN CLARO (SEGMENTO)'}")
    print("-" * 60)

    full_mantra = []
    for i, (start, end, g) in enumerate(gears):
        block = golden[start:end]
        shifted = [(idx - g) % 29 for idx in block]
        text = rt.translate_to_latin([rt.INDEX_TO_RUNE[idx] for idx in shifted])
        print(f"{i:5d}  | {g:7d} | {text}")
        full_mantra.append(text)

    print("\n[MANTRA REENSAMBLADO COMPLETO]")
    print(" ".join(full_mantra))

if __name__ == "__main__":
    solve_full_mantra()
