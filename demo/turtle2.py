import turtle

wn = turtle.Screen()

#Tạo con trỏ
pen = turtle.Turtle()

#chỉnh màu viền


#chỉnh màu nên (màu viền, màu tô)
pen.color("red", "grey")

#bắt đầu tô
pen.begin_fill()

#điều chỉnh tốc độ
pen.speed(3)
#Nhấc bút lên
pen.penup()

#Đặt bút xuống
pen.pendown()

#di chuyên
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.forward(100)
pen.left(120)
pen.forward(100)

#dừng tô màu
pen.end_fill()

pen.penup()

#Hiện ra màn hình
turtle.done()