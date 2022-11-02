arr = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l',
'o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']



# for i in range(len(arr)//2):
#     arr[i], arr[-1-i] = arr[-1-i], arr[i]
# arr2 = "".join(arr)
arr2 = arr[::-1]
arr2 = "".join(arr2)
print(arr2)