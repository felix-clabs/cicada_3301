import csv
import os

def rank_order(values):
    indexed = list(enumerate(values))
    sorted_v = sorted(indexed, key=lambda x: (x[1], x[0]))
    rank_array = [0] * len(values)
    for rank, (original_idx, value) in enumerate(sorted_v):
        rank_array[original_idx] = rank
    return rank_array

def extract_double_transp_keys(filepath):
    if not os.path.exists(filepath):
        return None, None

    notes = []
    deltas = []
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        last_t = 0
        for row in reader:
            if len(row) >= 5 and "Note_on_c" in row[2]:
                t = int(row[1])
                note = int(row[4])
                vel = int(row[5])

                if len(deltas) < 16:
                    deltas.append(t - last_t)
                elif len(notes) < 16:
                    notes.append(note) # or velocity

                last_t = t
                if len(notes) >= 16: break

    return rank_order(deltas), rank_order(notes)

if __name__ == "__main__":
    d, n = extract_double_transp_keys("tool/storage/song.csv")
    print(f"Col Shuffle (Delta Rank): {d}")
    print(f"Row Shuffle (Note Rank): {n}")
