# chương trình in ra các số lẻ từ 1 đến n với n nhập từ bàn phím
'''n=int(input('Nhập số nguyên n='))
for i in range (1,n):
    if i %2==1:
        print(i,end='-')'''
# trong giao trinh
n=int(input('Nhâp n:'))
for x in range (1,n,1):
    if x%2==0:
        continue
    print('x=',x,'la so le')

