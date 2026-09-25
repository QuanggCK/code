ciphertext = "IRXUVFRUHDQGVHYHQBHDUVDJR"
k = 3

plaintext_chars = []
for char in ciphertext:
    if 'A' <= char <= 'Z':
        plaintext_chars.append(chr((ord(char) - ord('A') - k) % 26 + ord('A')))
    elif 'a' <= char <= 'z':
        # Dịch ngược k vị trí trong bảng chữ cái in thường
        plaintext_chars.append(chr((ord(char) - ord('a') - k) % 26 + ord('a')))
    else:
        plaintext_chars.append(char)

plaintext = "".join(plaintext_chars)

print("Bản mã  :", ciphertext)
print("Bản rõ  :", plaintext)