def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

sum = 0

for i in range(1,1001):
    if is_prime(i):
        sum += i
print(sum)