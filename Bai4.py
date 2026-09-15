def vigenere_encrypt(plaintext: str, key: str) -> str:
    ciphertext = []
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            p_val = ord(char) - base
            k_val = ord(key[key_index % key_length]) - ord('A')
            c_val = (p_val + k_val) % 26
            ciphertext.append(chr(c_val + base))
            key_index += 1
        else:
            ciphertext.append(char)

    return "".join(ciphertext)

plaintext = "explanation"
key = "LEG"
print("Bản mã:", vigenere_encrypt(plaintext, key))