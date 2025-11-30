# Tính chu vi dien tich hinh tron
import math
try:
    r=float(input("Mời bạn nhập bán kính hình tròn:"));
    cv=2*math.pi*r
    dt=r**2
    print("Chu vi=",cv)
    print("Dien tich=",dt)
except:
    print("lỗi rồi")