shop = {"HP": 20, "DELL": 50, "MACBOOK": 12, "ASUS": 30}
price = {'HP':600, 'DELL':650, 'MACBOOK':1200, 'ASUS':400}

total = 0
brand = input("Input a brand: ").upper()
amount = int(input("Input amount to buy: "))
if brand in price:
    total = price[brand]*amount
print(f"Total price: {total}\n")

shop.update({f"{brand}":shop[brand]-amount})
print("Available products:")
for key,value in shop.items():
    print(f"- {key}: {value}")