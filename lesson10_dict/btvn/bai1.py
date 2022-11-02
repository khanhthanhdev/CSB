numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}

roman_number = input('Input a Roman number: ').upper()

if roman_number in numbers:
    print(f"Arabic number: {numbers[roman_number]}")
else:
    print('Not found.')
