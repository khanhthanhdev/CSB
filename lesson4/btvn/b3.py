n = int(input())
giai_thua=1
if n<0:
    print("Invalid")
elif n==0 or n==1:
    print(giai_thua)
else:
    for i in range(2,n+1):
        giai_thua = giai_thua*i
    print(giai_thua)