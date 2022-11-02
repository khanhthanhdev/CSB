import datetime 

time_now = datetime.datetime.now()

file = open("D:\\CSB\\lesson12-file\\btvn\\user-inputs.txt", "a")

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

file.write(f"== Inputs at {time_now} == \n")
file.write(f"{user_writing} \n")
file.write("\n")