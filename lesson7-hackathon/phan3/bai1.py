list = [5, 1, 8, 92, -1, 30]
n = int(input("Input number: "))
if n not in list:
    print("Number not found")
if n in list:
    print(f"Number found at position: {list.index(n)+1} ")