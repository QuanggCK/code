
import tkinter as tk
from tkinter import ttk
from collections import Counter

# Tạo cửa sổ
root = tk.Tk()
root.title("Giải mã thay thế đơn giản")
root.geometry("1000x550")

# Văn bản mã hóa
tk.Label(root, text="Văn bản mã hóa").grid(row=0, column=0)

txt = tk.Text(root, height=8, width=35)
txt.grid(row=1, column=0, rowspan=2)

# Văn bản giải mã
tk.Label(root, text="Văn bản giải mã").grid(row=3, column=0)

result = tk.Text(root, height=8, width=35)
result.grid(row=4, column=0)

# Thứ tự tần suất chữ cái tiếng Anh (cố định)
chu_xep_hang = (
    "Thứ tự: e > t > a > o > i > n > s > h > r > d > l > u > c > m > f > w > y > g > p > b > v > k > x > j > q > z"
)

lbl_ti_le = tk.Label(
    root,
    text=chu_xep_hang,
    wraplength=500,
    justify="left",
    anchor="w",
    font=("Arial", 12)
)

lbl_ti_le.grid(row=6, column=0, sticky="w")

# Bảng thống kê chữ cái
bang = ttk.Treeview(
    root,
    columns=("Chu", "TanSo", "Thay"),
    show="headings",
    height=15
)

bang.heading("Chu", text="Chữ")
bang.heading("TanSo", text="Tần số")
bang.heading("Thay", text="Thay thế")

bang.column("Chu", width=50, anchor="center")
bang.column("TanSo", width=60, anchor="center")
bang.column("Thay", width=70, anchor="center")
bang.grid(row=1, column=1, rowspan=4)

# Bảng Digram
digram = ttk.Treeview(
    root,
    columns=("Cap", "TanSo"),
    show="headings",
    height=15
)

digram.heading("Cap", text="Digram")
digram.heading("TanSo", text="Tần số")

digram.column("Cap", width=70, anchor="center")
digram.column("TanSo", width=60, anchor="center")
digram.grid(row=1, column=2, rowspan=4)

# Bảng Trigram
trigram = ttk.Treeview(
    root,
    columns=("BoBa", "TanSo"),
    show="headings",
    height=15
)

trigram.heading("BoBa", text="Trigram")
trigram.heading("TanSo", text="Tần số")

trigram.column("BoBa", width=80, anchor="center")
trigram.column("TanSo", width=60, anchor="center")
trigram.grid(row=1, column=3, rowspan=4)


# Hàm giải mã
def giai_ma():
    van_ban = txt.get("1.0", "end-1c").upper()

    # Lấy các chữ thay thế trong bảng
    bang_thay = {}

    for dong in bang.get_children():
        gia_tri = bang.item(dong, "values")

        chu_ma = gia_tri[0]
        chu_giai_ma = gia_tri[2].strip().upper()

        # Chỉ lưu chữ khi ô Thay đã được nhập
        if chu_giai_ma:
            bang_thay[chu_ma] = chu_giai_ma[0]

    ket_qua = ""

    for chu in van_ban:
        if "A" <= chu <= "Z":
            # Có chữ thay thế thì hiển thị chữ đã giải mã
            if chu in bang_thay:
                ket_qua += bang_thay[chu]
            else:
                # Chưa có chữ thay thế thì hiển thị dấu -
                ket_qua += "-"
        else:
            # Giữ nguyên dấu cách và dấu câu
            ket_qua += chu

    # Xóa nội dung giải mã cũ
    result.delete("1.0", "end")

    # Hiển thị kết quả mới
    result.insert("1.0", ket_qua)


# Sửa chữ trong cột Thay thế bằng cách nhấp đúp
def sua_chu(event):
    item = bang.identify_row(event.y)
    cot = bang.identify_column(event.x)

    # Chỉ cho phép sửa cột thứ 3
    if not item or cot != "#3":
        return

    vi_tri = bang.bbox(item, cot)

    if not vi_tri:
        return

    x, y, w, h = vi_tri

    o_nhap = tk.Entry(bang, justify="center")
    o_nhap.place(x=x, y=y, width=w, height=h)
    o_nhap.insert(0, bang.set(item, "Thay"))
    o_nhap.focus_set()

    def luu(event=None):
        if not o_nhap.winfo_exists():
            return

        chu_moi = o_nhap.get().strip()[:1]
        bang.set(item, "Thay", chu_moi)
        o_nhap.destroy()
        giai_ma()

    o_nhap.bind("<Return>", luu)
    o_nhap.bind("<FocusOut>", luu)

bang.bind("<Double-Button-1>", sua_chu)


# Hàm thống kê
def thong_ke():
    van_ban = txt.get("1.0", "end-1c").upper()

    # Chỉ lấy chữ cái A-Z để thống kê
    van_ban = "".join(
        chu for chu in van_ban if "A" <= chu <= "Z"
    )

    if not van_ban:
        # Xóa dữ liệu cũ
        for bang_hien_tai in (bang, digram, trigram):
            for dong in bang_hien_tai.get_children():
                bang_hien_tai.delete(dong)

        giai_ma()
        return

    # Xóa dữ liệu thống kê cũ
    for bang_hien_tai in (bang, digram, trigram):
        for dong in bang_hien_tai.get_children():
            bang_hien_tai.delete(dong)

    # 1. Thống kê chữ cái
    dem_chu = Counter(van_ban)

    for chu, so_lan in dem_chu.most_common():
        bang.insert("", "end", values=(chu, so_lan, ""))

    # 2. Thống kê cặp chữ (Digram)
    dem_cap = Counter(
        van_ban[i:i+2]
        for i in range(len(van_ban) - 1)
    )

    for cap, so_lan in dem_cap.most_common():
        digram.insert("", "end", values=(cap, so_lan))

    # 3. Thống kê bộ ba chữ (Trigram)
    dem_bo_ba = Counter(
        van_ban[i:i+3]
        for i in range(len(van_ban) - 2)
    )

    for bo_ba, so_lan in dem_bo_ba.most_common():
        trigram.insert("", "end", values=(bo_ba, so_lan))

    # Giải mã lại nếu đã có chữ thay thế
    giai_ma()


# Nút bấm
tk.Button(
    root,
    text="Thống kê",
    command=thong_ke
).grid(row=5, column=1)

tk.Button(
    root,
    text="Giải mã",
    command=giai_ma
).grid(row=5, column=2)

root.mainloop()
