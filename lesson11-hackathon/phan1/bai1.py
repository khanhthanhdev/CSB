# laptop = {'HP':20, 'DELL':50, 'MACBOOK':12, 'ASUS':30}

# print(f"Available MACBOOKs: {laptop['MACBOOK']}")

# name = input("Input a brand: ").upper()
# if name in laptop:
#     print(f"Available {name}s: {laptop['name']}")
shop = {"HP": 20, "DELL": 50, "MACBOOK": 12, "ASUS": 30}
# Bai2
print(f"Available MACBOOKs: {shop['MACBOOK']}")
# bai3
laptop = input("Input trandmark: ").upper()
if laptop in shop:
        print(f"Available {laptop}s : {shop[laptop]}")
else:
        print("Your trandmark is none")