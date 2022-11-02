print("== Welcome to Mindx Restaurant == \n")

menu = []

dish = input("Please choose a dish: ")

menu.append(dish)

in_menu = input("Great choice! Anything else? (y/n): ")

while in_menu == "y":
    dish = input("Please choose a dish: ")
    if dish in menu:
        in_menu = input("You chose this already. Anything else? (y/n): ")
    elif dish not in menu:
        menu.append(dish)
        in_menu = input("Anything else? (y/n): ")

print("Well done! Your order: ")
for i in menu:
    print("- " + i, end = "\n")