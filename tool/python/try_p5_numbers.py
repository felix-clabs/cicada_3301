import rune_tools as rt

p5_numbers = [272, 138, 131, 151, 18, 226, 245]
key_indices = [n % 29 for n in p5_numbers]

with open("liber_primus/markdown/17_transcription.txt", "r") as f:
    content = f.read()

dec = rt.vigenere_decrypt(content, key_indices)
print("Decryption of Page 17 using Page 5 numbers as Vigenere key:")
print(rt.translate_to_latin(dec[:100]))
print(f"IC: {rt.calculate_ic(dec):.4f}")
