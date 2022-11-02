n = int(input())
tong=0

while n >0:
    tong = tong + n%10
    n = int(n/10)
print(tong)