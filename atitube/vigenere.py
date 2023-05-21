def vigenere_encrypt(plaintext, key):
    """
    Encrypts plaintext using Vigenere Cipher with the given key
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = (ord(key[i % len(key)].upper()) - 65)
            plaintext_char = plaintext[i].upper()
            ciphertext += chr(((ord(plaintext_char) - 65 + shift) % 26) + 65)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = (ord(key[i % len(key)].upper()) - 65)
            ciphertext_char = ciphertext[i].upper()
            plaintext += chr(((ord(ciphertext_char) - 65 - shift) % 26) + 65)
        else:
            plaintext += ciphertext[i]
    return plaintext


