plaintext = input()
key = input()

result = ""

for i in range(len(plaintext)):
    p = ord(plaintext[i]) - ord('A')
    k = ord(key[i % len(key)]) - ord('A')

    c = (p + k) % 26

    result += chr(c + ord('A'))

print(result)
    