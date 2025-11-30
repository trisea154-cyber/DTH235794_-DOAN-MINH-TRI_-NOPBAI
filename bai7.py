# viết chương trình in ra một chuỗi ký tự bất kỳ. Nội dung chuỗi được nhập từ tham số dòng lệnh của chương trình.
import sys
# sys.argv[0] là tên file chương trinh
# các tham số truyên vào là bắt đầu từ sys.argv[1]
if len(sys.argv)<=1:
    print('Vui lòng nhập lệnh qua tham số dòng lệnh')
else:
        #ghép các tham số thành một chuỗi hoàn chỉnh
        chuoi=" ".join(sys.argv[1:])
        print('chuỗi bạn đã nhập là:',chuoi)
