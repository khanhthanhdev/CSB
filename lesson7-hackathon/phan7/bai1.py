
numbers = [78,56,67]
lenth = len(numbers)
new = int(input("input new score: "))
# Lặp từ phần tử đầu đến kế cuối,
# Vì khi đến phần tử cuối là đã sắp xếp thànhcông
for i in range(0, lenth - 1):
    for j in range(i + 1, lenth):
        if (numbers[i] < numbers[j]):
            numbers[i], numbers[j] = numbers[j], numbers[i]
for i in numbers:    
    print(i)