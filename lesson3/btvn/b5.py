username = "admin"
userpassword = "12345"

nameinput = input("username: ")
passinput = input("password: ")

if nameinput == username and passinput == userpassword:
    print("You are logged in, admin")
else:
    print("Wrong username or password")