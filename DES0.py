from Cryptodome.Cipher import DES

def pad(tmp):
    n = len(tmp) % 8
    if n > 0: n = 8-n
    return tmp + (b' ' * n)

# đọc vào input kiểu string và convert sang mảng byte - bytes
# (chú ý kiểu bytes: không chỉnh sửa - immutable; kiểu bytearray: chỉnh sửa được - mutable)
key = input().encode()
plain = input().encode()
# padding khoảng trắng vào bytes
padded = pad(plain)

des = DES.new(key, DES.MODE_ECB)
# mã hóa cho ra bản mã cũng kiểu bytes
cipher = des.encrypt(padded)
print(len(cipher))
for v in cipher:  print(v, end=' ')
print()

tmp = des.decrypt(cipher)  
# convert kiểu bytes sang kiểu string
text = tmp.decode()
print(text)