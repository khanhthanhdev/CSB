def max_number(a,b,c):
    max = a
    if max < b:
        max=b
    if max<c:
        max = c
    return max

a = float(input())
b = float(input())
c = float(input())

print(max_number(a,b,c))
