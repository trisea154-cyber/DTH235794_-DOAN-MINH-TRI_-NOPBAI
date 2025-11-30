#
def nam_nhuan(nam):
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)

def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if nam_nhuan(nam) else 28
    else:
        return 0  # tháng không hợp lệ

# --- Nhập dữ liệu ---
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# --- Xác định số ngày trong tháng ---
so_ngay = so_ngay_trong_thang(thang, nam)

if so_ngay == 0 or ngay < 1 or ngay > so_ngay:
    print("Ngày hoặc tháng không hợp lệ!")
else:
    # --- Tăng ngày ---
    ngay += 1
    if ngay > so_ngay:
        ngay = 1
        thang += 1
        if thang > 12:
            thang = 1
            nam += 1

    print(f"Ngày kế tiếp là: {ngay}/{thang}/{nam}")
