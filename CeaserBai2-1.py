# BAI TAP: 2.1, 2.3, 2.4, 2.5 (tu tu lam), 2.6, 2.7 (lam roi) (bai + diem = lam phan mem thong ke so lan xuat hien), 2.9
# 1. Giải mã bản mã sau, giả sử mã hóa Ceasar được sử dụng để mã hóa với k=3:
# IRXUVFRUHDQGVHYHQBHDUVDJR
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