import rune_tools as rt

def isolate_payload():
    with open("liber_primus/markdown/20.md", "r") as f:
        md = f.read()

    # Extract lines and runes within them
    lines_raw = [l for l in md.split('\n') if any(c in rt.RUNE_TO_INDEX for c in l)]

    # We want to identify the "last rune of the first 7 lines"
    runes_by_line = []
    for line in lines_raw:
        r_list = [c for c in line if c in rt.RUNE_TO_INDEX]
        if r_list:
            runes_by_line.append(r_list)

    print(f"Total lines with runes: {len(runes_by_line)}")

    # Variant A: Remove last rune of first 7 lines
    payload_a = []
    for i, line_runes in enumerate(runes_by_line):
        if i < 7:
            payload_a.extend(line_runes[:-1])
        else:
            payload_a.extend(line_runes)

    # Variant B: Remove first 7 runes
    all_runes = [c for c in "".join(rt.get_runes_only(md))]
    payload_b = all_runes[7:]

    # Variant C: Remove last 7 runes
    payload_c = all_runes[:-7]

    # Variant D: The 7 red "dots" might be embedded? (unlikely but let's stick to the 7-null hypothesis)

    # Save the variants
    with open("liber_primus/p20_payload_a.txt", "w") as f:
        f.write("".join(payload_a[:256]))
    with open("liber_primus/p20_payload_b.txt", "w") as f:
        f.write("".join(payload_b[:256]))
    with open("liber_primus/p20_payload_c.txt", "w") as f:
        f.write("".join(payload_c[:256]))

    print(f"Payload A length: {len(payload_a)}")
    print(f"Payload B length: {len(payload_b)}")
    print(f"Payload C length: {len(payload_c)}")

if __name__ == "__main__":
    isolate_payload()
