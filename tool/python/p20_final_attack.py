import rune_tools as rt

# Key extracted from P20 dots and decrypted with P71
KEY = [15, 23, 28, 19, 5, 7, 20, 10, 26, 2, 23, 28, 0, 15, 3, 11, 25, 1, 6, 16, 19, 21, 16, 2, 21, 4, 6, 6]

def get_p20_black():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
        return [rt.RUNE_TO_INDEX[r] for r in runes[23:]]

def routine1():
    """Vigenere Subtraction."""
    black = get_p20_black()
    res = [(c - KEY[i % 28]) % 29 for i, c in enumerate(black)]
    return "".join([rt.INDEX_TO_RUNE[idx] for idx in res])

def routine2():
    """Columnar Transposition."""
    black = get_p20_black()
    cols = 28
    rows = len(black) // cols
    matrix = [black[r*cols : (r+1)*cols] for r in range(rows)]
    indexed_key = list(enumerate(KEY))
    sorted_key = sorted(indexed_key, key=lambda x: (x[1], x[0]))
    new_order = [x[0] for x in sorted_key]
    new_matrix = [[row[i] for i in new_order] for row in matrix]
    h_res = [idx for row in new_matrix for idx in row]
    return "".join([rt.INDEX_TO_RUNE[idx] for idx in h_res])

if __name__ == "__main__":
    print(f"P20 Analysis with Key: {rt.translate_to_latin([rt.INDEX_TO_RUNE[i] for i in KEY])}")
    r1 = routine1()
    print(f"Routine 1 (Vigenere) IC: {rt.calculate_ic(r1):.4f}")
    r2 = routine2()
    print(f"Routine 2 (Transposition) IC: {rt.calculate_ic(r2):.4f}")
