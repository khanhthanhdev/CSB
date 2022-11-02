firstName = input("First name: " + '\033[1m')
lastName = input('\033[0m' + "Last name: " + '\033[1m')
phoneNumber = input('\033[0m' + "Phone number: " + '\033[1m' )

print('\033[0m' + "Your registered name is " + firstName + ' '+ lastName)
print("Your phone number is ", phoneNumber)
