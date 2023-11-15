from zadanie4 import decrypt_vigenere, encrypt_vigenere

def test_encrypt_standard():
    assert encrypt_vigenere("TAJNE", "TO JEST BARDZO TAJNY TEKST") == "MO SRWM BJEHSO CNNGY CROLT"


def test_decrypt_standard():
    assert decrypt_vigenere("TAJNE", "MO SRWM BJEHSO CNNGY CROLT") == "TO JEST BARDZO TAJNY TEKST"