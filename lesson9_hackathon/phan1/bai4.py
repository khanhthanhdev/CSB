from typing import NewType


text = input("Input a text: ")

def is_palindrome(text):
    return text == text[::-1]

if is_palindrome(text):
    print("This is a palindrome")
else:
    print("This is not a palindrome")
