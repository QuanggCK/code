alphabet = "abcdefghijklmnopqrstuvwxyz"

clear_message = input()
lock = input()

cipher = ""

for c in clear_message:
    if c == " ":
        cipher += " "
    else:
        i = alphabet.index(c) # Kiếm chỉ số của chữ cái c
        cipher += lock[i]  # Sau khi tìm được vị trí i, lấy ký tự tương ứng trong khóa.

print(cipher)