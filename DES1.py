from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes

key = input().encode()
n = int(input())
data = bytes(list(map(int, input().split())))

iv = get_random_bytes(8)
des = DES.new(key, DES.MODE_CBC, iv)
padded = pad(data, DES.block_size, 'pkcs7') # data là dãy byte câ mã hoá

res = iv + des.encrypt(padded)

print(len(res))
for v in res: print(v, end = ' ') 