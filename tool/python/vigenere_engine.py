"""
Vigenere Engine Module
Supports standard repeating-key Vigenere and Autokey (plaintext as key).
Modular 29 math for Gematria Primus.
"""

def vigenere_process(indices, key_indices, decrypt=True, autokey=False):
    res = []
    current_key = list(key_indices)
    for i in range(len(indices)):
        if autokey:
            if i < len(key_indices):
                k = key_indices[i]
            else:
                k = res[i - len(key_indices)] if decrypt else indices[i - len(key_indices)]
        else:
            k = current_key[i % len(current_key)]
        if decrypt:
            val = (indices[i] - k) % 29
        else:
            val = (indices[i] + k) % 29
        res.append(val)
    return res

def process_text(text, key_indices, decrypt=True, autokey=False):
    import gp_core
    runes_only = gp_core.get_runes_from_text(text)
    input_indices = gp_core.runes_to_indices(runes_only)
    output_indices = vigenere_process(input_indices, key_indices, decrypt, autokey)
    output_runes = gp_core.indices_to_runes(output_indices)
    res = []
    rune_idx = 0
    for char in text:
        if char in gp_core.RUNE_TO_INDEX:
            res.append(output_runes[rune_idx])
            rune_idx += 1
        else:
            res.append(char)
    return "".join(res)
