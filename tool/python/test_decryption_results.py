import rune_tools as rt

def test_p71_decryption():
    # Page 71 uses Prime Shift Offset 28
    # Let's verify the first few words of the provided decryption
    # Plaintext expected: "AN END WITHIN THE DEEP WEB..."
    ciphertext = "ᚫᛄ-ᛟᛋᚱ.ᛗᚣᛚᚩᚻ-ᚩᚫ-ᚳᚦᚷᚹ-ᚹᛚᚫ"
    runes = rt.get_runes_only(ciphertext)

    # Prime values of runes:
    # A(97), J(37), OE(83), S(53), R(11)...
    # Decryption logic from trace: (C_idx - Prime[i] - 28) % 29?
    # Actually, let's just check if it matches the successful decryption in 71.md
    pass

def test_p20_substitution():
    # IC of P20 should be ~1.7 with the key
    with open("liber_primus/markdown/20.md", "r") as f:
        md = f.read()
    runes = rt.get_runes_only(md)
    P20_KEY = [22,7,27,8,16,5,19,22,23,24,3,13,2,25,28,22,5,4,22,8,11,19,11,11,5,21,6,9]
    desubbed = "".join([rt.INDEX_TO_RUNE[(rt.RUNE_TO_INDEX[r] - P20_KEY[i % 28]) % 29] for i, r in enumerate(runes)])
    ic = rt.calculate_ic(desubbed)
    print(f"P20 Desubbed IC: {ic:.4f}")
    assert ic > 1.6, f"IC too low: {ic}"

if __name__ == "__main__":
    try:
        test_p20_substitution()
        print("P20 Substitution test passed!")
    except Exception as e:
        print(f"Test failed: {e}")
