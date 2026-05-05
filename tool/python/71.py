import sys
sys.path.append("tool/python")
import rune_tools as rt

def run():
    with open("liber_primus/markdown/71.md", "r") as f:
        runes = rt.get_runes_only(f.read())
    c_indices = [rt.RUNE_TO_INDEX[r] for r in runes]

    p_indices = rt.to_indices("ANENDWITHINTHEDEEPWEBTHEREEXISTSTAPAGETHATHASHESTOITIS")

    # K = (C - P) % 29
    key = [(c_indices[i] - p_indices[i]) % 29 for i in range(len(p_indices))]
    print(f"KEY = {key}")

if __name__ == "__main__":
    run()
