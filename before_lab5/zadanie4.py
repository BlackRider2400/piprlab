import math
import string


def encrypt_vigenere( key, plaintext):
    output = ""
    key_i = 0
    for i in plaintext:
        if i != " ":
            letter = string.ascii_uppercase[(string.ascii_uppercase.index(i) + string.ascii_uppercase.index(key[key_i])) % 26]
            output = output + letter
            key_i = key_i + 1
            if key_i > len(key) - 1:
                key_i = 0
        else:
            output = output + " "
    return output


def decrypt_vigenere( key, ciphertext):
    output = ""
    key_i = 0
    for i in ciphertext:
        if i != " ":
            letter = string.ascii_uppercase[(string.ascii_uppercase.index(i) + 26 - string.ascii_uppercase.index(key[key_i])) % 26]
            output = output + letter
            key_i = key_i + 1
            if key_i > len(key) - 1:
                key_i = 0
        else:
            output = output + " "
    return output