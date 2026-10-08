a, n = map(int, input().split())
a3=n
b3=a
a2=0
b2=1
for i in range(n):
    if a3 > b3:
        q = a3 // b3
        r3 = a3 % b3
        r2 = a2 - b2 * q
        a3 = b3
        b3 = r3
        a2 = b2
        b2 = r2
        if b3 == 1:
            break

result = b2 + n
print(result)

