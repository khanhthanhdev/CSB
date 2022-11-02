import xlwings
from PIL import Image
file = Image.open("D:\\anh2.png")
height = file.height
width = file.width

pix = file.load()
def pick_color(x, y):
    color = '#%02x%02x%02x%02x' % pix[x, y]
    return color[:-2]
sht = xlwings.sheets.active
try:
    for y in range(1, height):
        for x in range(1, width):
            sht.range(y, x).color = pick_color(x, y)
except:
    ''