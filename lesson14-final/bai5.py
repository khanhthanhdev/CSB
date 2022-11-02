phone = {"Iphone12":28000000, "Samsung N10": 16000000, "Oppo 93": 7500000, "Vsmart": 7400000, "Vivo": 4200000}

# Chương trình 1
# input_phone = input("Input name of a phone: ")
# for i in phone:
#     if input_phone == i:
#         print(phone[f"{input_phone}"])

# Chương trình 2
budget = float(input("Input your budget: "))
for key,value in phone.items():
    if budget > phone[key]:
        print(f"- {key} : {value}")