p, q, e, M = map(int, input().split())
N = p * q
n = (p-1) * (q-1)
a3 = n
b3 = e
a2 = 0
b2 = 1

while b3 != 0:
    cjd = a3 // b3
    r3 = a3 % b3
    r2 = a2 - b2 * cjd
    a3 = b3
    b3 = r3
    a2 = b2
    b2 = r2
    
d = a2 % n
C = pow(M, d, N)
M_giai_ma = pow(C, e, N)

print(e, N)
print(d, N)
print(C)
print(M_giai_ma)