file = open("D:\CSB\lesson12-file\in.pnm", "r")
count_file = open("cout.txt", "w")
d = file.read()
d = d.replace("\n","")
d = d.split(" ")
dic = {}
for i in d:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1


sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print(dic)
for i in sorted_dic:
    count_file.write(i[0] + ": " + str(i[1]) + "\n")

