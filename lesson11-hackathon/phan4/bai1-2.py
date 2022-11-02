price = {'HP':600, 'DELL':650, 'MACBOOK':1200, 'ASUS':400}
# sum = price['ASUS']*5
# print(sum)

total = 0
brand = input("Input a brand: ").upper()
amount = int(input("INput amount to buy: "))
if brand in price:
    total = price[brand]*amount
print(f"Total price: {total}")