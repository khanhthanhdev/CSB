# file = open("text.txt", "w")

# text = "Machine learning (ML) is the study of computer algorithms that can improve automatically through experience and by the use of data.It is seen as a part of artificial intelligence. Machine learning algorithms build a model based on sample data, known as training data, in order to make predictions or decisions without being explicitly programmed to do so.Machine learning algorithms are used in a wide variety of applications, such as in medicine, email filtering, speech recognition, and computer vision, where it is difficult or unfeasible to develop conventional algorithms to perform the needed tasks."
# text = text.replace(",","")
# dot_text = text.split(".")
# for i in dot_text:
#     file.write(f"{i}\n")



f = open("text.txt", "r")

d = f.read()
# Dùng replace để loại bỏ \n
d = d.replace("\n","")

#  DÙng split để tách từng chữ ra bởi dấu ""
d = d.split(" ")

dic = {}

#  duyệt từng chữ trong d

for i in d:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)




