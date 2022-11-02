
# mutable: dữ liệU có thể thay đổi(list, dict,set)
# immutable: không thể thay đổi(int,float,bool,tuple,string)

# ví dụ: mutable
# color = ['red', 'blue', 'green']
# color[0] = 'pink'
# print(color)

# ví dụ immutable
# color = ('red','blue','green')
# color[0] = 'pink'
# print(color)
# a=1
# a=2
# print(a)

# list: là một kiểu dữ liệu dùng để chứa nhiều giá trị cùng 1 lúc

fruit = ['apple','orange','mango']
# Lấy độ dài của list
# print(len(fruit)) #độ dài : 3
# # index là thứ tự của các phần tử trong list, bắt đầu là 0

# # slicing:Lấy 1 phần tử ở vị trí bất kì
# print(fruit[2])
# # Muốn lấy 1 vài vị trí mà biết vị trí bắt đầu 
# print(fruit[0:2]) # lấy từ 0 đến 2-1=1
# print(fruit[1:]) # lấy từ 1 đến hết
# print(fruit[:2]) #lấy từ 0 đến 2-1=1

# # Muốn thêm phần tử: append
# fruit.append('coconut') # thêm vào vị trí cuối của list
# print(fruit)
# # Thêm phần tử vào vị trí bất kì : insert(vị trí, giá trị)
# fruit.insert(1,'melon')
# print(fruit)

# # Muốn xoá phần tử: remove(giá trị cần xoá)
# fruit.remove('apple')
# print(fruit)
# # Xoá nhiều phần tử: del
# del fruit[0] #xoá phần tử 0
# del fruit[0:2] # xoá từ 0 đến 2-1=1

# # Xoá hết list
# del fruit =>> []

# Duyệt list
# cách 1: dùng for
# for i in fruit:
#     print(i)
#  Cách 2: dùng for
# for i in range(len(fruit)):
#     print(fruit[i])
# Cách 3: dùng while
# i = 0
# while i<len(fruit):
#     print(fruit[i])
#     i +=1
# Cách viết ngắn gọn
# [print(i) for i in fruit]

# Tuple: tương tự list những immutable

color = ('red','color','green')
# Lấy độ dài: len()
# index bắt đầu 0
# slicing: giống list
# print(len(color))

# Duyệt tuple: 3 cách: giống list, ngoại trừ cách cuối cùng

# Chuyển tuple -> list
print(list(color))
# Chuyển list -> tuple
print(tuple(color))