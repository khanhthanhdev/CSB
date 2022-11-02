a = float(input("Nhập số: "))

# kiemtra = a.is_integer()

# if (kiemtra == 1):
#     print(f"{a} là số nguyên")
# elif (kiemtra == 0):
#     print(f"{a} là số thực")

# cách 2
if (a%1==0):
    print(f"{a} là số nguyên")
elif (a%1 != 0):
    print(f"{a} là số thực")

