price = {'HP':600, 'DELL':650, 'MACBOOK':1200, 'ASUS':400}

brand = input("Input a brand: ").upper()

print(f"Price of ASUS: {price['ASUS']}")
# bai 3
print(f"Price of {brand}: {price[brand]}")