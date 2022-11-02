lst = [5, 1, 8, 92, -1, 30]
print("Original list: \n")
for i in lst:
    print(i, end=" ")
print("\n")
def sap_xep(lst):
    for i in range(0,len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
print("Sorted list: \n")
for i in sap_xep(lst):
    print(i, end=" ")
