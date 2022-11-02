n = int(input("Input a number: "))

def check(n):
    if n%2==0:
        return True
    if n%2==1:
        return False
if check(n):
    print("This number is even")
else:
    print("This number is not even")