# Nhập hai giá trị và phép toán
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
phep_toan = input("Nhập phép toán (+, -, *, /): ")

# Xử lý theo phép toán
if phep_toan == '+':
    kq = a + b
elif phep_toan == '-':
    kq = a - b
elif phep_toan == '*':
    kq = a * b
elif phep_toan == '/':
    if b == 0:
        print("Lỗi: không thể chia cho 0!")
        exit()  # dừng chương trình
    kq = a / b
else:
    print("Phép toán không hợp lệ!")
    exit()

# Xuất kết quả
print("Kết quả:", a, phep_toan, b, "=", kq)

