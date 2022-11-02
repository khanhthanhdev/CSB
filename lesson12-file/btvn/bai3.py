
file = open("D:\\CSB\\lesson12-file\\btvn\\user-inputs.txt", "w")

print("== Input file content below ==")
user_writing = [] 
while True: 
	line = input() 
	if line:
		user_writing.append(line) 
	elif line == "": 
		break
user_writing = '\n'.join(user_writing) 
#  Ấn sapce 2 lần để thoát input
print("== Input recorded in user-inputs.txt ==")

file.write(user_writing)