DICTIONARY = {
    "AN", "BAN", "BUA", "CHAO", "DANG", "DUNG", "GAP", "HEN", "HOM",
    "KHOE", "KHONG", "LAI", "MOI", "MUA", "NAM", "NANG", "NAY",
    "NGAY", "SANG", "THOI", "TIET", "TOI", "TROI", "VIET", "YEU"
}

def solve_caesar(ciphertext: str) -> str:
    for k in range(26):
        decrypted_chars = []
        for char in ciphertext:
            if 'A' <= char <= 'Z':
                decrypted_chars.append(chr((ord(char) - ord('A') - k) % 26 + ord('A')))
            elif 'a' <= char <= 'z':
                decrypted_chars.append(chr((ord(char) - ord('a') - k) % 26 + ord('a')))
            else:
                decrypted_chars.append(char)

        decrypted_text = "".join(decrypted_chars)
        words = decrypted_text.split()

        if words and all(word.upper() in DICTIONARY for word in words):
            return decrypted_text

    return ciphertext


if __name__ == "__main__":
    ciphertext = input().strip()
    if ciphertext:
        print(solve_caesar(ciphertext))