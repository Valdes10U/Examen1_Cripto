def decrypt_cesar(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

ciphertext = input("Ingrese el texto cifrado: ")

print("Texto descifrado con todas las combinaciones posibles de César:")
for shift in range(26):
    plaintext = decrypt_cesar(ciphertext, shift)
    print(f"Desplazamiento {shift}: {plaintext}\n")