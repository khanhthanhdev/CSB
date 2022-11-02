print("== Registration == \n")

username = input("Username: ")
password = input("Password: ")
re_password = input("Repeat password: ")

if username != "" and password != "" and password!=re_password:
    while re_password!=password:
        print("Passwords not match. Please input again.")
        re_password = input("Repeat password: ")
if re_password == password:
    email = input("Email: ")
    if email !="":
        print("Registered successfully")
    
    