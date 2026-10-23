import hashlib
mat_khau = input()
# Tính giá trị băm MD5
md5 = hashlib.md5(mat_khau.encode()).hexdigest()
# Tính giá trị băm SHA256
sha256 = hashlib.sha256(mat_khau.encode()).hexdigest()
# In kết quả
print(md5)
print(sha256)
