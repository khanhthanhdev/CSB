import turtle
n = int(input("Nhập số cạnh: "))
wn = turtle.Screen()

pen = turtle.Turtle()



for i in range(n):
    pen.forward(100)
    pen.right(360/n)

turtle.done()