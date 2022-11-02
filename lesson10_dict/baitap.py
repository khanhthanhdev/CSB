# shop = {"HP": 20, "DELL": 50, "MACBOOK": 12, "ASUS": 30}
# print(shop["MACBOOK"])

# laptop = input("Input trandmark: ").upper()
# if laptop in shop:
#         print(shop[laptop])
# else:
#         print("Your trandmark is none")

# Bai 2

# character = {"name": "Light",
#              "age":17,"strength":8,
#              "defense": 10,
#              "hp":100,
#              "backpack":["shield","bread loaf"],
#              "gold":100,
#              "level":2}
# character["gold"] += 50
# character["backpack"] += ["flintstone"]
# character["pocket"] = ["monsterdex","flashlight"]
# print(character)

# Bài 3
shop = {"HP": 20, "DELL": 50, "MACBOOK": 12, "ASUS": 30}

laptop = input("Input trandmark: ").upper()
quatily = int(input("Input quatily: "))
laptop2 = input("Input trandmark: ").upper()
quatily2 = int(input("Input quatily: "))
laptop3 = input("Input trandmark: ").upper()
quatily3 = int(input("Input quatily: "))
if laptop not in shop:
    shop.update({f"{laptop}":quatily,f"{laptop2}":quatily2,f"{laptop3}":quatily3})
new={}
value = sorted(shop.values(), reverse=True)
key = sorted(shop.keys())
for i in range(len(value)):
    for k in range(len(key)):
        if value[i] == shop[key[k]]:
            new[key[k]] = value[i]
for laptop,quantily in new.items():
    print(f"{laptop}: {quantily}")


    # Cách 2
dic = sorted(shop.items(), key=lambda x : x[1])
for i in dic:
    print(i[0], i[1])

    #cách 3
for key, value in sorted(shop.items(), key=lambda x : x[1]):
    print(key, value)





