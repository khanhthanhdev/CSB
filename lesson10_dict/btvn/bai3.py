number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']

arap_number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# def Convert(number_list):
#     res_dct = {number_list[i]: number_list[i + 1] for i in range(0, len(number_list), 2)}
#     return res_dct

numbers = {}
for key in number_list:
    for value in arap_number:
        numbers[key] = value
        arap_number.remove(value)
        break
# numbers = dict.fromkeys(number_list,arap_number)
print(numbers)
roman_number = input('Input a Roman number: ').upper()
if roman_number in numbers:
    print(f"Arabic number: {numbers[roman_number]}")
else:
    print('Not found.')
