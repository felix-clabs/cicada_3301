import rune_tools as rt
import csv

def get_midi_permutation():
    # Delta times from song.csv
    deltas = []
    try:
        with open("tool/storage/song.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                deltas.append(int(row['delta']))
    except:
        return list(range(256))

    # Use the first 256 deltas as a rank-order permutation
    if len(deltas) < 256:
        deltas = deltas * (256 // len(deltas) + 1)
    deltas = deltas[:256]

    # Rank order: stable sort to get unique indices 0-255
    indexed_deltas = sorted(range(len(deltas)), key=lambda k: deltas[k])
    return indexed_deltas

def final_attack():
    with open("liber_primus/markdown/20.md", "r") as f:
        md = f.read()

    raw_runes = rt.get_runes_only(md)
    # Best known substitution key (cycle 28)
    P20_KEY = [22,7,27,8,16,5,19,22,23,24,3,13,2,25,28,22,5,4,22,8,11,19,11,11,5,21,6,9]
    desubbed = [rt.INDEX_TO_RUNE[(rt.RUNE_TO_INDEX[r] - P20_KEY[i % 28]) % 29] for i, r in enumerate(raw_runes)]

    # Payload: 256 runes starting after the red Line 1 (21 runes) + some nulls?
    # Let's try the first 256 desubbed runes
    payload = desubbed[:256]

    perm = get_midi_permutation()

    # Apply Permutation
    reordered = [payload[i] for i in perm]

    latin = rt.translate_to_latin("".join(reordered))
    print(f"MIDI Reorder Result: {latin[:100]}...")

    # Also check Chi-Square
    chi = rt.calculate_chi_square(rt.translate_to_latin("".join(reordered)))
    print(f"Chi-Square: {chi:.2f}")

if __name__ == "__main__":
    final_attack()
