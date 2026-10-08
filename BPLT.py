a, x, n = map(int, input().split())
kqua = []
dap_an = 1
# Thêm mod
kqua.append(a % n)

for i in range(1, x.bit_length()):
    kqua.append((kqua[i - 1] ** 2) % n)

# Kiểm tra từng bit của x để kiếm các giá trị có 
# xuất hiện số 1 để thực hiện tính đáp án cuối cùng
for i in range(x.bit_length()):
    if (x >> i) & 1:
        dap_an = (dap_an * kqua[i]) % n

print(dap_an)