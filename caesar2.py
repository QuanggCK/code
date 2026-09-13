s = input()
k = int(input())

result = "" # Để kqua trong day

for c in s:
    if 'A' <= c <= 'Z':
        result += chr((ord(c) - ord('A') + k) % 26 + ord('A'))
    elif 'a' <= c <= 'z':
        result += chr((ord(c) - ord('a') + k) % 26 + ord('a'))
    else:
        result += c

# chr: Chuyển đổi hệ số sang mã ASCII
# ord: Chuyển đổi hệ ASCII sang hệ số

print(result)