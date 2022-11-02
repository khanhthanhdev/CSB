file = open("D:\\CSB\\lesson12-file\\btvn\\question-bank.txt", 'r')
print("Give the correct answers to get points")
count = sum(1 for line in file)
point = 0
for i in range(1,count+1):
    question = file.readlines(i)
    listToStr = ' '.join(map(str, question)).strip().split(',')
    answer = int(input(f"{listToStr[0]}"))
    if answer == int(listToStr[1]):
        point += 1
print(f"== You get {point}/{count} points ==")

