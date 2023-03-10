def decrypt_shift_cipher(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_code = ord(char)
            # Handle uppercase letters
            if char.isupper():
                ascii_code = (ascii_code - shift - 65) % 26 + 65
            # Handle lowercase letters
            else:
                ascii_code = (ascii_code - shift - 97) % 26 + 97
            plaintext += chr(ascii_code)
        else:
            plaintext += char
    return plaintext

ciphertext = "ZRPHQ, OLIH, DQG IUHHGRP!"

for shift in range(26):
    plaintext = decrypt_shift_cipher(ciphertext, shift)
    print(f"Shift amount {shift}: {plaintext}")