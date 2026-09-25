s = input()
k = int(input())

result = ""

for c in s:
    result += chr((ord(c) - ord('a') - k) % 26 + ord('a'))

print(result)
    