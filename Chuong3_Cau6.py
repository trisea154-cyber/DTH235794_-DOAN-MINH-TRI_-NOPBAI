
def doc_so_hai_chu(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", 
            "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 0 or n > 99:
        return "Chỉ nhập số từ 0 đến 99"

    if n < 10:
        return "không" if n == 0 else don_vi[n]

    hang_chuc = n // 10
    hang_dv = n % 10

    if hang_chuc == 1:
        if hang_dv == 0:
            return "mười"
        elif hang_dv == 5:
            return "mười lăm"
        else:
            return "mười " + don_vi[hang_dv]
    else:
        if hang_dv == 0:
            return chuc[hang_chuc]
        elif hang_dv == 1:
            return chuc[hang_chuc] + " mốt"
        elif hang_dv == 5:
            return chuc[hang_chuc] + " lăm"
        else:
            return chuc[hang_chuc] + " " + don_vi[hang_dv]


# ----- Chạy chương trình -----
n = int(input("Nhập số n (0-99): "))
print("Cách đọc:", doc_so_hai_chu(n))
