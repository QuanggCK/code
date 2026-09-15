ciphertext = "CSYEVIXIVQMREXIH"

for k in range(26):
    plaintext = "".join(
        chr((ord(char) - ord('A') - k) % 26 + ord('A'))
        for char in ciphertext
    )
    print(f"k = {k:d}: {plaintext}")