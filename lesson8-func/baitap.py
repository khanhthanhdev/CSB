# def max(a,b):
#     if a>b:
#         return a
#     elif a<b:
#         return b
#     else:
#         print("a b bang nhau")
# print(max(1,1))

# def nam_nhuan(year):
#     if year%4==0 and year%100!=0 or year%400==0:
#         print("Leap year")
#     else:
#         print("Not a leap year") 
# nam_nhuan(2022)

# nam = int(input("Nhap nam: "))
# def nam_nhuan(year):
#     if year%4==0 and year%100!=0 or year%400==0:
#         return "Leap year"
#     else:
#         return "Not a leap year"
# print(nam_nhuan(nam))

# toan = float(input("Nhap diem toan: "))
# van = float(input("Nhap diem van: "))
# anh = float(input("Nhap diem anh: "))
# def nhap_diem(toan,van,anh):
#     average = (toan+van+anh)/3
#     return average

# def hoc_luc(average):
#     if average>=8:
#         print("hoc sinh gioi")
#     elif average >=6.5:
#         print("hoc sinh kha")
#     else:
#         print("hoc sinh trung binh")
# nhap_diem()

# num = int(input("Nhap so: "))
# def kiemtra(num):
#     if num%2==0:
#         return "so chan"
#     elif num%2==1:
#         return "so le"
# print(kiemtra(num))

# def kiemtra(num):
#     if num%2==0:
#         print("so chan")
#     elif num%2==1:
#         print("so le")
# kiemtra(num)

# lst = [1,3,5,7,'a']
# def sum(lst):
#     tong=0
#     for i in lst:
#         if 48 <= ord(str(i)) <= 57:
#             tong += i
#         else:
#             tong+=0
#     return tong
# print(sum(lst))
# lst = []
text = input("input: ")
lst = []
def sap_xep(text):
    
    for i in range(len(text)):
        lst.append(ord(text[i]))
    lst.sort()  
    for i in lst:
        print(chr(i), end = ' ')
    
sap_xep(text)


            
