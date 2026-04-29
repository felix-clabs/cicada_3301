import rune_tools as rt

def find_indices():
    with open("liber_primus/markdown/20.md", "r") as f:
        content = f.read()

    # Get all runes
    runes = rt.get_runes_only(content)
    all_runes = "".join(runes)

    print(f"Total runes: {len(all_runes)}")

    # Transcription line by line to calculate offsets
    lines = [
        "ᚱᚫᛉᚻᛄᚫᛗᛚᚠᚳᛝᛞᛁᛝᚩᚳᛋᛟᛖᚣᛟᚻᚢ", # L1 (21)
        "ᚷᛞᚹᚪᛖᛋᚷᛝᚠᛉᛞᛉᛄᛠᚻᛁᚦᛈᛉᚣᛡ",    # L2 (20)
        "ᛇᛞᛇᛝᛇᛝᛖᛠᛞᚱᛚᛇᛏᛉᛏᚣᚱᛇᛈᛝᛇ",    # L3 (20)
        "ᛈᚩᛁᛚᛖᚠᛇᚫᚪᚣᛝᚠᚣᚠᛞᚾᛚᛉᛏᚾᚫᛋᛁᚩ",  # L4 (21)
        "ᚳᚢᚣᛠᚾᛏᚷᚳᚪᛉᛡᛇᚦᛄᚣᛄᛚᛟᛖᛚᚣ",    # L5 (22)
        "ᛈᛡᛖᚹᛟᛇᚾᚪᚻᛞᛇᛋᚦᚣᛇᚦᛄᚦᚱᚢᚳᛠ",    # L6 (21)
        "ᚪᚢᛄᛡᛈᚣᚫᛇᛋᚻᛠᛏᚣᛞᚣᚫᚠᚻᚩᛟᛗ",    # L7 (21)
        "ᛉᛟᛄᚷᚢᛡᚱᛡᚳᛁᚠᛟᛁᛄᛈᛒᛖᛝᚣᚦᚩᚫᚣ",  # L8 (22)
        "ᛠᛉᛡᛖᛚᛁᚱᚣᛞᛠᛄᚫᚳᛗᚷᛁᚫᚢᚪᚫᛄᚪ",    # L9 (21)
        "ᚻᛈᚠᛞᛚᛁᛠᛈᛟᚣᚩᚢᛒᚷᛝᛟᚢᛝᛋᚢᚳᛏ",    # L10 (24)
        "ᛞᚫᛈᚩᛄᛒᚻᚱᛁᚷᚻᛄᚣᚹᛗᛇᚾᚫᛞᛝᛇᛟᛄ",  # L11 (25)
        "ᛝᚳᛖᛠᛉᚪᚱᚣᚪᚢᛏᚳᛈᚳᚩᛇᛟᚫᛈᛏ"     # L12 (25)
    ]

    # Calculate starting indices
    offsets = [0]
    for i in range(len(lines)-1):
        offsets.append(offsets[-1] + len(lines[i]))

    # Block 1 Red Runes (L1 indices 0 to 11)
    red1 = list(range(0, 12))
    print(f"Red Group 1 (Line 1): {red1} -> {''.join([all_runes[i] for i in red1])}")

    # Block 2 Red Runes (L7)
    # Based on image, it's the Giant and the next few.
    # In transcription L7: 125 (Giant), 134-136 (ᚻᛠᛏ)
    red2 = [125, 134, 135, 136]
    print(f"Red Group 2 (Line 7): {red2} -> {''.join([all_runes[i] for i in red2])}")

    # Dots
    print("Dot Clusters (approx locations):")
    print(f"Cluster 1: Between index 11 and 12")
    print(f"Cluster 2: After index 124")
    print(f"Cluster 3: After index 125")

find_indices()
