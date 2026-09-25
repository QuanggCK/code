
plaintext = input().strip()
key = input().strip()

so_cot = len(key)

i = 0

while len(plaintext) % so_cot != 0:
    plaintext += chr(ord('A') + i)
    i += 1

so_hang = len(plaintext) // so_cot

# Tạo bảng rỗng gồm so_hang hàng và so_cot cột
bang = []

# Đưa lần lượt từng ký tự của bản rõ vào bảng
for i in range(so_hang):
    hang = []

    for j in range(so_cot):
        # Vị trí ký tự trong chuỗi bản rõ
        vi_tri = i * so_cot + j

        hang.append(plaintext[vi_tri])

    bang.append(hang)

# Danh sách lưu chỉ số các cột theo thứ tự khóa
thu_tu_cot = list(range(so_cot))

# Ttìm cột có chữ khóa nhỏ nhất rồi đưa về vị trí đầu tiên chưa được sắp xếp
for i in range(so_cot - 1):

    vi_tri_nho_nhat = i

    for j in range(i + 1, so_cot):

        # So sánh chữ khóa tại hai cột
        if key[thu_tu_cot[j]] < key[thu_tu_cot[vi_tri_nho_nhat]]:
            vi_tri_nho_nhat = j

    # Đổi chỗ hai cột trong danh sách thứ tự
    tam = thu_tu_cot[i]
    thu_tu_cot[i] = thu_tu_cot[vi_tri_nho_nhat]
    thu_tu_cot[vi_tri_nho_nhat] = tam

ciphertext = ""

# Duyệt qua các cột theo thứ tự đã sắp xếp
for cot in thu_tu_cot:

    # Đọc từ trên xuống dưới trong cột đó
    for hang in range(so_hang):
        ciphertext += bang[hang][cot]


# In bản mã
print(ciphertext)