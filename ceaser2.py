# A -> Z = 65 -> 90
# a -> z = 97 -> 122
cipher_text = input()
k = int(input())

plain_text = []
for char in cipher_text:
    shifted_char = (ord(char) - ord('a') - k) % 26 + ord('a')
    plain_text.append(chr(shifted_char))

print(''.join(plain_text))

