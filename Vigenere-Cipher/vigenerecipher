# Function to encrypt the plaintext using the Vigenère Cipher
def vigenere_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_text = ""
    key_index = 0
    key = key.upper()

    for letter in plaintext:
        if letter.upper() in alphabet:
            # Get the shift value from the key
            shift = alphabet.index(key[key_index % len(key)])
            # Find the encrypted letter
            encrypted_letter = (alphabet.index(letter.upper()) + shift) % 26
            cipher_text += alphabet[encrypted_letter]
            key_index += 1
        else:
            cipher_text += letter  # Non-alphabet characters are added as-is

    return cipher_text

# Function to decrypt the ciphertext using the Vigenère Cipher
def vigenere_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plain_text = ""
    key_index = 0
    key = key.upper()

    for letter in ciphertext:
        if letter.upper() in alphabet:
            # Get the shift value from the key
            shift = alphabet.index(key[key_index % len(key)])
            # Find the decrypted letter
            decrypted_letter = (alphabet.index(letter.upper()) - shift) % 26
            plain_text += alphabet[decrypted_letter]
            key_index += 1
        else:
            plain_text += letter  # Non-alphabet characters are added as-is

    return plain_text

# Main program to take user input
if __name__ == "__main__":
    # Taking plaintext input from the user
    plaintext = input("Enter the plaintext: ").upper()

    # Taking key input from the user
    key = input("Enter the key: ").upper()

    # Encrypting the plaintext
    encrypted_text = vigenere_encrypt(plaintext, key)
    print(f"Encrypted Text: {encrypted_text}")

    # Decrypting the ciphertext
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print(f"Decrypted Text: {decrypted_text}")
