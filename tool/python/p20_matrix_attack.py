import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    # Range of widths: 16 to 28
    for w in range(16, 29):
        # 1. Matriz
        rows = [indices[i:i+w] for i in range(0, len(indices), w)]

        # 2. Inversión Boustrophedon (Filas Impares invertidas)
        flat = []
        for i, row in enumerate(rows):
            if i % 2 == 1: flat.extend(row[::-1])
            else: flat.extend(row)

        # 3. Sustitución Vigenere P71 Continua
        for g in range(29):
            dec = [(flat[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(flat))]
            text = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])

            # Verificación simultánea de PIGEON y diálogo
            if "PIGEON" in text:
                dialogue_found = [w for w in ["LITTLE", "WHILE", "AGO", "WALKING", "STANDING", "SAID"] if w in text]
                if dialogue_found:
                    print(f"!!! HIT !!! W={w} G={g:2d} | Found: PIGEON + {dialogue_found}")
                    print(f"TEXT: {text}")

if __name__ == "__main__":
    attack()
