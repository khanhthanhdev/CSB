# from math import *
# # # # and: a và b true thì trả về true
# # # # or: a hoặc b true thì trả về true
# # # # nếu a sai thì trả về false

# # # #dạng 1: có 1 vế if
# # # # a=4
# # # # if(a%2==0):
# # # #     print("số chẵn")

# # # # Dạng 2: có vế if và else
# # # # a=7
# # # if(a%2==0):
# # #     print("chẵn")
# # # else:
# # #     print("số lẻ")    

# # #dạng 3: có elif
# # a=9
# # if(a==0):
# #     print("=0")
# # elif(a>0):
# #     print("dương")
# # else(a<0):
# #     print("âm")


# # a = int(input("Nhập số 1: "))
# # b = int(input("Nhập số 2: "))
# # c = int(input("Nhập số 3: "))
# # if a > b and a > c:
# #     print(f"{a} là số lớn nhất")
# # elif b > c:
# #     print(f"{b} là số lớn nhất")
# # else:
# #     print(f"{c} là số lớn nhất")


# # height = float(input("nhập chiều cao(m): "))
# # weight = float(input("Nhập cân nặng(kg): "))

# # bmi = round(weight / height**2,2)

# # if bmi <=18.5:
# #     print(f"chỉ số bmi của bạn là: {bmi} , bạn thuộc underweight")
# # elif 18.5 <bmi<24.9:
# #     print(f"chỉ số bmi của bạn là: {bmi} ,bạn thuộc nhóm normal")
# # elif 25<=bmi<=29.9:
# #     print(f"chỉ số bmi của bạn là: {bmi} ,bạn thuộc nhóm overweight")
# # else:
# #     bmi(f"chỉ số bmi của bạn là: {bmi} ,bạn thuộc nhóm obese")

# # a = float(input("nhập độ dài cạnh 1: "))
# # b = float(input("nhập độ dài cạnh 2: "))
# # c = float(input("nhập độ dài cạnh 3: "))

# # if (a+b>c and a+c>b and b+c>a):
# #     # print("có thể tạo được")
# #     if (a*a==b*b+c*c or b*b==a*a+c*c or c*c==b*b+a*a):
# #         if(c==sqrt(a*a+b*b)):
# #             print("có thể tạo được tam giác vuông cân")
# #         else:
# #             print("có thể tạo được tam giác vuông")
# #     elif(a==b or b==c or a==c):
# #         print("có thể tạo được tam giác cân")
# #     elif(a==b==c):
# #         print("có thể tạo được tam giác đều")
# #     elif(a*a>b*b+c*c or b*b>a*a+c*c or c*c>b*b+a*a):
# #         print("có thể tạo được tam giác tù")
    
# #     else:
# #         print("có thể tạo được tam giác nhọn")
# # else:
# #     print("không thể tạo đc")

# # nam = int(input("Nhập năm: "))
# # if nam % 4==0:
# #     print("năm nhuận")
# # elif (nam%19==0) or (nam%19==3) or (nam%19==6) or (nam%19==9) or (nam%19==11) or (nam%19==14) or (nam%19==17):
# #     print("năm nhuận")
# # else: 
# #     print("không phải năm nhâunj")

# # a = float(input("Nhập a: "))
# # b = float(input("Nhập b: "))
# # c = float(input("Nhập c: "))

# # if a == 0:
# #     if b == 0:
# #         if c == 0:
# #             print("Phương trình vô số nghiệm!")
# #         else:
# #             print("Phương trình vô nghiệm!")
# #     else:
# #         if c == 0:
# #             print("Phương trình có 1 nghiệm x = 0")
# #         else:
# #             print("Phương trình có 1 nghiệm x = ", -c / b)
# # else:
# #     delta = b ** 2 - 4 * a * c
# #     if delta < 0:
# #         print("Phương trình vô nghiệm")
# #     elif delta == 0:
# #         print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
# #     else:
# #         print("Phương trình có 2 nghiệm phân biệt là : ")
# #         print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
# #         print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))

# # thuchanh = float(input("Nhập điểm thực hành: "))
# # baitap = float(input("nhập điểm bài tập: "))
# # lithuyet = float(input("Nhập điểm lí thuyết: "))

# # tongdiem = round((thuchanh*30/100)+(baitap*30/100)+(lithuyet*40/100),2)

# # if(tongdiem >= 5):
# #     print("qua môn")
# # else:
# #     print("thi lại")

# diem = float(input("nhập điểm: "))

# if(9<=diem<=10):
#     print("outstanding")
# elif(8<=diem<9):
#     print("giỏi")
# elif(7<=diem<8):
#     print("khá")
# elif(6<=diem<7):
#     print("trung bình khá")
# elif(5<=diem<6):
#     print("trung bình")
# elif(4<=diem<5):
#     print("yếu")
# else:
#     print("thi lại")
# diem = float(input("nhập điểm: "))

# if(8.5<=diem<=10):
#     print("A")
# elif(7.0<=diem<=8.4):
#     print("B")
# elif(5.5<=diem<=6.9):
#     print("C")
# elif(4.0<=diem<=5.4):
#     print("D")
# else:
#     print("F")

# số chính phương
# n = int(input())
# check = False
# for i in range(1, n + 1 ):
#     if (i**2 == n):
#         check = True
#         break
# if (check == True):
#     print("YES")
# else:
#     print("NO")

so = int(input())
bac1 = 2000
bac2= 2500
bac3 = 3000
bac4 = 3500
bac5 = 4000
 
if(so<0):
    print("So dien khong duoc nho hon 0")
elif(so<=50):
    tienDien=so*bac1
    print(tienDien)
elif(so<=150):
    tienDien=50*bac1+((so-50)*bac2)
    print(tienDien)
elif(so<=250):
    tienDien=50*bac1+(100*bac2)+((so-150)*bac3)
    print(tienDien)
elif(so<=350):
    tienDien=50*bac1+(100*bac2)+(100*bac3)+((so-250)*bac4)
    print(tienDien)
elif(so>350):
    tienDien=50*bac1+(100*bac2)+(100*bac3)+(100*bac4)+((so-350)*bac5)
    print(tienDien)


