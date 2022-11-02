shop = {"HP": 20, "DELL": 50, "MACBOOK": 12, "ASUS": 30}
#bai1
# shop.update({'TOSHIBA':10})

# Bai 2
laptop = input("Input trandmark: ").upper()
quatily = int(input("Input quatily: "))
if laptop not in shop:
    shop.update({f"{laptop}":quatily})
print("Avaliable products: ")

for key,value in shop.items():
    print(f"- {key}: {value}")


