# In số dòng cầu thang
n = int(input())
for i in range(1, n+1):
    for k in range(1, i+1):
        print('#', end="")
    print("")