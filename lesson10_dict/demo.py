'''
list và tuple đều lưu được nhiều giá trị. Tuy nhiên sẽ có 1 số trường hợp cần biết giá trị lưu trữ đó 
có ý nghĩa gì

=>> dictionary: là kiểu dữ liệu được dùng luuw trữ theo dạng key-value

-Cách khởi tạo
    <tên-biến> = {}

- ví dụ:
    dic = {"ios": "iphone", "android" : "samsung"}

- lấy độ dài của dict

- để lấy giá trị của value thông qua key
    + lấy giá trị của "ios" ==> x = dic["ios"] => x = "iphone"
    + cách khác: x = dic.get("ios")

- để lấy danh sách các khoá của dictionary ==> <tên biến>.keys()
    print(dic.keys()) ===> dict_keys(['ios', 'android'])
- để lấy danh sách các values của dictionary ==? <ten bien>.values()
    print(dic.values()) ==> "iphone", "samsung"

- thêm giá trị mới vào dic có sẵn
    dic["tablet"] = "ipad"

- In ra dưới dạng tuple:
    print(dic.items())

- Kiểm tra key có trong dict không/;
    if "ios" in dic:

- Thay đổi giá trị (value) của 1 khoá:
    thay đổi giá trị ipad của key tablet thành "tab"

-Lệnh update:
    thay đổi giá trị tab của key tablet thành ipad

- Xoá 1 cặp key-value thông quan tên key
    xoá key "tablet"
        dic.pop("tablet")
-Xoá cặp key-value cuối cùng:
    dic.popitem()
'''
# dic = {"ios": "iphone", "android" : "samsung"}
# print(len(dic))
# dic["tablet"] = "ipad"
# print(dic.items())
# dic["tablet"] = "tab"
# dic.update({"tablet" : "ipad"})
# # Xoá 1 cặp key-value thông quan tên key
# dic.pop("tablet")
# # -Xoá cặp key-value cuối cùng:
# dic.popitem()
# # Xoá luôn dict
# # del dic
# print(dic)

'''
-Vòng lặp trong dictionary:
    + In ra tất cả các key trong dict:
        for i in dic:
    + cách khác:
        for i in dic.keys()
            print(i)
    + In ra giá trị key,value
        for key, value in dic.items()
            print(key,value)
'''
b = tuple({'a':1},)
print(b)