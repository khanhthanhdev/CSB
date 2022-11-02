number = int(input("Input a number: "))

def print_fiblo(n):
    a = 0
    b = 1
    c = 0
    fibonacci = ""
    for i in range(0, n):
        a = b
        b = c
        c = a + b
        fibonacci += str(c) + " "
    return fibonacci


print(f"First {number} Fibonacci numbers: {print_fiblo(number)}")