import rune_tools as rt

def find_vigenere_key_len(ciphertext, max_len=30):
    runes = rt.get_runes_only(ciphertext)
    for l in range(1, max_len + 1):
        ics = []
        for i in range(l):
            slice = runes[i::l]
            if len(slice) > 1:
                ics.append(rt.calculate_ic("".join(slice)))
        if ics:
            avg_ic = sum(ics) / len(ics)
            if avg_ic > 1.3:
                print(f"Len {l:2}: Avg IC {avg_ic:.4f}")

if __name__ == "__main__":
    for i in range(17, 73):
        fname = f"liber_primus/markdown/{i:02}_transcription.txt"
        try:
            with open(fname, "r") as f:
                content = f.read()
            print(f"--- Page {i} ---")
            find_vigenere_key_len(content)
        except FileNotFoundError:
            pass
