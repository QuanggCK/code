alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipher = input()
count = {} # Tạo 1 dictonary rỗng

# Đếm từng chữ trong mã
for c in cipher:
    if c not in count:
        count[c] = 1
    else:
        count[c] += 1

# Sắp xếp các chữ theo số giảm dần
sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
# Tạo 1 hàm lambda sau đó lọc theo số lần xuất hiện, lấy vị trí số 1 của 
# vì do sorted là bé đến lớn nên dùng reversed đảo lại

# 3 chữ xuất hiện nhiều nhất
first = sorted_count[0][0]
second = sorted_count[1][0]
third = sorted_count[2][0]

# In chữ và số lượng
print(first, count[first])
print(second, count[second])
print(third, count[third])

# Tạo bản rõ

result = ""
for c in cipher:
    if c == first:
        result += "E"
    elif c == second:
        result += "T"
    elif c == third:
        result += "A"
    else: result += "-"

print(result)