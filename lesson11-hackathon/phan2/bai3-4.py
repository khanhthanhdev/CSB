shop = {"HP": 20, "DELL": 50, "MACBOOK": 12, "ASUS": 30}

# shop['DELL'] += 10
# shop['MACBOOK'] -= 10
# print("Available products:")
# for key,value in shop.items():
#     print(f"- {key}: {value}")


# bai 4
sum=0
for value in shop.values():
    sum += int(value)
print(f"Total products: {sum}")