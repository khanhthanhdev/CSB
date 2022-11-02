import math


def giaiptbac2(a, b, c):
    # kiểm tra các hệ số
    if (a == 0):
        if (b == 0):
            print ("Phương trình vô nghiệm!");
        else:
            print ("Phương trình có một nghiệm: x = ", + (-c / b))
        return

    delta = b * b - 4 * a * c
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
        print ("The equation has 2 solutions. \nx = ",x1, "or x = ",x2)
    elif (delta == 0):
        x1 = (-b / (2 * a))
        print("the equation has double solutions: x1 = x2 = ", x1)
    else:
        print("the equation has no solutions!")
 
a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))

giaiptbac2(a, b, c)