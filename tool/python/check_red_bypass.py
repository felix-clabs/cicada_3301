import rune_tools as rt

P71_KEY = [22, 7, 27, 8, 16, 5, 19, 22, 23, 24, 3, 13, 2, 25, 28, 22, 5, 4, 22, 8, 11, 19, 11, 11, 5, 21, 6, 9]

with open("liber_primus/markdown/20.md", "r") as f:
    lines = [l for l in f if rt.get_runes_only(l)]
    line1 = rt.get_runes_only(lines[0])

# P E N U M B R A
# indices: 13, 18, 9, 1, 19, 17, 4, 24
target = [13, 18, 9, 1, 19, 17, 4, 24]

# G=24 on R, AE, X gives 9, 1, 19 (N, U, M)
# If the word starts with PE... maybe shift is different for each letter?
# Or maybe the first word is not "PENUMBRA" but "NUM..."
