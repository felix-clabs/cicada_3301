import rune_tools as rt

p16_numbers = [434, 1311, 312, 278, 966, 204, 812, 934, 280, 1071, 626, 620, 809, 620, 626, 1071, 280, 934, 812, 204, 966, 278, 312, 1311, 434]
key_indices = [n % 29 for n in p16_numbers]

with open("liber_primus/markdown/17_transcription.txt", "r") as f:
    content = f.read()

dec = rt.vigenere_decrypt(content, key_indices)
print("Decryption of Page 17 using Page 16 numbers as Vigenere key:")
print(rt.translate_to_latin(dec[:100]))
print(f"IC: {rt.calculate_ic(dec):.4f}")
