import rune_tools as rt

for i in range(17, 73):
    fname = f"liber_primus/markdown/{i:02}_transcription.txt"
    try:
        with open(fname, "r") as f:
            content = f.read()
        atb = rt.atbash(content)
        ic = rt.calculate_ic(atb)
        if ic > 1.3:
            print(f"Page {i} Atbash IC: {ic:.4f}")
    except FileNotFoundError:
        pass
