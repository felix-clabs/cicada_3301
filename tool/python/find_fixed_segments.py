import rune_tools as rt

P20_KEY = [22,7,27,8,16,5,19,22,23,24,3,13,2,25,28,22,5,4,22,8,11,19,11,11,5,21,6,9]

if __name__ == "__main__":
    with open("liber_primus/markdown/20.md", "r") as f:
        content = f.read()
    runes = rt.get_runes_only(content)

    # Check for constant shift within a sliding window
    # Maybe only red runes are Shift 0.
    # Where are they?
    # Usually red text in LP is at the beginning or end of lines or chapters.

    # Try common words in raw Latin
    for word in ["SHADOW", "HAS", "WAS", "THE", "AND", "WITH"]:
        for i in range(len(runes)):
             # check shift for window of len(word)
             pass
