prime = [2]
n = int(input("Input number: "))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


def print_list_prime(n):
    count = 0
    i=2
    while count<n:
        if is_prime(i):
            print(f"{i}", end=" ")
            count+=1
        i +=1
print_list_prime(n)

# for i in prime:
