import rune_tools as rt

def get_p20_lines():
    with open("liber_primus/markdown/20.md", "r") as f:
        lines = []
        for line in f:
            r = rt.get_runes_only(line)
            if r:
                lines.append(r)
        return lines

lines = get_p20_lines()
# Total runes: 263
all_runes = [r for line in lines for r in line]

# Dot Mapping:
# 10 dots: last 2 of L1-L5
# 9 dots: last 9 of L6
# 9 dots: first 9 of L7

dot_absolute_indices = []

# Cumulative offsets
offsets = [0]
for i in range(len(lines)-1):
    offsets.append(offsets[-1] + len(lines[i]))

# Cluster 1 (L1-L5 last 2)
for i in range(5):
    line_len = len(lines[i])
    dot_absolute_indices.append(offsets[i] + line_len - 2)
    dot_absolute_indices.append(offsets[i] + line_len - 1)

# Cluster 2 (L6 last 9)
l6_len = len(lines[5])
for i in range(l6_len - 9, l6_len):
    dot_absolute_indices.append(offsets[5] + i)

# Cluster 3 (L7 first 9)
for i in range(9):
    dot_absolute_indices.append(offsets[6] + i)

print(f"Total dots: {len(dot_absolute_indices)}")
print(f"Absolute Indices: {dot_absolute_indices}")

# Calculate pos mod 28
mod_positions = [idx % 28 for idx in dot_absolute_indices]
print(f"Positions mod 28: {mod_positions}")
print(f"Unique positions: {len(set(mod_positions))}")

# Map pos to dot index
pos_to_dot = {}
for i, pos in enumerate(mod_positions):
    if pos in pos_to_dot:
        print(f"COLLISION at pos {pos}: dots {pos_to_dot[pos]} and {i}")
    pos_to_dot[pos] = i

missing = [p for p in range(28) if p not in pos_to_dot]
print(f"Missing positions: {missing}")
