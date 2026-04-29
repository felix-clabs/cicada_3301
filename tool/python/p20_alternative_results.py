import rune_tools as rt

P71_KEY = [22,7,27,8,16,5,19,22,23,24,3,13,2,25,28,22,5,4,22,8,11,19,11,11,5,21,6,9]

def get_p20_lines():
    with open("liber_primus/markdown/20.md", "r") as f:
        return [rt.get_runes_only(l) for l in f.readlines() if rt.get_runes_only(l)]

def task1():
    lines = get_p20_lines()
    # Distance Vector based on line lengths (10-9-9 distribution)
    # v1 (10 dots) after L1-L5
    v1 = [len(lines[0]), 0, len(lines[1]), 0, len(lines[2]), 0, len(lines[3]), 0, len(lines[4]), 0]
    # v2 (9 dots) after L6
    v2 = [len(lines[5])] + [0]*8
    # v3 (9 dots) after v2, before L7
    v3 = [0]*9
    vector = v1 + v2 + v3
    return vector

def task2():
    lines = get_p20_lines()
    # Extraction based on 10-9-9 spatial mapping
    # 10 dots: last 2 of L1-L5
    c1 = []
    for i in range(5): c1.extend(lines[i][-2:])
    # 9 dots: last 9 of L6
    c2 = lines[5][-9:]
    # 9 dots: first 9 of L7
    c3 = lines[6][:9]
    extracted = c1 + c2 + c3

    plaintext = ""
    for i, r in enumerate(extracted):
        idx = rt.RUNE_TO_INDEX[r]
        shift = P71_KEY[i % 28]
        plaintext += rt.INDEX_TO_RUNE[(idx - shift) % 29]
    return "".join(extracted), rt.translate_to_latin(plaintext)

if __name__ == "__main__":
    print(f"Task 1 (Distance Vector): {task1()}")
    seq, dec = task2()
    print(f"Task 2 (Extracted Sequence): {seq}")
    print(f"Task 2 (Decrypted Mask): {dec}")
