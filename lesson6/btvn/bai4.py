
number = int(input("Number of items: "))
menu = []
main_menu = []
sum = 0
for i in range(1,number+1):
    food = input(f"Item {i}: ")
    menu.append(food)
    price = input(f"Price of item {i}: ")
    menu.append(price)
for i in range(1,len(menu), 2):
    sum = sum + float(menu[i])
average=sum/number
print(f"Average price: {average}")
print(menu)

for i in range(1,len(menu),2):
    if int(menu[i]) > average:
        main_menu.append(menu[i])
        main_menu.append(menu[i-1])
print(f"Item(s) above average price: {main_menu}")





