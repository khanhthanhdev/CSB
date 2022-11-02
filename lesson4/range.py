'''
hàm range: dùng để tạo 1 tập hợp các số nguyên trong khoảng [a,b)
[: lấy
): bỏ

ví dụ [1,5)
lấy 1 2 3 4 

Có 3 loại [tập hợp]
    -Loại 1: range(start, end, step)
    ví dụ: range(0,10,2) =>> 0 2 4 6 8

    -Loại 2:range(start, end) => step mặc định là 1
    ví dụ: range(0,5) ==> 0 1 2 3 4

    -Lại 3: range(end). start = 0; stop =1
    ví dụ: range(5) ==> 0 1 2 3 4

for: dùng để thực hiện 1 việc nhiều lần với sô lần biết trước
for [tên biến] in range():
    statements
    ..............
ví dụ: in 5 lần hello world

while: dùng để thực hiện 1 việc nhiều lần với sô lần không biết trước
while (điều kiệN dừng)

'''
import math
# for i in range(5):
#     print("hello world")


# IN dãy 0 -> 10
# for i in range(11):
#     print(i, end=" ")


# In dãy 100 101 102 103 104 105
# for i in range(100, 106):
#     print(i, end=" ")

# IN dãy số 9 8 7 6 5 4 3 2
# n = 10
# while n>2:
#     n -= 1
#     print(n, end=" ")


# IN các số chia hết cho 3 từ 0->20
# for i in range(21):
#     if i % 3 == 0:
#         print(i, end=" ")

# In ra màn hình dãy từ 0 -> n
# n = int(input())
# for i in range(0, n+1):
#     print(i)


# Đếm số chữ số 1 số nguyên 
# n = int(input())
# i=0
# while n !=0:
#     i +=1
#     n //= 10
# print(f"n có {i} chữ số")\


# Tính tông S = 1^2 + 2^2 =.. +n^2
# n = int(input())
# # cách 1
# sum = 0
# i = 1
# while i<= n:
#     sum = sum +i*i
#     i +=1
# print(sum) 
# # cách 2
# tong = 0
# k = 0
# for i in range(1, n+1):
#     tong += i*i
# print(tong)


# Tính S = 1/2 + 2/3 + 3/4 +.. + n/n+1
# n = int(input())
# #  Cách 1
# # i =1
# # sum= 0
# # while i <=n:
# #     sum = sum +  i/(i+1)
# #     i +=1
# # print(sum)
# # cách 2
# tong = 0
# for i in range(0, n+1):
#     tong += i/(i+1)
# print(tong)


# Liệt kê các ước số nguyên của n
# n = int(input())
# for i in range(1, n+1):
#     if (n %i==0):
#         print(i, end=" ")


# In số dòng cầu thang
# n = int(input())
# for i in range(1, n+1):
#     for k in range(1, i+1):
#         print('#', end="")
#     print("")


# Tìm số đảo ngược  
# n = int(input())
# while n > 0:
#     print(n%10, end="")
#     n = n //10

# In các số nguyên tố từ 1 -> n
# n = int(input())
# for i in range(1, n+1):
#     if i >1:
#         for k in range(2, int(math.sqrt(i))+1):
#             if i % k ==0:
#                 break
#         else:
#             print(i, end=" ")


# tìm số hoàn hảo
# n = int(input())
# tong = 0
# for i in range(1, n):
#     if n %i ==0:
#         tong += i
# if tong == n:
#     print("n là số hoàn hảo")
# else: 

#     print("n không phải là số hoàn hảo")