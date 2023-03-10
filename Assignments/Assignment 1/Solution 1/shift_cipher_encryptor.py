def shift_cipher_encrypt(plaintext, shift):
    ciphertext = ""

    for char in plaintext:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift the character by the shift value and wrap around if needed
            ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift the character by the shift value and wrap around if needed
            ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        # For all other characters, add them as is to the ciphertext
        else:
            ciphertext += char

    return ciphertext

plaintext = "Thisisasecretmessage"
shift = 8
ciphertext = shift_cipher_encrypt(plaintext, shift)
print(ciphertext)