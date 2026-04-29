import rune_tools as rt
import re

P20_KEY = [22,7,27,8,16,5,19,22,23,24,3,13,2,25,28,22,5,4,22,8,11,19,11,11,5,21,6,9]

def get_best_runes():
    with open("liber_primus/markdown/20.md", "r") as f:
        content = f.read()
    runes_raw = rt.get_runes_only(content)
    return "".join([rt.INDEX_TO_RUNE[(rt.RUNE_TO_INDEX[r] - P20_KEY[i % 28]) % 29] for i, r in enumerate(runes_raw)])

def get_smart_variants(text):
    variants = []

    # 1. Punctuation filter: Dots (.), hyphens (-), slashes (/) are delimiters.
    # In P20.md, we see . and / at end of lines.
    # Let's read the MD file to see where they are in the sequence.
    with open("liber_primus/markdown/20.md", "r") as f:
        md = f.read()
    # The delimiters in LP are often runes themselves or special markers.
    # Page 20 has 12 lines.
    # Let's try removing the LAST character of the first 7 lines.
    lines = [rt.get_runes_only(l) for l in md.split('\n') if rt.get_runes_only(l)]

    trimmed_lines = []
    removed = 0
    for l in lines:
        if removed < 7:
            trimmed_lines.append(l[:-1])
            removed += 1
        else:
            trimmed_lines.append(l)

    # Flatten and substitute
    flat = []
    for l in trimmed_lines: flat.extend(l)
    # Re-apply substitution key to the flat list
    subbed = "".join([rt.INDEX_TO_RUNE[(rt.RUNE_TO_INDEX[r] - P20_KEY[i % 28]) % 29] for i, r in enumerate(flat)])
    if len(subbed) >= 256:
        variants.append(("Last Rune of first 7 lines removed", subbed[:256]))

    # 2. Fibonacci filter (positions: 1, 2, 3, 5, 8, 13, 21...)
    fib = [1, 2, 3, 5, 8, 13, 21] # exactly 7
    fib_trimmed = []
    for i, char in enumerate(text):
        if (i + 1) not in fib:
            fib_trimmed.append(char)
    if len(fib_trimmed) >= 256:
        variants.append(("Fibonacci positions removed", "".join(fib_trimmed[:256])))

    return variants

if __name__ == "__main__":
    text = get_best_runes()
    vars = get_smart_variants(text)
    for name, v in vars:
        print(f"Variant: {name} | IC: {rt.calculate_ic(v):.4f}")
