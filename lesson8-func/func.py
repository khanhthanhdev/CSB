# Muốn tìm tổng của nhiều list thì dùng vòng lặp nhiều lần
# về logic thì làm như vậy cũng được, tuy nhiên mất thời gian copy paste nhiều lần

# Hàm là một đoạn code dùng để thực hiện 1 việc nào đó nhắm mục đích tái sử dụng
# có 2 loại hàm: 1. built-in : print(), max()
#                2. Hàm tự định nghĩa
# Cách viết :
#  def <tên hàm> (tham số nếu có):
#   các loại trả về: return (nếu hàm cần trả về giá trị nào đó thì return giá trị đó)
#   nếu không return sẽ trả về none
#  sau return thì coi như hàm sẽ break, code sau return sẽ khonog chạy

# Các loại biến: global, local
'''
    -global được khai báo ngoài hàm, được sử dụng toàn bộ chương trình
    -local được khai báo trong hàm, có tác dụng trong hàm, sẽ biến mất khi hàm kết thúc
    - trong hàm: có tên biến local giống global -> ưu tiên dùng local
'''
'''
Module: tách hàm ra 1 fiel riêng để sử dụng nhiều chương trình khác
File hàm và file code cùng 1 folder
Cách làm:
    import <ten file>
    cách gọi:  <ten file>.<ten ham>
'''
# num1 = 7 #khai báo global
# num2 = 1
# def sum():
#     tong = num1+num2 #tong được khai báo trong hàm, khi hàm kết thúc sẽ biến mất
#     return num1+num2

# x = 10
# print(sum()+x)

import pri
a = [1,2,3,4,5]
pri.print_list(a)
