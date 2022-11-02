
# number = []
# for i in range(0, 10):
#     ele = int(input("Nhập 10 số"))
#     number.append(ele)
# print(number)







lst = [ ] 
for i in range(0, 10): 
    number= input(f"Nhập số thứ {i+1}: ")
    lst.append(number) 
dem = 0
sum = 0
for i in lst:
    if int(i) % 3 == 0:
        sum += int(i)
        dem += 1
average = sum/dem
print(f"Trung bình cộng là {average}")


