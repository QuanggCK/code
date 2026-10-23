import urllib.request
from PIL import Image
from io import BytesIO

# Nhập URL ảnh và thông điệp
url = input()
thong_diep = input()

# Tải ảnh từ Internet
du_lieu = urllib.request.urlopen(url).read()
anh = Image.open(BytesIO(du_lieu)).convert("RGB")

# Lấy kích thước ảnh
rong, cao = anh.size
pixel = anh.load()

# Chuyển thông điệp thành chuỗi bit ASCII
bits = ""
for ky_tu in thong_diep:
    ma = ord(ky_tu)
    bits += format(ma, "08b")

# Tính số pixel cần dùng
k = len(thong_diep)
p = (k * 8 - 1) // 3 + 1

# Giấu từng bit vào các kênh R, G, B
vi_tri = 0

for i in range(cao):
    for j in range(rong):
        if vi_tri >= len(bits):
            break

        r, g, b = pixel[j, i]
        mau = [r, g, b]

        for c in range(3):
            if vi_tri < len(bits):
                # Thay bit cuối của kênh màu
                mau[c] = (mau[c] & 254) | int(bits[vi_tri])
                vi_tri += 1

        pixel[j, i] = tuple(mau)

        if vi_tri >= len(bits):
            break

    if vi_tri >= len(bits):
        break

# In kết quả
print(p)

for i in range(cao):
    for j in range(rong):
        if p == 0:
            break

# In p pixel đầu tiên theo thứ tự hàng, cột
dem = 0
for i in range(cao):
    for j in range(rong):
        if dem < p:
            r, g, b = pixel[j, i]
            print(r, g, b)
            dem += 1
        else:
            break
    if dem >= p:
        break
