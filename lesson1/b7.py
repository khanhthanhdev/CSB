import turtle
import math
pen = turtle.Turtle()
pen.penup()
pen.setx(-100)
pen.sety(-100)
pen.pendown()
pen.setx(100)
pen.sety(100)
pen.setx(-100)
pen.sety(-100)

pen.penup()
pen.setpos(0, (200/math.sqrt(2)))
pen.pendown()
pen.setpos((200/math.sqrt(2)), 0)
pen.setpos(0, -(200/math.sqrt(2)))
pen.setpos(-(200/math.sqrt(2)), 0)
pen.setpos(0, (200/math.sqrt(2)))


