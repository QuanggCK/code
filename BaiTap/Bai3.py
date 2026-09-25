
def monoalphabetic_encrypt(plaintext: str, key: str) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = str.maketrans(
        alphabet + alphabet.lower(),
        key + key.lower()
    )
    return plaintext.translate(table)

key = "IAUTMOCSNREBDLHVWYFPZJXKGQ"
plaintext = "enemy coming"
ciphertext = monoalphabetic_encrypt(plaintext, key)

print("Bản rõ :", plaintext)
print("Bản mã :", ciphertext)