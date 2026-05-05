import gp_core

def vigenere_process(text_indices, key_indices, mode='decrypt'):
    """
    Applies Vigenere cipher (modular 29) to a list of indices.
    mode: 'encrypt' (add) or 'decrypt' (subtract).
    """
    result = []
    key_len = len(key_indices)
    for i, val in enumerate(text_indices):
        key_val = key_indices[i % key_len]
        if mode == 'encrypt':
            result.append((val + key_val) % 29)
        else:
            result.append((val - key_val) % 29)
    return result

def process_page(content, key_indices, mode='decrypt'):
    """
    Processes a full page string, preserving non-runic characters.
    """
    runes = gp_core.get_runes_from_text(content)
    rune_indices = [gp_core.rune_to_index(r) for r in runes]

    processed_indices = vigenere_process(rune_indices, key_indices, mode)
    processed_runes = [gp_core.index_to_rune(i) for i in processed_indices]

    # Reconstruction
    output = []
    rune_ptr = 0
    for char in content:
        if char in gp_core.RUNE_TO_INDEX:
            output.append(processed_runes[rune_ptr])
            rune_ptr += 1
        else:
            output.append(char)

    return "".join(output)

if __name__ == "__main__":
    # Quick test
    text = "ᚠᚢᚦ" # indices 0, 1, 2
    key = [1, 1, 1]
    encrypted = vigenere_process([0, 1, 2], key, 'encrypt')
    print(f"Encrypted indices: {encrypted}") # Should be 1, 2, 3
    decrypted = vigenere_process(encrypted, key, 'decrypt')
    print(f"Decrypted indices: {decrypted}") # Should be 0, 1, 2
