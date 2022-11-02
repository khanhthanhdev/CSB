n = int(input("Nhập n: ")) 
fibonacci = [1, 1]
if n==1 or n==2:
    print(1)
elif n>2:
    for x in range(2, n):
        next = fibonacci[x - 1] + fibonacci[x - 2]
        fibonacci.append(next)
    for i in fibonacci:
        print(i, end=" ")