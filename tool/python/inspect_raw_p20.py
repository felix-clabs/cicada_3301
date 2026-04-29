import rune_tools as rt

with open("liber_primus/markdown/20.md", "r") as f:
    content = f.read()

runes = rt.get_runes_only(content)
raw_latin = rt.translate_to_latin("".join(runes))
print("Raw Latin (Shift 0):")
print(raw_latin)

# Searching for "SHADOW", "HE HAS"
if "SHADOW" in raw_latin.replace(" ", ""):
    print("Found SHADOW in raw text!")

# Maybe it's "O S/Z H A D O W T H E"
# Gematria Primus says S is S/Z, TH is TH.
# O: ᚩ, S/Z: ᛋ, H: ᚻ, A: ᚪ, D: ᛞ, O: ᚩ, W: ᚹ, TH: ᚦ, E: ᛖ
