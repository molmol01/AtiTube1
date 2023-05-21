def vigenere_encrypt(plaintext, key):
    """
    Encrypts plaintext using Vigenere Cipher with the given key
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            # Convert plaintext and key characters to uppercase and calculate shift amount
            shift = (ord(key[i % len(key)].upper()) - 65)
            plaintext_char = plaintext[i].upper()
            # Shift plaintext character and append to ciphertext
            ciphertext += chr(((ord(plaintext_char) - 65 + shift) % 26) + 65)
        else:
            # Non-alphabetic characters are added as-is
            ciphertext += plaintext[i]
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    """
    Decrypts ciphertext using Vigenere Cipher with the given key
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            # Convert ciphertext and key characters to uppercase and calculate shift amount
            shift = (ord(key[i % len(key)].upper()) - 65)
            ciphertext_char = ciphertext[i].upper()
            # Shift ciphertext character and append to plaintext
            plaintext += chr(((ord(ciphertext_char) - 65 - shift) % 26) + 65)
        else:
            # Non-alphabetic characters are added as-is
            plaintext += ciphertext[i]
    return plaintext


