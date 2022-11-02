# toan = 0
# ly = 0
# hoa = 0
# van = 0
# anh = 0
# def average_score():
#   toan = float(input())
#   ly = float(input())
#   hoa = float(input())
#   van = float(input())
#   anh = float(input())
#   average = (toan+ly+hoa+van+anh)/5
#   return average

# def hoc_luc(diem):
#     if diem < 5:
#         print("Yeu")
#     elif 5 <= diem <=6.9:
#         print("Trung binh")
#     elif 7<= diem <=8.9:
#         print("Kha")
#     elif 9<=diem<=10:
#         print("gioi")

# trung_binh = average_score()
# hoc_luc(trung_binh)
print("Chương trình tính điểm trung bình của học sinh")
toan = 0
ly = 0
hoa = 0
van = 0
anh = 0

def nhap_diem():
    print("Nhập điểm môn toán: ")
    toan = float(input())
    print("Nhập điểm môn Lý: ")
    ly = float(input())
    print("Nhập điểm môn Hóa: ")
    hoa = float(input())
    print("Nhập điểm môn Văn: ")
    van = float(input())
    print("Nhập điểm môn Anh: ")
    anh = float(input())
    trungbinh = (toan + ly + hoa + van + anh) / 5
    return trungbinh

def hoc_luc(diem):
    if diem < 5:
        print("Yeu")
    elif 5 <= diem <=6.9:
        print("Trung binh")
    elif 7<= diem <=8.9:
        print("Kha")
    elif 9<=diem<=10:
        print("gioi")

trungbinh = nhap_diem()
hoc_luc(trungbinh)
