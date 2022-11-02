input_str = input("Write a sentence: ")
word_list = input_str.split()
new_list = []
for i in range(len(word_list)):
    if word_list[i] not in new_list:
        new_list.append(word_list[i])
# print(new_list)
print(f"Number of unique words: {len(new_list)}")
