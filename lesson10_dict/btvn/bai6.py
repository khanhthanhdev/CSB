sequence = input('Input sequence: ')

count = {}

for i in sequence:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(f"Frequency of characters: {count}")