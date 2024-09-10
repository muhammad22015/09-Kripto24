def encrypt(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        if char.isupper(): # Huruf kapital
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower(): # Huruf kecil
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else: # Karakter non-huruf
            result += char

    return result

def decrypt(cipher_text, shift):
    return encrypt(cipher_text, -shift)

# Input user
text = input("Masukkan teks: ")
shift = int(input("Masukkan jumlah shift: "))

# Enkripsi
encrypted_text = encrypt(text, shift)
print(f"Hasil Enkripsi: \"{encrypted_text}\"")

# Dekripsi
decrypted_text = decrypt(encrypted_text, shift)
print(f"Hasil Dekripsi: \"{decrypted_text}\"")
