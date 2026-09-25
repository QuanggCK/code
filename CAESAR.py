s = input()
k = int(input())

result = ""

for c in s:
    if 'A' <= c <= 'Z':
        result += chr((ord(c) - ord('A') + k) % 26 + ord('A'))
    elif 'a' <= c <= 'z':
        result += chr((ord(c) - ord('a') + k) % 26 + ord('a'))
    else:
        result += c

print(result)
    