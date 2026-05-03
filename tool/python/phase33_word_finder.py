import sys
sys.path.append("tool/python")
import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

COMMON_WORDS = [
    "THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL", "ANY", "CAN", "HAD", "WAS", "ONE", "OUR", "OUT", "DAY", "GET", "HAS", "HIM", "HIS", "HOW", "NOW", "SEE", "WAY", "WHO", "DID", "ITS", "LET", "PUT", "SAY", "SHE", "TOO", "USE",
    "SAID", "ASKED", "WHILE", "AGO", "LITTLE", "WALK", "STAND", "STILL", "DEPEND", "SIT", "RISE", "WHY"
]

def attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    # Scan from index 23 to 150
    search_indices = indices[23:150]

    print("--- [PHASE 33: WORD FREQUENCY SCAN] ---")

    results = []
    for g in range(29):
        # 1. Linear
        dec = [(search_indices[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(search_indices))]
        latin = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec])

        found = []
        for w in COMMON_WORDS:
            if w in latin:
                found.append(w)
        if found:
            results.append((g, "LIN", len(found), found, latin[:60]))

        # 2. Boustrophedon (Assuming Line 2 reversed)
        l2 = search_indices[:21]
        rem = search_indices[21:]
        reading = l2[::-1] + rem
        dec_b = [(reading[i] - P71_KEY[i % 28] - g) % 29 for i in range(len(reading))]
        latin_b = "".join([rt.RUNE_TO_LATIN[rt.INDEX_TO_RUNE[idx]].split('/')[0] for idx in dec_b])
        found_b = []
        for w in COMMON_WORDS:
            if w in latin_b:
                found_b.append(w)
        if found_b:
            results.append((g, "BOU", len(found_b), found_b, latin_b[:60]))

    # Sort by number of words found
    results.sort(key=lambda x: x[2], reverse=True)
    for g, orient, count, words, text in results[:20]:
        print(f"G={g:2d} | {orient} | Words({count}): {words} | {text}...")

attack()
