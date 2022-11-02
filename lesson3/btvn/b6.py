from math import *

a = float(input("nhập độ dài cạnh 1: "))
b = float(input("nhập độ dài cạnh 2: "))
c = float(input("nhập độ dài cạnh 3: "))

if (a+b>c and a+c>b and b+c>a):
    # print("có thể tạo được")
    if (a*a==b*b+c*c or b*b==a*a+c*c or c*c==b*b+a*a):
        if(c==sqrt(a*a+b*b)):
            print("có thể tạo được tam giác vuông cân")
        else:
            print("có thể tạo được tam giác vuông")
    elif(a==b or b==c or a==c):
        print("có thể tạo được tam giác cân")
    elif(a==b==c):
        print("có thể tạo được tam giác đều")
    elif(a*a>b*b+c*c or b*b>a*a+c*c or c*c>b*b+a*a):
        print("có thể tạo được tam giác tù")
    
    else:
        print("có thể tạo được tam giác nhọn")
else:
    print("không thể tạo đc")