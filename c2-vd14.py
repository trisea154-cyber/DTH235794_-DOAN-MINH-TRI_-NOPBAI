''' Viết chương trình nhập số tự nhiên n từ bàn phím và 
kiểm tra n có phải là số hoàn hảo không.biết số tự nhiên được gọi là số hoàn hảo nếu số 
đó bằng tổng các ước số thực sự của mình
'''
n=int(input("Nhập số n:"))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==n:
    print(n,' là số hoàn hỏa')
else:
    print(n,' không phải là số hoàn hảo')
