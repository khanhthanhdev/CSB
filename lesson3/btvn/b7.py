import turtle

a = float(input("Input length 1: "))
b = float(input("Input length 2: "))
c = float(input("Input length 3: "))

if a + b > c and b + c > a and a + c > b:
    if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
        print("The 3 line segments can form a right triangle.")
    elif a == b == c:
        turtle.Screen()
        print("The 3 line segments can form an equilateral triangle.")
        pen = turtle.Turtle()
        for i in range(3):
            pen.forward(a)
            pen.left(180-60)
        turtle.done()
    else:
        print("The 3 line segments can form a triangle.")
else:
    print("The 3 line segments cannot form a triangle.")