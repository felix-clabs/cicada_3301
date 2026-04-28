import csv
import os

def rank_order(values):
    indexed = list(enumerate(values))
    # Stable sort
    sorted_v = sorted(indexed, key=lambda x: (x[1], x[0]))
    rank_array = [0] * len(values)
    for rank, (original_idx, value) in enumerate(sorted_v):
        rank_array[original_idx] = rank
    return rank_array

def extract_deep_midi(filepath, count=28):
    if not os.path.exists(filepath):
        return None, None

    delta_times = []
    control_changes = []

    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 3: continue

            # 1. Delta Times (difference between row[1] and previous)
            # Actually row[1] in this format is usually the absolute time (ticks)
            # but let's see.
            timestamp = int(row[1])

            if "Note_on_c" in row[2]:
                if len(delta_times) < count:
                    # Use the relative time if possible, or just the absolute timestamp sequence
                    delta_times.append(timestamp)

            if "Control_c" in row[2]: # Control Change events
                if len(control_changes) < count:
                    val = int(row[4]) # Value of the CC
                    control_changes.append(val)

    # Convert absolute timestamps to actual deltas
    deltas = [delta_times[0]] + [delta_times[i] - delta_times[i-1] for i in range(1, len(delta_times))]

    res_delta = rank_order(deltas) if len(deltas) >= count else None
    res_cc = rank_order(control_changes) if len(control_changes) >= count else None

    return res_delta, res_cc

if __name__ == "__main__":
    path = "tool/storage/song.csv"
    d, c = extract_deep_midi(path)
    if d: print(f"MIDI Delta Rank: {d}")
    if c: print(f"MIDI CC Rank: {c}")
