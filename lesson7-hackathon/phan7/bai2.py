
numbers = [78,56,67]

new = int(input("input new score: "))
numbers.append(new)
lenth = len(numbers)

for i in range(0, lenth - 1):
    for j in range(i + 1, lenth):
        if (numbers[i] < numbers[j]):
            numbers[i], numbers[j] = numbers[j], numbers[i]

print('High scores:')
for i, score in enumerate(numbers):
  print(f'{i+1}. {score}')