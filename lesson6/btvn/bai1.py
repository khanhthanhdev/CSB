arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {arr}")

for i in arr:
    arr[i] +=2
print(f"Add 2: {arr}")

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in arr:
    arr[i] = arr[i] *2

print(f"Multiply by 2 : {arr}")

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del arr[0:2]
arr.extend((0,1))
print(f"Shift 2: {arr}")