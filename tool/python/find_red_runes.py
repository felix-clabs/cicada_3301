import rune_tools as rt

if __name__ == "__main__":
    with open("liber_primus/markdown/20.md", "r") as f:
        content = f.read()
    runes = "".join(rt.get_runes_only(content))

    # Check for G (ᚷ) and E (ᛖ) clusters or suspicious sequences
    # "O SHADOW THE"
    # O (3), S (15), H (8), A (24), D (23), O (3), W (7), TH (2), E (18)

    latin_all = rt.translate_to_latin(runes).replace(" ", "")
    print(f"Latin sequence excerpt: {latin_all[:100]}")

    # "HE HAS"
    # H (8), E (18), H (8), A (24), S (15)

    if "HEHAS" in latin_all:
        print(f"HEHAS found at {latin_all.find('HEHAS')}")
    if "SHADOW" in latin_all:
        print(f"SHADOW found at {latin_all.find('SHADOW')}")
