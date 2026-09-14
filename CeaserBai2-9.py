def find_vigenere_key(plaintext: str, ciphertext: str) -> str:
    full_key = []

    for p, c in zip(plaintext, ciphertext):
        if p.isalpha() and c.isalpha():
            p_val = ord(p.lower()) - ord('a')
            c_val = ord(c.lower()) - ord('a')
            k_val = (c_val - p_val) % 26
            full_key.append(chr(k_val + ord('A')))

    full_key_str = "".join(full_key)

    # Tìm chu kỳ lặp ngắn nhất của khóa
    for length in range(1, len(full_key_str) + 1):
        pattern = full_key_str[:length]
        if (pattern * (len(full_key_str) // length + 1))[:len(full_key_str)] == full_key_str:
            return pattern

    return full_key_str


plaintext = "networksecurity"
ciphertext = "PVRLHFMJCRNFKKW"

key = find_vigenere_key(plaintext, ciphertext)
print("Khóa K là:", key)