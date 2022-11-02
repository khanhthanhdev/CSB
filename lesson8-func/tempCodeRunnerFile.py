text = input("input: ")
def sap_xep(text):
    lst = []
    for i in range(len(text)):
        lst.append(ord(text[i]))
    lst.sort()  
    for i in lst:
        print(chr(i), end = ' ')
    
sap_xep(text)