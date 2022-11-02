radius = float(input("Input radius: "))

def cal_area(radius):
    area = radius**2 * 3.14
    return area

print(f"Circle's area: {cal_area(radius)}")