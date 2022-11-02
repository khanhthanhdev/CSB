# foods = []
# n = int(input("Nhập số món ăn: "))
# for i in range(n):
#     food = input("Nhập món : ")
#     foods.append(food)
# for i in foods:
#     print(i)
# food_remove = input("bạn muốn bỏ món nào: ")
# while food_remove not in foods:
#     if food_remove in foods:
#         foods.remove(food_remove)
#     food_remove = input("nhập lại món muốn bỏ món số mấy: ")
# foods.remove(food_remove)
# for i in foods:
#     print(i)

# Bài2:

# n = int(input("Nhập số lượng số: "))
# list_number = []
# while n < 0:
#     n = int(input("Nhập số lượng số: "))
# for i in range(n):
#     list_number.append(int(input()))
# for i in list_number:
#     print(i, end=' ')
# sum = 0
# for i in list_number:
#     sum += i
# print(f"\ntổng là : {sum}")


# max = list_number[0]
# for i in list_number:
#     if i > max:
#         max=i
# print(f"số lớn nhất là: {max}")

# Bài 3 
numbers = [3,5,1,6]
lenth = len(numbers)
 
# Lặp từ phần tử đầu đến kế cuối,
# Vì khi đến phần tử cuối là đã sắp xếp thànhcông
for i in range(0, lenth - 1):
    for j in range(i + 1, lenth):
        if (numbers[i] > numbers[j]):
            # Hoán đổi vị trí
            tmp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = tmp
 
print(numbers)

