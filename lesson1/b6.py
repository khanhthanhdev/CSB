import turtle

wn = turtle.Screen()

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
pen.pensize(2)
pen.setx(-125)
pen.sety(-125)
pen.pendown()
pen.setx(125)
pen.sety(125)
pen.setx(-125)
pen.sety(-125)

pen.penup()
pen.setx(0)
pen.sety(0)
pen.pendown()

pen.done()
