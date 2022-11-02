text = input("Input a text: ")

def reverse_str(text):
    new = list(reversed(text))
    new_str = ''.join(new)
    return new_str
print(f"Reversed text: {reverse_str(text)}")