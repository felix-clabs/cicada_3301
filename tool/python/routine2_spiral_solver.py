import rune_tools as rt

P20_KEY = [22,7,27,8,16,5,19,22,23,24,3,13,2,25,28,22,5,4,22,8,11,19,11,11,5,21,6,9]

def spiral_read(matrix):
    # matrix is 16x16
    rows = 16
    cols = 16
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1
    result = []

    while top <= bottom and left <= right:
        # Move right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        # Move down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        # Move left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        # Move up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

def solve_variants():
    with open("liber_primus/markdown/20.md", "r") as f:
        md = f.read()

    raw_runes = rt.get_runes_only(md)
    # Apply substitution FIRST (on 263 runes)
    desubbed = [rt.INDEX_TO_RUNE[(rt.RUNE_TO_INDEX[r] - P20_KEY[i % 28]) % 29] for i, r in enumerate(raw_runes)]

    # Payload A: Remove last rune of first 7 lines
    lines_runes = []
    current = 0
    line_lengths = [21, 20, 20, 21, 22, 21, 21, 22, 21, 24, 25, 25] # From previous analysis
    for length in line_lengths:
        lines_runes.append(desubbed[current:current+length])
        current += length

    payload_a = []
    for i, line in enumerate(lines_runes):
        if i < 7: payload_a.extend(line[:-1])
        else: payload_a.extend(line)
    payload_a = payload_a[:256]

    # Payload B: Remove first 7
    payload_b = desubbed[7:263]

    # Payload C: Remove last 7
    payload_c = desubbed[0:256]

    variants = [("Line-End Nulls", payload_a), ("Prefix Nulls", payload_b), ("Suffix Nulls", payload_c)]

    for name, p in variants:
        # Create 16x16 matrix
        matrix = [p[i:i+16] for i in range(0, 256, 16)]

        # 1. Spiral Clockwise Inward
        spiral_cw = "".join(spiral_read(matrix))
        latin = rt.translate_to_latin(spiral_cw)
        print(f"Variant {name} (Spiral CW): {latin[:50]}...")

        # 2. Row by Row (Standard)
        std = "".join(p)
        latin_std = rt.translate_to_latin(std)
        print(f"Variant {name} (Standard): {latin_std[:50]}...")

if __name__ == "__main__":
    solve_variants()
