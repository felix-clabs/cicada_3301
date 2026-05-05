import sys
sys.path.append('tool/python')
import gp_core
import vigenere_engine
import ioc_scanner

def test_integration():
    # 1. GP Core
    text = "F U TH O R"
    indices = gp_core.latin_to_indices(text)
    assert indices == [0, 1, 2, 3, 4]
    runes = gp_core.indices_to_runes(indices)
    assert gp_core.runes_to_indices(runes) == indices

    # 2. Vigenere
    key = [1, 2]
    encrypted = vigenere_engine.vigenere_process(indices, key, mode='encrypt')
    # 0+1=1, 1+2=3, 2+1=3, 3+2=5, 4+1=5
    assert encrypted == [1, 3, 3, 5, 5]
    decrypted = vigenere_engine.vigenere_process(encrypted, key, mode='decrypt')
    assert decrypted == indices

    # 3. IoC
    # High IoC for constant stream
    const_stream = [5] * 100
    ioc = ioc_scanner.calculate_ioc(const_stream)
    assert ioc > 20.0 # Highly periodic/constant

    print("Integration tests passed!")

if __name__ == "__main__":
    test_integration()
