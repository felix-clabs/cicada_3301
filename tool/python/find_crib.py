import rune_tools as rt

def find_crib(ciphertext, crib):
    runes = rt.get_runes_only(ciphertext)
    crib_runes = rt.get_runes_only(crib)
    n = len(runes)
    m = len(crib_runes)

    found = False
    for i in range(n - m + 1):
        window = runes[i:i+m]
        shifts = []
        for j in range(m):
            shift = (rt.RUNE_TO_INDEX[window[j]] - rt.RUNE_TO_INDEX[crib_runes[j]]) % 29
            shifts.append(shift)

        if len(set(shifts)) == 1:
            print(f"  [{crib}] at index {i}: shift {shifts[0]}")
            found = True
    return found

if __name__ == "__main__":
    common_words = ["ᚹᛖᛚᚳᚩᛗᛖ", "ᛈᛁᛚᚷᚱᛁᛗ", "ᚦᛖ", "ᚪᚾᛞ", "ᚠᚩᚱ", "ᚣᚩᚢ"]

    for page in range(17, 73):
        fname = f"liber_primus/markdown/{page:02}_transcription.txt"
        try:
            with open(fname, "r") as f:
                content = f.read()
            # print(f"Page {page}:")
            any_found = False
            for word in common_words:
                if find_crib(content, word):
                    if not any_found:
                        print(f"Page {page} has matches.")
                        any_found = True
        except FileNotFoundError:
            pass
