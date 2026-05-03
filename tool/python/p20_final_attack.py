import sys
import os

# Import rune_tools
sys.path.append('tool/python')
import rune_tools as rt

def run_attack():
    # P71 KEY
    P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

    # Load Page 20 runes and mark red indices
    with open('liber_primus/markdown/20.md', 'r') as f:
        lines = f.readlines()

    # Filter lines that contain runes (inside the code block)
    rune_lines = []
    in_code_block = False
    for line in lines:
        if '```' in line:
            in_code_block = not in_code_block
            continue
        if in_code_block and line.strip():
            rune_lines.append(line.strip())

    all_runes = []
    red_indices = set()

    current_idx = 0
    # Headers are Line 1 and Line 7 (0-indexed: 0 and 6)
    for i, line in enumerate(rune_lines):
        runes_in_line = rt.get_runes_only(line)
        for r in runes_in_line:
            if i == 0 or i == 6:
                red_indices.add(current_idx)
            all_runes.append(r)
            current_idx += 1

    print(f"Total runes: {len(all_runes)}")
    print(f"Red runes count: {len(red_indices)}")

    # Matrix W=27
    W = 27
    indices = [rt.RUNE_TO_INDEX[r] for r in all_runes]

    # Create rows
    rows = []
    # We also need to track the "original red status" for each position in the matrix
    is_red_map = [i in red_indices for i in range(len(indices))]

    matrix_indices = []
    matrix_red = []

    for i in range(0, len(indices), W):
        matrix_indices.append(indices[i:i+W])
        matrix_red.append(is_red_map[i:i+W])

    # Apply Boustrophedon (reverse odd rows)
    flat_indices = []
    flat_red = []
    for i in range(len(matrix_indices)):
        row_indices = matrix_indices[i]
        row_red = matrix_red[i]
        if i % 2 == 1:
            flat_indices.extend(row_indices[::-1])
            flat_red.extend(row_red[::-1])
        else:
            flat_indices.extend(row_indices)
            flat_red.extend(row_red)

    # Decrypt
    decoded_indices = []
    k_ptr = 0
    for i in range(len(flat_indices)):
        val = flat_indices[i]
        is_red = flat_red[i]

        if is_red:
            decoded_indices.append(val) # Shift 0
        else:
            shift = P71_KEY[k_ptr % len(P71_KEY)]
            # Using Subtraction (Vigenere standard for Cicada)
            dec = (val - shift) % 29
            decoded_indices.append(dec)
            k_ptr += 1

    # Convert to Latin
    result = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in decoded_indices])

    print("RESULT (First 100 chars):")
    print(result[:100])
    print("\nFULL RESULT:")
    print(result)

if __name__ == "__main__":
    run_attack()
