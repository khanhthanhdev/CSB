#viết ct cho usẻ nhập vào hai số và tính +-*/ rồi in ra
from math import floor
number1 = (input("nhập số thứ 1: "))
number2 = (input("nhập số thứ 2: "))
number1 = int(number1)
number2 = int(number2)

print(f"Phép cộng là: {number1 + number2}") 
print(f"Phép trừ là: {number1 - number2}")
print(f"Phép nhân là: {number1 * number2}")
if(number2 != 0):
    print(f"Phép chia là: {round(number1 / number2,2)}")
else:
    print("Không thể chia cho  0")


